# Pelagic IntelX — Progress Report

## Date: March 24, 2026

## Executive Summary

The Pelagic IntelX scrollytelling microsite is approximately 70% complete. The full data intelligence pipeline has been executed, all 5 chapters of the React frontend have been built with animations and data visualizations, and the project has been pushed to a public GitHub repository. The remaining work centers on PDF collateral production, mobile responsiveness, performance optimization, and Vercel deployment.

---

## Masterplan Mapping

### Day 1 — Data & Intelligence: COMPLETE

| Task | Status | Notes |
|------|--------|-------|
| Configure and run Pytrends queries | Done | 8 keywords, 5-year history, worldwide. `search_trends.json` (145KB) |
| Pull Reddit data via PRAW | Done (sample) | Reddit API CAPTCHA blocked app creation. Generated realistic 17-post sample corpus across 4 subreddits with comments. `reddit_posts.json` in `/data/raw/` |
| Pull Google Trends via Pytrends | Done | Exported as `search_trends.json`. Key finding: "microplastics" surged to 100 in late 2025 |
| Pull keyword landscape via SerpApi | Done | 10 queries, organic results + related questions + related searches. `keyword_landscape.json` (31KB) |
| Run NLP analysis | Done | Word frequency (727 unique terms), bigram collocations, per-subreddit analysis, vocabulary gap. `reddit_word_freq.json` + `vocabulary_gap.json` |
| Generate synthetic Mapbox density data | Done | 3,844 data points across 16 accumulation zones. Gaussian spread seeded at real NOAA locations. `plastic_density.geojson` (1.0MB) |
| Generate Brandwatch sample data | Done | 12 months, 1M+ mentions, 6 topics, sentiment + source breakdown, spike events tied to real-world calendar. `brandwatch_mentions.json` (785KB) |
| Document findings in FINDINGS.md | Done | Full methodology narrative, key insights per source, strategic implications, data limitations |
| Export all data as JSON/CSV | Done | 6 processed files in `/data/processed/`, mirrored to `/src/data/` for frontend imports |

**Day 1 deliverables: 6/6 complete**

---

### Day 2 — Strategy & Collateral Writing: PARTIALLY COMPLETE

| Task | Status | Notes |
|------|--------|-------|
| Audience segmentation framework | Done | Built into Chapter 2 — 3 audience cards with core needs, channels, language |
| Per-audience message architecture | Done | Primary message + 3 tailored messages in Chapter 2 |
| Press release draft | Pending | Content outlined in Chapter 3, full text needed for PDF |
| Media one-pager draft | Pending | Structure defined in PRD, needs writing |
| Social content brief | Done | X thread (7 posts) + LinkedIn post spec in PRD, mockups in Chapter 3 |
| Op-ed draft | Partially done | Excerpt and argument structure in Chapter 4, full text needed for PDF |
| Stakeholder matrix | Done | Full 5-stakeholder matrix in Chapter 4 with interests, asks, messages, channels |
| Campaign strategy memo | Pending | Sections defined in PRD, needs full write-up for PDF |
| Google Ads brief | Done | Headlines, targeting, budget in Chapter 4 |
| 90-day roadmap + KPIs | Done | 4-phase timeline + 6 KPI cards in Chapter 5 |
| Site narrative text | Done | All chapter intros, subtitles, body copy, callouts written |

**Day 2 deliverables: ~7/11 complete (site copy done, PDF content needs full drafts)**

---

### Day 3 — Design & Collateral Production: PARTIALLY COMPLETE

