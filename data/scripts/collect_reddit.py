"""
Pelagic IntelX — Reddit Data Collection via PRAW
Mines posts and comments from target subreddits on ocean plastic topics.
Output: data/raw/reddit_posts.json
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import praw

RAW_DIR = Path(__file__).parent.parent / "raw"
RAW_DIR.mkdir(exist_ok=True)

load_dotenv(Path(__file__).parent.parent / ".env")

SUBREDDITS = ["environment", "Futurology", "collapse", "MachineLearning"]

SEARCH_QUERIES = [
    "ocean plastic",
    "microplastics",
    "plastic pollution ocean",
    "AI ocean monitoring",
    "satellite ocean plastic",
    "ocean cleanup",
    "marine debris",
    "plastic pollution map",
]

POSTS_PER_QUERY = 25
COMMENTS_PER_POST = 10


def collect_reddit():
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT", "pelagic_intelx_research/1.0")

    if not client_id or not client_secret:
        print("ERROR: REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET required in .env")
        sys.exit(1)

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )

    all_posts = []

    for subreddit_name in SUBREDDITS:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"\nSearching r/{subreddit_name}...")

        for query in SEARCH_QUERIES:
            print(f"  Query: '{query}'")
            try:
                for post in subreddit.search(query, limit=POSTS_PER_QUERY, sort="relevance", time_filter="year"):
                    post_data = {
                        "subreddit": subreddit_name,
                        "query": query,
                        "title": post.title,
                        "selftext": post.selftext[:2000] if post.selftext else "",
                        "score": post.score,
                        "num_comments": post.num_comments,
                        "created_utc": datetime.fromtimestamp(post.created_utc).isoformat(),
                        "url": post.url,
                        "permalink": f"https://reddit.com{post.permalink}",
                        "comments": [],
                    }

                    # Collect top comments
                    post.comments.replace_more(limit=0)
                    for comment in post.comments[:COMMENTS_PER_POST]:
                        post_data["comments"].append({
                            "body": comment.body[:1000],
                            "score": comment.score,
                        })

                    all_posts.append(post_data)
            except Exception as e:
                print(f"  Error: {e}")

    # Deduplicate by permalink
    seen = set()
    unique_posts = []
    for post in all_posts:
        if post["permalink"] not in seen:
            seen.add(post["permalink"])
            unique_posts.append(post)

    output = {
        "source": "reddit",
        "subreddits": SUBREDDITS,
        "queries": SEARCH_QUERIES,
        "post_count": len(unique_posts),
        "collected_at": datetime.now().isoformat(),
        "posts": unique_posts,
    }

    output_path = RAW_DIR / "reddit_posts.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nSaved {len(unique_posts)} unique posts to {output_path}")
    return output


if __name__ == "__main__":
    collect_reddit()
