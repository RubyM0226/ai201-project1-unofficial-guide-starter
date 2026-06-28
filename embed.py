import json
import chromadb
from sentence_transformers import SentenceTransformer

# ── Config ────────────────────────────────────────────────────────────────────
CHUNKS_FILE   = "chunks.json"
COLLECTION    = "study_spots"
EMBED_MODEL   = "all-MiniLM-L6-v2"
TOP_K         = 4

# ── Test queries (3 of your 5 evaluation questions) ───────────────────────────
TEST_QUERIES = [
    "What coffee shops do UF students recommend for studying?",
    "Is Pascal's Coffeehouse open late enough for a night study session?",
    "What do students say about studying outdoors at UF?",
]

# ── Step 1: Load chunks ───────────────────────────────────────────────────────
def load_chunks(path):
    print(f"Loading chunks from {path}...")
    with open(path, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    print(f"  Loaded {len(chunks)} chunks")
    return chunks


# ── Step 2: Set up ChromaDB ───────────────────────────────────────────────────
def setup_chromadb(collection_name):
    print(f"\nSetting up ChromaDB collection: '{collection_name}'...")
    client = chromadb.Client()

    # Delete existing collection if it exists (fresh embed each run)
    try:
        client.delete_collection(collection_name)
        print("  Cleared existing collection")
    except Exception:
        pass

    collection = client.create_collection(collection_name)
    print("  Collection ready")
    return collection


# ── Step 3: Embed and store ───────────────────────────────────────────────────
def embed_and_store(chunks, collection, model):
    print(f"\nEmbedding {len(chunks)} chunks with {EMBED_MODEL}...")
    print("  (This may take a minute on first run while the model downloads)")

    texts     = [c["text"]      for c in chunks]
    ids       = [str(i)         for i in range(len(chunks))]
    metadatas = [
        {
            "source":     c.get("source", "unknown"),
            "spot_name":  c.get("spot_name", "unknown"),
            "type":       c.get("type", "unknown"),
            "token_count": str(c.get("token_count", 0)),
        }
        for c in chunks
    ]

    # Embed in one batch
    embeddings = model.encode(texts, show_progress_bar=True).tolist()

    # Store in ChromaDB
    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )
    print(f"  Stored {len(chunks)} chunks in ChromaDB")


# ── Step 4: Retrieve ──────────────────────────────────────────────────────────
def retrieve(query, collection, model, k=TOP_K):
    query_embedding = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )
    return results


# ── Step 5: Print results ─────────────────────────────────────────────────────
def print_results(query, results):
    print(f"\n{'='*60}")
    print(f"QUERY: {query}")
    print(f"{'='*60}")

    docs      = results["documents"][0]
    metas     = results["metadatas"][0]
    distances = results["distances"][0]

    for i, (doc, meta, dist) in enumerate(zip(docs, metas, distances)):
        relevance = "GOOD" if dist < 0.5 else "WEAK — check this chunk"
        print(f"\n  -- Result {i+1} | distance: {dist:.3f} | {relevance}")
        print(f"     Source : {meta['source']}")
        print(f"     Type   : {meta['type']} | Spot: {meta['spot_name']}")
        print(f"     Text   : {doc[:300]}{'...' if len(doc) > 300 else ''}")


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    # Load
    chunks = load_chunks(CHUNKS_FILE)

    # Embed model
    print(f"\nLoading embedding model: {EMBED_MODEL}...")
    model = SentenceTransformer(EMBED_MODEL)
    print("  Model ready")

    # ChromaDB
    collection = setup_chromadb(COLLECTION)

    # Embed and store
    embed_and_store(chunks, collection, model)

    # Test retrieval
    print("\n" + "="*60)
    print("RETRIEVAL TESTS")
    print("="*60)

    all_passed = True
    for query in TEST_QUERIES:
        results = retrieve(query, collection, model)
        print_results(query, results)

        # Check if top result is a good match
        top_distance = results["distances"][0][0]
        if top_distance > 0.5:
            all_passed = False

    # Summary
    print(f"\n{'='*60}")
    print("RETRIEVAL SUMMARY")
    print(f"{'='*60}")
    if all_passed:
        print("All top results scored below 0.5 — retrieval looks good!")
        print("You are clear to move to Milestone 5.")
    else:
        print("Some results scored above 0.5 — retrieval may need tuning.")
        print("Debug checklist:")
        print("  1. Print a full returned chunk — is it actually relevant?")
        print("  2. Check chunks.json — do chunks have enough content?")
        print("  3. Try increasing CHUNK_SIZE in ingest.py and re-running")


if __name__ == "__main__":
    main()
