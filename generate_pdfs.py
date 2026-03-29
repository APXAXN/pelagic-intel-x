#!/usr/bin/env python3
"""Generate 8 professional PDF documents for Pelagic IntelX portfolio."""

from fpdf import FPDF
import os

OUTPUT_DIR = "/Users/nathanfitzgerald/pelagic_intel_x/public/downloads"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Design system colors (RGB tuples) — white background with brand accents
BG = (255, 255, 255)
ACCENT = (232, 91, 138)
TEAL_MID = (42, 96, 112)
TEAL_LIGHT = (230, 242, 246)
TEXT = (30, 35, 40)
TEXT_SEC = (90, 100, 110)

FOOTER = "PELAGIC INTELX -- PORTFOLIO CASE STUDY -- SIMULATED FOR Ai2 APPLICATION"


class PelagicPDF(FPDF):
    """Base PDF class with Pelagic IntelX design system."""

    def __init__(self, title=""):
        super().__init__()
        self.doc_title = title
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 6)
        self.set_text_color(*TEXT_SEC)
        self.cell(0, 10, FOOTER, align="C")

    def section_title(self, text, size=14):
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*ACCENT)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def subsection_title(self, text, size=11):
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*TEAL_MID)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text, size=9):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*TEXT)
        self.multi_cell(0, 4.5, text)
        self.ln(2)

    def secondary_text(self, text, size=8):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*TEXT_SEC)
        self.multi_cell(0, 4, text)
        self.ln(1)

    def accent_text(self, text, size=9):
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*ACCENT)
        self.multi_cell(0, 4.5, text)
        self.ln(1)

    def divider(self):
        y = self.get_y()
        self.set_draw_color(200, 210, 215)
        self.set_line_width(0.3)
        self.line(10, y, 200, y)
        self.ln(4)

    def accent_bar(self):
        y = self.get_y()
        self.set_fill_color(*ACCENT)
        self.rect(10, y, 190, 1.5, "F")
        self.ln(5)

    def stat_box(self, label, value, x, y, w=42, h=22):
        self.set_fill_color(*TEAL_LIGHT)
        self.rect(x, y, w, h, "F")
        # Teal left accent strip
        self.set_fill_color(*TEAL_MID)
        self.rect(x, y, 2, h, "F")
        self.set_xy(x + 2, y + 3)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(*ACCENT)
        self.cell(w - 4, 7, value, align="C")
        self.set_xy(x + 2, y + 12)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*TEXT)
        self.cell(w - 4, 5, label, align="C")

    def quote_block(self, quote, attribution):
        y_start = self.get_y()
        # Render quote text first to calculate height
        self.set_x(18)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(*TEXT_SEC)
        self.multi_cell(170, 4.5, f'"{quote}"')
        self.set_x(18)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*ACCENT)
        self.cell(170, 5, f"-- {attribution}")
        y_end = self.get_y() + 5
        # Draw accent bar on left spanning full height
        self.set_fill_color(*ACCENT)
        self.rect(12, y_start, 2, y_end - y_start, "F")
        self.set_y(y_end)
        self.ln(4)

    def title_block(self, title, subtitle=""):
        self.ln(5)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*TEAL_MID)
        self.cell(0, 5, "PELAGIC INTELX", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(*TEXT)
        self.multi_cell(0, 9, title)
        self.ln(1)
        self.accent_bar()
        if subtitle:
            self.set_font("Helvetica", "", 10)
            self.set_text_color(*TEXT_SEC)
            self.multi_cell(0, 5, subtitle)
            self.ln(3)


def create_press_release():
    pdf = PelagicPDF("Press Release")
    pdf.add_page()

    # Header
    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*TEAL_MID)
    pdf.cell(0, 5, "PELAGIC INTELX", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 6, "FOR IMMEDIATE RELEASE", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 8, "Pelagic IntelX Launches First AI-Powered\nPacific Plastic Density Map")
    pdf.ln(1)
    pdf.accent_bar()

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT_SEC)
    pdf.cell(0, 5, "Seattle, WA -- March 25, 2026", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(*TEXT_SEC)
    pdf.multi_cell(0, 4.5, "\"Mapping the Invisible\" campaign reveals 16 previously undocumented plastic accumulation zones across the Pacific basin using AI-satellite fusion technology.")
    pdf.ln(4)

    # Stats row — 3 across
    y_stats = pdf.get_y()
    pdf.stat_box("Data Points", "3,844", 10, y_stats, 60, 20)
    pdf.stat_box("Accumulation Zones", "16", 73, y_stats, 60, 20)
    pdf.stat_box("Peak Density", "580K/km\u00b2", 136, y_stats, 60, 20)
    pdf.set_y(y_stats + 24)

    # Body paragraphs
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 4.5,
        "The world's oceans absorb an estimated 11 million metric tons of plastic waste annually, yet the distribution of this debris across open water remains poorly understood. Current monitoring relies on vessel-based trawl surveys that cover less than 0.1% of ocean surface area, leaving vast stretches of the Pacific effectively unmapped. This data gap has stalled international enforcement and undermined the scientific basis for the Global Plastics Treaty negotiations.")
    pdf.ln(2)

    pdf.multi_cell(0, 4.5,
        "Pelagic IntelX today announced the public release of its Pacific Plastic Density Map, the first comprehensive AI-generated model of marine plastic distribution across the Pacific basin. The map synthesizes 3,844 validated data points drawn from multispectral satellite imagery, autonomous sensor networks, and historical trawl survey records to produce a continuous density surface at 25-kilometer resolution. The platform identified 16 previously undocumented accumulation zones, including a high-density corridor between the Marshall Islands and Wake Atoll where concentrations reached 580,000 particles per square kilometer -- 40% above existing model predictions.")
    pdf.ln(2)

    pdf.multi_cell(0, 4.5,
        "The release marks the launch of \"Mapping the Invisible,\" a communications campaign designed to translate Pelagic IntelX's data intelligence into actionable policy tools. The interactive scrollytelling microsite allows policymakers, researchers, and journalists to explore accumulation zones by depth, density, and proximity to maritime boundaries. An accompanying open-access dataset and API enable third-party researchers to integrate the findings into independent models. The campaign arrives ahead of INC-6, the final negotiating session for the Global Plastics Treaty, where Pacific Island delegates have cited the absence of granular spatial data as a barrier to binding source-reduction targets.")
    pdf.ln(2)

    # Quotes
    pdf.quote_block(
        "We built this platform because you cannot regulate what you cannot see. For the first time, enforcement agencies have a near-real-time picture of where plastic accumulates, how deep it extends, and which upstream sources are most likely responsible.",
        "Dr. Elena Vasquez, CEO, Pelagic IntelX"
    )
    pdf.quote_block(
        "The depth-resolved data is what sets this apart. Previous satellite estimates captured surface debris only. Pelagic's volumetric model shows that nearly 60% of microplastic mass sits below the neuston layer, invisible to conventional remote sensing.",
        "Dr. James Okonkwo, Senior Research Scientist, NOAA Marine Debris Program"
    )

    pdf.divider()

    # About section
    pdf.section_title("About Pelagic IntelX", 11)
    pdf.body_text(
        "Pelagic IntelX is an ocean intelligence company that applies machine learning and satellite remote sensing to map marine plastic pollution at scale. Founded in 2023, the company partners with national environment agencies, intergovernmental bodies, and research institutions to close the data gap that limits enforcement of marine pollution regulations. Pelagic IntelX is headquartered in Seattle, WA.")

    pdf.section_title("Media Contact", 11)
    pdf.body_text("Nathan Fitzgerald, Director of Strategic Communications\nnathan@pelagicintelx.com | +1 (206) 555-0147 | Press kit: press.pelagicintelx.com")

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-press-release.pdf"))
    print("  Created: pelagicintelx-press-release.pdf")


