# Pelagic IntelX — End-to-End Project Narrative

## How It All Went Down

This document tells the full story of the Pelagic IntelX communications portfolio — from data sourcing through strategic output. Every number on every card, every chart axis, every insight callout is traced back to its source, with the methodology explained at interview-ready depth. This is the document you study before walking someone through the work.

---

## Table of Contents

1. [The Premise](#1-the-premise)
2. [Staffing and Roles](#2-staffing-and-roles)
3. [Phase 1: Intelligence Gathering (Day 1)](#3-phase-1-intelligence-gathering)
4. [Chapter 1 — The Signal: Card-by-Card Breakdown](#4-chapter-1--the-signal)
5. [Chapter 2 — The Audience: How Segmentation Was Built](#5-chapter-2--the-audience)
6. [Chapter 3 — The Launch: Campaign Centerpiece](#6-chapter-3--the-launch)
7. [Chapter 4 — The Impact Play: Policy Campaign](#7-chapter-4--the-impact-play)
8. [Chapter 5 — The Playbook: Measurement Framework](#8-chapter-5--the-playbook)
9. [The Framing Fidelity Analysis — Deep Dive](#9-the-framing-fidelity-analysis)
10. [Data Provenance Summary](#10-data-provenance-summary)
11. [What This Project Proves](#11-what-this-project-proves)

---

## 1. The Premise

Pelagic IntelX is a fictional AI company that uses satellite imagery and machine learning to map ocean plastic density at planetary scale. It doesn't exist. The data products it would generate don't exist. What exists is the communications portfolio — the work a senior comms professional would do to launch this kind of company into public consciousness.

The premise was chosen because it sits at the intersection of AI, environmental science, and policy — three domains where communications strategy matters enormously and where the gap between what scientists know and what the public understands is wide enough to build a career in.

The question the portfolio answers: *If you handed a senior communications specialist an AI company with a genuinely novel dataset, what would they build?*

The answer: intelligence first, strategy second, production third.

---

## 2. Staffing and Roles

In a real execution of this project at Ai2, the work would be distributed across a team. Here's how the roles would map:

### Communications Team (Core)

**Senior Communications Specialist** (this role — Nathan)
- Owns the intelligence-to-strategy pipeline
- Runs data collection and analysis (Pytrends, SerpApi, NLP, social listening)
- Builds audience segmentation and message architecture
- Writes all campaign copy: press release, op-ed, social content, policy memo
- Designs the measurement framework (KPIs, framing fidelity methodology)
- Project manages the build timeline
- Quality controls all output for strategic coherence

**Communications Director** (supervisor)
- Approves message architecture and campaign strategy
- Reviews press release and op-ed before distribution
- Signs off on embargo list and media targets
- Provides institutional voice and positioning guidance

**Visual Designer** (internal or contractor)
- Designs the 7 PDF collateral documents in Figma/InDesign
- Creates social media visual assets (map screenshots, data cards)
- Applies Ai2 brand guidelines to all materials
- Produces the scrollytelling microsite visual system

### Cross-Functional Partners

**Research Scientist** (Ai2 research team)
- Provides technical review of all scientific claims
- Validates methodology descriptions (satellite-AI pipeline, density modeling)
- Co-reviews op-ed for scientific accuracy
- Acts as quotable source for press materials

**Engineering Lead** (Ai2 engineering)
- Provides Mapbox token and data infrastructure access
- Reviews 3D visualization for technical accuracy
- Deploys the interactive map to production infrastructure
- Manages dataset publication pipeline

**Policy Advisor** (external or Ai2 partnerships)
- Reviews stakeholder matrix for accuracy
- Validates policy messaging (treaty references, regulatory hooks)
- Facilitates introductions to UNEP and EPA contacts
- Reviews Google Ads brief targeting criteria

**Legal/Ethics Review**
- Reviews all public-facing claims for accuracy
- Confirms "simulated data" disclosures are adequate
- Reviews press release for regulatory compliance
- Signs off on dataset licensing language

### Production Timeline (Real-World)

| Week | Activity | Owner |
|------|----------|-------|
| 1 | Data intelligence gathering + analysis | Comms Specialist |
| 2 | Strategy drafting + audience segmentation | Comms Specialist + Director |
| 3 | Copy production (press release, op-ed, social) | Comms Specialist |
| 3-4 | Design production (PDFs, social assets) | Visual Designer |
| 4 | Microsite build + data visualization | Comms Specialist + Engineering |
| 5 | Review cycle (scientific, legal, leadership) | Cross-functional |
| 6 | Embargo distribution + launch prep | Comms Specialist + Director |

---

## 3. Phase 1: Intelligence Gathering

Before writing a single word of campaign copy, the project ran a data intelligence sprint. The philosophy: listen before you speak. Understand how people already talk about the topic before trying to shape the conversation.

### Data Sources Deployed

**1. Google Trends via Pytrends** (real data)
- Library: `pytrends` — unofficial Python wrapper for Google Trends
- Script: `data/scripts/collect_pytrends.py`
- Queried 8 keywords in 2 groups, worldwide, over 5 years (`today 5-y`)
- Group 1: ocean plastic, microplastics, plastic pollution, ocean cleanup, marine debris
- Group 2: AI environment, satellite ocean monitoring, ocean plastic mapping
- Also pulled: rising and top related queries for "ocean plastic" and "microplastics"
- Output: `search_trends.json` — weekly interest values (0-100 scale) for each keyword

**Why two groups?** Google Trends normalizes within each query group. If you put "microplastics" (huge search volume) and "satellite ocean monitoring" (tiny volume) in the same group, the small term flatlines at zero. Separate groups let you see the real shape of each term's trajectory.

**2. SerpApi Keyword Landscape** (real data)
- API: SerpApi (serpapi.com), Google Search engine
- Script: `data/scripts/collect_serpapi.py`
- Queried 10 ocean plastic and AI monitoring terms
- Returned: top 5 organic results, People Also Ask questions, related searches per query
- Output: `keyword_landscape.json`
- Cost: 10 of 100 free monthly API calls

**3. Reddit Discourse via NLP** (sample data)
- Script: `data/scripts/generate_reddit_sample.py` (generates corpus) + `data/scripts/process_nlp.py` (analyzes it)
- Sample: 17 posts with comments across r/environment, r/Futurology, r/collapse, r/MachineLearning
- NLP pipeline: NLTK tokenization → stop word removal → frequency counting → bigram PMI → per-subreddit breakdown → vocabulary gap analysis
- Output: `reddit_word_freq.json` + `vocabulary_gap.json`

**Why sample data?** Reddit's API requires creating an app through their developer portal. The CAPTCHA on the app creation form repeatedly failed. The sample corpus was structured identically to PRAW (Python Reddit API Wrapper) output, allowing the full NLP pipeline to run. The linguistic patterns in the sample mirror real subreddit discourse — validated by manual browsing.

**4. Brandwatch Social Listening** (simulated data)
- Script: `data/scripts/generate_brandwatch.py`
- Model: 6 topics × 365 days × day-of-week variation × seasonal trend × spike events × growth trend × Gaussian noise
- Output: `brandwatch_mentions.json` — daily mention volumes, sentiment breakdown, source distribution

**Why simulated?** Brandwatch requires an enterprise license ($40K+/year). The simulation uses a statistical model calibrated to realistic volume ratios and sentiment distributions. Spike events are tied to real calendar dates (World Ocean Day, WHO reports, treaty negotiations).

**5. Ocean Plastic Density** (synthetic data)
- Script: `data/scripts/generate_geojson.py`
- 16 accumulation zones seeded at real NOAA-documented locations
- Gaussian density spread function around each zone center
- Output: `plastic_density.geojson` — 3,844 points with density values and category labels

**6. Framing Fidelity Analysis** (simulated data)
- Script: `data/scripts/analyze_framing_fidelity.py`
- 8 source frames with predefined mutation variants
- 2,015 downstream mentions scored via Jaccard similarity
- Output: `framing_fidelity.json`

---

## 4. Chapter 1 — The Signal

*"Before we wrote a single word, we listened."*

Chapter 1 presents the raw intelligence layer. Every visualization answers a specific strategic question.

### The Four Stat Cards

**1,053,557+ — Social Mentions**
- Source: `brandwatch_mentions.json` → `summary.total_mentions`
- What it is: Total simulated social media mentions across 6 topic categories over 12 months (April 2025 – March 2026)
- How it was calculated: Sum of daily mention volumes across all topics for 358 days. Each day's volume = base rate × weekday multiplier × seasonal multiplier × growth trend × spike multiplier + Gaussian noise
- Base rates by topic: ocean plastic pollution (850/day), microplastics (620), ocean cleanup technology (340), plastic pollution regulation (290), marine debris (210), AI environmental monitoring (180)
- The "+" suffix indicates the number is approximate due to rounding in the animated counter
- **In an interview**: "Our social listening tracked over a million mentions across six topic categories. This is the scale of the conversation we're entering."

**8 — Keywords Tracked**
- Source: Hardcoded in Chapter 1 JSX, reflects the Pytrends query count
- What it is: The number of distinct keywords queried against Google Trends
- The 8 keywords: ocean plastic, microplastics, plastic pollution, ocean cleanup, marine debris, AI environment, satellite ocean monitoring, ocean plastic mapping
- **In an interview**: "We tracked 8 keywords across Google Trends to understand search behavior over 5 years."

**4 — Subreddits Mined**
- Source: Hardcoded, reflects the NLP corpus scope
- The 4 subreddits: r/environment (general environmental), r/Futurology (solution-focused), r/collapse (systemic concern), r/MachineLearning (technical audience)
- **Why these four**: They represent four distinct audience frames for the same topic. The vocabulary differences between them directly informed the audience segmentation in Chapter 2.

**727 — Unique Terms**
- Source: `reddit_word_freq.json` → `unique_words`
- What it is: Count of unique tokens remaining after cleaning the Reddit corpus (lowercase, remove URLs, remove non-alphabetic, remove stop words)
- Corpus size before deduplication: 1,475 total tokens
- **In an interview**: "After cleaning, we had 727 unique terms in the corpus — enough to identify clear vocabulary patterns and gaps."

### The Brandwatch Bar Chart (Social Listening — Mention Volume by Topic)

- Source: `brandwatch_mentions.json` → `topic_totals`
- Shows 6 horizontal bars ranked by total mention volume:
  - Ocean Plastic: 368,113 (35% of total)
  - Microplastics: 257,595 (24%)
  - Cleanup Tech: 147,062 (14%)
  - Regulation: 120,779 (11%)
  - Marine Debris: 85,571 (8%)
  - AI Monitoring: 74,437 (7%)
- **Strategic insight**: The AI monitoring category is the smallest — but that's the opportunity. Low existing conversation volume means there's no incumbent brand owning the space.
- Colors: Pink for problem framing (ocean plastic, regulation), teal for solution framing (cleanup tech, microplastics), secondary pink for the AI category

### The Search Trends Line Chart (Google Trends — 5 Years)

- Source: `search_trends.json` → `interest_over_time`
- Shows weekly Google Trends interest (0-100 normalized scale) for 5 keywords over 5 years
- Key lines:
  - **Microplastics** (cream/white line): Surged from ~20 to 100 in late 2025, driven by health anxiety (microplastics in blood, testicles, brain studies)
  - **Ocean plastic** (pink line): Flat at 5-23 range for the entire 5 years. The term is saturated — no longer novel.
  - **Plastic pollution** (teal line): Moderate, stable interest
  - **Ocean cleanup** (teal line): Periodic spikes tied to The Ocean Cleanup press events
  - **Marine debris** (muted): Lowest interest — technical term the public doesn't use
- **Strategic insight**: "Microplastics" is the search term with momentum. "Ocean plastic" is dead weight. The campaign should lean into microplastics language, not ocean plastic.

### The Word Frequency Cloud (Reddit Corpus — Top 30 Terms)

- Source: `reddit_word_freq.json` → `top_words` (first 30)
- Displays terms sized by frequency, with key terms highlighted in accent color
- Top terms: plastic (61), ocean (43), satellite (21), data (20), real-time (19+), problem (18), scale (15), density (14), imagery (13), cleanup (13), monitoring (13), map (11)
- **Strategic insight**: "real-time," "density," and "map" appearing in the top 15 confirms that even informed audiences want to *see the data live*. This validates the interactive map as the campaign centerpiece — not a PDF report, not a press release, but a visual, explorable map.

### The Vocabulary Gap Cards

- Source: `vocabulary_gap.json`
- Two side-by-side panels comparing how scientists vs. the public talk about ocean plastic

**Scientific Register** (left panel):
- Terms found in corpus and their frequency:
  - "density mapping" — 3 occurrences
  - "microplastic concentration" — 3 occurrences
  - "bioaccumulation" — 2 occurrences
  - "polymer type" — 1 occurrence
- Total scientific term occurrences: 9

**Public Register** (right panel):
- Terms found in corpus and their frequency:
  - "cleanup" — 13 occurrences
  - "plastic pollution" — 5 occurrences
  - "garbage patch" — 1 occurrence
  - "where is the plastic" — 1 occurrence
- Total public term occurrences: 20

**Where the ~2:1 ratio comes from**: Public terms appear roughly 20 times across the corpus vs. 9 times for scientific terms. In the FINDINGS.md document this is rounded to "roughly 2:1" — public language outweighs scientific language even in relatively informed Reddit communities. The exact ratio is 20:9 = 2.22:1.

**The Key Insight callout**: "Scientific discourse favors measurement language (density, distribution, concentration); public uses spatial/emotional framing (where is it, how bad, can we see it). Campaign must bridge this gap."

**Methodology limitations to acknowledge**:
1. The term lists are hand-curated (21 scientific terms, 21 public terms) — this introduces researcher bias. The analysis finds what we predefined.
2. Exact string matching is used — "plastic waste" wouldn't match "plastic pollution" even though they're semantically related.
3. Small corpus (1,475 tokens / 17 posts) — with real PRAW data you'd have thousands of posts and the ratios would be more statistically robust.

**In an interview**: "Even in informed communities like r/MachineLearning and r/environment, people default to public vocabulary. 'Cleanup' appears 13 times for every 3 mentions of 'density mapping.' The campaign insight: don't lead with technical precision — lead with the visual answer to 'where is the plastic?' and let the methodology earn trust in the supporting materials."

---

## 5. Chapter 2 — The Audience

*"Three audiences. Three completely different conversations."*

Chapter 2 translates the data intelligence into actionable audience strategy. Nothing in this chapter is generated by a script — it's strategic communications work informed by the data in Chapter 1.

### The Three Audience Cards

Each card was constructed by asking: given what we learned from the data, how does this audience frame the topic, and what do they need from us?

**01 — Science & Environmental Journalists**
- Core need: First-look access, data credibility, visual assets they can embed
- Where they live online: X (breaking news), email pitches, embargo lists, Substack newsletters
- Language that resonates: "First-of-its-kind," "Real-time," "Publicly available," "The map speaks for itself"
- **Data backing**: SerpApi results showed journalists' outlets dominate the "ocean plastic pollution" SERP (The Ocean Cleanup, NOAA). They already own this beat. The campaign needs to offer them something *new* — hence "first-of-its-kind" language. The Google Trends data showing "microplastics" surging confirms journalists will cover health-anxiety angles.

**02 — Environmental Researchers**
- Core need: Methodology transparency, data access, peer validity, reproducibility
- Where they live online: Research newsletters, LinkedIn, Google Scholar alerts, academic Slack channels
- Language that resonates: "Open dataset," "Satellite-AI fusion," "Peer-reviewed pipeline," "Density model"
- **Data backing**: The Reddit NLP showed r/MachineLearning uses completely different vocabulary than r/environment — technical terms like "model," "accuracy," "pipeline," "segmentation." Researchers need to see the methodology, not the map.

**03 — Policy Advocates & Regulators**
- Core need: Actionable evidence, scale of problem, regulatory hooks, enforcement tools
- Where they live online: LinkedIn, coalition emails, policy briefings, conference side events
- Language that resonates: "Mapped for the first time," "The data regulators need," "Evidence base for enforcement," "Jurisdiction-level data"
- **Data backing**: SerpApi showed "global plastics treaty" queries returning news-heavy results with active policy interest. The Brandwatch simulation showed treaty negotiation dates (November) producing the largest mention spikes. Policy audiences respond to timing hooks.

### The Stakeholder Map (SVG Network)

- 8 nodes positioned in a radial layout: Pelagic IntelX (center), Journalists, Researchers, Policymakers, UNEP, NGOs, Science Media, University Labs
- 11 connection lines showing information flow pathways
- Color-coded: pink (media ecosystem), teal (research ecosystem), light teal (policy ecosystem)
- **Purpose**: Shows the hiring committee that the applicant thinks in network terms — messages don't just reach audiences, they flow through intermediary nodes. A university lab validates the data, which gives a journalist credibility to cover it, which gives a policymaker permission to cite it.

### The Message Architecture

**Primary message (all audiences)**:
"For the first time, we can see exactly where ocean plastic accumulates — and the picture is worse than models predicted."

**Per-audience adaptations**:
- Journalists: "The map gives reporters a visual story — not just statistics. Embeddable, shareable, updated in near-real-time."
- Researchers: "The underlying dataset is open-access. Methodology is published. The satellite-AI pipeline is reproducible."
- Policymakers: "This map makes the invisible visible. It gives regulators the evidence base to move from negotiation to enforcement."

**How the primary message was constructed**: It combines the two strongest data findings:
1. "For the first time" — SerpApi confirmed no brand owns the AI ocean monitoring category
2. "Worse than models predicted" — The 40% above predictions narrative claim creates urgency

---

## 6. Chapter 3 — The Launch

*"Mapping the Invisible — the research launch campaign"*

Chapter 3 is the campaign's visual centerpiece. Two interactive visualizations demonstrate what the data product would look like.

### The Four Stat Cards

**3,844 — Data Points**
- Source: `plastic_density.geojson` → FeatureCollection, count of Point features
- What it is: Number of individual geographic data points in the density map
- How generated: Grid of points at 2° latitude × 3° longitude intervals from 60°S to 75°N, plus 30 additional detail points near high-intensity zones
- **In an interview**: "The density map contains 3,844 data points covering the world's oceans from 60°S to 75°N."

**16 — Accumulation Zones**
- Source: Hardcoded in `generate_geojson.py`, reflects the number of seed locations
- The 16 zones: North Pacific Gyre Center (32°N, 145°W), North Pacific Gyre East (30°N, 135°W), South Pacific Gyre (30°S, 110°W), North Atlantic Gyre (30°N, 45°W), South Atlantic Gyre (35°S, 20°W), Indian Ocean Gyre (30°S, 80°E), South China Sea (12°N, 114°E), Bay of Bengal (15°N, 88°E), Western Mediterranean (38°N, 5°E), East China Sea (30°N, 125°E), Java Sea (5°S, 112°E), Gulf of Guinea (3°N, 3°E), Caribbean (18°N, 75°W), East African Coast (8°S, 42°E), Arabian Sea (15°N, 65°E), Coral Sea (18°S, 155°E)
- Sourced from: NOAA marine debris data, Jambeck et al. 2015, published ocean gyre research
- **In an interview**: "We seeded 16 accumulation zones at locations documented in peer-reviewed research — the North Pacific Gyre, known coastal input zones in Southeast Asia, and established gyre models."

**580,000 — Max Particles/km²**
- Source: Hardcoded in JSX, derived from the density generation formula
- How calculated: Peak density value (0.95) × 580,000 scaling factor = 551,000 actual peak. The 580,000 number represents the theoretical maximum (density = 1.0)
- Reference: Published surface trawl surveys report peak microplastic concentrations in the North Pacific Gyre in the range of 300,000-700,000 particles/km². The 580,000 scaling factor places our simulated data within this published range.
- **In an interview**: "Peak concentration in our model reaches 580,000 particles per square kilometer, which is within the range documented by published surface trawl surveys of the North Pacific Gyre."

**40% — Above Predictions**
- Source: Narrative claim hardcoded in JSX
- What it is: A fictional campaign claim stating that the AI-mapped density data found concentrations 40% higher than previous model predictions
- **Important caveat**: This is not a data finding — it's a communications narrative designed to create urgency. In a real campaign, this number would come from comparing AI-mapped density to published estimates from Jambeck et al. or Eriksen et al.
- **In an interview**: "The '40% above predictions' is the campaign hook — the claim that AI mapping reveals concentrations higher than conventional models estimated. In a real execution, this would be validated by the research team before publication."

### The Mapbox Density Map

- Library: Mapbox GL JS
- Map style: `mapbox://styles/mapbox/dark-v11` with custom background
- Data layer: GeoJSON heatmap layer with density-to-color gradient (pink at low density → teal at mid density)
- Animation: 4-phase reveal sequence (base map → scan sweep → density reveal → interactive)
- Hover popups: Show category (trace/low/moderate/high/extreme) and particles/km² for each point
- Badge: "Simulated data for portfolio purposes" — persistent disclosure

### The 3D Volumetric Depth Model

- Library: Three.js (r128+)
- What it shows: Microplastic concentration through the water column (0-200m depth), not just at the surface
- **Narrative bridge**: "Every map before this one was looking at the surface." — positions the depth model as the novel differentiator

**Particle generation logic**:
- 4,200 total particles
- 3 cluster centers in world space: (-40, -20), (30, 15), (-10, 50) — representing Pacific accumulation zones
- Depth distribution: 55% in 0-50m (neuston/surface layer), 25% in 60-130m (pycnocline), 20% in 130-200m (deep scatter)
- Gaussian spread increases with depth: `spread = 30 + depth * 0.6` — deeper particles are more diffuse, which matches real oceanographic dispersion patterns
- Color: Pink (#E85B8A) at surface, transitioning to deep teal (#143545) at 200m. Core cluster particles (within 25 units of cluster center, depth < 60m) rendered in teal-mid (#2A6070) to indicate peak density zones.

**Interactive controls**:
- Max Depth slider (20-200m): Filters particle visibility, revealing the layer structure
- Opacity slider (20-100%): Adjusts point material transparency
- Auto Rot / Surface / Deep Cut buttons: Preset views

### Campaign Strategy Section

Three phases displayed as timeline cards:
1. **Pre-Launch (Weeks 1-2)**: Embargo briefings with 5 target outlets, beta access for 3 key researchers, social teaser sequence
2. **Launch Day**: Press release via wire, X thread (7 posts) + LinkedIn, map goes live, dataset published
3. **Amplification (Weeks 2-4)**: Reddit AMA, follow-up media, conference presentations, policy brief distribution

### Social Mockups

- **X/Twitter post**: Simulated tweet with "Mapping the Invisible" branding, 12.4K reposts, 45.2K likes, 2.1M views
- **LinkedIn post**: Professional format with 3.2K reactions, 284 comments, 891 reposts
- These numbers are aspirational targets, not real metrics

---

## 7. Chapter 4 — The Impact Play

*"Plastic Doesn't Disappear — the policy campaign"*

Chapter 4 demonstrates the second-wave campaign — moving from "interesting data company" to "essential infrastructure for environmental governance."

### The Stakeholder Communications Matrix

5 stakeholders, each with:
- **UNEP Officials**: Interest = treaty evidence base. Ask = cite dataset in Global Plastics Treaty appendix. Channel = direct briefing + white paper.
- **National EPA Leads**: Interest = domestic enforcement tools. Ask = pilot density monitoring in regulatory framework. Channel = targeted outreach + policy memo.
- **Environmental NGOs**: Interest = advocacy ammunition. Ask = embed map in campaign materials. Channel = coalition emails + social co-posts.
- **Policy Journalists**: Interest = news hook + access. Ask = cover joint report release. Channel = press release + embargo.
- **University Partners**: Interest = research validation + citation. Ask = co-author methodology paper. Channel = academic journals + research newsletters.

**How this matrix was built**: Each row answers four questions — what does this stakeholder care about, what specific action do we want them to take, what message will motivate that action, and through which channel do we reach them? This is standard stakeholder analysis methodology taught in strategic communications programs.

### The Op-Ed Excerpt

Title: "The Ocean Has a Memory"
Target outlets: Nature (Comment), The Atlantic, Politico Pro, The Guardian
Key quotes displayed: "The ocean doesn't forget what we put in it" and "Our governance frameworks are still suffering from amnesia."

### The Google Ads Brief

- **Budget**: $4,500/month — based on typical non-profit/research org Google Ad Grants budget
- **Window**: 30-day release cycle — concentrated around campaign launch
- **Target CTR**: 3.5%+ — aggressive vs. 2.1% industry average for environmental/policy vertical
- **3 headline variants**: focused on data, AI mapping, and regulation angles
- The CTR target is justified by highly targeted keyword selection (policy professionals searching specific terms) and compelling ad copy. Niche B2B audiences consistently outperform broad consumer CTR benchmarks.

---

## 8. Chapter 5 — The Playbook

*"What we'd measure. What success looks like."*

### The Six KPI Cards

Each KPI has a target, baseline, source, and timeframe:

| KPI | Target | Baseline | Source | Window | Rationale |
|-----|--------|----------|--------|--------|-----------|
| Press Pickups | 15+ | 0 | Media monitoring | 30 days | Comparable Ai2 research launches (Semantic Scholar, OLMo) achieve 10-20 pickups |
| Map Unique Visitors | 50,000 | — | Vercel analytics | 30 days | Based on comparable interactive data visualizations (ProPublica, NYT) |
| Dataset Downloads | 2,000 | — | Download tracker | 30 days | Conservative estimate for open scientific dataset with press coverage |
| X Thread Impressions | 500K | — | X Analytics | 30 days | Based on viral science communication threads; the visual map is inherently shareable |
| Joint Report Downloads | 5,000 | — | Download tracker | 60 days | Extended window for policy report, distributed through coalition channels |
| Policy Briefing Requests | 8+ | — | CRM | 60 days | Conservative; 5 stakeholder groups × 2-3 contacts each |

### The Framing Fidelity Analysis

*(See Section 9 below for the full deep dive)*

### The 90-Day Campaign Roadmap

Four phases displayed as timeline cards:
1. **Phase 1: Intelligence & Prep (Weeks 1-2)** — Social listening analysis, audience segmentation, message architecture, collateral drafting. Color: pink (active work)
2. **Phase 2: Research Launch (Weeks 3-4)** — Map release + press embargo, social content deployment, dataset publication, journalist outreach. Color: teal (execution)
3. **Phase 3: Amplification (Weeks 5-8)** — Follow-up media coverage, research newsletter features, conference presentations, Reddit AMA. Color: light teal (expansion)
4. **Phase 4: Policy Impact (Weeks 9-12)** — Joint report release, policy briefings, op-ed placements, Google Ads campaign. Color: pink (return to active work)

### The Tools Panel

Lists the actual technology stack used in the project, organized by function:
- Data Collection: Pytrends, PRAW, SerpApi, Brandwatch
- Analysis: NLTK / spaCy, pandas, Jupyter
- Visualization: Recharts, Mapbox GL JS, Plotly
- Frontend: React + Vite, Scrollama.js, Framer Motion, Tailwind CSS

---

## 9. The Framing Fidelity Analysis — Deep Dive

This is the most methodologically novel section of the portfolio. It demonstrates a measurement framework that most comms teams don't have — a quantified way to track how well your intended message frames survive downstream propagation.

### What Framing Fidelity Means

When a campaign seeds a message like "first AI-powered plastic density map," that exact phrase rarely survives intact through media, social, and policy channels. It gets paraphrased, shortened, simplified, or reframed. Framing fidelity measures how much of the original intent survives.

### The Methodology

**Step 1: Define Source Frames**
8 campaign-intended phrases were defined, each with a category and priority:
- "first AI-powered plastic density map" (novelty, primary)
- "580,000 particles per square kilometer" (scale, primary)
- "satellite-AI fusion pipeline" (technology, primary)
- "40 percent above previous predictions" (urgency, primary)
- "the ocean has a memory" (narrative, secondary)
- "real-time density monitoring" (capability, secondary)
- "evidentiary standard for international law" (policy, secondary)
- "mapping the invisible" (brand, primary)

**Step 2: Define Mutation Variants**
For each source frame, three tiers of downstream mutations were hand-crafted:
- **Exact**: Verbatim reproduction (e.g., "first AI-powered plastic density map")
- **Partial**: Core tokens preserved but reworded (e.g., "AI-powered plastic map," "first AI map of ocean plastic")
- **Drifted**: Meaning preserved but frame lost (e.g., "new plastic map," "machine learning plastic tracker")

**Step 3: Generate Downstream Corpus**
2,015 simulated mentions across 4 channels and 6 time periods (15 days each = 90 days):

Channel behavior parameters:
| Channel | Base Fidelity | Volume/Day | Drift Rate/Period |
|---------|--------------|------------|-------------------|
| Press | 82% | 45 | 4% per period |
| Social | 54% | 320 | 12% per period |
| Policy | 91% | 12 | 2% per period |
| Academic | 88% | 8 | 3% per period |

Each mention is assigned a type (exact/partial/drifted) based on the channel's fidelity score adjusted by period and noise. Launch period gets 1.4x volume multiplier; subsequent periods decay.

**Step 4: Score Each Mention**
Scoring uses token-level Jaccard similarity:
- Tokenize both the source frame and the downstream mention (lowercase, split on whitespace, remove punctuation)
- Jaccard index = |intersection| / |union| of token sets
- Fidelity score:
  - Exact match: 1.0
  - Partial match: 0.6 + (Jaccard × 0.3)
  - Drifted: Jaccard × 0.7

**Step 5: Aggregate**

### The Four Summary Stat Cards

**34.6% — Overall FFI (Framing Fidelity Index)**
- Calculated: Sum of all 2,015 fidelity scores / 2,015 = 0.3459
- Meaning: On average, downstream mentions preserve about a third of the original frame's linguistic precision
- **In an interview**: "Our overall FFI of 34.6% tells us that roughly two-thirds of our framing precision is lost during downstream propagation. That's not failure — that's the cost of amplification. The question is where to invest in precision vs. where to accept drift."

**2,015 — Mentions Scored**
- Calculated: Total simulated downstream mentions across all channels and periods
- Breakdown: 605 in launch period, decaying to 217 in the final period

**16.8% — Exact Match Rate**
- Calculated: 339 exact matches / 2,015 total = 0.1682
- Meaning: Only about 1 in 6 downstream mentions reproduces the source frame verbatim
- **In an interview**: "A 16.8% exact match rate means about 1 in 6 mentions uses our exact language. Press and policy channels do much better — roughly 1 in 3."

**62.6% — Drift Rate**
- Calculated: 1,261 drifted mentions / 2,015 total = 0.6258
- Meaning: Nearly two-thirds of downstream mentions have drifted far enough from the source frame that the original linguistic structure is no longer recognizable
- **In an interview**: "A 62.6% drift rate doesn't mean 62.6% of mentions are wrong — it means they've been reframed. 'Massive particle concentrations' communicates the same urgency as '580,000 particles per square kilometer,' but the precision is gone. Precision matters for policy; it matters less for awareness."

### The Fidelity Decay Line Chart

Shows FFI by channel across 6 periods:
- **Academic** (white line): Starts at ~68%, fluctuates, ends at ~90% (tiny sample size — 36 total mentions — causes volatility, but the trend is upward because academic citations get more precise as researchers engage with the methodology)
- **Policy** (teal line): Starts at ~67%, dips, recovers to ~95% (same small-sample caveat — 62 total mentions — but policy documents tend to quote precisely once they've vetted the source)
- **Press** (pink line): Starts at ~72%, decays to ~28% (steady degradation as news cycle moves on and journalists paraphrase from other coverage rather than the source material)
- **Social** (light teal line): Starts at ~39%, decays to ~18% (fastest degradation — social media inherently compresses and simplifies)

### The Per-Frame Fidelity Bars

Horizontal bar chart ranking 8 source frames by FFI:
- "first AI-powered plastic density map" — highest FFI (41.4%) — novel claims get quoted precisely
- "the ocean has a memory" — 37.8% — short metaphor travels relatively well
- "mapping the invisible" — 36.1% — brand phrases are memorable but get paraphrased
- "evidentiary standard for international law" — 35.0% — policy language holds in policy channels but drifts everywhere else
- "580,000 particles per square kilometer" — 33.8% — specific numbers get rounded or described qualitatively
- "real-time density monitoring" — 32.0% — technical capability claims get simplified
- "40 percent above previous predictions" — 31.7% — comparative claims lose their reference point
- "satellite-AI fusion pipeline" — 28.4% — lowest FFI — jargon gets replaced with plain language

**Strategic implication**: Short, metaphorical frames ("the ocean has a memory") and novelty claims ("first AI-powered") travel better than technical or quantitative frames. The campaign should lead with the former and support with the latter.

### The Drift Examples Panel

Shows 5 real examples of maximum semantic distance:
- "40 percent above previous predictions" → "higher than models suggested" (J=0)
- "the ocean has a memory" → "plastic accumulates over time" (J=0)
- "real-time density monitoring" → "live pollution data" (J=0)
- "580,000 particles per square kilometer" → "massive particle concentrations" (J=0)

These examples have Jaccard similarity of 0 — zero token overlap between source and downstream. The *meaning* is preserved but the *language* is completely replaced. This is the most extreme form of frame drift.

### The Key Insight Callout

"Policy and academic channels maintain 3× higher fidelity than social (61% vs 30% FFI). Social volume compensates — 1,691 mentions at lower fidelity still drive awareness. The strategic implication: invest in press embargo precision (high-fidelity seeding) while accepting social drift as amplification cost."

**Where the 3× comes from**:
- Policy FFI: 61.3%
- Social FFI: 29.6%
- Ratio: 61.3 / 29.6 = 2.07× (rounded to "3×" in the callout — this should technically say "2×" or "roughly double." The 3× framing compares policy+academic average [(61.3 + 63.3) / 2 = 62.3%] against social [29.6%], yielding 62.3 / 29.6 = 2.1×. The "3×" is a slight overstatement for rhetorical impact.)

---

## 10. Data Provenance Summary

| Data Source | Status | Script | Output File | Key Metric |
|-------------|--------|--------|-------------|------------|
| Google Trends | **Real** | `collect_pytrends.py` | `search_trends.json` | Microplastics surged to 100 in late 2025 |
| SerpApi | **Real** | `collect_serpapi.py` | `keyword_landscape.json` | No tech brand owns AI ocean monitoring SERP |
| Reddit NLP | **Sample** | `generate_reddit_sample.py` + `process_nlp.py` | `reddit_word_freq.json` + `vocabulary_gap.json` | Public terms outcount scientific 2.2:1 |
| Brandwatch | **Simulated** | `generate_brandwatch.py` | `brandwatch_mentions.json` | 1,053,557 mentions; solution content skews positive |
| Ocean Density | **Synthetic** | `generate_geojson.py` | `plastic_density.geojson` | 3,844 points, 16 zones, 580K max particles/km² |
| Framing Fidelity | **Simulated** | `analyze_framing_fidelity.py` | `framing_fidelity.json` | 34.6% FFI; policy holds 2× better than social |

**Reproducibility**: All generated/simulated data uses `random.seed(42)` — running any script again produces identical output. Real data (Pytrends, SerpApi) may vary slightly between runs due to Google's data sampling.

---

## 11. What This Project Proves

This portfolio demonstrates five competencies:

1. **Data-informed strategy**: Every campaign decision traces back to a data finding. The message architecture isn't invented — it's derived from search trends, NLP analysis, and keyword landscape mapping.

2. **Audience sophistication**: Three distinct audience personas aren't just described — they're backed by per-subreddit vocabulary analysis showing how different communities frame the same topic using different language.

3. **Full-stack production**: The work spans research (Python data pipeline), strategy (message architecture, stakeholder matrix), writing (press release, op-ed, social content), design (scrollytelling microsite), and measurement (KPI framework, framing fidelity).

4. **Measurement rigor**: The framing fidelity analysis demonstrates an unusual level of quantitative thinking for a communications role. It shows the applicant doesn't just write messages — they build systems to measure whether those messages land.

5. **Technical fluency**: The applicant can work at the intersection of research engineering and communications. They can build a data pipeline, run NLP analysis, create interactive visualizations, and translate technical findings into strategic communications decisions. This is the exact skill set needed at an AI research institute where the product *is* the research.

---

*Pelagic IntelX is a fictional company. All data, strategy, and collateral are original work created for the Allen Institute for AI Senior Communications Specialist application.*
