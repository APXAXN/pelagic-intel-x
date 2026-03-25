# Pelagic IntelX -- Communications Intelligence Findings

**Date:** March 24, 2026
**Analyst:** Nathan Fitzgerald
**Purpose:** Inform the communications strategy for Pelagic IntelX, an AI company that maps ocean plastic via satellite and drone imagery. This analysis synthesizes search behavior, social listening, Reddit discourse, and vocabulary gap data to identify messaging opportunities.

---

## 1. Methodology

### Data Sources and Collection

This analysis draws on five data pipelines, each targeting a different layer of public attention and discourse:

| Source | Tool / API | What It Captures | Time Range |
|---|---|---|---|
| Google Trends | pytrends | Relative search interest over time, related and rising queries | 5-year lookback (Mar 2021 -- Mar 2026) |
| SerpApi | SerpApi (Google SERP) | Organic results, "People Also Ask" questions, related searches for 10 keyword queries | Point-in-time snapshot |
| Reddit NLP | PRAW + NLTK | Word frequencies, bigram collocations across r/environment, r/Futurology, r/collapse, r/MachineLearning | Corpus of 1,475 relevant words across 727 unique terms |
| Vocabulary Gap | Custom analysis | Comparison of scientific vs. public terminology usage in the Reddit corpus | Derived from Reddit NLP data |
| Brandwatch | Simulated social listening (structure mirrors Brandwatch export) | Daily mention volumes, sentiment, source breakdown across 6 topic categories | Apr 2025 -- Mar 2026 |

Additionally, a synthetic GeoJSON dataset (`plastic_density.geojson`) was generated for map visualization, seeded from published accumulation zone data (NOAA, Jambeck et al. 2015) across 16 known gyre and coastal hotspots. This is not observational data; it exists to demonstrate the mapping layer of the product concept.

### Processing Approach

- Google Trends data was pulled for three keywords ("ocean plastic," "microplastics," "plastic pollution") on a worldwide, weekly basis.
- SerpApi queries covered the full thematic range: pollution basics, microplastics, AI/satellite monitoring, mapping, cleanup technology, regulation, and environmental data.
- Reddit NLP used standard stop-word removal and bigram collocation scoring (PMI-based) to surface meaningful term pairings.
- The vocabulary gap analysis compared frequency of precise scientific terms (e.g., "microplastic concentration," "bioaccumulation") against colloquial public-facing terms (e.g., "cleanup," "garbage patch").
- Brandwatch data tracks six topic categories across Twitter, news, Reddit, blogs, forums, and Instagram, with daily sentiment breakdowns.

---

## 2. Key Findings

### 2.1 Google Trends: Search Interest Over Time

**Keywords tracked:** "ocean plastic," "microplastics," "plastic pollution"

**"Microplastics" is the breakout term.** Over the five-year window, "microplastics" went from a relative search interest of 6 (March 2021) to a peak of 100 (late November 2025), representing roughly a 16x increase in normalized search volume. The term spiked sharply in mid-to-late 2025, with sustained values in the 70--100 range from August through December 2025. As of March 2026, interest remains elevated (58--87 range), well above historical baselines.

**"Ocean plastic" is stable but flat.** Search interest fluctuated between 5 and 23 over the entire five-year window, with a modest uptick in early 2026 (reaching 21--23 in February before settling back to 10--12). This term shows seasonal dips around year-end holidays and modest bumps aligned with Earth Day (April) and back-to-school periods.

**"Plastic pollution" tracked similarly to "ocean plastic"** -- a steady, low-intensity term that has not seen the explosive growth of "microplastics."

**Rising queries reveal a health-anxiety frame.** The fastest-rising queries associated with "microplastics" are overwhelmingly about human health impacts:
- "microplastics testicles" (+48,750%)
- "microplastics found in human blood" (+30,300%)
- "microplastics heart attack" (+9,300%)
- "how to get microplastics out of your body" (+8,450%)
- "microplastics in brain" (+1,450%)
- "microplastics in breast milk" (+2,200%)

