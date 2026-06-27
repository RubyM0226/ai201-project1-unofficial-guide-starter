import os
import re
import json
import requests
from bs4 import BeautifulSoup

# ── Config ────────────────────────────────────────────────────────────────────
DOCUMENTS_DIR = "documents"
CHUNKS_OUTPUT  = "chunks.json"
CHUNK_SIZE     = 350   # target tokens per chunk
OVERLAP        = 60    # overlap tokens between chunks
HEADERS        = {"User-Agent": "Mozilla/5.0 (research project; UF AI201)"}

# ── Sources ───────────────────────────────────────────────────────────────────
SOURCES = [
    {"url": "https://sweetwatergainesville.com/resources/best-study-spots-uf/",
     "spot_name": "multiple", "type": "blog", "filename": "sweetwater_study_spots.txt"},
    {"url": "https://subjectsaviors.com/the-top-10-best-study-spots-in-gainesville/",
     "spot_name": "multiple", "type": "blog", "filename": "subjectsaviors_study_spots.txt"},
    {"url": "https://www.swamprentals.com/help-finding-apartments/gainesville-study-spots-near-campus",
     "spot_name": "multiple", "type": "blog", "filename": "swamprentals_study_spots.txt"},
    {"url": "https://gatorrentals.com/blog/best-study-spots-on-campus/",
     "spot_name": "multiple", "type": "blog", "filename": "gatorrentals_study_spots.txt"},
    {"url": "https://www.staygainesville.com/uf-campus-insider-tips-best-study-spots-hidden-gems",
     "spot_name": "multiple", "type": "blog", "filename": "staygainesville_study_spots.txt"},
    {"url": "https://spoonuniversity.com/school/ufl/uf-s-best-coffee-shops-for-study-sessions-coffee-shop-in-gainesville/",
     "spot_name": "coffee shops", "type": "review", "filename": "spoonuniversity_coffee_shops.txt"},
    {"url": "https://www.hercampus.com/school/ufl/5-gainesville-coffee-shops-to-visit-this-semester/",
     "spot_name": "coffee shops", "type": "review", "filename": "hercampus_coffee_shops.txt"},
    {"url": "https://www.collegemagazine.com/top-10-local-coffee-shops-that-all-uf-students-need-to-try/",
     "spot_name": "coffee shops", "type": "review", "filename": "collegemagazine_coffee_shops.txt"},
    {"url": "https://www.yelp.com/biz/pascals-coffeehouse-at-christian-study-center-gainesville",
     "spot_name": "Pascal's Coffeehouse", "type": "yelp_reviews", "filename": "yelp_pascals.txt"},
    {"url": "https://www.hercampus.com/school/ufl/gainesville-bucket-list/",
     "spot_name": "multiple", "type": "blog", "filename": "hercampus_bucket_list.txt"},
    {"url": "https://www.reddit.com/r/ufl/comments/oqbhhq/best_unknown_study_spots_on_campus/",
     "spot_name": "multiple", "type": "reddit", "filename": "reddit_unknown_study_spots.txt"},
    {"url": "https://www.reddit.com/r/ufl/comments/16tqs1w/whats_your_favorite_place_to_study/",
     "spot_name": "multiple", "type": "reddit", "filename": "reddit_favorite_study_place.txt"},
    {"url": "https://www.reddit.com/r/ufl/comments/j0yaz0/pretty_outdoor_study_spots_around_gainesville/",
     "spot_name": "outdoor", "type": "reddit", "filename": "reddit_outdoor_study_spots.txt"},
    {"url": "https://www.reddit.com/r/ufl/comments/xnrfer/what_are_some_good_coffee_shopsplaces_to_study_",
     "spot_name": "coffee shops", "type": "reddit", "filename": "reddit_coffee_shops_study.txt"},
    {"url": "https://ufl.pb.unizin.org/ulaguide/chapter/library-west/", 
     "spot_name": "library west", "type": "blog", "filename": "uflpb_libwest_review.txt"},
    {"url": "https://spoonuniversity.com/school/ufl/a-peek-inside-coterie-market/", 
     "spot_name": "coterie market", "type": "blog", "filename": "spoonuniversity_coterie_market.txt"},
    {"url": "https://www.theodysseyonline.com/review-uf-campus-libraries", 
     "spot_name": "multiple", "type": "blog", "filename": "odysseyonline.txt"},
    {"url": "https://carlymccullough.com/2018/03/13/stress-free-study-spots-on-uf-campus/", 
     "spot_name": "multiple", "type": "blog", "filename": "carlymccullough.txt"},
]

BOILERPLATE = [
    r"cookie[s]? policy.*", r"privacy policy.*", r"terms of (use|service).*",
    r"all rights reserved.*", r"subscribe to.*newsletter.*", r"sign up for.*",
    r"share this (post|article).*", r"follow us on.*", r"read more.*",
    r"click here.*", r"advertisement", r"sponsored",
    r"\[deleted\]", r"\[removed\]",
]

# ── Token helpers (1 token ≈ 0.75 words) ─────────────────────────────────────
def count_tokens(text):
    return int(len(text.split()) / 0.75)