def create_media_one_pager():
    pdf = PelagicPDF("Media One-Pager")
    pdf.add_page()

    pdf.title_block(
        "Media Brief: Mapping the Invisible",
        "At-a-glance reference for editorial coverage of the Pacific Plastic Density Map"
    )

    # Key stats grid
    pdf.section_title("Key Findings", 12)
    y = pdf.get_y()
    pdf.stat_box("Data Points Analyzed", "3,844", 10, y, 44, 24)
    pdf.stat_box("Accumulation Zones", "16", 57, y, 44, 24)
    pdf.stat_box("Peak Density (particles/km\u00b2)", "580,000", 104, y, 44, 24)
    pdf.stat_box("Above Prior Predictions", "40%", 151, y, 44, 24)
    pdf.set_y(y + 30)

    pdf.divider()

    # What makes this different
    pdf.section_title("What Makes This Different", 12)

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(5, 5, ">")
    pdf.set_text_color(*TEXT)
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(40, 5, "AI + Satellite Fusion:")
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(0, 5, "Combines multispectral satellite imagery with autonomous ocean sensor data and historical trawl records through a machine learning pipeline to produce continuous density estimates -- not isolated point samples.")
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(5, 5, ">")
    pdf.set_text_color(*TEXT)
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(40, 5, "Depth-Resolved Model:")
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(0, 5, "Goes beyond surface-only estimates. The volumetric model maps plastic distribution across three depth layers (0-50m, 60-130m, 130-200m), revealing that nearly 60% of microplastic mass is invisible to conventional remote sensing.")
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(5, 5, ">")
    pdf.set_text_color(*TEXT)
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(40, 5, "Policy-Ready Output:")
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(0, 5, "Data is structured for direct integration into maritime enforcement systems and treaty negotiations. Open API available. Designed for the INC-6 Global Plastics Treaty timeline.")
    pdf.ln(4)

    pdf.divider()

    # Embed-ready quotes
    pdf.section_title("Embed-Ready Quotes", 12)

    pdf.quote_block(
        "You cannot regulate what you cannot see. This map gives enforcement agencies a near-real-time picture of where plastic accumulates and which upstream sources are most likely responsible.",
        "Dr. Elena Vasquez, CEO, Pelagic IntelX"
    )
    pdf.quote_block(
        "The depth-resolved data is what sets this apart. Nearly 60% of microplastic mass sits below the neuston layer, invisible to conventional remote sensing.",
        "Dr. James Okonkwo, NOAA Marine Debris Program"
    )
    pdf.quote_block(
        "Pacific Island nations have been negotiating blind. Granular spatial data like this is exactly what delegates need to push for binding source-reduction targets at INC-6.",
        "Rina Talei, Pacific Islands Forum Environment Adviser"
    )
    pdf.ln(3)

    pdf.divider()

    # Resources
    pdf.section_title("Resources", 12)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    items = [
        ("Interactive Map:", "map.pelagicintelx.com"),
        ("Open Dataset & API:", "data.pelagicintelx.com/api/v1"),
        ("Methodology Paper:", "pelagicintelx.com/methodology"),
        ("Press Kit & Assets:", "press.pelagicintelx.com"),
    ]
    for label, url in items:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*TEXT)
        pdf.cell(40, 5, label)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(0, 5, url, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.divider()
    pdf.section_title("Media Contact", 10)
    pdf.body_text("Nathan Fitzgerald, Director of Strategic Communications\nnathan@pelagicintelx.com | +1 (206) 555-0147")

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-media-one-pager.pdf"))
    print("  Created: pelagicintelx-media-one-pager.pdf")


def create_social_content_brief():
    pdf = PelagicPDF("Social Content Brief")
    pdf.add_page()

    pdf.title_block(
        "Social Content Deployment Plan",
        "Mapping the Invisible Campaign -- Launch Week Content Calendar"
    )

    # X/Twitter Thread
    pdf.section_title("X/Twitter Launch Thread", 12)
    pdf.secondary_text("Deploy: Launch Day, 9:00 AM ET | Account: @PelagicIntelX")

    tweets = [
        ("1/7", "We just released the first AI-generated map of plastic pollution across the entire Pacific basin. 3,844 data points. 16 accumulation zones no one had documented before. Here's what we found.", "268 chars | Attach: hero map image"),
        ("2/7", "The biggest surprise: a high-density corridor between the Marshall Islands and Wake Atoll. 580,000 particles per square kilometer. That's 40% above what existing models predicted.", "214 chars | Attach: density heatmap detail"),
        ("3/7", "Why didn't we know this before? Because vessel surveys cover less than 0.1% of ocean surface. We combined satellite imagery, ocean sensors, and machine learning to fill in the rest.", "222 chars | Attach: methodology infographic"),
        ("4/7", "And here's what no satellite can show you: the depth. Nearly 60% of microplastic mass sits below 50 meters, invisible from above. Our volumetric model maps three depth layers down to 200m.", "230 chars | Attach: 3D depth model screenshot"),
        ("5/7", "This matters right now. INC-6 -- the final negotiation for the Global Plastics Treaty -- starts in weeks. Pacific Island delegates have said they can't push for binding targets without spatial data. Now they have it.", "252 chars | No attachment"),
        ("6/7", "The full dataset is open access. The API is live. If you're a researcher, policymaker, or journalist, you can query any coordinate in the Pacific and get density estimates by depth layer.", "227 chars | Attach: API documentation screenshot"),
        ("7/7", "Explore the interactive map yourself. We built it to make the invisible visible. [link]\n\n#OceanPlastic #GlobalPlasticsTreaty #MarineScience #ClimateData #AI", "195 chars | Attach: microsite preview GIF"),
    ]

    for num, text, meta in tweets:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ACCENT)
        pdf.cell(10, 5, num)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(170, 4.2, text)
        pdf.set_font("Helvetica", "I", 7)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(0, 4, f"   {meta}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    pdf.ln(2)
    pdf.divider()

    # LinkedIn
    pdf.section_title("LinkedIn Long-Form Post", 12)
    pdf.secondary_text("Deploy: Launch Day, 11:00 AM ET | Personal profile + Company page")

    pdf.subsection_title("Hook (first 2 lines, visible before 'see more'):")
    pdf.body_text("The Pacific Ocean is hiding something. We just mapped it for the first time.")

    pdf.subsection_title("Body:")
    pdf.body_text(
        "Today Pelagic IntelX publicly released the Pacific Plastic Density Map -- the first AI-generated continuous model of marine plastic distribution across the Pacific basin.\n\n"
        "We synthesized 3,844 validated data points from satellite imagery, autonomous sensors, and historical surveys. The result: 16 previously undocumented accumulation zones, peak concentrations of 580,000 particles/km2, and a volumetric depth model showing that nearly 60% of microplastic mass is invisible from the surface.\n\n"
        "This matters because international enforcement requires spatial data that, until now, didn't exist at this resolution. With INC-6 -- the final Global Plastics Treaty negotiation -- approaching, Pacific Island nations finally have the granular evidence needed to advocate for binding source-reduction targets.\n\n"
        "The dataset is open access. The API is live. The interactive map is public.")

    pdf.subsection_title("CTA:")
    pdf.body_text("Explore the map: [link] | Access the API: [link] | Read the methodology: [link]\n\nIf you work in ocean policy, environmental research, or marine conservation, I'd welcome your perspective on what this data reveals. What patterns do you see?")

    pdf.add_page()

    # Posting schedule
    pdf.section_title("Posting Schedule: Launch Week", 12)
    schedule = [
        ("Launch Day", "X thread (9 AM ET) + LinkedIn post (11 AM ET) + Instagram carousel (1 PM ET)"),
        ("Day 2", "X: Quote-tweet thread post #4 (depth model) with new visual + LinkedIn: Comment engagement on Day 1 post"),
        ("Day 3", "X: Single post with partner quote (Dr. Okonkwo) + Share any earned media coverage"),
        ("Day 4", "X: Data spotlight -- Marshall Islands corridor finding + Instagram Story: Behind the methodology"),
        ("Day 5", "LinkedIn: Article repost or op-ed excerpt + X: Respond to substantive replies from thread"),
        ("Day 6", "X: Weekend engagement -- poll on ocean plastic awareness + Instagram: Reel (30s map flythrough)"),
        ("Day 7", "X: Week-in-review thread (3 posts) with engagement metrics + LinkedIn: Thank you + next steps post"),
    ]
    for day, content in schedule:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ACCENT)
        pdf.cell(22, 5, day)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(158, 4.5, content)
        pdf.ln(1.5)

    pdf.ln(2)
    pdf.divider()

    # Hashtag strategy
    pdf.section_title("Hashtag Strategy", 12)
    pdf.subsection_title("Primary (use on all posts):")
    pdf.body_text("#OceanPlastic  #GlobalPlasticsTreaty  #MarineScience  #ClimateData  #MappingTheInvisible")
    pdf.subsection_title("Secondary (rotate by post):")
    pdf.body_text("#PlasticPollution  #OceanConservation  #AIforGood  #BluePlanet  #INC6")
    pdf.ln(2)

    pdf.divider()

    # Engagement templates
    pdf.section_title("Engagement Response Templates", 12)

    pdf.subsection_title("Scenario 1: Skeptic (\"AI models aren't reliable\" / \"How do you validate this?\")")
    pdf.body_text("Valid question. Our model is validated against 412 in-situ trawl survey records with a mean absolute error of 8.3%. The full methodology and validation dataset are open access: [link]. We welcome independent replication.")

    pdf.subsection_title("Scenario 2: Enthusiast (\"This is incredible!\" / \"How can I help?\")")
    pdf.body_text("Thank you! Three ways to amplify: (1) Share the interactive map with your network, (2) if you're a researcher, the open API lets you integrate our data into your own models, (3) follow our work as we expand coverage to the Atlantic basin in Q3.")

    pdf.subsection_title("Scenario 3: Journalist DM (\"Can we set up an interview?\")")
    pdf.body_text("Absolutely. Our CEO Dr. Elena Vasquez and our lead data scientist are both available for interviews. I'll DM you our media contact (nathan@pelagicintelx.com) to coordinate scheduling and share the press kit.")

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-social-content-brief.pdf"))
    print("  Created: pelagicintelx-social-content-brief.pdf")


