"""
Framing Fidelity Analysis — Pelagic IntelX

Measures how well campaign-intended message frames survive downstream
propagation through media, social, and policy channels.

Method:
  1. Define SOURCE FRAMES — the exact language the campaign intends to seed
  2. Define DOWNSTREAM CORPUS — simulated media pickups, social shares,
     policy citations across 90-day campaign window
  3. Score each downstream mention against source frames using:
     - Exact match rate (frame appears verbatim)
     - Partial match rate (≥60% of frame tokens present)
     - Semantic drift score (Jaccard similarity of token sets)
  4. Aggregate by channel, frame, and time period
  5. Calculate overall Framing Fidelity Index (FFI)

Output: framing_fidelity.json → consumed by Chapter 5 KPI visualization
"""

import json
import random
import os
from collections import Counter
from datetime import datetime, timedelta

random.seed(42)

# ── SOURCE FRAMES ──────────────────────────────────────────────
# These are the exact phrases the campaign intends to seed
SOURCE_FRAMES = [
    {
        "id": "f1",
        "frame": "first AI-powered plastic density map",
        "category": "novelty",
        "priority": "primary",
    },
    {
        "id": "f2",
        "frame": "580,000 particles per square kilometer",
        "category": "scale",
        "priority": "primary",
    },
    {
        "id": "f3",
        "frame": "satellite-AI fusion pipeline",
        "category": "technology",
        "priority": "primary",
    },
    {
        "id": "f4",
        "frame": "40 percent above previous predictions",
        "category": "urgency",
        "priority": "primary",
    },
    {
        "id": "f5",
        "frame": "the ocean has a memory",
        "category": "narrative",
        "priority": "secondary",
    },
    {
        "id": "f6",
        "frame": "real-time density monitoring",
        "category": "capability",
        "priority": "secondary",
    },
    {
        "id": "f7",
        "frame": "evidentiary standard for international law",
        "category": "policy",
        "priority": "secondary",
    },
    {
        "id": "f8",
        "frame": "mapping the invisible",
        "category": "brand",
        "priority": "primary",
    },
]

# ── DOWNSTREAM CHANNELS ────────────────────────────────────────
CHANNELS = {
    "press": {
        "fidelity_base": 0.82,  # journalists tend to quote accurately
        "volume_base": 45,
        "drift_rate": 0.04,     # slow drift per period
    },
    "social": {
        "fidelity_base": 0.54,  # social paraphrases heavily
        "volume_base": 320,
        "drift_rate": 0.12,     # fast drift
    },
    "policy": {
        "fidelity_base": 0.91,  # policy docs quote precisely
        "volume_base": 12,
        "drift_rate": 0.02,     # very slow drift
    },
    "academic": {
        "fidelity_base": 0.88,  # academic citation is precise
        "volume_base": 8,
        "drift_rate": 0.03,
    },
}

# ── DOWNSTREAM MENTION VARIANTS ────────────────────────────────
# For each source frame, define how it mutates downstream
MUTATIONS = {
    "f1": {
        "exact": "first AI-powered plastic density map",
        "partial": [
            "AI-powered plastic map",
            "first AI plastic density map",
            "AI-driven plastic density mapping",
            "first AI map of ocean plastic",
        ],
        "drifted": [
            "new plastic map",
            "AI ocean map",
            "machine learning plastic tracker",
            "plastic pollution mapping tool",
            "computer-generated pollution map",
        ],
    },
    "f2": {
        "exact": "580,000 particles per square kilometer",
        "partial": [
            "580,000 particles per km²",
            "580K particles per square km",
            "nearly 600,000 particles per km²",
        ],
        "drifted": [
            "hundreds of thousands of particles",
            "massive particle concentrations",
            "extremely high plastic density",
            "more plastic than expected",
        ],
    },
    "f3": {
        "exact": "satellite-AI fusion pipeline",
        "partial": [
            "satellite and AI fusion",
            "satellite-AI data pipeline",
            "AI satellite fusion system",
        ],
        "drifted": [
            "satellite monitoring system",
            "AI analysis of satellite data",
            "space-based plastic tracking",
            "remote sensing technology",
        ],
    },
    "f4": {
        "exact": "40 percent above previous predictions",
        "partial": [
            "40% above predictions",
            "40 percent higher than predicted",
            "forty percent above earlier estimates",
        ],
        "drifted": [
            "significantly more than expected",
            "far exceeding predictions",
            "much worse than thought",
            "higher than models suggested",
        ],
    },
    "f5": {
        "exact": "the ocean has a memory",
        "partial": [
            "ocean has a memory",
            "the ocean remembers",
        ],
        "drifted": [
            "plastic accumulates over time",
            "ocean pollution is persistent",
            "the sea doesn't forget",
            "long-term ocean contamination",
        ],
    },
    "f6": {
        "exact": "real-time density monitoring",
        "partial": [
            "real-time plastic monitoring",
            "real-time density tracking",
            "live density monitoring",
        ],
        "drifted": [
            "continuous monitoring",
            "ongoing tracking system",
            "live pollution data",
            "always-on sensors",
        ],
    },
    "f7": {
        "exact": "evidentiary standard for international law",
        "partial": [
            "evidentiary standards for international regulation",
            "evidence standard for global treaties",
            "legal evidentiary standard",
        ],
        "drifted": [
            "evidence for policy",
            "data for regulation",
            "supporting treaty enforcement",
            "scientific evidence for lawmakers",
        ],
    },
    "f8": {
        "exact": "mapping the invisible",
        "partial": [
            "map the invisible",
            "mapping what's invisible",
            "making the invisible visible",
        ],
        "drifted": [
            "revealing hidden pollution",
            "seeing the unseen",
            "uncovering ocean plastic",
            "showing what we couldn't see",
        ],
    },
}


