import os
import json
import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────
CHUNKS_FILE  = "chunks.json"
COLLECTION   = "study_spots"
EMBED_MODEL  = "all-MiniLM-L6-v2"
GROQ_MODEL   = "llama-3.3-70b-versatile"
TOP_K        = 4

# ── System prompt — enforces grounding ───────────────────────────────────────
SYSTEM_PROMPT = """You are a helpful guide for University of Florida students looking for study spots in and around campus.

Answer the user's question using ONLY the information provided in the context documents below.
Do NOT use any outside knowledge or make assumptions beyond what is written in the documents.

Rules:
- If the documents contain enough information, give a specific, helpful answer.
- Always mention which source(s) your answer came from (e.g. "According to [source]...").
- If the documents do not contain enough information to answer the question, respond with exactly: "I don't have enough information on that in my sources."
- Never invent details, hours, locations, or opinions that are not in the documents.
"""

# ── Load model and ChromaDB once at module level ──────────────────────────────
print("Loading embedding model...")
_model = SentenceTransformer(EMBED_MODEL)

print("Setting up ChromaDB...")
_client = chromadb.Client()

# Rebuild collection from chunks.json on every startup
try:
    _client.delete_collection(COLLECTION)
except Exception:
    pass

_collection = _client.create_collection(COLLECTION)

print("Embedding chunks into ChromaDB...")
with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
    _chunks = json.load(f)

_texts     = [c["text"] for c in _chunks]
_ids       = [str(i) for i in range(len(_chunks))]
_metadatas = [
    {
        "source":    c.get("source", "unknown"),
        "spot_name": c.get("spot_name", "unknown"),
        "type":      c.get("type", "unknown"),
    }
    for c in _chunks
]
_embeddings = _model.encode(_texts, show_progress_bar=True).tolist()
_collection.add(ids=_ids, documents=_texts, embeddings=_embeddings, metadatas=_metadatas)
print(f"Ready — {len(_chunks)} chunks loaded.\n")

# ── Groq client ───────────────────────────────────────────────────────────────
_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ── Core ask function ─────────────────────────────────────────────────────────
def ask(question: str) -> dict:
    """
    Retrieve top-k chunks, build a grounded prompt, generate an answer.
    Returns {"answer": str, "sources": list[str], "chunks": list[str]}
    """
    # 1. Embed the query
    query_embedding = _model.encode([question]).tolist()

    # 2. Retrieve top-k chunks
    results = _collection.query(
        query_embeddings=query_embedding,
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"],
    )

    docs      = results["documents"][0]
    metas     = results["metadatas"][0]
    distances = results["distances"][0]

    # 3. Build context block with source labels
    context_parts = []
    sources = []
    for i, (doc, meta, dist) in enumerate(zip(docs, metas, distances)):
        source_label = meta["source"]
        context_parts.append(f"[Document {i+1} — {source_label}]\n{doc}")
        if source_label not in sources:
            sources.append(source_label)

    context = "\n\n".join(context_parts)

    # 4. Build user message
    user_message = f"""Context documents:
{context}

Question: {question}

Answer using only the context documents above. Cite which document(s) you used."""

    # 5. Call Groq
    response = _groq.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.2,  # low temp = more faithful to context
        max_tokens=512,
    )

    answer = response.choices[0].message.content.strip()

    return {
        "answer":  answer,
        "sources": sources,
        "chunks":  docs,
    }
