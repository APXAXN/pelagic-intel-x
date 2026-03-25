# Pelagic IntelX — Build Plan

## Project Summary

Production-grade scrollytelling microsite serving as a communications portfolio for Nathan's Ai2 Senior Communications Specialist application. Built with React + Vite, deployed on Vercel. Five-chapter single-page scroll narrative showcasing two campaign concepts for a fictional AI ocean-plastic mapping company.

---

## Day 1 — Data & Intelligence Pipeline

*Goal: All data collected, processed, and exported as static JSON/CSV for frontend consumption.*

| # | Task | Output | Est. |
|---|------|--------|------|
| 1.1 | Set up `/data` directory with Python environment (venv, requirements.txt) | Project scaffold | 30m |
| 1.2 | Configure and run Pytrends queries — keywords: ocean plastic, microplastics, AI environmental monitoring, ocean pollution | `search_trends.json` | 1h |
| 1.3 | Pull Reddit data via PRAW — r/environment, r/Futurology, r/collapse, r/MachineLearning — posts + comments on ocean plastic topics | Raw Reddit corpus | 1.5h |
| 1.4 | Pull keyword landscape via SerpApi — SERP features, question clusters | Keyword data | 1h |
| 1.5 | Process Brandwatch export (if available) or generate representative social listening dataset | `brandwatch_mentions.json` | 1h |
| 1.6 | Run NLP analysis (NLTK/spaCy) — word frequency, key phrase extraction, vocabulary gap between scientific and public language | `reddit_word_freq.json`, `vocabulary_gap.json` | 2h |
| 1.7 | Generate synthetic ocean plastic density GeoJSON — seed known accumulation zones (North Pacific Gyre, SE Asia, Mediterranean), apply Gaussian spread + noise | `plastic_density.geojson` | 1.5h |
| 1.8 | Document all key findings, methodology decisions, data limitations | `FINDINGS.md` | 1h |
| 1.9 | Create Jupyter notebooks documenting reproducible pipeline | `/data/notebooks/` | 1h |

**Day 1 Deliverables:** 6 data files ready for frontend (`search_trends.json`, `reddit_word_freq.json`, `brandwatch_mentions.json`, `vocabulary_gap.json`, `plastic_density.geojson`, `FINDINGS.md`)

---

## Day 2 — Strategy & Collateral Writing

*Goal: All written content drafted — campaign copy, collateral documents, site narrative text.*

| # | Task | Output | Est. |
|---|------|--------|------|
| 2.1 | Write audience segmentation framework — Journalists / Policymakers / Science Community — informed by Day 1 data | Audience framework doc | 1h |
| 2.2 | Write per-audience message architecture — what they care about, language that works, channel priority | Message architecture doc | 1h |
| 2.3 | Write press release — "Pelagic IntelX Publishes First Real-Time AI Map of Pacific Ocean Plastic Density" | Press release draft | 1h |
| 2.4 | Write media one-pager — single-page scannable brief | One-pager draft | 45m |
| 2.5 | Write social content brief — X thread (7 posts) + LinkedIn post for launch day | Social brief draft | 1h |
| 2.6 | Write op-ed — "The Ocean Has a Memory" — argument: data → regulatory gap → coalition → call to action | Op-ed draft | 1.5h |
| 2.7 | Write stakeholder communications matrix — UNEP, EPA leads, NGOs, journalists, university partners | Stakeholder matrix doc | 1h |
| 2.8 | Write campaign strategy memo — exec summary through budget allocation | Strategy memo draft | 1.5h |
| 2.9 | Write Google Ads brief — keywords, headline variants, audience targeting, budget | Ads brief draft | 30m |
| 2.10 | Write 90-day roadmap + KPI framework | Roadmap + KPIs doc | 1h |
| 2.11 | Write all site narrative text — chapter intros, callouts, hero copy, footer | Site copy doc | 1h |

**Day 2 Deliverables:** 7 collateral drafts ready for design, all site copy, campaign strategy documentation

---

## Day 3 — Design, Collateral Production & Project Scaffold

*Goal: All PDFs designed and exported, React project scaffolded with design system, chart and map components built.*

