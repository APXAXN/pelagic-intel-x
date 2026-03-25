"""
Pelagic IntelX — SerpApi Keyword Landscape Collection
Pulls SERP features, question clusters, and keyword data.
Output: data/processed/keyword_landscape.json
"""

import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

PROCESSED_DIR = Path(__file__).parent.parent / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

load_dotenv(Path(__file__).parent.parent / ".env")

QUERIES = [
    "ocean plastic pollution",
    "microplastics in ocean",
    "AI ocean monitoring",
    "satellite plastic detection",
    "ocean plastic map",
    "microplastic density Pacific",
    "plastic pollution data",
    "ocean cleanup technology",
    "AI environmental monitoring",
    "global plastics treaty",
]


def collect_serp_data():
    import serpapi

    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        print("ERROR: SERPAPI_KEY not found in .env")
        sys.exit(1)

    client = serpapi.Client(api_key=api_key)
    results = []

    for query in QUERIES:
        print(f"Querying: {query}")
        result = client.search({
            "engine": "google",
            "q": query,
            "num": 10,
            "gl": "us",
            "hl": "en",
        })

        entry = {
            "query": query,
            "organic_results": [],
            "related_questions": [],
            "related_searches": [],
        }

        # Organic results
        for r in result.get("organic_results", [])[:5]:
            entry["organic_results"].append({
                "title": r.get("title", ""),
                "link": r.get("link", ""),
                "snippet": r.get("snippet", ""),
                "position": r.get("position", 0),
            })

        # People Also Ask
        for q in result.get("related_questions", []):
            entry["related_questions"].append({
                "question": q.get("question", ""),
                "snippet": q.get("snippet", ""),
            })

        # Related searches
        for s in result.get("related_searches", []):
            entry["related_searches"].append(s.get("query", ""))

        results.append(entry)

    output = {
        "source": "serpapi",
        "query_count": len(results),
        "queries": results,
    }

    output_path = PROCESSED_DIR / "keyword_landscape.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Saved to {output_path}")
    return output


if __name__ == "__main__":
    collect_serp_data()