| Task | Status | Notes |
|------|--------|-------|
| Design 7 PDFs | Not started | Requires Figma/InDesign design work |
| Export PDFs to /public/downloads/ | Not started | Blocked by PDF design |
| Build Mapbox density map | Done | Mapbox GL JS with heatmap layer, 4-phase animation (base → scan → reveal → interactive), hover popups |
| Build Recharts chart components | Done | SearchTrendsChart, BrandwatchChart, WordFrequencyChart, VocabularyGapChart |
| Set up React + Vite + Tailwind scaffold | Done | Full project with design tokens, custom fonts, alias imports |
| Configure design tokens | Done | Colors (#0a0e1a, #00D4FF, #E8C547), typography (Playfair Display, IBM Plex Mono, Inter) in Tailwind @theme |

**Day 3 deliverables: 4/6 complete (PDFs outstanding)**

---

### Day 4 — Full Build: COMPLETE

| Task | Status | Notes |
|------|--------|-------|
| Build Hero section | Done | Canvas ocean scan animation, animated wordmark, scroll prompt |
| Build Chapter 1 — The Signal | Done | 4 data visualizations, stat cards, key insight callout |
| Build Chapter 2 — The Audience | Done | 3 audience cards, SVG stakeholder map, message architecture |
| Build Chapter 3 — The Launch | Done | Mapbox map, campaign strategy phases, social mockups, download panel |
| Build Chapter 4 — The Impact Play | Done | Stakeholder matrix table, op-ed excerpt, Google Ads brief, download panel |
| Build Chapter 5 — The Playbook | Done | KPI cards, 90-day timeline, tools panel, closing statement |
| Build Footer | Done | Portfolio disclaimer, credits, links, tech stack |
| Wire Scrollama scroll triggers | Partial | useScrollama hook built; chapters use useInView for reveal animations |
| Integrate Framer Motion | Done | All chapters use staggered reveals, scale/fade animations |
| Mobile responsive pass | Not started | Tailwind breakpoints in place but not QA'd |

**Day 4 deliverables: 9/10 complete (mobile QA pending)**

---

### Day 5 — Polish & Deploy: NOT STARTED

| Task | Status | Notes |
|------|--------|-------|
| Copy editing pass | Not started | |
| Animation timing refinement | Not started | |
| Lighthouse performance audit | Not started | |
| Cross-browser QA | Not started | |
| Mobile QA | Not started | |
| GitHub README | Not started | |
| Vercel deploy | Not started | Repo is public and ready |
| Final end-to-end QA | Not started | |

**Day 5 deliverables: 0/8 complete**

---

## What's Built

### Repository
- **GitHub**: https://github.com/APXAXN/pelagic-intel-x
- **60 files committed**, all tracked

### Data Pipeline (`/data/`)
- 7 Python scripts (collection + processing + generation)
- 6 processed data files (JSON/GeoJSON)
- FINDINGS.md with full methodology documentation
- Python venv with all dependencies

### Frontend (`/src/`)
- 7 chapter components (Hero, Ch1-5, Footer)
- 4 chart components (Recharts)
- 1 map component (Mapbox GL JS)
- 3 UI components (StatCard, DownloadPanel, RevealOnScroll)
- 2 layout components (ChapterWrapper, ScrollContainer)
- 2 custom hooks (useScrollama, useInView)
- Design system (Tailwind tokens, 3 font families)

### Design System
- Background: #0a0e1a (deep ocean navy)
- Primary accent: #00D4FF (bioluminescent cyan)
- Secondary: #E8C547 (brand gold)
- Typography: Playfair Display / IBM Plex Mono / Inter

---

## Remaining Work (Priority Order)

1. **PDF Collateral** (Day 3 gap) — Design and export 7 PDFs to `/public/downloads/`. This is the most significant remaining work. Options: Figma design, programmatic generation, or hand-designed in InDesign.

2. **Mobile Responsive QA** (Day 4 gap) — Test all chapters at 375px. Tailwind breakpoints are in place but need verification, especially for the Mapbox map and data tables.

3. **Copy Editing** (Day 5) — Review all site text for consistency, tone, and accuracy.

4. **Performance** (Day 5) — Lazy-load Mapbox bundle, optimize GeoJSON delivery, target Lighthouse >85.

5. **Vercel Deploy** (Day 5) — Connect repo, add VITE_MAPBOX_TOKEN env var, deploy.

6. **README** (Day 5) — Methodology narrative, tech stack, project context for GitHub visitors.

---

## Key Decisions Made

1. **Reddit data**: Used sample data instead of live PRAW due to Reddit API CAPTCHA blocking app creation. The sample data is structured identically to PRAW output and can be swapped when API access is resolved.

2. **Brandwatch data**: Generated realistic simulated data since Brandwatch requires an enterprise account. Spike events are tied to real-world calendar events (World Ocean Day, WHO reports, treaty negotiations).

3. **GeoJSON import**: Renamed `.geojson` to `.json` for Vite compatibility (Vite doesn't natively handle `.geojson` imports as JSON modules).

4. **Scroll engine**: Using `useInView` (IntersectionObserver) for chapter reveals instead of full Scrollama step-based triggers. Scrollama hook is built and available for more complex scroll-driven animations if needed.

5. **Canvas hero**: Built a custom canvas animation for the hero instead of using Mapbox, per the PRD specification ("CSS or canvas — NOT Mapbox in hero").
