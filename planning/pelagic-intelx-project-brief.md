# Pelagic IntelX — Communications Portfolio Project Brief
### For: Ai2 Senior Communications Specialist Application
### Build Method: Claude Code | Deploy: Vercel | Repo: GitHub

---

## Project Overview

You are helping build a **production-grade scrollytelling microsite** that serves as a communications portfolio piece for a job application at the Allen Institute for AI (Ai2). The project demonstrates senior-level communications strategy skills — audience intelligence, campaign architecture, research translation, and multichannel content creation — through a fictional but realistic AI company called **Pelagic IntelX**.

**Pelagic IntelX** is an AI company whose technology scans the ocean using satellite and drone imagery to identify plastic particulates, then maps the density and distribution of ocean plastic in real time.

The portfolio piece combines:
1. A **data-informed communications strategy** (built from real social listening and search intelligence)
2. **Two integrated campaign concepts** (a research launch + a policy impact campaign)
3. **Downloadable professional collateral** (press release, media one-pager, op-ed, stakeholder matrix)
4. All delivered inside a **scrollytelling microsite** that is itself the artifact

---

## The Two Campaign Concepts

### Concept 1 — "Mapping the Invisible" (Research Launch)
Pelagic IntelX releases its first publicly available ocean plastic density map — a real-time, AI-generated visualization of microplastic concentration across the Pacific. This is the "first of its kind" announcement moment.

### Concept 3 — "Plastic Doesn't Disappear" (Policy Impact Campaign)
Pelagic IntelX partners with a policy organization and university research lab to release a joint report on how AI-mapped plastic density data can inform international environmental regulation. This is the research-to-real-world-impact story.

Both campaigns are presented inside the same scrollytelling experience as sequential chapters.

---

## Design System

Use the established State Street Consulting / editorial dark aesthetic — adapted for Pelagic IntelX's ocean/tech identity:

```
Background:     #0a0e1a  (deep ocean navy, slightly warmer than pure black)
Primary accent: #00D4FF  (bioluminescent cyan — the "scan" color)
Secondary:      #E8C547  (existing brand gold — used sparingly for highlights)
Surface:        #0f1520  (card/panel backgrounds)
Text primary:   #F0F4F8
Text secondary: #8899AA
Border:         #1a2535

Typography:
  Display:  Playfair Display (editorial weight, for chapter titles)
  Mono:     IBM Plex Mono (data readouts, labels, metrics)
  Body:     Inter or DM Sans (readable prose, captions)

Aesthetic direction: Dark editorial meets oceanographic instrument panel.
Think: scientific rigor + environmental urgency + tech precision.
NOT: generic SaaS blue, startup cheerfulness, NGO earnestness.
```

---

## Site Architecture — Scroll Narrative

The site is a single long-scroll page divided into 5 chapters. Each chapter is triggered by scroll position using **Scrollama.js**. Transitions use **Framer Motion**.

```
INTRO / HERO
  - Pelagic IntelX wordmark + tagline
  - Animated ocean scan visualization (CSS or canvas — NOT Mapbox in hero)
  - Subhead: "A communications intelligence case study"
  - Scroll prompt

─────────────────────────────────────────

CHAPTER 1 — THE SIGNAL
"Before we wrote a single word, we listened."

  Sections:
  - Social listening landscape (Brandwatch data → Plotly chart)
  - Search trend visualization (Pytrends data → line chart)
  - Reddit language cluster analysis (NLP output → word frequency visual)
  - Key insight callout: the gap between scientific language and public vocabulary
  - Scroll-triggered stat reveals

─────────────────────────────────────────

CHAPTER 2 — THE AUDIENCE
"Three audiences. Three completely different conversations."

  Sections:
  - Audience segmentation cards (Journalists / Policymakers / Science Community)
  - Per-audience: what they care about, where they live online, what language resonates
  - Animated stakeholder map
  - Message architecture framework (scroll-revealed)

─────────────────────────────────────────

CHAPTER 3 — THE LAUNCH
"Mapping the Invisible — the research launch campaign"

  Sections:
  - Mapbox GL JS ocean plastic density map (THE emotional centerpiece)
    → Animated scan sweep on scroll trigger
    → Density heat layer reveal
  - Campaign strategy overview
  - Social content previews (X thread mockup, LinkedIn post mockup)
  - Downloadable collateral panel:
    → Press Release (PDF download)
    → Media One-Pager (PDF download)
    → Social Content Brief (PDF download)

─────────────────────────────────────────

CHAPTER 4 — THE IMPACT PLAY
"Plastic Doesn't Disappear — the policy campaign"

  Sections:
  - Campaign framing and coalition context
  - Stakeholder communications matrix (interactive table)
  - Op-ed excerpt with full PDF download
  - Podcast pitch preview
  - Google Ads brief summary
  - Downloadable collateral panel:
    → Full Op-Ed Draft (PDF download)
    → Stakeholder Matrix (PDF download)
    → Campaign Strategy Memo (PDF download)

─────────────────────────────────────────

CHAPTER 5 — THE PLAYBOOK
"What we'd measure. What success looks like."

  Sections:
  - KPI framework (animated metric cards)
  - 90-day campaign roadmap (horizontal timeline)
  - Tools & methodology transparency panel
  - GitHub link (data pipeline repo)
  - Closing statement

─────────────────────────────────────────

FOOTER
  - Pelagic IntelX fictional brand note ("This is a portfolio case study")
  - Nathan's contact / LinkedIn / portfolio links
```

---

## Tech Stack

### Frontend
- **React + Vite** — component framework
- **Scrollama.js** — scroll event triggers for chapter reveals
- **Framer Motion** — transitions, staggered reveals, panel animations
- **Mapbox GL JS** — ocean plastic density map in Chapter 3
- **Plotly.js or Recharts** — data visualizations (Charts 1–3)
- **Tailwind CSS** — utility styling with custom design tokens
- **Vercel** — deployment

