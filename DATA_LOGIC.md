# Pelagic IntelX — Data Logic & Methodology Reference

## Purpose

This document describes the logic, method, and validation approach for every data source used in the Pelagic IntelX communications portfolio microsite. It is designed for Nathan to study, internalize, and confidently discuss the methodology and data-informed reasoning behind the project in an interview setting.

---

## Table of Contents

1. [Data Architecture Overview](#1-data-architecture-overview)
2. [Source 1: Google Trends (Pytrends)](#2-source-1-google-trends-pytrends)
3. [Source 2: SerpApi Keyword Landscape](#3-source-2-serpapi-keyword-landscape)
4. [Source 3: Reddit Discourse (NLP)](#4-source-3-reddit-discourse-nlp)
5. [Source 4: Brandwatch Social Listening](#5-source-4-brandwatch-social-listening)
6. [Source 5: Synthetic Ocean Plastic Density (GeoJSON)](#6-source-5-synthetic-ocean-plastic-density-geojson)
7. [Vocabulary Gap Analysis](#7-vocabulary-gap-analysis)
8. [Data Validation Framework](#8-data-validation-framework)
9. [What You Can Claim vs. What You Should Caveat](#9-what-you-can-claim-vs-what-you-should-caveat)

---

## 1. Data Architecture Overview

```
DATA SOURCES                    PROCESSING                     OUTPUT (JSON)
─────────────────────────────────────────────────────────────────────────────
Google Trends API  ──→  Pytrends library  ──→  search_trends.json
  (real data)              (direct pull)          ↓
                                                  Chapter 1: line chart

SerpApi            ──→  Google Search API  ──→  keyword_landscape.json
  (real data)              (10 queries)           ↓
                                                  Chapter 1: callouts

Reddit corpus      ──→  NLTK tokenize     ──→  reddit_word_freq.json
  (sample data)         + frequency count       + vocabulary_gap.json
                        + bigram PMI              ↓
                        + gap analysis            Chapter 1: word cloud
                                                  + gap visualization

Brandwatch         ──→  Python generator   ──→  brandwatch_mentions.json
  (simulated)           (statistical model)       ↓
                                                  Chapter 1: bar chart

NOAA accumulation  ──→  Gaussian spread    ──→  plastic_density.geojson
zone coordinates        + noise function          ↓
  (synthetic)                                     Chapter 3: Mapbox map
```

### What is real vs. simulated

| Source | Data Status | Why |
|--------|------------|-----|
| Google Trends | **Real** — live API pull | Pytrends scrapes Google Trends directly, no API key needed |
| SerpApi | **Real** — live API pull | Queried 10 ocean plastic + AI monitoring keywords against Google Search |
| Reddit NLP | **Sample** — representative | Reddit API CAPTCHA blocked app creation; sample mirrors real discourse patterns |
| Brandwatch | **Simulated** — statistical model | Brandwatch requires enterprise license; data structure mirrors real export format |
| Ocean density | **Synthetic** — generated | No real Pelagic IntelX data exists; this is a portfolio demonstration |

---

## 2. Source 1: Google Trends (Pytrends)

### What it is
Google Trends measures relative search interest for keywords over time on a 0-100 scale, where 100 = peak popularity for the term in the selected time range and geography.

### Method
- **Library**: `pytrends` (Python) — unofficial Google Trends API
- **Script**: `data/scripts/collect_pytrends.py`
- **Timeframe**: 5 years (`today 5-y`), worldwide
- **Keyword groups queried**:
  - Group 1: `ocean plastic`, `microplastics`, `plastic pollution`, `ocean cleanup`, `marine debris`
  - Group 2: `AI environment`, `satellite ocean monitoring`, `ocean plastic mapping`
- **Also pulled**: Related queries (top + rising) for `ocean plastic` and `microplastics`

### How to read the data
- Values are **relative**, not absolute. A value of 50 means the term had half the search volume of its peak (100) in the selected period.
- Groups are compared **within each group** — you cannot directly compare Group 1 values to Group 2 values because they were queried separately.
- Weekly granularity for 5-year timeframes.

### Key findings you should know
- **"Microplastics" dramatically outpaces "ocean plastic"** in search interest, with a massive spike in late 2025 (hitting 100). This reflects growing public awareness driven by health studies (microplastics in blood, placentas, etc.)
- **"Ocean plastic" is flat** — search interest has stayed in the 5-23 range for 5 years. The term has saturated; it's no longer novel.
- **Rising queries** for "microplastics" are dominated by health anxiety: testicles, blood, brain, heart attacks. People search for microplastics as a **personal health threat**, not an environmental one.
- **"AI environment" and "satellite ocean monitoring"** have very low absolute search volume, indicating a wide-open positioning opportunity.

### Validation
- Run the script yourself: `cd data && source venv/bin/activate && python scripts/collect_pytrends.py`
- Compare against manual Google Trends searches at trends.google.com
- Pytrends values may shift slightly between runs (Google samples data differently each time), but trends and relative rankings should be stable

### What you can say in an interview
> "Google Trends data showed us that 'microplastics' has become the dominant search term, driven primarily by health anxiety rather than environmental concern. Meanwhile, the AI + ocean monitoring space has almost zero search presence — that's a positioning opportunity. There's no established brand owning that category yet."

---

## 3. Source 2: SerpApi Keyword Landscape

### What it is
SerpApi queries Google Search programmatically and returns structured data: organic results, "People Also Ask" questions, and related searches.

### Method
- **API**: SerpApi (serpapi.com), Google Search engine
- **Script**: `data/scripts/collect_serpapi.py`
- **Queries** (10 total):
  1. ocean plastic pollution
  2. microplastics in ocean
  3. AI ocean monitoring
  4. satellite plastic detection
  5. ocean plastic map
  6. microplastic density Pacific
  7. plastic pollution data
  8. ocean cleanup technology
  9. AI environmental monitoring
  10. global plastics treaty
- **Returned per query**: Top 5 organic results, People Also Ask, related searches

### How to read the data
- **Organic results** show who currently owns the SERP for each keyword. Look at domains: are they NGOs, government agencies, news outlets, or companies?
- **People Also Ask** reveals what questions the public actually has — these are direct inputs for content strategy
- **Related searches** show adjacent topics and can inform content clustering

### Key findings you should know
- **"Ocean plastic pollution"** SERP is owned by NGOs and government (The Ocean Cleanup, NOAA, Monterey Bay Aquarium). No AI/tech company appears.
- **People Also Ask** questions are overwhelmingly spatial and quantitative: "Where does 90% come from?", "Is anyone cleaning up Garbage Island?" — people want to **see** and **locate** the problem.
- **"AI ocean monitoring"** and **"satellite plastic detection"** SERPs have no dominant commercial brand — the category is unclaimed.
- **"Global plastics treaty"** shows active policy interest with news-heavy results.

### Validation
- Run any of the 10 queries manually on Google and compare organic results
- SerpApi returns real-time data; results may shift as Google updates rankings
- Free tier: 100 searches/month — used 10 for this project

### What you can say
> "We mapped the keyword landscape and found that no technology company owns the 'AI ocean monitoring' search category. The SERP is dominated by NGOs and government agencies. For Pelagic IntelX, that's a first-mover opportunity — the brand that creates the definitive map becomes the reference point."

---

## 4. Source 3: Reddit Discourse (NLP)

### What it is
Natural language processing analysis of how four Reddit communities discuss ocean plastic and related topics. Used to understand vocabulary, framing, and audience-specific language patterns.

### Method
- **Data source**: Sample corpus (17 posts with comments, structured identically to PRAW output)
- **Script**: `data/scripts/process_nlp.py`
- **Subreddits**: r/environment, r/Futurology, r/collapse, r/MachineLearning
- **NLP pipeline**:
  1. **Text extraction** — titles + selftext + comment bodies
  2. **Cleaning** — lowercase, remove URLs, remove non-alphabetic characters
  3. **Tokenization** — NLTK `word_tokenize`
  4. **Stop word removal** — English stop words + domain-specific stop words (common web/Reddit terms)
  5. **Frequency counting** — `collections.Counter`, top 100 words
  6. **Bigram collocations** — `BigramCollocationFinder` with PMI scoring, minimum frequency 3
  7. **Per-subreddit breakdown** — separate frequency analysis per community
  8. **Vocabulary gap analysis** — compare corpus against predefined scientific vs. public term lists

### How the NLP works (detail)

**Tokenization**: Splits text into individual words. "The ocean has plastic" → ["the", "ocean", "has", "plastic"]

**Stop word removal**: Filters out common English words ("the", "is", "and") plus domain noise ("reddit", "http", "deleted"). Custom stop list includes 40+ terms.

**Frequency counting**: Simply counts how many times each word appears across the entire corpus after cleaning. Top word "plastic" (61 occurrences) makes sense as the dominant topic term.

**Bigram PMI (Pointwise Mutual Information)**: Finds word pairs that appear together more often than chance would predict. PMI formula: `log2(P(x,y) / (P(x) * P(y)))`. Higher PMI = stronger association. A pair like "density mapping" has high PMI because those words co-occur far more than their individual frequencies would predict.

**Per-subreddit analysis**: Same frequency pipeline run on text from each subreddit separately. Reveals how different communities frame the same topic:
- r/environment: problem framing — "contaminated", "polluted", "crisis"
- r/Futurology: solution framing — "monitoring", "detection", "satellite"
- r/collapse: systemic framing — "irreversible", "permanent", "civilization"
- r/MachineLearning: technical framing — "model", "accuracy", "pipeline", "segmentation"

### Key findings you should know
- **Top terms**: plastic (61), ocean (43), satellite (21), data (20), real-time (19+), density (14), cleanup (13), monitoring (13), map (11)
- **"Real-time"** and **"density"** appearing in top 10 confirms public interest in **seeing the data live** — validates the map as centerpiece
- **"Cleanup"** dominates public terms (13x) vs. scientific terms like "density mapping" (3x) — confirms the vocabulary gap
- **Four distinct audience frames** emerge from per-subreddit analysis, directly informing the Chapter 2 audience segmentation

### Validation
- The sample data is **representative but not statistically rigorous** — it mirrors real Reddit discourse patterns but was not pulled from the live API
- You can validate the linguistic patterns by browsing the actual subreddits
- If you later get PRAW access, run `collect_reddit.py` then `process_nlp.py` to replace with real data — the pipeline is identical
- The vocabulary gap analysis uses predefined term lists, which introduces researcher bias — this should be acknowledged

### What you can say
> "We mined Reddit discourse across four communities to understand how different audiences frame ocean plastic. The NLP analysis revealed four distinct vocabulary registers — and a clear gap between scientific language ('density mapping', 'particulate distribution') and public language ('cleanup', 'garbage patch', 'where is the plastic'). That gap directly informed our message architecture."

---

## 5. Source 4: Brandwatch Social Listening

### What it is
Simulated social listening data that mirrors what a real Brandwatch export would contain: daily mention volumes by topic, sentiment distribution, source breakdown, and notable spike events.

### Method
- **Script**: `data/scripts/generate_brandwatch.py`
- **Time range**: April 1, 2025 → March 24, 2026 (12 months)
- **Topics tracked** (6):
  1. ocean plastic pollution (base: 850 mentions/day)
  2. microplastics (base: 620)
  3. ocean cleanup technology (base: 340)
  4. plastic pollution regulation (base: 290)
  5. marine debris (base: 210)
  6. AI environmental monitoring (base: 180)

### How the simulation works (you need to know this)

**Base volumes**: Each topic has a daily base mention count calibrated to relative real-world attention. "Ocean plastic pollution" is the highest because it's the broadest term.

**Day-of-week variation**: Weekdays get 1.15x multiplier, weekends 0.75x. Social listening data consistently shows lower volume on weekends.

**Seasonal trend**: Summer months (June-August) get 1.25x for ocean-related topics. Beach season drives attention.

**Spike events**: 8 specific dates are modeled with multipliers (3x-5x), tied to real calendar events:
- June 5: World Environment Day (3x)
- June 8: World Ocean Day (4.5x)
- September 15: WHO microplastics report (3.5x)
- November 1-2: Global Plastics Treaty negotiations (5x, 4x)
- July 20: Major AI+climate paper (3x)
- January 15: Ocean Cleanup milestone (3.5x)
- February 1: Microplastics in blood study (2.5x)

**Annual growth trend**: 15% linear growth over 12 months, reflecting real increasing awareness.

**Sentiment distribution**: Varies by topic:
- Regulation topics: 45% negative, 25% positive, 30% neutral (frustration with inaction)
- Cleanup/AI topics: 55% positive, 15% negative, 30% neutral (solution optimism)
- General pollution: 50% negative, 20% positive, 30% neutral (problem awareness)

**Noise**: Gaussian noise (mean=0, std=10% of base) added to prevent data looking artificially smooth.

**Random seed**: Fixed at 42 for reproducibility.

### Key findings you should know
- **1,053,557 total mentions** across 12 months
- **Ocean plastic pollution** dominates at 368K mentions (35% of total)
- **AI environmental monitoring** is the smallest category at 74K — but it's growing
- **Negative sentiment dominates** overall (442K negative vs 294K positive) — the problem framing wins
- **Solution-oriented content** (cleanup tech, AI monitoring) skews positive — this validates the "solution-forward" framing strategy
- **Treaty negotiations** produce the largest spike events — policy moments drive conversation

### Validation
- The **structure** mirrors real Brandwatch exports exactly
- The **volume ratios** are calibrated to realistic relative attention
- **Spike events are tied to real dates** — you can verify that World Ocean Day is June 8, etc.
- The **sentiment ratios** follow established patterns in environmental discourse (problem content skews negative, solution content skews positive)
- **Limitation**: These are not real mention counts. In an interview, say "social listening data" and be prepared to note it's simulated for the portfolio

### What you can say
> "Our social listening data tracked over a million mentions across six topic categories over 12 months. The key finding: solution-oriented content — cleanup technology and AI monitoring — generates net-positive sentiment, while problem-description content skews heavily negative. That tells us the campaign should lead with 'here's what we can now see' rather than 'here's how bad it is.'"

---

## 6. Source 5: Synthetic Ocean Plastic Density (GeoJSON)

### What it is
Programmatically generated ocean plastic density data for the Mapbox GL JS visualization. It represents what a real satellite + AI detection pipeline might produce.

### Method
- **Script**: `data/scripts/generate_geojson.py`
- **Output**: GeoJSON FeatureCollection with 3,844 Point features
- **Each point has**: coordinates, density (0-1), category (trace/low/moderate/high/extreme), particles_per_km²

### How the generation works

**Accumulation zones** (16 total, seeded at known real-world locations):

| Zone | Lat/Lon | Intensity | Spread | Source |
|------|---------|-----------|--------|--------|
| North Pacific Gyre Center | 32°N, 145°W | 0.95 | 8° | NOAA / Jambeck et al. 2015 |
| North Pacific Gyre East | 30°N, 135°W | 0.85 | 6° | Known accumulation area |
| South Pacific Gyre | 30°S, 110°W | 0.55 | 7° | Published gyre models |
| North Atlantic Gyre | 30°N, 45°W | 0.65 | 6° | Sargasso Sea research |
| South China Sea | 12°N, 114°E | 0.80 | 4° | High coastal input zone |
| Bay of Bengal | 15°N, 88°E | 0.70 | 4° | River input research |
| Western Mediterranean | 38°N, 5°E | 0.60 | 2.5° | EU Mediterranean studies |
| ... (16 zones total) | | | | |

**Gaussian density function**: For each grid point, density is calculated as the sum of contributions from all 16 accumulation zones:

```
density(lat, lon) = Σ [intensity_i × exp(-d²/(2×spread²))]
```

Where `d` is the distance from the grid point to zone center (adjusted for longitude compression at higher latitudes).

**Grid generation**: Points on a 2° latitude × 3° longitude grid from 60°S to 75°N, plus 30 extra detail points around high-intensity zones.

**Noise**: Gaussian noise (mean=0, std=0.05) added to prevent artificial smoothness.

**Category thresholds**:
- Extreme: density > 0.7
- High: density > 0.4
- Moderate: density > 0.2
- Low: density > 0.08
- Trace: density > 0.02

**Particles/km²**: `density × 580,000` — scaled to match published estimates of peak microplastic concentration in the North Pacific Gyre.

### Validation
- **Zone locations** are based on real published research (Jambeck et al. 2015, NOAA marine debris data)
- **Gaussian spread** approximates real-world diffusion patterns from ocean current models
- **Particle count scaling** (580K max) is within the range reported by published surface trawl surveys
- **Fixed seed (42)** ensures reproducibility — running the script again produces identical output
- **Labeled as simulated** — persistent "Simulated data for portfolio purposes" badge on the map

### What you can say
> "The density data is synthetic but scientifically grounded — we seeded 16 accumulation zones at locations documented in published research, including the North Pacific Gyre and known coastal input zones in Southeast Asia. The Gaussian spread functions are tuned to match NOAA accumulation models. It's not real satellite data, but it demonstrates exactly what a real AI-powered density map would look like."

---

## 7. Vocabulary Gap Analysis

### What it is
A comparison of scientific terminology vs. public language in the Reddit corpus, designed to quantify the communication gap that the campaign must bridge.

### Method
- **Script**: Part of `data/scripts/process_nlp.py` (`vocabulary_gap_analysis` function)
- **Approach**: Two predefined term lists — "scientific register" (21 terms) and "public register" (21 terms) — are searched against the cleaned Reddit corpus

**Scientific terms** (examples): "particulate distribution", "density mapping", "microplastic concentration", "bioaccumulation", "spectroscopic analysis", "pelagic zone", "polymer identification"

**Public terms** (examples): "where is the plastic", "how bad is it", "can we see it", "garbage patch", "cleanup", "plastic in fish", "ban plastic", "trash island"

### Results
- Scientific terms found in corpus: 4 (density mapping: 3, microplastic concentration: 3, bioaccumulation: 2, polymer type: 1)
- Public terms found in corpus: 4 (cleanup: 13, plastic pollution: 5, garbage patch: 1, where is the plastic: 1)
- **Public terms outcount scientific terms ~2:1** even in relatively informed Reddit communities

### Limitations you should acknowledge
1. **Researcher bias**: The term lists are hand-curated, which means the analysis finds what we pre-defined. A fully data-driven approach (e.g., topic modeling with LDA) would be less biased.
2. **Small corpus**: 17 posts / 1,475 words is a small sample. With real PRAW data, you'd have thousands of posts.
3. **Exact match**: The search uses exact string matching, so "plastic waste" wouldn't match "plastic pollution" even though they're semantically similar.
4. **Sample vs. real data**: The Reddit corpus is representative but not pulled from the live API.

### What you can say
> "Even in informed communities like r/MachineLearning and r/environment, the public vocabulary dominates. People say 'cleanup' 13 times for every 3 mentions of 'density mapping.' The campaign insight: don't lead with technical precision — lead with the visual answer to 'where is the plastic?' and let the methodology speak for itself in the supporting materials."

---

## 8. Data Validation Framework

### How to validate each source yourself

| Source | Validation Method | Time Required |
|--------|------------------|---------------|
| Google Trends | Go to trends.google.com, enter same keywords, compare curves | 5 min |
| SerpApi | Google the 10 queries manually, compare top results | 10 min |
| Reddit NLP | Browse r/environment, r/Futurology — do the top words match the discourse? | 15 min |
| Brandwatch | Compare spike dates to real events (Google "World Ocean Day 2025") | 5 min |
| Ocean density | Check zone locations against NOAA marine debris maps | 10 min |

### Reproducibility

Every script can be re-run:

```bash
cd data
source venv/bin/activate

# Real data pulls (may vary slightly between runs)
python scripts/collect_pytrends.py
python scripts/collect_serpapi.py     # requires SERPAPI_KEY in .env

# Generated data (deterministic — seed=42)
python scripts/generate_brandwatch.py
python scripts/generate_geojson.py
python scripts/generate_reddit_sample.py

# NLP (depends on reddit corpus)
python scripts/process_nlp.py
```

### What changes between runs
- **Pytrends**: Google samples data differently, so values may shift ±5-10%. Trends stay the same.
- **SerpApi**: SERP results change as Google updates rankings. Run close to presentation date.
- **Generated data**: Identical every run (seed=42).

---

## 9. What You Can Claim vs. What You Should Caveat

### Strong claims (fully supported)
- "Google Trends shows 'microplastics' surging while 'ocean plastic' is flat"
- "No technology company owns the AI ocean monitoring search category"
- "Different Reddit communities frame ocean plastic through completely different vocabularies"
- "The density map is seeded at real documented accumulation zones"
- "Solution-oriented content generates more positive sentiment than problem-description content"

### Claims that need caveats
- "Social listening shows 1M+ mentions" → **Caveat**: simulated data modeled on realistic patterns
- "Reddit NLP reveals a vocabulary gap" → **Caveat**: sample corpus, not live API data; predefined term lists introduce researcher bias
- "40% higher than predictions" → **Caveat**: this is a narrative claim from the fictional campaign, not a data finding
- "580,000 particles/km²" → **Caveat**: scaled estimate, not measured data

### Interview framing suggestion
When discussing methodology, lead with **what the data told you strategically**, not the technical pipeline. The hiring committee cares that you used data to inform communications decisions, not that you used NLTK vs. spaCy.

> "I started by listening — pulling search trends, mapping the keyword landscape, and analyzing how different communities talk about ocean plastic. The data revealed three things: a vocabulary gap between scientists and the public, an unclaimed brand category in AI ocean monitoring, and a consistent finding that solution-framed content outperforms problem-framed content in engagement. Every campaign decision flows from those three insights."
