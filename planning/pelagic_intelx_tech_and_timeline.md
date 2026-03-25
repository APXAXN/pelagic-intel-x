# Pelagic IntelX — Tech Stack & Build Timeline

Communications portfolio microsite · Ai2 Senior Communications Specialist Application
*Version 1.0 · March 2026*

---

## Tech Stack

### Frontend

| Tool | Role |
|---|---|
| **React + Vite** | Component framework — project scaffold and build pipeline |
| **Scrollama.js** | Scroll event triggers — chapter and section reveals |
| **Framer Motion** | Transitions, staggered reveals, panel animations |
| **Tailwind CSS** | Utility styling with custom design tokens |

### Visualization

| Tool | Role |
|---|---|
| **Mapbox GL JS** | Ocean plastic density map (Chapter 3) — synthetic GeoJSON layer, scroll-triggered scan animation |
| **Recharts** | Social listening + search trend charts (Chapter 1) — rendered from pre-processed JSON |
| **GeoJSON** | Synthetic density data layer — programmatically generated, labeled as simulated |

### Data Pipeline (Python)

| Tool | Role |
|---|---|
| **Pytrends** | Google Trends — search interest over time by keyword |
| **PRAW** | Reddit API — post/comment mining across r/environment, r/Futurology, r/collapse, r/MachineLearning |
| **NLTK / spaCy** | NLP — frequency analysis, key phrase extraction, vocabulary gap analysis |
| **SerpApi** | Keyword landscape — SERP features, question clusters |
| **Brandwatch** | Social listening — mention volume, sentiment, source breakdown (exported as JSON/CSV) |

### Data Outputs (Static JSON/CSV)

| File | Consumed By |
|---|---|
| `search_trends.json` | Chapter 1 — Recharts line chart |
| `reddit_word_freq.json` | Chapter 1 — word frequency visualization |
| `brandwatch_mentions.json` | Chapter 1 — social listening chart |
| `vocabulary_gap.json` | Chapter 1 — language cluster callout |
| `plastic_density.geojson` | Chapter 3 — Mapbox GL JS density layer |
| `findings.md` | GitHub README — methodology narrative |

### Collateral + Design

| Tool / Asset | Role |
|---|---|
| **Figma / InDesign** | PDF design — all 7 downloadable collateral documents |
| **7 PDFs** | Stored in `/public/downloads/` — linked from Chapter 3 and Chapter 4 panels |
| **Playfair Display + IBM Plex Mono** | Brand typography — display/editorial + data/mono |

### Deploy + Repo

| Tool | Role |
|---|---|
| **Vercel** | Deploy from GitHub main — zero-config, public URL |
| **GitHub** | Public repo with documented README and methodology |
| **Jupyter** | Documented data pipeline notebooks — reproducible, linked from site |
| **Lighthouse >85** | Mobile performance target — lazy-load charts and Mapbox bundle |

---

## 5-Day Build Timeline

### Day 1 — Data & Intelligence
*Pull everything before writing a word*

**Tasks**

- Configure Brandwatch queries — ocean plastic, AI environmental
- Pull Reddit via PRAW — r/environment, r/Futurology, r/collapse, r/MachineLearning
- Pull Google Trends via Pytrends
- Pull keyword landscape via SerpApi
- Run NLP — frequency, clusters, vocabulary gap analysis
- Document findings in `FINDINGS.md`
- Export all chart data as JSON/CSV

**Outputs**

`search_trends.json` · `reddit_word_freq.json` · `brandwatch_mentions.json` · `vocabulary_gap.json` · `FINDINGS.md`

---

### Day 2 — Strategy & Collateral Writing
*All written content, informed by Day 1 intelligence*

**Tasks**

- Write audience segmentation framework
- Write per-audience message architecture
- Write press release — Mapping the Invisible
- Write media one-pager
- Write op-ed — The Ocean Has a Memory
- Write stakeholder communications matrix
- Write campaign strategy memo
- Write 90-day roadmap + KPI framework
- Draft X thread (7 posts) + LinkedIn post

**Outputs**

7 written drafts · Social content brief · KPI framework

---

### Day 3 — Design & Collateral Production
*PDFs designed, map built, charts assembled*

**Tasks**

- Design all 7 PDFs in Figma / InDesign
- Export PDFs to `/public/downloads/`
- Build Mapbox synthetic density layer (GeoJSON)
- Build Recharts components from processed JSON
- Set up React + Vite + Tailwind + Scrollama scaffold
- Configure design tokens in Tailwind config

**Outputs**

7 PDFs → `/public/downloads/` · `plastic_density.geojson` · Project scaffold

---

### Day 4 — Full Build
*All 5 chapters wired and animated*

**Tasks**

- Build all 5 chapters as React components
- Wire Scrollama triggers to chapter / section reveals
- Integrate Framer Motion animations + staggered reveals
- Embed Recharts visualizations (Chapter 1)
- Embed Mapbox map with scan animation (Chapter 3)
- Build collateral download panels (Chapters 3 + 4)
- Build stakeholder map visualization (Chapter 2)
- Build 90-day timeline component (Chapter 5)
- Mobile responsive pass — Tailwind breakpoints

**Outputs**

Full working site · Map animated · All downloads live

---

### Day 5 — Polish & Deploy
*Ship it. QA everything. Make it undeniable.*

**Tasks**

- Copy edit — all site text, callouts, chapter intros
- Animation timing refinement
- Lighthouse performance audit — target >85 mobile
- Write GitHub README — methodology + pipeline docs
- Deploy to Vercel from main branch
- Final QA — Chrome, Safari, Firefox, iPhone 14

**Outputs**

Public Vercel URL · Public GitHub repo · Definition of Done ✓

---

*Pelagic IntelX is a fictional company created for portfolio purposes. All content is original communications strategy work.*