def tokenize(text):
    """Simple whitespace + lowercase tokenizer."""
    return set(text.lower().replace(",", "").replace("²", "").split())


def jaccard_similarity(set_a, set_b):
    """Jaccard index of two token sets."""
    if not set_a or not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)


def score_mention(source_tokens, mention_text, mention_type):
    """Score a single downstream mention against its source frame."""
    mention_tokens = tokenize(mention_text)
    jaccard = jaccard_similarity(source_tokens, mention_tokens)

    if mention_type == "exact":
        return {"exact_match": True, "partial_match": True, "jaccard": round(jaccard, 3), "fidelity": 1.0}
    elif mention_type == "partial":
        return {"exact_match": False, "partial_match": True, "jaccard": round(jaccard, 3), "fidelity": round(0.6 + jaccard * 0.3, 3)}
    else:
        return {"exact_match": False, "partial_match": False, "jaccard": round(jaccard, 3), "fidelity": round(jaccard * 0.7, 3)}


def generate_downstream_corpus(campaign_start, periods=6):
    """
    Generate simulated downstream mentions across 6 periods (15 days each = 90 days).
    Fidelity degrades over time as frames drift through re-sharing.
    """
    corpus = []

    for period_idx in range(periods):
        period_start = campaign_start + timedelta(days=period_idx * 15)
        period_end = period_start + timedelta(days=14)
        period_label = f"Day {period_idx * 15 + 1}–{(period_idx + 1) * 15}"

        for channel_name, channel_cfg in CHANNELS.items():
            # Volume scales down slightly over time (news cycle decay)
            volume_multiplier = max(0.3, 1.0 - period_idx * 0.1)
            if period_idx == 0:
                volume_multiplier = 1.4  # launch spike
            elif period_idx == 3:
                volume_multiplier = 0.9  # mid-campaign bump (op-ed)

            mention_count = max(1, int(channel_cfg["volume_base"] * volume_multiplier * random.uniform(0.8, 1.2)))

            # Fidelity degrades per period
            period_fidelity = max(0.25, channel_cfg["fidelity_base"] - period_idx * channel_cfg["drift_rate"])

            for _ in range(mention_count):
                # Pick a random source frame
                frame = random.choice(SOURCE_FRAMES)
                frame_id = frame["id"]
                source_tokens = tokenize(frame["frame"])
                mutations = MUTATIONS[frame_id]

                # Determine mention type based on period fidelity + noise
                roll = random.random()
                adjusted_fidelity = period_fidelity * random.uniform(0.85, 1.15)

                if roll < adjusted_fidelity * 0.4:
                    # Exact match
                    mention_text = mutations["exact"]
                    mention_type = "exact"
                elif roll < adjusted_fidelity * 0.85:
                    # Partial match
                    mention_text = random.choice(mutations["partial"])
                    mention_type = "partial"
                else:
                    # Drifted
                    mention_text = random.choice(mutations["drifted"])
                    mention_type = "drifted"

                scores = score_mention(source_tokens, mention_text, mention_type)

                corpus.append({
                    "period": period_label,
                    "period_idx": period_idx,
                    "channel": channel_name,
                    "frame_id": frame_id,
                    "frame_category": frame["category"],
                    "frame_priority": frame["priority"],
                    "source_frame": frame["frame"],
                    "downstream_text": mention_text,
                    "mention_type": mention_type,
                    **scores,
                })

    return corpus