For "ocean plastic," the rising queries skew toward consumer products ("microsoft ocean plastic mouse" at +50,550%, "ocean plastic pots"), indicating that the general public increasingly encounters the ocean plastic issue through branded products rather than environmental reporting.

**Strategic read:** The public conversation has shifted from "where is the plastic?" to "is the plastic in me?" Pelagic IntelX messaging should connect the ocean-scale mapping work to the upstream source tracking that makes the health conversation actionable.

### 2.2 SerpApi: The Keyword Landscape

Ten queries were analyzed for organic results, "People Also Ask" questions, and related searches.

**Dominant SERP players.** The Ocean Cleanup, NOAA, and major conservation nonprofits (Biological Diversity, Monterey Bay Aquarium, Oceanic Society) dominate the first page for core queries. Academic publishers (Nature, ScienceDirect) appear for technical queries. This means Pelagic IntelX content would need to compete with well-established institutional voices.

**"People Also Ask" questions reveal public framing:**
- "Where does 90% of ocean plastic pollution come from?" (rivers in Asia/Africa -- a geographic framing)
- "Is anyone cleaning up Garbage Island?" (action/solution framing)
- "Should I stop eating fish due to microplastics?" (personal health framing)
- "Can you flush microplastics out of your body?" (remediation framing)
- "What is the #1 source of microplastics?" (accountability framing)

**AI + ocean monitoring is an emerging but thin SERP space.** The query "AI ocean monitoring" surfaces results from Global Fishing Watch, MBARI, ScienceDirect, and IBM Research, but with no dominant brand. Related searches include "Ocean Vision AI" and "Deep sea AI" -- indicating nascent category formation. The "satellite plastic detection" query surfaces ESA, NASA, and academic sources, but no clear commercial leader. This represents a positioning opportunity.

**The "global plastics treaty" query space is active and contested.** UNEP's INC process, WWF, and advocacy coalitions dominate. Related questions reveal public frustration with stalled negotiations ("Why did Global Plastic Treaty Talks collapse?"). This policy conversation is a natural hook for data-driven messaging.

### 2.3 Reddit NLP: Community Discourse Analysis

A corpus of 1,475 words across four subreddits was analyzed after stop-word removal.

**Top words across all subreddits:** plastic (61), ocean (43), satellite (21), data (20), real (20), time (19), problem (18), scale (15), density (14), imagery (13), cleanup (13), monitoring (13).

**Top bigram collocations (by PMI score):**

| Bigram | Score | Interpretation |
|---|---|---|
| computer vision | 8.2 | Technical ML audience uses precise terminology |
| plastics treaty | 8.2 | Policy discourse is tightly coupled |
| voluntary commitments | 7.94 | Skepticism about non-binding pledges |
| global plastics | 7.72 | Geopolitical framing |
| accumulation zones | 7.3 | Geographic/scientific framing |
| satellite imagery | 6.02 | Core technology term |
| density mapping | 5.98 | Directly relevant to Pelagic IntelX value proposition |
| real time | 5.76 | Expectation of live data |

**Per-subreddit differences reveal distinct audience frames:**

- **r/environment** (523 words): Emphasizes "pollution," "negotiations," "voluntary," "antarctic," "ice." This audience connects ocean plastic to broader environmental and policy narratives. They are skeptical of voluntary commitments and track treaty negotiations closely.

- **r/Futurology** (348 words): Emphasizes "cleanup," "real," "time," "drones," "powered," "density." This audience wants to see technology in action -- real-time systems, drone deployments, tangible outputs. Solution-oriented and optimistic.

- **r/collapse** (257 words): Emphasizes "production," "smaller," "particles," "every," "food," "chain," "contamination," "binding." This audience focuses on the irreversibility of plastic contamination, food chain impacts, and the failure of governance. Doomer framing, but scientifically engaged.

