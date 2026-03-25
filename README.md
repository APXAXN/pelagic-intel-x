# Pelagic IntelX — Mapping the Invisible

A scrollytelling communications portfolio microsite demonstrating data-informed campaign strategy for a fictional AI ocean plastic intelligence company. Built as a case study for the Senior Communications Specialist position at the Allen Institute for AI (Ai2).

## What This Is

Pelagic IntelX is a fictional company that uses satellite imagery and AI to map ocean plastic density at planetary scale. This microsite is the communications portfolio — it demonstrates how a senior comms professional would research, strategize, and produce a full campaign around a complex scientific product.

Every strategic decision is backed by real data analysis.

## Architecture

**Frontend**: React + Vite, Tailwind CSS, Framer Motion, Scrollama, Recharts, Mapbox GL JS, Three.js

**Data Pipeline**: Python (NLTK, pandas, Pytrends, SerpApi)

**Design System**: Ai2 Dark — Fraunces (display) + Epilogue (body) + IBM Plex Mono (data)

## The Five Chapters

| Chapter | Title | What It Demonstrates |
|---------|-------|---------------------|
| 1 | The Signal | Data intelligence — Google Trends, SerpApi keyword landscape, Reddit NLP, social listening analysis |
| 2 | The Audience | Audience segmentation — 3 personas, message architecture, stakeholder mapping |
| 3 | The Launch | Campaign centerpiece — Mapbox density map, 3D volumetric depth model, social content brief |
| 4 | The Impact Play | Policy campaign — stakeholder matrix, op-ed, Google Ads brief |
| 5 | The Playbook | Measurement — KPI framework, framing fidelity analysis, 90-day roadmap |

## Data Pipeline

Seven Python scripts in `data/scripts/` power the intelligence layer:

| Script | Source | Output |
|--------|--------|--------|
| `collect_pytrends.py` | Google Trends API | Search interest over 5 years, 8 keywords |
| `collect_serpapi.py` | Google Search API | Keyword landscape, 10 queries |
| `generate_reddit_sample.py` | Sample corpus | 17 posts across 4 subreddits |
| `process_nlp.py` | NLTK | Word frequency, bigrams, vocabulary gap |
| `generate_brandwatch.py` | Statistical model | 12-month social listening simulation |
| `generate_geojson.py` | NOAA zone data | 3,844-point ocean density GeoJSON |
| `analyze_framing_fidelity.py` | Jaccard similarity | 2,015-mention framing fidelity analysis |

**Real data**: Google Trends (Pytrends), SerpApi keyword landscape
**Simulated**: Brandwatch social listening, ocean density, Reddit corpus, framing fidelity

## Collateral

Eight PDF documents in `public/downloads/` — press release, media one-pager, social content brief, depth model methodology, op-ed, stakeholder matrix, campaign strategy memo, Google Ads brief.

## Running Locally

```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Run data pipeline (optional — processed data is committed)
cd data
pip install -r requirements.txt
python scripts/collect_pytrends.py
python scripts/collect_serpapi.py      # requires SERPAPI_KEY in .env
python scripts/generate_brandwatch.py
python scripts/generate_geojson.py
python scripts/generate_reddit_sample.py
python scripts/process_nlp.py
python scripts/analyze_framing_fidelity.py
```

## Environment Variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `VITE_MAPBOX_TOKEN` | Yes (for map) | Mapbox GL JS access token |
| `SERPAPI_KEY` | For data pipeline | SerpApi Google Search queries |

## Built By

Nathan Fitzgerald — Senior Communications Specialist Application, Allen Institute for AI (Ai2)