def create_depth_model_methodology():
    pdf = PelagicPDF("Depth Model Methodology")
    pdf.add_page()

    pdf.title_block(
        "Sub-Surface Volumetric Density Model:\nMethodology and Validation",
        "Pelagic IntelX Technical Report | March 2026"
    )

    # Abstract
    pdf.section_title("Abstract", 12)
    pdf.body_text(
        "This report describes the methodology for constructing a three-dimensional volumetric model of marine plastic density across the Pacific basin. The model fuses multispectral satellite imagery, acoustic depth-profiling sensor data, and historical trawl survey records through a supervised machine learning pipeline to estimate particle concentrations across three defined depth layers: the neuston layer (0-50m), the pycnocline transition zone (60-130m), and the deep scatter layer (130-200m). The resulting model provides continuous density surfaces at 25-kilometer horizontal resolution and three-layer vertical resolution, validated against 412 independent in-situ observations with a mean absolute error of 8.3%. We identify 16 previously undocumented accumulation zones and document peak concentrations of 580,000 particles per square kilometer in a corridor between the Marshall Islands and Wake Atoll."
    )

    pdf.divider()

    # 1. Data Fusion Approach
    pdf.section_title("1. Data Fusion Approach", 12)
    pdf.body_text(
        "The model integrates three primary data streams, each contributing distinct observational capabilities and covering different spatial and temporal scales."
    )

    pdf.subsection_title("1.1 Multispectral Satellite Imagery")
    pdf.body_text(
        "Surface reflectance data from Sentinel-2 MSI and Landsat-9 OLI sensors provide the foundation for surface-layer density estimation. We process Level-2A atmospherically corrected imagery at 10-meter native resolution, applying a spectral unmixing algorithm trained on verified marine debris signatures in the near-infrared (Band 8, 842nm) and shortwave infrared (Band 11, 1610nm) channels. Cloud-masked composites are generated at 16-day intervals over a 24-month collection window (March 2024 - February 2026), yielding 2,180 valid observation tiles across the study area. The spectral signature library includes 340 verified plastic debris samples covering polyethylene, polypropylene, and nylon polymer types."
    )

    pdf.subsection_title("1.2 Acoustic Depth-Profiling Sensors")
    pdf.body_text(
        "Sub-surface particle estimates derive from a network of 23 autonomous profiling floats equipped with 200kHz acoustic backscatter sensors, deployed across the North and South Pacific gyres from June 2024 through January 2026. Each float executes daily depth profiles from surface to 200 meters, recording backscatter intensity at 1-meter vertical resolution. Particle concentration is inferred from backscatter cross-section using a transfer function calibrated against collocated net-tow samples (n=87, r-squared=0.81). The acoustic data provide the primary observational constraint for the pycnocline and deep scatter layers."
    )

    pdf.subsection_title("1.3 Historical Trawl Survey Records")
    pdf.body_text(
        "We incorporate 1,664 georeferenced trawl survey records from the NOAA Marine Debris Monitoring database, the 5 Gyres Institute sampling archive, and published literature spanning 2015-2025. Records are standardized to particles per square kilometer using reported tow parameters (net width, tow distance, depth). These records serve dual purposes: as training labels for the satellite-acoustic fusion model and as an independent validation set (412 records withheld from training)."
    )

    pdf.add_page()

    # 2. Depth Layer Definitions
    pdf.section_title("2. Depth Layer Definitions", 12)
    pdf.body_text(
        "The model resolves plastic distribution across three oceanographically defined depth layers, selected to capture distinct physical transport regimes."
    )

    layers = [
        ("Neuston Layer (0-50m)",
         "The surface-influenced zone where wind-driven Ekman transport and Stokes drift concentrate buoyant plastic debris. This layer is partially observable via satellite remote sensing and represents the domain where most historical survey data was collected. Physical characteristics: dominated by wind mixing, temperature gradients of 0.5-2.0 degrees C, and diurnal vertical migration of biofouled particles."),
        ("Pycnocline Transition Zone (60-130m)",
         "The density-stratified layer where negatively buoyant and biofouled particles accumulate at isopycnal surfaces. This layer is invisible to satellite observation and is the primary domain where the acoustic sensor network contributes novel observational data. The pycnocline acts as a physical trap, concentrating particles that have lost buoyancy through biofouling or fragmentation. Model results indicate this layer contains approximately 35% of total water-column plastic mass."),
        ("Deep Scatter Layer (130-200m)",
         "The region below the main pycnocline where vertical flux of fragmenting microplastics intersects with the deep scattering layer biological community. Particle residence times in this layer are estimated at 18-36 months, significantly longer than the neuston layer (2-6 months). This layer accounts for approximately 25% of total estimated mass and represents the least-observed component of the marine plastic inventory."),
    ]
    for title, desc in layers:
        pdf.subsection_title(title)
        pdf.body_text(desc)

    pdf.divider()

    # 3. Particle Generation Methodology
    pdf.section_title("3. Particle Generation Methodology", 12)
    pdf.body_text(
        "For the interactive visualization platform, we generate a representative particle field of 4,200 synthetic particles that reproduces the spatial statistics of the full-resolution density model while remaining computationally tractable for browser-based rendering."
    )

    pdf.subsection_title("3.1 Cluster Centers")
    pdf.body_text(
        "Three cluster centers are defined based on the highest-density regions identified in the full model: (1) the North Pacific Subtropical Gyre core (30.5N, 140.2W), (2) the Marshall Islands - Wake Atoll corridor (15.8N, 167.3E), and (3) the South Pacific convergence zone (22.1S, 148.7W). These centers correspond to the three highest-density accumulation zones in the model output."
    )

    pdf.subsection_title("3.2 Gaussian Spread Formula")
    pdf.body_text(
        "Particles are distributed around each cluster center using an anisotropic 2D Gaussian distribution:\n\n"
        "    P(x, y) = A * exp(-((x-x0)^2 / (2*sx^2) + (y-y0)^2 / (2*sy^2)))\n\n"
        "Where (x0, y0) is the cluster center, sx and sy are the longitudinal and latitudinal standard deviations (set to 15 degrees and 8 degrees respectively to reflect the elongated geometry of subtropical gyres), and A is the amplitude normalized to produce the target particle count per cluster. Depth assignment follows a weighted multinomial distribution: 40% neuston, 35% pycnocline, 25% deep scatter, with Gaussian noise (sigma = 5m) applied to individual particle depths within each layer."
    )

    pdf.add_page()

    # 4. Validation
    pdf.section_title("4. Validation Approach", 12)
    pdf.body_text(
        "Model accuracy is assessed against a withheld validation set of 412 in-situ trawl survey records not used in model training. The validation protocol follows three complementary approaches:\n\n"
        "Point-to-point comparison: Model-predicted density at each validation site is compared against observed density. The mean absolute error across all validation sites is 8.3%, with a root mean square error of 12,400 particles/km2. Correlation between predicted and observed values yields r-squared = 0.79 (p < 0.001).\n\n"
        "Spatial pattern validation: The model correctly identifies 14 of 16 accumulation zones (sensitivity = 87.5%) with 2 false positives (specificity = 91.2%). The two missed zones are in the eastern South Pacific where acoustic sensor coverage is sparsest.\n\n"
        "Depth layer validation: For the 87 sites with collocated acoustic-trawl depth profiles, the model correctly assigns the peak-density layer in 74 cases (accuracy = 85.1%). Misassignment occurs primarily at the neuston-pycnocline boundary where biofouling-driven vertical migration creates temporal variability."
    )

    pdf.divider()

    # 5. Limitations
    pdf.section_title("5. Limitations", 12)
    pdf.body_text(
        "Several limitations constrain the current model and should be considered when interpreting results:\n\n"
        "Temporal resolution: The model produces a time-averaged density surface over a 24-month window and does not capture seasonal or event-driven variability. Monsoon-season transport pulses and ENSO-related gyre shifts may produce transient patterns not represented in the current output.\n\n"
        "Polymer-type discrimination: The spectral unmixing algorithm distinguishes broad polymer categories (PE, PP, nylon) but cannot resolve specific product types or degradation states. Size-class estimates below 1mm are extrapolated from empirical fragmentation models rather than directly observed.\n\n"
        "Depth layer boundaries: The three-layer vertical structure is a simplification of continuous depth distributions. The 10-meter gap between the neuston and pycnocline layers (50-60m) reflects the transition zone where neither surface nor acoustic sensors provide reliable constraints.\n\n"
        "Spatial coverage: Acoustic sensor coverage is concentrated in the North Pacific subtropical gyre, with sparser coverage in the South Pacific and equatorial regions. Model uncertainty increases in areas distant from sensor deployment sites."
    )

    pdf.divider()

    # 6. References
    pdf.section_title("6. References", 12)
    refs = [
        "Eriksen, M., et al. (2014). Plastic pollution in the world's oceans. PLoS ONE, 9(12), e111913.",
        "Lebreton, L., et al. (2018). Evidence that the Great Pacific Garbage Patch is rapidly accumulating plastic. Scientific Reports, 8, 4666.",
        "van Sebille, E., et al. (2020). The physical oceanography of the transport of floating marine debris. Environmental Research Letters, 15(2), 023003.",
        "Kukulka, T., et al. (2012). The effect of wind mixing on the vertical distribution of buoyant plastic debris. Geophysical Research Letters, 39, L07601.",
        "Koelmans, A.A., et al. (2017). All is not lost: Deriving a top-down mass budget of plastic at sea. Environmental Research Letters, 12(11), 114028.",
        "Maximenko, N., et al. (2019). Toward the integrated marine debris observing system. Frontiers in Marine Science, 6, 447.",
    ]
    for ref in refs:
        pdf.set_font("Helvetica", "", 7.5)
        pdf.set_text_color(*TEXT_SEC)
        pdf.multi_cell(0, 3.5, ref)
        pdf.ln(1.5)

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-depth-model-methodology.pdf"))
    print("  Created: pelagicintelx-depth-model-methodology.pdf")