- **r/MachineLearning** (347 words): Emphasizes "imagery," "detection," "density," "pipeline," "sentinel," "multispectral," "accuracy," "spectral." This audience evaluates the technical stack. They care about model architecture, sensor inputs (Sentinel-2 satellite data), and detection pipeline accuracy.

**Strategic read:** Four distinct audiences require four distinct messages -- but "satellite imagery," "density mapping," and "real time" are bridging terms that resonate across all groups.

### 2.4 Vocabulary Gap Analysis

The gap analysis compared scientific terminology against public terminology within the Reddit corpus.

**Scientific terms found and their frequencies:**
- "density mapping" -- 3 occurrences
- "microplastic concentration" -- 3 occurrences
- "bioaccumulation" -- 2 occurrences
- "polymer type" -- 1 occurrence

**Public terms found and their frequencies:**
- "cleanup" -- 13 occurrences
- "plastic pollution" -- 5 occurrences
- "garbage patch" -- 1 occurrence
- "where is the plastic" -- 1 occurrence

**The gap insight (from the analysis itself):** Scientific discourse favors precise measurement language -- density, distribution, concentration. Public conversation uses spatial and emotional framing -- where is it, how bad, can we see it. A successful communications campaign must bridge this divide by offering visual answers to public questions while maintaining scientific credibility.

**Ratio:** Public terms outnumber scientific terms roughly 2:1 in overall frequency (20 vs. 9 occurrences), even in a corpus skewed toward informed Reddit users. In truly general audiences, the gap would be far wider.

### 2.5 Brandwatch Social Listening: Mention Volumes and Sentiment

**Note:** This dataset is simulated for portfolio purposes but structured to mirror a real Brandwatch export.

**Total mentions tracked:** 1,053,557 across the 12-month period (Apr 2025 -- Mar 2026), averaging approximately 2,951 mentions per day across all topics and sources.

**Topic breakdown by total mentions:**

| Topic | Total Mentions | Share |
|---|---|---|
| Ocean plastic pollution | 368,113 | 34.9% |
| Microplastics | 257,595 | 24.4% |
| Ocean cleanup technology | 147,062 | 14.0% |
| Plastic pollution regulation | 120,779 | 11.5% |
| Marine debris | 85,571 | 8.1% |
| AI environmental monitoring | 74,437 | 7.1% |

**Sentiment analysis reveals a negativity-dominant conversation:**

| Sentiment | Total Mentions | Share |
|---|---|---|
| Negative | 442,433 | 42.0% |
| Neutral | 314,789 | 29.9% |
| Positive | 293,957 | 27.9% |

Negative sentiment dominates the two largest topics (ocean plastic pollution and microplastics), consistent with the alarm-driven framing seen in search trends. However, "ocean cleanup technology" and "AI environmental monitoring" skew positive -- indicating that solution-oriented and technology-oriented content generates more favorable engagement.

**Source distribution** (from sampled daily entries): Twitter/X accounts for roughly 40% of mentions, followed by news (~17%), Reddit (~10%), Instagram (~10%), blogs (~8%), and forums (~7%).

**Sentiment by topic (illustrative daily snapshot):**
- Ocean plastic pollution: ~50% negative, ~20% positive -- alarm framing dominates
- Microplastics: ~51% negative, ~22% positive -- health anxiety drives negativity
- Ocean cleanup technology: ~52% positive, ~10% negative -- solution content earns goodwill
- AI environmental monitoring: ~52% positive, ~14% negative -- tech audiences are receptive
- Plastic pollution regulation: ~44% negative, ~26% positive -- frustration with policy inaction
- Marine debris: ~50% negative, ~19% positive -- general environmental concern

---

## 3. Strategic Implications

### 3.1 Messaging Opportunity: Bridge the "Where" and the "In Me" Conversations