# ── Fetching ──────────────────────────────────────────────────────────────────
def fetch_url(url, is_reddit=False):
    try:
        if is_reddit:
            json_url = url.rstrip("/") + ".json?limit=100"
            r = requests.get(json_url, headers=HEADERS, timeout=15)
            r.raise_for_status()
            return r.text
        else:
            r = requests.get(url, headers=HEADERS, timeout=15)
            r.raise_for_status()
            return r.text
    except Exception as e:
        print(f"  WARNING: Could not fetch {url}: {e}")
        return ""

def parse_reddit_json(raw, url):
    try:
        data = json.loads(raw)
        lines = []
        post = data[0]["data"]["children"][0]["data"]
        lines.append(post.get("title", ""))
        if post.get("selftext"):
            lines.append(post["selftext"])
        for c in data[1]["data"]["children"]:
            body = c["data"].get("body", "")
            if body and body not in ("[deleted]", "[removed]"):
                lines.append(body)
        return "\n\n".join(lines)
    except Exception as e:
        print(f"  WARNING: Reddit parse error for {url}: {e}")
        return ""

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script","style","nav","header","footer",
                     "aside","form","iframe","noscript","button"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [l.strip() for l in text.splitlines()]
    text = "\n".join(l for l in lines if l)
    for pattern in BOILERPLATE:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.replace("&amp;","&").replace("&nbsp;"," ").replace("&#39;","'").replace("&quot;",'"')
    return text.strip()

# ── Chunking ──────────────────────────────────────────────────────────────────
def chunk_text(text, source_meta):
    chunk_words = int(CHUNK_SIZE * 0.75)   # ~262 words
    overlap_words = int(OVERLAP * 0.75)    # ~45 words
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_words, len(words))
        chunk_str = " ".join(words[start:end])
        chunks.append({
            "text": chunk_str,
            "source": source_meta["url"],
            "spot_name": source_meta["spot_name"],
            "type": source_meta["type"],
            "token_count": count_tokens(chunk_str),
        })
        if end == len(words):
            break
        start += chunk_words - overlap_words
    return chunks

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(DOCUMENTS_DIR, exist_ok=True)
    all_chunks = []
    failed = []

    print("=" * 60)
    print("STEP 1 — Fetching and cleaning documents")
    print("=" * 60)

    for source in SOURCES:
        url = source["url"]
        is_reddit = source["type"] == "reddit"
        filepath = os.path.join(DOCUMENTS_DIR, source["filename"])

        print(f"\n-> {source['filename']}")

        if os.path.exists(filepath):
            print("  (already saved - loading from disk)")
            with open(filepath, "r", encoding="utf-8") as f:
                clean = f.read()
        else:
            raw = fetch_url(url, is_reddit=is_reddit)
            if not raw:
                failed.append(url)
                continue
            clean = parse_reddit_json(raw, url) if is_reddit else clean_html(raw)
            if len(clean) < 100:
                print(f"  WARNING: Very short after cleaning ({len(clean)} chars)")
                failed.append(url)
                continue
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(clean)

        print(f"  OK: {len(clean):,} chars | ~{count_tokens(clean):,} tokens")

    print("\n" + "=" * 60)
    print("STEP 2 — Chunking documents")
    print("=" * 60)

    for source in SOURCES:
        filepath = os.path.join(DOCUMENTS_DIR, source["filename"])
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_text(text, source)
        all_chunks.extend(chunks)
        print(f"  {source['filename']}: {len(chunks)} chunks")

    print("\n" + "=" * 60)
    print("STEP 3 — Saving chunks")
    print("=" * 60)

    with open(CHUNKS_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
    print(f"\nSaved {len(all_chunks)} chunks to {CHUNKS_OUTPUT}")

    print("\n" + "=" * 60)
    print("STEP 4 — Sample chunks (inspect these!)")
    print("=" * 60)

    if all_chunks:
        sample_indices = [0, len(all_chunks)//4, len(all_chunks)//2,
                          3*len(all_chunks)//4, len(all_chunks)-1]
        for i, idx in enumerate(sample_indices):
            c = all_chunks[idx]
            print(f"\n-- Chunk {i+1} (index {idx}) --")
            print(f"Source : {c['source']}")
            print(f"Type   : {c['type']}  |  Spot: {c['spot_name']}")
            print(f"Tokens : ~{c['token_count']}")
            print(f"Text   :\n{c['text'][:400]}{'...' if len(c['text']) > 400 else ''}")

    print("\n" + "=" * 60)
    print("STEP 5 — Validation summary")
    print("=" * 60)
    print(f"Total chunks : {len(all_chunks)}")
    print(f"Target range : 50 - 2,000")
    if len(all_chunks) < 50:
        print("WARNING: Too few chunks - consider reducing chunk size")
    elif len(all_chunks) > 2000:
        print("WARNING: Too many chunks - consider increasing chunk size")
    else:
        print("Chunk count looks good!")

    if failed:
        print(f"\nFailed sources ({len(failed)}) - save these manually as .txt in documents/:")
        for url in failed:
            print(f"   - {url}")

if __name__ == "__main__":
    main()