def create_op_ed():
    pdf = PelagicPDF("Op-Ed")
    pdf.add_page()

    pdf.title_block(
        "The Ocean Has a Memory",
        "Op-Ed Draft | Target: Nature Comment / The Atlantic / The Guardian"
    )

    # Meta info
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT_SEC)
    pdf.cell(0, 4, "Word count: ~810 | By Dr. Elena Vasquez, CEO, Pelagic IntelX", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.divider()

    # Target outlets
    pdf.section_title("Target Outlets (ranked)", 10)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT_SEC)
    pdf.cell(0, 4, "1. Nature Comment  |  2. The Atlantic (Planet section)  |  3. The Guardian (Environment Opinion)", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.divider()

    # Body
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*TEXT)

    paragraphs = [
        "The ocean remembers what we throw away. Not as a metaphor -- as a physical fact. Every polyethylene bottle cap, every fragment of polypropylene fishing net, every degraded sliver of nylon packaging enters a fluid archive that sorts, concentrates, and preserves debris according to the same forces that govern currents, salinity gradients, and thermocline depth. The ocean does not forget. It files.",

        "For decades, our attempts to read that archive have been laughably inadequate. The primary tool for measuring marine plastic pollution remains the manta trawl: a fine-mesh net towed behind a research vessel for 30 minutes at a time, sampling a strip roughly one meter wide. By the most generous estimates, trawl surveys have directly observed less than 0.1% of the Pacific Ocean's surface area. We have been trying to read a library by glancing at a single page.",

        "This is not merely an academic problem. The Global Plastics Treaty -- the most significant multilateral environmental agreement since Paris -- enters its final negotiating session this year at INC-6. Delegates from Pacific Island nations, who bear the most disproportionate burden of marine plastic accumulation relative to their own waste generation, have repeatedly stated that they cannot advocate for binding source-reduction targets without granular spatial data showing where plastic accumulates and where it originates. The absence of evidence has become a negotiating weapon for nations that prefer voluntary commitments to enforceable ones.",

        "Artificial intelligence is changing this calculus. At Pelagic IntelX, we have spent three years building a machine learning pipeline that fuses multispectral satellite imagery, autonomous acoustic sensor profiles, and historical survey records into a continuous density model of the Pacific basin. The result, published today as an open-access interactive map, identifies 16 previously undocumented accumulation zones and documents peak concentrations of 580,000 particles per square kilometer in a corridor between the Marshall Islands and Wake Atoll -- 40% higher than any existing model predicted.",

        "But the surface is only part of the story. Our volumetric depth model, constrained by acoustic profiling data from 23 autonomous floats, reveals that nearly 60% of microplastic mass sits below 50 meters, trapped along pycnocline density gradients where biofouled particles lose buoyancy and accumulate. This sub-surface reservoir is invisible to satellite observation, absent from every surface-only model that has informed policy discussions to date, and orders of magnitude larger than previously estimated. The ocean's memory extends downward.",

        "The policy implications are immediate and concrete. First, source attribution. By combining density patterns with oceanographic transport models, it is now possible to trace accumulation zones back to probable discharge points along coastlines and river mouths. This transforms plastic pollution from a diffuse global problem into a geographically specific enforcement challenge. If we can show that a particular accumulation zone is fed primarily by discharge from three river systems across two national jurisdictions, the question shifts from 'who should act' to 'how fast.'",

        "Second, depth matters for impact assessment. The ecological damage models used in treaty negotiations rely almost exclusively on surface encounter rates between marine organisms and debris. If 60% of the mass is below the surface, these models are systematically underestimating biological exposure -- particularly for mesopelagic fish species, deep-diving marine mammals, and filter-feeding organisms that operate at pycnocline depths.",

        "Third, the data architecture matters as much as the data itself. We have released a full open-access API precisely because closed datasets reproduce the power asymmetries that have stalled negotiations. When Pacific Island delegates walk into INC-6, they should be able to query the same data, at the same resolution, as any delegation with a well-funded national research program.",

        "The ocean's memory is long, but it is not infinite. Plastic does fragment. It does disperse. And the signal-to-noise ratio in satellite imagery degrades as particles shrink below detection thresholds. The window for mapping the current generation of macroplastic debris -- before it fragments into microplastic confetti that is functionally unmappable -- is measured in years, not decades.",

        "We have the tools. We have the data. What remains is the question that has always defined environmental governance: whether evidence will be allowed to compel action, or whether the absence of perfect certainty will continue to serve as permission for indefinite delay. The ocean remembers. The question is whether we will."
    ]

    for p in paragraphs:
        pdf.multi_cell(0, 5, p)
        pdf.ln(3)

    pdf.ln(2)
    pdf.divider()
    pdf.secondary_text("Dr. Elena Vasquez is the CEO and co-founder of Pelagic IntelX, an ocean intelligence company headquartered in Seattle. She previously served as a research scientist at NOAA's Pacific Marine Environmental Laboratory and holds a PhD in physical oceanography from the University of Washington.")

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-op-ed.pdf"))
    print("  Created: pelagicintelx-op-ed.pdf")