The public conversation has bifurcated: one thread asks "where is ocean plastic accumulating?" (the mapping question Pelagic IntelX directly answers), while the faster-growing thread asks "are microplastics in my body?" (a health question). The opportunity is to position Pelagic IntelX's mapping capability as the upstream intelligence layer that connects ocean-scale accumulation data to source tracking, supply chain accountability, and ultimately the health impacts people are searching for.

### 3.2 Position in the "AI for Oceans" Category Before It Consolidates

The SERP landscape for "AI ocean monitoring" and "satellite plastic detection" has no dominant commercial brand. Institutional players (ESA, NASA, NOAA, Global Fishing Watch) occupy this space, but a clear product-company narrative is missing. This is a narrow window for category creation.

### 3.3 Tailor Content by Audience Segment

Reddit discourse analysis reveals four distinct audience frames. Communications should develop modular content that can be reassembled for each:

- **General public / media:** Lead with visuals and the "where is it?" question. Use "plastic pollution," "cleanup," and map imagery.
- **Policy / advocacy:** Connect to treaty negotiations, binding commitments, and accountability data. Use "accumulation zones," "production caps," and enforcement framing.
- **Technical / ML community:** Emphasize the pipeline: Sentinel-2 data, multispectral imagery, computer vision models, detection accuracy. Publish benchmarks.
- **Futurist / solution-seeking audiences:** Lead with "real-time monitoring," drone deployments, and scale of coverage. Emphasize what is newly possible.

### 3.4 Lean Into Positive Sentiment Territory

Cleanup technology and AI monitoring content consistently generates more positive sentiment than problem-description content. Communications should default to a solution-forward frame: "here is what we can now see and do" rather than "here is how bad it is."

### 3.5 Ride the Policy Moment

The global plastics treaty (UNEP INC process) is actively generating search interest and social mentions, with a new chair elected in February 2026 and INC-5.3 negotiations ongoing. Pelagic IntelX can position its data products as essential infrastructure for treaty monitoring and compliance verification.

### 3.6 Address the Consumer Product Crossover

Rising queries for "ocean plastic" increasingly relate to consumer products (Microsoft ocean plastic mouse, Tom Ford ocean plastic watch, recycled ocean plastic products). This signals that corporate sustainability claims tied to ocean plastic are a growing content category. Pelagic IntelX could position as a verification layer -- providing the data that validates (or challenges) corporate ocean plastic claims.

---

## 4. Data Limitations and Notes

1. **Simulated data.** The Brandwatch social listening data and the GeoJSON plastic density data are simulated for portfolio demonstration purposes. Their structure mirrors real export formats, and the patterns were tuned to reflect plausible real-world dynamics, but they should not be cited as empirical evidence.

2. **Google Trends normalization.** Google Trends values are relative (0--100 scale normalized to peak), not absolute search volumes. Cross-keyword comparisons reflect relative proportions within Google's sample, not raw demand.

3. **Reddit corpus size.** The NLP analysis draws on a corpus of 1,475 words (post-stopword removal) across four subreddits. This is sufficient to identify dominant themes and collocations but is not large enough for robust statistical inference about rare terms.

4. **SerpApi point-in-time.** SERP results represent a snapshot and change frequently. Rankings, "People Also Ask" boxes, and related searches shift based on Google's algorithms and current events.

5. **Vocabulary gap scope.** The gap analysis compared a curated list of scientific and public terms against the Reddit corpus only. A broader analysis would include news articles, policy documents, and social media at scale.

6. **Geospatial data.** The `plastic_density.geojson` file uses Gaussian spread functions seeded at known accumulation zones. It is useful for demonstrating visualization capabilities but does not represent real satellite observations.

---

*This analysis was produced as part of a portfolio project for an Ai2 Senior Communications Specialist application. It demonstrates the use of programmatic intelligence gathering to inform strategic communications -- the kind of data-driven approach that should underpin any modern science communications program.*