| # | Task | Output | Est. |
|---|------|--------|------|
| 3.1 | Initialize React + Vite project with Tailwind CSS | Project scaffold | 30m |
| 3.2 | Configure Tailwind design tokens — colors (#0a0e1a, #00D4FF, #E8C547, #0f1520, #F0F4F8, #8899AA, #1a2535), typography (Playfair Display, IBM Plex Mono, Inter) | `tailwind.config.js` | 30m |
| 3.3 | Install and configure dependencies — Scrollama, Framer Motion, Mapbox GL JS, Recharts | `package.json` | 15m |
| 3.4 | Design all 7 PDFs (Figma/InDesign) — brand-consistent dark editorial style, portfolio disclaimer footer | 7 PDF source files | 3h |
| 3.5 | Export all PDFs to `/public/downloads/` with naming convention (`pelagicintelx-[name].pdf`) | 7 PDFs deployed | 30m |
| 3.6 | Build Recharts chart components — social listening chart, search trends line chart, word frequency visualization | Chart components | 2h |
| 3.7 | Build Mapbox GL JS density map component — synthetic GeoJSON layer, scroll-triggered scan animation (4-phase: base → scan sweep → heat reveal → interactive) | Map component | 2h |
| 3.8 | Build base layout — scroll container, chapter wrapper, section wrapper | Layout components | 1h |

**Day 3 Deliverables:** 7 PDFs in `/public/downloads/`, working chart and map components, project scaffold with design system

---

## Day 4 — Full Build

*Goal: All 5 chapters built, wired, animated, and responsive.*

| # | Task | Output | Est. |
|---|------|--------|------|
| 4.1 | Build Hero section — Pelagic IntelX wordmark, tagline, CSS ocean scan animation, scroll prompt | Hero component | 1.5h |
| 4.2 | Build Chapter 1 "The Signal" — Brandwatch chart, search trends line chart, Reddit word frequency visual, vocabulary gap callout, scroll-triggered stat reveals | Ch1 component | 2h |
| 4.3 | Build Chapter 2 "The Audience" — audience segmentation cards (3), animated stakeholder map, message architecture framework (scroll-revealed) | Ch2 component | 2h |
| 4.4 | Build Chapter 3 "The Launch" — Mapbox density map (centerpiece), campaign strategy overview, social content mockups (X thread + LinkedIn), collateral download panel (3 PDFs) | Ch3 component | 2h |
| 4.5 | Build Chapter 4 "The Impact Play" — campaign framing, stakeholder matrix (interactive table), op-ed excerpt + PDF link, podcast pitch preview, Google Ads brief, download panel (4 PDFs) | Ch4 component | 2h |
| 4.6 | Build Chapter 5 "The Playbook" — KPI metric cards (animated), 90-day timeline (horizontal), tools/methodology panel, GitHub link, closing statement | Ch5 component | 1.5h |
| 4.7 | Build Footer — fictional brand note, Nathan's contact/LinkedIn/portfolio links | Footer component | 30m |
| 4.8 | Wire all Scrollama scroll triggers — chapter enters, section reveals, stat animations | Scroll integration | 1h |
| 4.9 | Integrate Framer Motion — staggered reveals, panel transitions, card animations | Animation layer | 1h |
| 4.10 | Mobile responsive pass — all chapters, cards, map, charts at 375px+ | Responsive layout | 1.5h |

**Day 4 Deliverables:** Full working site with all chapters, animations, map, charts, and downloads

---

## Day 5 — Polish & Deploy

*Goal: Ship. Everything works. It's undeniable.*

| # | Task | Output | Est. |
|---|------|--------|------|
| 5.1 | Copy editing pass — all site text, chapter intros, callouts, data labels | Clean copy | 1.5h |
| 5.2 | Animation timing refinement — scroll trigger thresholds, reveal stagger timing, map animation pacing | Polished animations | 1h |
| 5.3 | Performance audit — Lighthouse target >85 mobile, lazy-load Mapbox bundle + chart components | Performance pass | 1h |
| 5.4 | Cross-browser QA — Chrome, Safari, Firefox | Browser compat | 1h |
| 5.5 | Mobile QA — iPhone 14 / 375px viewport, iOS Safari | Mobile compat | 1h |
| 5.6 | Write GitHub README — methodology narrative, data pipeline docs, tech stack, project context | `README.md` | 1h |
| 5.7 | Initialize git repo, push to GitHub (public) | GitHub repo live | 30m |
| 5.8 | Deploy to Vercel from main branch | Public Vercel URL | 30m |
| 5.9 | Final end-to-end QA — scroll through all chapters, test all downloads, verify map, check mobile | Sign-off | 1h |

**Day 5 Deliverables:** Public Vercel URL, public GitHub repo with documented README, Definition of Done met

---

## Definition of Done

- [ ] Site deployed and publicly accessible on Vercel
- [ ] All 5 chapters scroll and animate correctly
- [ ] All 7 PDF downloads work
- [ ] Mapbox map loads and animates on Chapter 3 scroll trigger
- [ ] All data visualizations render from processed JSON
- [ ] GitHub repo is public with documented README
- [ ] Site works on mobile (375px+)
- [ ] A hiring manager at Ai2 can navigate and understand the strategic argument in under 5 minutes

---

## Tech Stack Summary

| Layer | Tools |
|-------|-------|
| **Framework** | React + Vite |
| **Scroll** | Scrollama.js |
| **Animation** | Framer Motion |
| **Map** | Mapbox GL JS + synthetic GeoJSON |
| **Charts** | Recharts |
| **Styling** | Tailwind CSS (custom design tokens) |
| **Data Pipeline** | Python — Pytrends, PRAW, NLTK/spaCy, SerpApi, Brandwatch |
| **PDFs** | Figma/InDesign → `/public/downloads/` |
| **Deploy** | Vercel (zero-config from GitHub main) |

---

## File Structure

```
pelagic_intel_x/
├── planning/                    # PRDs, briefs, reference docs
├── data/
│   ├── notebooks/               # Jupyter — reproducible pipeline
│   ├── raw/                     # Raw API outputs
│   ├── processed/               # Clean JSON/CSV for frontend
│   └── FINDINGS.md              # Key insights + methodology
├── src/
│   ├── components/
│   │   ├── layout/              # ScrollContainer, ChapterWrapper
│   │   ├── chapters/            # Hero, Ch1-Ch5, Footer
│   │   ├── charts/              # Recharts visualizations
│   │   ├── map/                 # Mapbox density map
│   │   └── ui/                  # Cards, download panels, metrics
│   ├── data/                    # Static JSON imports
│   ├── styles/                  # Global styles, fonts
│   └── App.jsx
├── public/
│   └── downloads/               # 7 designed PDFs
├── tailwind.config.js
├── vite.config.js
├── package.json
└── README.md
```