def create_stakeholder_matrix():
    pdf = PelagicPDF("Stakeholder Matrix")
    pdf.add_page("L")  # Landscape

    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*TEAL_MID)
    pdf.cell(0, 5, "PELAGIC INTELX", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(*TEXT)
    pdf.cell(0, 8, "Stakeholder Communications Matrix", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.set_fill_color(*ACCENT)
    pdf.rect(10, pdf.get_y(), 277, 1.2, "F")
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT_SEC)
    pdf.cell(0, 4, "Mapping the Invisible Campaign | Stakeholder Engagement Framework", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Table header
    cols = [
        ("Stakeholder", 30),
        ("Primary Interest", 38),
        ("Ask / CTA", 35),
        ("Key Message", 46),
        ("Channel Strategy", 38),
        ("Timing", 30),
        ("Success Metric", 38),
    ]
    total_w = sum(c[1] for c in cols)

    # Header row
    pdf.set_fill_color(*TEAL_MID)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_text_color(255, 255, 255)
    x_start = 10
    y_start = pdf.get_y()
    for label, w in cols:
        pdf.set_xy(x_start, y_start)
        pdf.cell(w, 8, label, border=0, fill=True, align="C")
        x_start += w
    pdf.ln(10)

    # Data rows
    rows = [
        [
            "UNEP Officials",
            "Spatial data quality for INC-6 treaty text; enforcement feasibility evidence",
            "Cite Pelagic IntelX data in INC-6 working documents; endorse methodology",
            "First continuous-density Pacific map validated against 412 in-situ records -- ready for treaty-grade citation",
            "Direct briefing (Geneva); technical white paper; closed-door data workshop at INC-6 side event",
            "8 weeks pre-INC-6; follow-up brief 2 weeks before session opens",
            "Data citation in 1+ INC-6 working document; briefing attendance by 3+ UNEP programme officers",
        ],
        [
            "National EPA Leads",
            "Domestic enforcement tools; source attribution for river-to-ocean discharge pathways",
            "Pilot the source-attribution dashboard with 2 national agencies; co-publish enforcement case study",
            "Our model traces accumulation zones back to specific discharge points -- turning diffuse pollution into enforceable geography",
            "1:1 meetings at regional EPA convenings; demo of source-attribution dashboard; technical integration brief",
            "Launch week outreach; 30-day follow-up with pilot proposal",
            "2 signed pilot MOUs within 90 days; dashboard demo completed with 3+ agencies",
        ],
        [
            "Environmental NGOs",
            "Campaign ammunition for plastic treaty advocacy; shareable data visualizations",
            "Amplify map findings through NGO channels; co-brand data insights for advocacy reports",
            "16 undocumented zones and 580K particles/km2 peak -- the evidence base for binding targets, not voluntary pledges",
            "Pre-launch embargo briefing; social media asset kit; co-branded infographics; webinar partnership",
            "Embargo briefing 48hrs pre-launch; asset kit on launch day; webinar Week 3",
            "3+ NGO partner amplifications in launch week; co-branded content reaching 500K+ combined audience",
        ],
        [
            "Policy Journalists",
            "Exclusive data story; novel angle on plastics treaty coverage; visual assets",
            "File coverage of map launch; attend INC-6 with Pelagic data as analytical frame",
            "AI satellite fusion reveals 40% more plastic than models predicted -- and 60% of it is invisible below the surface",
            "Embargoed press release (72hrs); 1:1 briefing with CEO + data scientist; press kit with publication-ready visuals",
            "Embargo drop 72hrs pre-launch; interview availability launch day through Day 3",
            "4+ earned media placements in tier-1 outlets within 10 days; 2+ stories framing INC-6 coverage around Pelagic data",
        ],
        [
            "University Partners",
            "Open data for research; API access; co-publication opportunities; methodology validation",
            "Use open API for independent research; co-author validation studies; host student researcher cohort",
            "Full open-access dataset and API -- designed for independent replication, not proprietary lock-in",
            "Academic listserv announcement; direct outreach to 15 target PIs; conference poster at Ocean Sciences 2026",
            "API announcement on launch day; PI outreach Weeks 1-2; conference engagement Month 2-3",
            "50+ API registrations from .edu domains in 60 days; 2+ independent validation studies initiated",
        ],
    ]

    row_height = 27
    for i, row in enumerate(rows):
        y = pdf.get_y()
        if y + row_height > 195:
            pdf.add_page("L")
            y = 15

        # Alternate row bg
        if i % 2 == 0:
            pdf.set_fill_color(*TEAL_LIGHT)
        else:
            pdf.set_fill_color(255, 255, 255)

        x_pos = 10
        max_h = row_height
        for j, (_, w) in enumerate(cols):
            pdf.set_xy(x_pos, y)
            if j == 0:
                pdf.set_font("Helvetica", "B", 6.5)
                pdf.set_text_color(*TEAL_MID)
            else:
                pdf.set_font("Helvetica", "", 6)
                pdf.set_text_color(*TEXT)
            pdf.multi_cell(w, 3, row[j], border=0, fill=True)
            x_pos += w

        pdf.set_y(y + max_h)

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-stakeholder-matrix.pdf"))
    print("  Created: pelagicintelx-stakeholder-matrix.pdf")


def create_campaign_strategy_memo():
    pdf = PelagicPDF("Campaign Strategy Memo")
    pdf.add_page()

    pdf.title_block(
        "Strategic Communications Plan",
        "Pelagic IntelX | FY2026 Campaign Architecture"
    )
    pdf.secondary_text("CONFIDENTIAL -- For internal planning use")
    pdf.ln(2)

    # 1. Situation Analysis
    pdf.section_title("1. Situation Analysis", 12)
    pdf.body_text(
        "Pelagic IntelX has developed the first AI-generated continuous density model of Pacific marine plastic pollution, a technical capability that represents a significant advancement over existing survey-based approaches. However, the company faces a narrow strategic window: the Global Plastics Treaty enters its final negotiating session (INC-6) within months, Pacific Island delegations are actively seeking spatial data to support binding commitments, and several competing research groups are developing similar satellite-based models. The communications challenge is to establish Pelagic IntelX as the authoritative source for marine plastic spatial intelligence before the INC-6 window closes, while simultaneously building the brand credibility needed for commercial partnerships with national enforcement agencies.")
    pdf.body_text(
        "Current market position: Pre-revenue, seed-stage. Brand awareness among target stakeholders is near zero. No earned media history. No established journalist relationships in the ocean policy beat. The communications function must build credibility from a standing start within a 90-day operational window.")

    pdf.divider()

    # 2. Objectives
    pdf.section_title("2. Communications Objectives", 12)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(5, 5, "1.")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 4.5, "Establish Pelagic IntelX as the cited authority on Pacific plastic density data in at least 4 tier-1 media placements and 1 intergovernmental document within 90 days of campaign launch.")
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(5, 5, "2.")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 4.5, "Drive 25,000 unique visitors to the interactive map microsite in the first 30 days, with a 3.5-minute average session duration indicating substantive engagement with the data.")
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(5, 5, "3.")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 4.5, "Generate 3 qualified inbound leads from national environment agencies or intergovernmental bodies for pilot deployment of the source-attribution dashboard.")
    pdf.ln(4)

    pdf.divider()

    # 3. Target Audiences
    pdf.section_title("3. Target Audiences", 12)
    audiences = [
        ("Primary:", "UNEP programme officers and INC-6 national delegates; national EPA enforcement leads (US, AU, JP, KR); Pacific Islands Forum environment policy staff."),
        ("Secondary:", "Environmental policy journalists (NYT Climate, Guardian Environment, Nature News, Reuters Planet); ocean science researchers at R1 universities and NOAA."),
        ("Tertiary:", "Environmental NGO communications teams (Ocean Conservancy, 5 Gyres, Surfrider); climate-aware general public following treaty negotiations."),
    ]
    for label, desc in audiences:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ACCENT)
        pdf.cell(22, 5, label)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 4.5, desc)
        pdf.ln(1)

    pdf.add_page()

    # 4. Key Messages
    pdf.section_title("4. Key Messages", 12)
    pdf.subsection_title("Primary Message:")
    pdf.body_text("Pelagic IntelX's AI-powered Pacific Plastic Density Map makes the invisible visible -- providing the first continuous, depth-resolved picture of where marine plastic accumulates, how deep it extends, and where it originates.")

    pdf.subsection_title("For Policy Audiences:")
    pdf.body_text("You cannot enforce what you cannot measure. Our open-access data gives treaty negotiators the granular spatial evidence needed to move from voluntary commitments to binding, geographically specific reduction targets.")

    pdf.subsection_title("For Scientific Audiences:")
    pdf.body_text("The volumetric depth model reveals that 60% of microplastic mass sits below the neuston layer -- a sub-surface reservoir absent from every surface-only model informing current policy. The full dataset and API are open for independent validation.")

    pdf.subsection_title("For Media Audiences:")
    pdf.body_text("AI satellite fusion found 40% more plastic than existing models predicted, including 16 accumulation zones no one knew existed. And most of it is hidden below the surface, invisible to every previous estimate.")

    pdf.divider()

    # 5. Campaign Architecture
    pdf.section_title("5. Campaign Architecture", 12)

    pdf.subsection_title("Campaign 1: Mapping the Invisible")
    pdf.secondary_text("Window: Launch through Day 30 | Objective: Awareness + Authority")
    pdf.body_text(
        "The flagship launch campaign centered on the interactive microsite and open dataset release. Core narrative: AI and satellite technology reveal a Pacific plastic crisis 40% larger than anyone predicted. Tactics include embargoed press outreach, social media launch thread, NGO co-amplification, and a data journalism partnership. The microsite serves as the campaign hub, translating density data into an accessible scrollytelling experience for non-technical audiences while providing API access for researchers.")
    pdf.ln(1)

    pdf.subsection_title("Campaign 2: Plastic Doesn't Disappear")
    pdf.secondary_text("Window: Day 31 through Day 90 | Objective: Policy Influence + Lead Generation")
    pdf.body_text(
        "A sustained advocacy campaign timed to the INC-6 preparation period. Core narrative: sub-surface plastic represents a hidden reservoir that current models undercount, and the treaty must account for volumetric distribution, not just surface estimates. Tactics include an op-ed placement (target: Nature Comment), a closed-door data briefing for INC-6 delegates, a source-attribution dashboard demo for national agencies, and a co-published research brief with a university partner. This campaign shifts tone from awareness to action, converting the attention generated by Campaign 1 into institutional relationships and pilot commitments.")

    pdf.add_page()

    # 6. Channel Strategy
    pdf.section_title("6. Channel Strategy", 12)
    channels = [
        ("Earned Media", "Embargoed press release + 1:1 journalist briefings with CEO and lead scientist. Target 4 tier-1 placements. Priority outlets: Nature News, NYT Climate, Guardian Environment, Reuters Planet, Wired Science."),
        ("Owned Digital", "Interactive microsite (scrollytelling map), company blog (3 posts over 30 days: launch, methodology deep dive, depth model findings), email newsletter to research community."),
        ("Social Media", "X/Twitter launch thread (7 posts) + LinkedIn long-form post. Daily engagement cadence for 14 days. Paid amplification on LinkedIn targeting policy professionals ($1,200 budget)."),
        ("Direct Outreach", "1:1 briefing requests to 8 UNEP programme officers, 5 national EPA contacts, and 15 university PIs. Personalized outreach with data relevant to each stakeholder's jurisdiction or research focus."),
        ("Events", "INC-6 side event (data briefing, 45 min); Ocean Sciences 2026 poster presentation; 2 webinar partnerships with NGOs."),
        ("Paid Search", "Google Ads policy search campaign targeting policy professionals and researchers. $4,500/month budget. 30-day release window. See separate Google Ads Brief for details."),
    ]
    for label, desc in channels:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ACCENT)
        pdf.cell(30, 5, label)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 4.2, desc)
        pdf.ln(2)

    pdf.divider()

    # 7. 90-Day Roadmap
    pdf.section_title("7. 90-Day Roadmap", 12)
    phases = [
        ("Phase 1: Pre-Launch (Days -14 to 0)", [
            "Finalize press kit and media one-pager",
            "Embargo outreach to 12 target journalists",
            "Pre-brief 3 NGO partners for co-amplification",
            "Stage social content and schedule deployment",
            "Conduct CEO media training for on-camera interviews",
        ]),
        ("Phase 2: Launch (Days 1-14)", [
            "Embargo lift + press release distribution",
            "Social media launch thread + LinkedIn post",
            "Monitor and engage earned media coverage",
            "1:1 briefings with responding journalists",
            "Begin direct outreach to UNEP and EPA contacts",
        ]),
        ("Phase 3: Sustain (Days 15-45)", [
            "Op-ed submission to Nature Comment",
            "University PI outreach with API access",
            "NGO webinar partnership (reach target: 2,000 registrants)",
            "Source-attribution dashboard demo for 3 national agencies",
            "Blog post 2: methodology deep dive",
        ]),
        ("Phase 4: Convert (Days 46-90)", [
            "INC-6 side event data briefing",
            "Follow-up with agency contacts for pilot MOUs",
            "Co-publish research brief with university partner",
            "Campaign performance report and FY2027 planning",
            "Blog post 3: depth model findings + next steps (Atlantic expansion)",
        ]),
    ]
    for phase_title, items in phases:
        pdf.subsection_title(phase_title)
        for item in items:
            pdf.set_font("Helvetica", "", 8.5)
            pdf.set_text_color(*TEXT_SEC)
            pdf.cell(5, 4, "-")
            pdf.set_text_color(*TEXT)
            pdf.cell(0, 4, item, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    pdf.add_page()

    # 8. KPI Framework
    pdf.section_title("8. KPI Framework", 12)
    kpis = [
        ("Earned Media Placements", "4 tier-1 articles", "30 days", "Media monitoring (Meltwater)"),
        ("Microsite Unique Visitors", "25,000", "30 days", "Google Analytics"),
        ("Average Session Duration", "3.5 minutes", "30 days", "Google Analytics"),
        ("API Registrations (.edu)", "50+", "60 days", "Registration database"),
        ("Agency Pilot MOUs", "2 signed", "90 days", "BD pipeline tracker"),
        ("INC-6 Document Citation", "1+ working document", "90 days", "UNEP document review"),
    ]
    # Mini table
    pdf.set_fill_color(*TEAL_MID)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 7, "  Metric", fill=True)
    pdf.cell(35, 7, "  Target", fill=True)
    pdf.cell(25, 7, "  Window", fill=True)
    pdf.cell(60, 7, "  Measurement", fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

    for metric, target, window, measurement in kpis:
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*TEXT)
        pdf.cell(50, 6, f"  {metric}")
        pdf.set_text_color(*ACCENT)
        pdf.set_font("Helvetica", "B", 8)
        pdf.cell(35, 6, f"  {target}")
        pdf.set_font("Helvetica", "", 8)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(25, 6, f"  {window}")
        pdf.cell(60, 6, f"  {measurement}", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)
    pdf.divider()

    # 9. Budget Overview
    pdf.section_title("9. Budget Overview", 12)
    budget = [
        ("Paid social amplification (LinkedIn)", "$1,200"),
        ("Google Ads policy search campaign (30 days)", "$4,500"),
        ("Media monitoring (Meltwater, 3 months)", "$2,400"),
        ("Press release distribution (PR Newswire)", "$800"),
        ("INC-6 side event logistics", "$3,500"),
        ("Conference materials (Ocean Sciences poster)", "$600"),
        ("Webinar platform + promotion", "$900"),
        ("Contingency (15%)", "$2,085"),
    ]
    total = 0
    for item, cost in budget:
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.cell(130, 5, f"  {item}")
        pdf.set_text_color(*ACCENT)
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.cell(30, 5, cost, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)
    pdf.set_fill_color(*TEAL_MID)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(130, 7, "  Total Campaign Budget", fill=True)
    pdf.cell(30, 7, "$15,985", fill=True, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.divider()

    # 10. Risk Mitigation
    pdf.section_title("10. Risk Mitigation", 12)
    risks = [
        ("Data accuracy challenge:", "If a journalist or researcher questions model validity, respond with validation metrics (8.3% MAE, r2=0.79) and point to open methodology paper and withheld validation dataset. Offer to facilitate independent replication."),
        ("Competitor preemption:", "If a competing model publishes before our launch, pivot messaging to emphasize depth-resolved volumetric capability (unique differentiator) rather than surface density (which others can replicate)."),
        ("Treaty delay:", "If INC-6 is postponed, shift Campaign 2 timeline accordingly but accelerate agency pilot outreach to maintain momentum independent of the diplomatic calendar."),
        ("Negative media framing:", "If coverage frames AI ocean monitoring as surveillance or dual-use concern, emphasize open-access data policy, academic partnership model, and the defensive purpose (environmental protection, not maritime intelligence)."),
    ]
    for risk, mitigation in risks:
        if pdf.get_y() > 250:
            pdf.add_page()
        pdf.set_x(10)
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*ACCENT)
        pdf.multi_cell(0, 4.5, risk)
        pdf.set_x(10)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 4.2, mitigation)
        pdf.ln(2)

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-campaign-strategy-memo.pdf"))
    print("  Created: pelagicintelx-campaign-strategy-memo.pdf")


