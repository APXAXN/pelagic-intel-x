"""
Pelagic IntelX — NLP Processing Pipeline
Processes Reddit corpus for word frequency, key phrases, and vocabulary gap analysis.
Outputs: data/processed/reddit_word_freq.json, data/processed/vocabulary_gap.json
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# Download required NLTK data
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

RAW_DIR = Path(__file__).parent.parent / "raw"
PROCESSED_DIR = Path(__file__).parent.parent / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

# Scientific vocabulary (how researchers talk about ocean plastic)
SCIENTIFIC_TERMS = {
    "particulate distribution", "density mapping", "microplastic concentration",
    "polymer identification", "spectroscopic analysis", "surface accumulation",
    "pelagic zone", "gyral accumulation", "anthropogenic debris",
    "marine litter", "plastic flux", "bioaccumulation",
    "trophic transfer", "fragmentation rate", "weathering",
    "nanoplastics", "polymer type", "environmental persistence",
    "spatial distribution", "temporal variation", "sampling methodology",
}

# Public vocabulary (how people actually talk about ocean plastic)
PUBLIC_TERMS = {
    "where is the plastic", "how bad is it", "can we see it",
    "ocean garbage", "trash island", "garbage patch",
    "plastic in fish", "plastic in water", "cleanup",
    "ban plastic", "reduce plastic", "recycling doesn't work",
    "microplastics in food", "plastic pollution", "ocean trash",
    "save the ocean", "plastic waste", "single use plastic",
    "plastic crisis", "toxic plastic", "plastic everywhere",
}

# Custom stop words for this domain
DOMAIN_STOPWORDS = {
    "would", "could", "also", "like", "one", "get", "think",
    "know", "really", "even", "much", "going", "thing", "things",
    "way", "still", "well", "actually", "just", "people", "make",
    "good", "new", "use", "used", "using", "many", "lot",
    "say", "said", "says", "want", "need", "see", "take",
    "come", "go", "got", "back", "look", "year", "years",
    "http", "https", "www", "com", "org", "reddit", "removed",
    "deleted", "amp", "edit", "source", "link",
}


def load_reddit_data():
    """Load Reddit posts from raw data."""
    reddit_path = RAW_DIR / "reddit_posts.json"
    if not reddit_path.exists():
        print("ERROR: reddit_posts.json not found. Run collect_reddit.py first.")
        sys.exit(1)

    with open(reddit_path) as f:
        data = json.load(f)
    return data


def extract_text_corpus(data):
    """Extract all text from posts and comments."""
    texts = []
    for post in data["posts"]:
        texts.append(post["title"])
        if post["selftext"]:
            texts.append(post["selftext"])
        for comment in post["comments"]:
            texts.append(comment["body"])
    return texts


def clean_text(text):
    """Clean text for NLP processing."""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", " ", text)  # Keep only letters
    text = re.sub(r"\s+", " ", text).strip()
    return text


def compute_word_frequencies(texts):
    """Compute word frequencies from corpus."""
    stop_words = set(stopwords.words("english")) | DOMAIN_STOPWORDS
    all_words = []

    for text in texts:
        cleaned = clean_text(text)
        tokens = word_tokenize(cleaned)
        words = [w for w in tokens if len(w) > 2 and w not in stop_words]
        all_words.extend(words)

    freq = Counter(all_words)
    top_words = freq.most_common(100)

    # Per-subreddit frequencies
    return {
        "total_words": len(all_words),
        "unique_words": len(freq),
        "top_100": [{"word": w, "count": c} for w, c in top_words],
    }


def compute_bigrams(texts):
    """Find significant bigram collocations."""
    stop_words = set(stopwords.words("english")) | DOMAIN_STOPWORDS
    all_words = []

    for text in texts:
        cleaned = clean_text(text)
        tokens = word_tokenize(cleaned)
        words = [w for w in tokens if len(w) > 2 and w not in stop_words]
        all_words.extend(words)

    finder = BigramCollocationFinder.from_words(all_words)
    finder.apply_freq_filter(3)
    scored = finder.score_ngrams(BigramAssocMeasures.pmi)

    return [
        {"phrase": f"{w1} {w2}", "score": round(score, 2)}
        for (w1, w2), score in scored[:50]
    ]


def compute_per_subreddit(data):
    """Compute word frequencies per subreddit."""
    subreddit_texts = {}
    for post in data["posts"]:
        sub = post["subreddit"]
        if sub not in subreddit_texts:
            subreddit_texts[sub] = []
        subreddit_texts[sub].append(post["title"])
        if post["selftext"]:
            subreddit_texts[sub].append(post["selftext"])
        for comment in post["comments"]:
            subreddit_texts[sub].append(comment["body"])

    stop_words = set(stopwords.words("english")) | DOMAIN_STOPWORDS
    per_sub = {}

    for sub, texts in subreddit_texts.items():
        all_words = []
        for text in texts:
            cleaned = clean_text(text)
            tokens = word_tokenize(cleaned)
            words = [w for w in tokens if len(w) > 2 and w not in stop_words]
            all_words.extend(words)

        freq = Counter(all_words)
        per_sub[sub] = {
            "total_words": len(all_words),
            "top_25": [{"word": w, "count": c} for w, c in freq.most_common(25)],
        }

    return per_sub


def vocabulary_gap_analysis(texts):
    """Analyze gap between scientific and public vocabulary in the corpus."""
    full_corpus = " ".join(clean_text(t) for t in texts)

    # Count occurrences of scientific terms
    scientific_counts = {}
    for term in SCIENTIFIC_TERMS:
        count = full_corpus.count(term.lower())
        if count > 0:
            scientific_counts[term] = count

    # Count occurrences of public terms
    public_counts = {}
    for term in PUBLIC_TERMS:
        count = full_corpus.count(term.lower())
        if count > 0:
            public_counts[term] = count

    # Terms unique to each register
    scientific_found = set(scientific_counts.keys())
    public_found = set(public_counts.keys())

    return {
        "scientific_terms_found": len(scientific_found),
        "public_terms_found": len(public_found),
        "scientific_term_counts": [
            {"term": t, "count": c}
            for t, c in sorted(scientific_counts.items(), key=lambda x: -x[1])
        ],
        "public_term_counts": [
            {"term": t, "count": c}
            for t, c in sorted(public_counts.items(), key=lambda x: -x[1])
        ],
        "gap_insight": (
            "Scientific discourse favors precise measurement language "
            "(density, distribution, concentration) while public conversation "
            "uses spatial and emotional framing (where is it, how bad, can we see it). "
            "The campaign must bridge this gap — offering visual answers to public "
            "questions while maintaining scientific credibility."
        ),
    }


def main():
    print("Loading Reddit data...")
    data = load_reddit_data()
    texts = extract_text_corpus(data)
    print(f"Corpus: {len(texts)} text segments from {data['post_count']} posts")

    print("\nComputing word frequencies...")
    word_freq = compute_word_frequencies(texts)
    print(f"  {word_freq['total_words']} total words, {word_freq['unique_words']} unique")

    print("Computing bigram collocations...")
    bigrams = compute_bigrams(texts)

    print("Computing per-subreddit frequencies...")
    per_subreddit = compute_per_subreddit(data)

    print("Running vocabulary gap analysis...")
    vocab_gap = vocabulary_gap_analysis(texts)

    # Save word frequency output
    freq_output = {
        "source": "reddit_nlp",
        "corpus_size": word_freq["total_words"],
        "unique_words": word_freq["unique_words"],
        "top_words": word_freq["top_100"],
        "bigram_collocations": bigrams,
        "per_subreddit": per_subreddit,
    }

    freq_path = PROCESSED_DIR / "reddit_word_freq.json"
    with open(freq_path, "w") as f:
        json.dump(freq_output, f, indent=2)
    print(f"\nSaved word frequencies to {freq_path}")

    # Save vocabulary gap output
    gap_path = PROCESSED_DIR / "vocabulary_gap.json"
    with open(gap_path, "w") as f:
        json.dump(vocab_gap, f, indent=2)
    print(f"Saved vocabulary gap analysis to {gap_path}")


if __name__ == "__main__":
    main()
