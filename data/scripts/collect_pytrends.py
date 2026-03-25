"""
Pelagic IntelX — Google Trends Data Collection
Pulls search interest over time for ocean plastic and AI environmental keywords.
Output: data/processed/search_trends.json
"""

import json
import os
import sys
from pathlib import Path
from pytrends.request import TrendReq

PROCESSED_DIR = Path(__file__).parent.parent / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

# Keyword groups to query
KEYWORD_GROUPS = [
    ["ocean plastic", "microplastics", "plastic pollution", "ocean cleanup", "marine debris"],
    ["AI environment", "satellite ocean monitoring", "ocean plastic mapping"],
]

TIMEFRAME = "today 5-y"  # Last 5 years
GEO = ""  # Worldwide


def collect_trends():
    pytrends = TrendReq(hl="en-US", tz=360)
    all_data = {}

    for group in KEYWORD_GROUPS:
        print(f"Querying: {group}")
        pytrends.build_payload(group, cat=0, timeframe=TIMEFRAME, geo=GEO)

        # Interest over time
        interest = pytrends.interest_over_time()
        if not interest.empty:
            interest = interest.drop(columns=["isPartial"], errors="ignore")
            for col in interest.columns:
                all_data[col] = [
                    {"date": date.strftime("%Y-%m-%d"), "value": int(val)}
                    for date, val in zip(interest.index, interest[col])
                ]

    # Related queries for top keywords
    related = {}
    for kw in ["ocean plastic", "microplastics"]:
        pytrends.build_payload([kw], cat=0, timeframe=TIMEFRAME, geo=GEO)
        related_queries = pytrends.related_queries()
        if kw in related_queries:
            top = related_queries[kw].get("top")
            rising = related_queries[kw].get("rising")
            related[kw] = {
                "top": top.to_dict("records") if top is not None and not top.empty else [],
                "rising": rising.to_dict("records") if rising is not None and not rising.empty else [],
            }

    output = {
        "timeframe": TIMEFRAME,
        "geo": GEO,
        "interest_over_time": all_data,
        "related_queries": related,
    }

    output_path = PROCESSED_DIR / "search_trends.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Saved to {output_path}")
    print(f"Keywords collected: {list(all_data.keys())}")
    return output


if __name__ == "__main__":
    collect_trends()