def create_google_ads_brief():
    pdf = PelagicPDF("Google Ads Brief")
    pdf.add_page()

    pdf.title_block(
        "Google Ads Policy Search Campaign Brief",
        "Pelagic IntelX | Mapping the Invisible Launch Window"
    )

    # Campaign overview
    pdf.section_title("Campaign Overview", 12)

    # Key params
    params = [
        ("Campaign Type:", "Google Search (text ads)"),
        ("Objective:", "Drive qualified traffic from policy professionals and environmental researchers to the interactive map microsite"),
        ("Budget:", "$4,500/month"),
        ("Window:", "30-day release cycle aligned with Mapping the Invisible launch"),
        ("CTR Target:", "3.5% (vs. 2.1% industry average for nonprofit/advocacy)"),
        ("Landing Page:", "map.pelagicintelx.com (interactive scrollytelling microsite)"),
    ]
    for label, value in params:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(35, 5, label)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*TEXT)
        pdf.cell(0, 5, value, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.divider()

    # Target audience
    pdf.section_title("Target Audience", 12)
    pdf.subsection_title("Primary: Policy Professionals")
    pdf.body_text("Government officials, intergovernmental body staff, and policy advisers working on marine pollution, environmental treaties, or ocean governance. Typically searching for data, reports, or evidence to inform policy positions.")
    pdf.subsection_title("Secondary: Environmental Researchers")
    pdf.body_text("University-based scientists, postdoctoral researchers, and research staff at agencies like NOAA, CSIRO, or JAMSTEC. Searching for datasets, methodology papers, or spatial data tools for marine debris research.")

    pdf.divider()

    # Keyword groups
    pdf.section_title("Keyword Strategy", 12)
    pdf.secondary_text("3 clusters, 15 keywords total. Organized by search intent.")

    pdf.ln(2)
    pdf.subsection_title("Cluster 1: Data & Research Intent")
    pdf.secondary_text("Users searching for marine plastic data, maps, or datasets")
    keywords1 = [
        "ocean plastic pollution map",
        "marine plastic density data",
        "Pacific Ocean plastic concentration",
        "marine debris spatial data",
        "microplastic distribution model",
    ]
    for kw in keywords1:
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.cell(0, 4.5, f"    {kw}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    pdf.subsection_title("Cluster 2: Policy & Treaty Intent")
    pdf.secondary_text("Users searching for policy-relevant information about plastics treaties")
    keywords2 = [
        "global plastics treaty data",
        "INC-6 plastic pollution evidence",
        "marine pollution enforcement data",
        "ocean plastic policy research",
        "plastic treaty negotiation evidence",
    ]
    for kw in keywords2:
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.cell(0, 4.5, f"    {kw}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    pdf.subsection_title("Cluster 3: Technology & Methodology Intent")
    pdf.secondary_text("Users searching for AI/satellite ocean monitoring approaches")
    keywords3 = [
        "AI ocean monitoring",
        "satellite marine debris detection",
        "machine learning ocean plastic",
        "remote sensing marine pollution",
        "ocean plastic tracking technology",
    ]
    for kw in keywords3:
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.cell(0, 4.5, f"    {kw}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.divider()

    # Ad copy
    pdf.section_title("Ad Copy", 12)

    pdf.subsection_title("Headline Variants (max 30 characters each):")
    headlines = [
        ("H1:", "Pacific Plastic Density Map", "26 chars"),
        ("H2:", "AI Ocean Plastic Intelligence", "29 chars"),
        ("H3:", "Map 16 Plastic Hotspots Free", "28 chars"),
    ]
    for label, text, chars in headlines:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ACCENT)
        pdf.cell(10, 5, label)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*TEXT)
        pdf.cell(80, 5, text)
        pdf.set_font("Helvetica", "", 7)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(0, 5, chars, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    pdf.subsection_title("Description Variants (max 90 characters each):")

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(10, 5, "D1:")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 5, "Explore 3,844 data points across 16 zones. Open-access AI density model. Free API.")
    pdf.set_font("Helvetica", "", 7)
    pdf.set_text_color(*TEXT_SEC)
    pdf.cell(0, 4, "82 chars", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)

    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*ACCENT)
    pdf.cell(10, 5, "D2:")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 5, "First depth-resolved Pacific plastic map. Validated data for policy and research.")
    pdf.set_font("Helvetica", "", 7)
    pdf.set_text_color(*TEXT_SEC)
    pdf.cell(0, 4, "81 chars", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.divider()

    # Audience targeting
    pdf.section_title("Audience Targeting Criteria", 12)
    targeting = [
        ("Geographic:", "United States, Australia, Japan, South Korea, Germany, United Kingdom, France, New Zealand, Fiji, Samoa, Tonga, Marshall Islands"),
        ("Language:", "English (primary), with Japanese and Korean ad variants in Phase 2"),
        ("Demographics:", "Age 28-65, all genders"),
        ("Affinity Audiences:", "Environmental advocates, Science & research professionals, Government & public policy"),
        ("In-Market:", "Environmental services, Scientific research tools, Government software"),
        ("Custom Intent:", "Users who searched for UNEP, plastics treaty, marine debris monitoring, ocean conservation data"),
        ("Exclusions:", "Job seekers, students under 22, consumer recycling searches (e.g., 'how to recycle plastic')"),
    ]
    for label, value in targeting:
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*ACCENT)
        pdf.cell(32, 5, label)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 4.5, value)
        pdf.ln(1)

    pdf.ln(2)
    pdf.divider()

    # Expected performance
    pdf.section_title("Expected Performance", 12)
    perf = [
        ("Monthly Budget:", "$4,500"),
        ("Avg. CPC (estimated):", "$2.80 - $3.50"),
        ("Monthly Clicks (estimated):", "1,285 - 1,607"),
        ("CTR Target:", "3.5% (industry avg: 2.1%)"),
        ("Impression Target:", "36,700 - 45,900"),
        ("Conversion Goal:", "API registration or dataset download"),
        ("Target Conversion Rate:", "8.5% of clicks (109 - 137 conversions/month)"),
        ("Cost per Conversion:", "$32.85 - $41.28"),
    ]
    for label, value in perf:
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(50, 5, label)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*TEXT)
        pdf.cell(0, 5, value, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)
    pdf.secondary_text("CTR target of 3.5% is justified by highly specific keyword targeting (low competition, high intent) and narrow audience definition. Industry average of 2.1% reflects broader advocacy/nonprofit campaigns with less targeted keyword selection.")

    pdf.ln(2)
    pdf.divider()

    # Landing page requirements
    pdf.section_title("Landing Page Requirements", 12)
    pdf.body_text("The landing page (map.pelagicintelx.com) must meet the following requirements for ad campaign effectiveness:")

    reqs = [
        "Load time under 3 seconds on mobile (current: 2.1s -- within threshold)",
        "Clear above-fold value proposition matching ad copy promises",
        "Visible CTA for API registration and dataset download within first scroll",
        "Mobile-responsive layout (policy professionals frequently access on mobile during travel/conferences)",
        "Google Ads conversion tracking pixel installed on: (a) API registration confirmation, (b) dataset download initiation, (c) microsite session > 2 minutes",
        "UTM parameter support for campaign attribution (utm_source=google, utm_medium=cpc, utm_campaign=mapping-invisible)",
        "No interstitial popups or modals on first visit (Google Ads policy compliance)",
        "Accessibility: WCAG 2.1 AA compliance for government audience requirements",
    ]
    for req in reqs:
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(*TEXT_SEC)
        pdf.cell(5, 4.5, "-")
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 4.5, req)
        pdf.ln(1)

    pdf.output(os.path.join(OUTPUT_DIR, "pelagicintelx-google-ads-brief.pdf"))
    print("  Created: pelagicintelx-google-ads-brief.pdf")


if __name__ == "__main__":
    print("Generating Pelagic IntelX PDF portfolio documents...")
    print()
    create_press_release()
    create_media_one_pager()
    create_social_content_brief()
    create_depth_model_methodology()
    create_op_ed()
    create_stakeholder_matrix()
    create_campaign_strategy_memo()
    create_google_ads_brief()
    print()
    print("All 8 PDFs generated successfully.")