### Data Pipeline (Python — separate `/data` directory in repo)
- **Pytrends** — Google Trends search interest data
- **PRAW (Reddit API)** — subreddit post/comment mining
- **NLTK / spaCy** — NLP: frequency analysis, key phrase extraction
- **pandas** — data cleaning and structuring
- **Plotly (Python)** — chart generation for export
- **Brandwatch** — social listening (exported as JSON/CSV, processed in Python)
- **SerpApi** — keyword landscape data

All raw data, Jupyter notebooks, and processed outputs live in `/data` with documented methodology. This is linked from the site and is part of the portfolio signal.

### Collateral (PDFs)
Built separately as designed documents, exported to PDF, stored in `/public/downloads/`.

---

## 5-Day Build Schedule

### Day 1 — Data & Intelligence
- [ ] Configure and run Brandwatch queries (ocean plastic, microplastics, AI environmental)
- [ ] Pull Reddit data via PRAW (r/environment, r/Futurology, r/collapse, r/MachineLearning)
- [ ] Pull Google Trends data via Pytrends
- [ ] Pull keyword landscape via SerpApi
- [ ] Run NLP analysis — frequency, clusters, vocabulary gap analysis
- [ ] Document key findings in `FINDINGS.md`
- [ ] Export all chart data as JSON/CSV for frontend consumption

### Day 2 — Strategy & Collateral Writing
- [ ] Write audience segmentation framework (informed by Day 1 data)
- [ ] Write message architecture (per-audience key messages)
- [ ] Write press release — "Mapping the Invisible"
- [ ] Write media one-pager
- [ ] Write op-ed draft — "Plastic Doesn't Disappear"
- [ ] Write stakeholder communications matrix
- [ ] Write campaign strategy memo
- [ ] Write 90-day roadmap + KPI framework
- [ ] Draft social content (X thread + LinkedIn post)

### Day 3 — Design & Collateral Production
- [ ] Design all PDFs in Figma or Adobe (press release, one-pager, op-ed, matrix, memo)
- [ ] Export all PDFs to `/public/downloads/`
- [ ] Build Mapbox ocean plastic density map (synthetic but realistic data layer)
- [ ] Build all Plotly/Recharts chart components from Day 1 data
- [ ] Set up React + Vite + Tailwind + Scrollama scaffold

### Day 4 — Full Build
- [ ] Build all 5 chapters as React components
- [ ] Wire Scrollama scroll triggers to chapter/section reveals
- [ ] Integrate Framer Motion animations
- [ ] Embed all charts and Mapbox map
- [ ] Build collateral download panels
- [ ] Build stakeholder map visualization
- [ ] Build 90-day timeline component
- [ ] Mobile responsive pass

### Day 5 — Polish & Deploy
- [ ] Copy editing — all site text, chapter intros, callouts
- [ ] Animation timing refinement
- [ ] Performance audit (Lighthouse)
- [ ] GitHub README — methodology narrative, data pipeline docs
- [ ] Vercel deploy + custom domain if applicable
- [ ] Final QA across Chrome, Safari, mobile

---

## Collateral Inventory

All documents written in Nathan's voice as Pelagic IntelX's communications lead.

| Document | Format | Chapter |
|---|---|---|
| Press Release — "Mapping the Invisible" | PDF | Chapter 3 |
| Media One-Pager | PDF | Chapter 3 |
| Social Content Brief (X thread + LinkedIn) | PDF | Chapter 3 |
| Op-Ed — "The Ocean Has a Memory" | PDF | Chapter 4 |
| Stakeholder Communications Matrix | PDF | Chapter 4 |
| Campaign Strategy Memo | PDF | Chapter 4 |
| Google Ads Brief | PDF | Chapter 4 |

---

## Key Constraints & Decisions

- **Mapbox map is synthetic** — realistic density data generated programmatically, not real Pelagic IntelX proprietary data. This should be noted with a small "Simulated data for portfolio purposes" label.
- **Brandwatch data is real** — pulled from actual social listening queries around ocean plastic and AI environmental topics. This is the legitimate intelligence backbone.
- **The fictional company framing is transparent** — the site's footer and intro make clear this is a portfolio case study for a real job application.
- **No backend required** — all data is pre-processed and shipped as static JSON. The site is fully static.
- **PDF downloads must be designed** — not auto-generated. These are communication artifacts and their design is part of the portfolio signal.

---

## Voice & Tone for All Written Content

Pelagic IntelX communications voice:
- **Precise but accessible** — technical credibility without jargon gatekeeping
- **Urgent but not alarmist** — the data speaks; we don't need to catastrophize
- **Confident and specific** — claims are grounded in data, always
- **Mission-forward** — the company exists to solve a problem; that purpose is felt in every sentence

---

## What Claude Code Should Know About Nathan

- Comfortable with React + Vite — this is his established stack
- Design system already established (dark editorial, IBM Plex Mono, Playfair Display, gold accent)
- Deploys to Vercel
- Experienced with Recharts and data visualization components
- Wants production-quality output, not scaffolding — full components, not placeholders
- Will iterate rapidly — build boldly, he'll redirect if needed

---

## Definition of Done

The project is complete when:
1. The site is deployed and publicly accessible on Vercel
2. All 5 chapters scroll and animate correctly
3. All PDF downloads work
4. The Mapbox map loads and animates on scroll trigger
5. All data visualizations render from real processed data
6. The GitHub repo is public with a documented README
7. The site works on mobile
8. A hiring manager at Ai2 could look at this and immediately understand both the strategic communications thinking AND the technical sophistication behind it
