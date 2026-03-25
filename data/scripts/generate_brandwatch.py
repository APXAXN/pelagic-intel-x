"""
Pelagic IntelX — Brandwatch Social Listening Sample Data
Generates realistic social listening data representing what a Brandwatch export would contain.
Output: data/processed/brandwatch_mentions.json
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

PROCESSED_DIR = Path(__file__).parent.parent / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

random.seed(42)

# Simulate 12 months of social listening data
START_DATE = datetime(2025, 4, 1)
END_DATE = datetime(2026, 3, 24)

TOPICS = [
    "ocean plastic pollution",
    "microplastics",
    "AI environmental monitoring",
    "ocean cleanup technology",
    "marine debris",
    "plastic pollution regulation",
]

SOURCES = ["twitter", "news", "blogs", "forums", "reddit", "instagram"]

SENTIMENT_LABELS = ["positive", "negative", "neutral"]


def generate_daily_mentions():
    """Generate daily mention volume with realistic patterns."""
    data = []
    current = START_DATE

    # Base mention volumes per topic
    base_volumes = {
        "ocean plastic pollution": 850,
        "microplastics": 620,
        "AI environmental monitoring": 180,
        "ocean cleanup technology": 340,
        "marine debris": 210,
        "plastic pollution regulation": 290,
    }

    # Spike events (dates where mentions surge — tied to real-world patterns)
    spike_events = [
        {"date": datetime(2025, 6, 8), "topic": "ocean plastic pollution", "multiplier": 4.5, "label": "World Ocean Day"},
        {"date": datetime(2025, 6, 5), "topic": "ocean plastic pollution", "multiplier": 3.0, "label": "World Environment Day"},
        {"date": datetime(2025, 9, 15), "topic": "microplastics", "multiplier": 3.5, "label": "WHO microplastics report"},
        {"date": datetime(2025, 11, 1), "topic": "plastic pollution regulation", "multiplier": 5.0, "label": "Global Plastics Treaty round"},
        {"date": datetime(2025, 11, 2), "topic": "plastic pollution regulation", "multiplier": 4.0, "label": "Treaty coverage"},
        {"date": datetime(2025, 7, 20), "topic": "AI environmental monitoring", "multiplier": 3.0, "label": "Major AI+climate paper"},
        {"date": datetime(2026, 1, 15), "topic": "ocean cleanup technology", "multiplier": 3.5, "label": "Ocean Cleanup milestone"},
        {"date": datetime(2026, 2, 1), "topic": "microplastics", "multiplier": 2.5, "label": "Microplastics in blood study"},
    ]

    while current <= END_DATE:
        for topic in TOPICS:
            base = base_volumes[topic]

            # Day-of-week variation (weekdays higher)
            dow_factor = 1.15 if current.weekday() < 5 else 0.75

            # Seasonal trend (summer months slightly higher for ocean topics)
            month = current.month
            seasonal = 1.0
            if month in [6, 7, 8]:
                seasonal = 1.25 if "ocean" in topic else 1.1

            # Check for spike events
            spike = 1.0
            event_label = None
            for event in spike_events:
                days_diff = abs((current - event["date"]).days)
                if event["topic"] == topic and days_diff <= 2:
                    spike = event["multiplier"] * max(0.3, 1 - days_diff * 0.3)
                    event_label = event["label"]

            # Overall upward trend (growing awareness)
            days_elapsed = (current - START_DATE).days
            trend = 1.0 + (days_elapsed / 365) * 0.15  # 15% annual growth

            volume = int(base * dow_factor * seasonal * spike * trend + random.gauss(0, base * 0.1))
            volume = max(0, volume)

            # Sentiment distribution (varies by topic)
            if "regulation" in topic:
                sent_dist = {"positive": 0.25, "negative": 0.45, "neutral": 0.30}
            elif "cleanup" in topic or "AI" in topic:
                sent_dist = {"positive": 0.55, "negative": 0.15, "neutral": 0.30}
            else:
                sent_dist = {"positive": 0.20, "negative": 0.50, "neutral": 0.30}

            # Source distribution
            source_dist = {
                "twitter": 0.40,
                "news": 0.20,
                "reddit": 0.12,
                "blogs": 0.10,
                "forums": 0.08,
                "instagram": 0.10,
            }

            entry = {
                "date": current.strftime("%Y-%m-%d"),
                "topic": topic,
                "mention_volume": volume,
                "sentiment": {
                    s: int(volume * p + random.gauss(0, volume * 0.02))
                    for s, p in sent_dist.items()
                },
                "sources": {
                    s: int(volume * p + random.gauss(0, volume * 0.02))
                    for s, p in source_dist.items()
                },
            }

            if event_label:
                entry["event"] = event_label

            data.append(entry)

        current += timedelta(days=1)

    return data


def generate_top_mentions():
    """Generate sample high-engagement mentions."""
    return [
        {
            "text": "New study finds microplastics in 90% of table salt brands worldwide. We're literally eating the ocean's plastic problem.",
            "source": "twitter",
            "engagement": 45200,
            "sentiment": "negative",
            "date": "2025-09-18",
        },
        {
            "text": "AI-powered satellite monitoring could finally give us a real-time picture of ocean plastic distribution. This changes the cleanup calculus entirely.",
            "source": "twitter",
            "engagement": 12800,
            "sentiment": "positive",
            "date": "2025-07-22",
        },
        {
            "text": "The Global Plastics Treaty negotiations just wrapped with no binding reduction targets. Again. How many rounds before we admit voluntary commitments don't work?",
            "source": "twitter",
            "engagement": 38500,
            "sentiment": "negative",
            "date": "2025-11-03",
        },
        {
            "text": "Researchers mapped microplastic concentration in the Pacific using computer vision on satellite data. Density is 40% higher than previous estimates in some zones.",
            "source": "news",
            "engagement": 8900,
            "sentiment": "negative",
            "date": "2025-08-14",
        },
        {
            "text": "The Ocean Cleanup just announced they've removed 50 million kg of trash from the Great Pacific Garbage Patch. But scientists warn the inflow rate still exceeds cleanup capacity.",
            "source": "news",
            "engagement": 67000,
            "sentiment": "neutral",
            "date": "2026-01-16",
        },
    ]


def compute_summary(daily_data):
    """Compute aggregate summary statistics."""
    total_mentions = sum(d["mention_volume"] for d in daily_data)
    topic_totals = {}
    for d in daily_data:
        topic_totals[d["topic"]] = topic_totals.get(d["topic"], 0) + d["mention_volume"]

    sentiment_totals = {"positive": 0, "negative": 0, "neutral": 0}
    for d in daily_data:
        for s, v in d["sentiment"].items():
            sentiment_totals[s] = sentiment_totals.get(s, 0) + v

    return {
        "total_mentions": total_mentions,
        "date_range": f"{START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}",
        "topic_totals": dict(sorted(topic_totals.items(), key=lambda x: -x[1])),
        "sentiment_totals": sentiment_totals,
        "avg_daily_mentions": total_mentions // ((END_DATE - START_DATE).days),
    }


def main():
    print("Generating Brandwatch social listening sample data...")

    daily_data = generate_daily_mentions()
    top_mentions = generate_top_mentions()
    summary = compute_summary(daily_data)

    print(f"Generated {len(daily_data)} daily data points")
    print(f"Total mentions: {summary['total_mentions']:,}")
    print(f"Date range: {summary['date_range']}")
    print(f"\nTopic volumes:")
    for topic, vol in summary["topic_totals"].items():
        print(f"  {topic}: {vol:,}")

    output = {
        "source": "brandwatch_simulated",
        "note": "Simulated social listening data for portfolio purposes. Structure mirrors Brandwatch export format.",
        "summary": summary,
        "daily": daily_data,
        "top_mentions": top_mentions,
    }

    output_path = PROCESSED_DIR / "brandwatch_mentions.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nSaved to {output_path}")


if __name__ == "__main__":
    main()