def compute_aggregates(corpus):
    """Compute aggregate fidelity metrics from the scored corpus."""

    # ── Overall FFI ────────────────────────────────────
    total_fidelity = sum(m["fidelity"] for m in corpus)
    overall_ffi = round(total_fidelity / len(corpus), 4)

    exact_count = sum(1 for m in corpus if m["exact_match"])
    partial_count = sum(1 for m in corpus if m["partial_match"] and not m["exact_match"])
    drifted_count = sum(1 for m in corpus if not m["partial_match"])
    exact_rate = round(exact_count / len(corpus), 4)
    partial_rate = round(partial_count / len(corpus), 4)
    drift_rate = round(drifted_count / len(corpus), 4)

    # ── By channel ─────────────────────────────────────
    by_channel = {}
    for ch in CHANNELS:
        ch_mentions = [m for m in corpus if m["channel"] == ch]
        if not ch_mentions:
            continue
        ch_fidelity = sum(m["fidelity"] for m in ch_mentions) / len(ch_mentions)
        ch_exact = sum(1 for m in ch_mentions if m["exact_match"]) / len(ch_mentions)
        by_channel[ch] = {
            "mention_count": len(ch_mentions),
            "ffi": round(ch_fidelity, 4),
            "exact_rate": round(ch_exact, 4),
            "avg_jaccard": round(sum(m["jaccard"] for m in ch_mentions) / len(ch_mentions), 4),
        }

    # ── By frame ───────────────────────────────────────
    by_frame = {}
    for frame in SOURCE_FRAMES:
        f_mentions = [m for m in corpus if m["frame_id"] == frame["id"]]
        if not f_mentions:
            continue
        f_fidelity = sum(m["fidelity"] for m in f_mentions) / len(f_mentions)
        f_exact = sum(1 for m in f_mentions if m["exact_match"]) / len(f_mentions)
        by_frame[frame["id"]] = {
            "frame": frame["frame"],
            "category": frame["category"],
            "mention_count": len(f_mentions),
            "ffi": round(f_fidelity, 4),
            "exact_rate": round(f_exact, 4),
            "avg_jaccard": round(sum(m["jaccard"] for m in f_mentions) / len(f_mentions), 4),
        }

    # ── By period (fidelity over time) ─────────────────
    by_period = []
    for period_idx in range(6):
        p_mentions = [m for m in corpus if m["period_idx"] == period_idx]
        if not p_mentions:
            continue
        p_fidelity = sum(m["fidelity"] for m in p_mentions) / len(p_mentions)
        p_exact = sum(1 for m in p_mentions if m["exact_match"]) / len(p_mentions)
        by_period.append({
            "period": p_mentions[0]["period"],
            "period_idx": period_idx,
            "mention_count": len(p_mentions),
            "ffi": round(p_fidelity, 4),
            "exact_rate": round(p_exact, 4),
            "drift_rate": round(1.0 - p_fidelity, 4),
        })

    # ── By channel × period (for line chart) ───────────
    channel_period_series = {}
    for ch in CHANNELS:
        series = []
        for period_idx in range(6):
            cp_mentions = [m for m in corpus if m["channel"] == ch and m["period_idx"] == period_idx]
            if not cp_mentions:
                continue
            cp_fidelity = sum(m["fidelity"] for m in cp_mentions) / len(cp_mentions)
            series.append({
                "period": cp_mentions[0]["period"],
                "period_idx": period_idx,
                "ffi": round(cp_fidelity, 4),
                "mention_count": len(cp_mentions),
            })
        channel_period_series[ch] = series

    # ── Top drifted examples ───────────────────────────
    drifted_examples = [
        {
            "source_frame": m["source_frame"],
            "downstream_text": m["downstream_text"],
            "channel": m["channel"],
            "jaccard": m["jaccard"],
            "period": m["period"],
        }
        for m in corpus
        if m["mention_type"] == "drifted"
    ]
    # Sort by lowest jaccard (most drifted)
    drifted_examples.sort(key=lambda x: x["jaccard"])
    top_drift = drifted_examples[:10]

    return {
        "overall": {
            "ffi": overall_ffi,
            "total_mentions": len(corpus),
            "exact_rate": exact_rate,
            "partial_rate": partial_rate,
            "drift_rate": drift_rate,
            "exact_count": exact_count,
            "partial_count": partial_count,
            "drifted_count": drifted_count,
        },
        "by_channel": by_channel,
        "by_frame": by_frame,
        "by_period": by_period,
        "channel_period_series": channel_period_series,
        "top_drift_examples": top_drift,
    }


def main():
    campaign_start = datetime(2026, 4, 1)
    corpus = generate_downstream_corpus(campaign_start)
    aggregates = compute_aggregates(corpus)

    output = {
        "source": "framing_fidelity_analysis",
        "generated": datetime.now().isoformat(),
        "method": "token-level Jaccard similarity + exact/partial match scoring",
        "campaign_window": "90 days (6 × 15-day periods)",
        "source_frames_count": len(SOURCE_FRAMES),
        "channels_analyzed": list(CHANNELS.keys()),
        "seed": 42,
        "metrics": aggregates,
        "source_frames": SOURCE_FRAMES,
    }

    # Write to processed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_dir = os.path.join(script_dir, "..", "processed")
    os.makedirs(processed_dir, exist_ok=True)

    out_path = os.path.join(processed_dir, "framing_fidelity.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Wrote {out_path} ({len(corpus)} scored mentions)")

    # Also copy to src/data for frontend
    src_data_dir = os.path.join(script_dir, "..", "..", "src", "data")
    os.makedirs(src_data_dir, exist_ok=True)
    src_path = os.path.join(src_data_dir, "framing_fidelity.json")
    with open(src_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Wrote {src_path}")


if __name__ == "__main__":
    main()
