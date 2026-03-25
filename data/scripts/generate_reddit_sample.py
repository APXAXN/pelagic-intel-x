"""
Pelagic IntelX — Sample Reddit Data Generator
Generates realistic Reddit post/comment data matching PRAW output structure.
Can be replaced with real PRAW data later.
Output: data/raw/reddit_posts.json
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "raw"
RAW_DIR.mkdir(exist_ok=True)

random.seed(42)

SUBREDDITS = ["environment", "Futurology", "collapse", "MachineLearning"]

# Realistic posts per subreddit — reflecting how each community talks about ocean plastic
POSTS_BY_SUBREDDIT = {
    "environment": [
        {
            "title": "Microplastics found in every single sample of Antarctic sea ice tested",
            "selftext": "Researchers found microplastic particles in all 17 samples of Antarctic sea ice they tested. The most common types were PET and polypropylene. This is alarming because Antarctic waters were thought to be relatively pristine. The plastic concentrations ranged from 12 to 340 particles per liter of melted ice.",
            "score": 4521,
            "comments": [
                {"body": "We've contaminated literally everywhere on the planet. There's nowhere left that's clean.", "score": 892},
                {"body": "The question isn't where is the plastic anymore, it's where ISN'T the plastic. And the answer is nowhere.", "score": 654},
                {"body": "Can someone explain how the plastic gets all the way to Antarctica? Is it ocean currents?", "score": 423},
                {"body": "What frustrates me is we've known about this for decades and the policy response has been essentially nothing. Voluntary pledges don't work.", "score": 387},
                {"body": "I work in marine biology. The concentration numbers here are consistent with what we're seeing globally. The ocean current systems act as conveyor belts.", "score": 312},
            ],
        },
        {
            "title": "New study maps plastic pollution density across the Pacific — concentrations are 40% higher than models predicted",
            "selftext": "A new study using satellite imagery combined with machine learning has produced the most detailed map of plastic pollution density in the Pacific Ocean. The results show concentrations in some areas are significantly higher than what previous models estimated, particularly in the subtropical convergence zones.",
            "score": 3847,
            "comments": [
                {"body": "40% higher than predicted is terrifying. How bad do our models have to be before we realize we've been underestimating this the whole time?", "score": 1203},
                {"body": "Can anyone link to where you can actually see this map? I want to see what areas are worst.", "score": 567},
                {"body": "The fact that we need AI and satellites to even see how bad it is tells you something about the scale of the problem.", "score": 445},
                {"body": "Cleanup efforts are pointless if we don't stop the input. It's like mopping the floor while the faucet is still running.", "score": 398},
                {"body": "I'm a researcher who works on ocean plastic modeling. The discrepancy between models and observations has been a known issue. Satellite+AI approaches like this are exactly what we need to calibrate our predictions.", "score": 356},
            ],
        },
        {
            "title": "The Global Plastics Treaty negotiations have stalled again. What's the point?",
            "selftext": "Another round of negotiations for the UN Global Plastics Treaty ended without agreement on binding reduction targets. The fossil fuel and petrochemical lobby successfully pushed for voluntary commitments only. After five rounds of negotiations, we still don't have enforceable limits on plastic production.",
            "score": 2956,
            "comments": [
                {"body": "Voluntary commitments are where ambition goes to die. We need binding targets with enforcement mechanisms.", "score": 789},
                {"body": "The problem is the treaty negotiations don't have access to good enough data about where the plastic actually ends up. Hard to regulate what you can't measure.", "score": 534},
                {"body": "The fossil fuel industry is the plastic industry. Same feedstocks, same lobbyists, same playbook as climate denial.", "score": 478},
                {"body": "We need to map this problem at scale before regulators will take it seriously. You can't enforce what you can't see.", "score": 356},
            ],
        },
        {
            "title": "Ocean plastic is now found in the Mariana Trench — the deepest point on Earth",
            "selftext": "Scientists have discovered microplastic fibers at the bottom of the Mariana Trench, nearly 11,000 meters below the surface. The finding suggests that no part of the ocean is untouched by plastic pollution.",
            "score": 5234,
            "comments": [
                {"body": "The ocean doesn't forget what we put in it. Plastic doesn't disappear — it just moves to places where we can't see it.", "score": 1567},
                {"body": "How does it even get down there? The ocean must be acting like a giant distribution system for our waste.", "score": 678},
                {"body": "We really need better mapping of where all this plastic is accumulating. We can track weather systems in real time but we have no idea where our trash ends up.", "score": 445},
                {"body": "This should be front page news everywhere. We've polluted the entire ocean from surface to floor.", "score": 398},
            ],
        },
        {
            "title": "Why don't we have a real-time map of ocean plastic pollution?",
            "selftext": "We can track storms, shipping containers, and ocean temperatures in real time. Why hasn't anyone built a comprehensive real-time monitoring system for plastic pollution? Is it a technology problem or a funding problem?",
            "score": 1876,
            "comments": [
                {"body": "It's both. Detecting plastic from satellites is much harder than detecting temperature. The particles are small and the ocean is big. But AI and computer vision are starting to make it possible.", "score": 534},
                {"body": "There are some projects working on this. Satellite imagery + machine learning is the most promising approach. But the resolution needed is expensive.", "score": 423},
                {"body": "Because nobody with money cares enough. The data would be embarrassing for too many industries and governments.", "score": 389},
                {"body": "The technology exists now. What we lack is the political will to fund it at scale. A global ocean plastic monitoring network would cost less than a single fighter jet.", "score": 312},
                {"body": "I think the bigger issue is that even if we had the map, would policymakers actually use it? We have mountains of climate data and look how slow that response has been.", "score": 267},
            ],
        },
        {
            "title": "Microplastics detected in human blood for the first time — what does this mean?",
            "selftext": "Dutch researchers have detected microplastic particles in human blood samples for the first time. PET and polystyrene were the most common types found. The health implications are still unclear but the finding has shocked the scientific community.",
            "score": 8934,
            "comments": [
                {"body": "We're literally becoming plastic. This is the bioaccumulation endpoint everyone warned about.", "score": 2345},
                {"body": "The ocean plastic problem isn't just an ocean problem anymore. It's a human health problem. The plastic cycle goes: ocean > fish > food > us.", "score": 1234},
                {"body": "How much of this comes from ocean sources vs packaging vs clothing fibers? We need better tracking of the pathways.", "score": 567},
                {"body": "This should be the wake-up call. When the pollution is literally inside us, maybe we'll finally act.", "score": 489},
            ],
        },
        {
            "title": "Satellite imagery reveals massive floating plastic accumulation off the coast of Indonesia",
            "selftext": "New satellite analysis has identified a previously unmapped concentration of floating plastic debris in the Java Sea. The accumulation zone spans approximately 200 square kilometers and appears to be fed by river systems carrying waste from major urban centers.",
            "score": 2134,
            "comments": [
                {"body": "Southeast Asia is ground zero for ocean plastic input. The river systems carry massive amounts of waste into the ocean.", "score": 567},
                {"body": "Can we see these satellite images anywhere? The public needs to see what this actually looks like at scale.", "score": 434},
                {"body": "This is why we need continuous monitoring. These accumulation zones shift with currents and seasons. A one-time survey misses the dynamic picture.", "score": 378},
                {"body": "The technology to detect and map this exists. What we need is the funding to deploy it globally and the regulatory framework to act on the data.", "score": 289},
            ],
        },
    ],
    "Futurology": [
        {
            "title": "AI-powered drones can now detect ocean plastic from altitude — could this scale to global monitoring?",
            "selftext": "A startup has demonstrated AI-powered drones that can identify and classify plastic debris on the ocean surface from 100m altitude. The computer vision model was trained on 50,000 annotated images and can distinguish between different polymer types based on spectral signatures.",
            "score": 3421,
            "comments": [
                {"body": "This combined with satellite data could give us the first real-time picture of ocean plastic distribution. The tech is finally catching up to the problem.", "score": 876},
                {"body": "The question is whether this can scale. Drones are great for coastal areas but the open ocean is massive. You'd need satellite coverage for that.", "score": 654},
                {"body": "I work in remote sensing. The spectral signature approach is solid science. Different polymers reflect light differently in near-infrared. AI just makes the classification faster and more accurate.", "score": 534},
                {"body": "If we can map plastic density across the entire Pacific in real-time, that fundamentally changes the cleanup calculus. You can target resources where they matter most.", "score": 478},
                {"body": "This is the kind of AI application I actually get excited about. Not chatbots — actual planetary-scale problem solving.", "score": 423},
            ],
        },
        {
            "title": "Computer vision + satellite imagery could give us real-time ocean plastic density maps within 5 years",
            "selftext": "Researchers at a major university have published a paper showing that combining multispectral satellite imagery with deep learning models can estimate microplastic concentration in surface waters with 85% accuracy. They project that with current satellite constellation plans, global near-real-time monitoring could be feasible by 2028.",
            "score": 2876,
            "comments": [
                {"body": "85% accuracy is already good enough to be useful for policy. You don't need perfect data to make better decisions than we're making with no data.", "score": 756},
                {"body": "The real breakthrough here is making the invisible visible. Right now ocean plastic is an abstract problem because you can't see it at scale. A density map changes that.", "score": 623},
                {"body": "5 years feels optimistic but the trajectory is right. The satellite tech and the AI are both improving fast.", "score": 445},
                {"body": "Imagine if regulators could actually see, in real time, where plastic is accumulating. That's a fundamentally different policy conversation than abstract tonnage estimates.", "score": 398},
            ],
        },
        {
            "title": "The Ocean Cleanup removed 50 million kg of plastic from the Pacific — but is it making a dent?",
            "selftext": "The Ocean Cleanup project has announced a milestone of 50 million kilograms of plastic removed from the Great Pacific Garbage Patch. Critics argue that the inflow rate still far exceeds cleanup capacity and that the project focuses on large debris while ignoring microplastics.",
            "score": 4567,
            "comments": [
                {"body": "It's doing something, which is more than most. But without stopping the inflow, it's an infinite cleanup job. We need both: cleanup AND prevention.", "score": 1234},
                {"body": "The real value of The Ocean Cleanup might not be the trash they pull out — it's the attention they bring to the problem and the data they collect about distribution patterns.", "score": 867},
                {"body": "Cleanup without monitoring is flying blind. We need density mapping to know where to deploy resources and whether efforts are actually working.", "score": 534},
                {"body": "An AI-powered monitoring system that maps plastic density in real time would make cleanup efforts 10x more efficient. Right now they're basically searching randomly.", "score": 478},
            ],
        },
        {
            "title": "What if we could see ocean plastic from space? New AI makes it possible",
            "selftext": "A new paper demonstrates that convolutional neural networks can detect floating plastic aggregations from Sentinel-2 satellite imagery. The system achieved 86% precision in identifying plastic patches larger than 5 meters across.",
            "score": 1987,
            "comments": [
                {"body": "Making the invisible visible is exactly what this problem needs. You can't clean up what you can't find.", "score": 567},
                {"body": "5 meters is still pretty large. The real danger is microplastics at sub-centimeter scale. But this is a great start for the big stuff.", "score": 445},
                {"body": "If we can map density and distribution patterns over time, that tells us about current flows, accumulation dynamics, and input sources. Way more useful than just counting individual pieces.", "score": 398},
                {"body": "The next step is making this data publicly available. Open data leads to better policy.", "score": 312},
            ],
        },
    ],
    "collapse": [
        {
            "title": "We've permanently contaminated the entire ocean with plastic. There is no cleanup scenario that works.",
            "selftext": "Even if we stopped all plastic production today, the plastic already in the ocean will continue to fragment into smaller and smaller particles for centuries. Microplastics are now in every ocean current system, every depth layer, and every food chain. This is irreversible contamination at planetary scale.",
            "score": 3456,
            "comments": [
                {"body": "The ocean has become a plastic soup and we're all eating from it. Microplastics in fish, in sea salt, in drinking water. The contamination loop is closed.", "score": 987},
                {"body": "What really gets me is that we can't even see most of it. The visible trash is maybe 1% of the problem. The rest is microscopic particles spread through every cubic meter of ocean water.", "score": 756},
                {"body": "Plastic doesn't disappear. It just gets smaller. And smaller plastic is actually MORE dangerous because it enters biological systems more easily.", "score": 634},
                {"body": "The fact that we're still increasing plastic production tells you everything about how seriously civilization takes long-term environmental threats. We can't even solve the problems we can see, let alone the ones we can't.", "score": 567},
                {"body": "Future generations will look at this the way we look at leaded gasoline. Obvious poison, everywhere, and we just kept making more.", "score": 478},
            ],
        },
        {
            "title": "Microplastics are now found in human placentas, lungs, and blood. We are the pollution.",
            "selftext": "Multiple studies have now confirmed microplastic particles in human organs. The health effects are still being studied but early research suggests inflammatory responses, endocrine disruption, and potential carcinogenic effects. We have turned the ocean's plastic problem into our own body's plastic problem.",
            "score": 5678,
            "comments": [
                {"body": "The bioaccumulation chain is complete. Ocean plastic > marine organisms > seafood > humans. We are eating our own waste.", "score": 1456},
                {"body": "And still people act like ocean plastic is someone else's problem. It's literally inside you right now.", "score": 987},
                {"body": "The invisible becomes personal. You can ignore trash on a beach. You can't ignore particles in your bloodstream.", "score": 756},
                {"body": "We need to map where this stuff is concentrating and how it's entering food chains. Without that data, we're just guessing at solutions.", "score": 534},
            ],
        },
        {
            "title": "The Global Plastics Treaty failed. Again. Voluntary commitments are worthless.",
            "selftext": "Another round of negotiations, another set of non-binding voluntary commitments. The petrochemical industry successfully lobbied against production caps. Without binding limits on plastic production, everything else is theater.",
            "score": 2345,
            "comments": [
                {"body": "You can't regulate what you can't measure. The treaty fails partly because we don't have good enough data on where the plastic goes and how bad the accumulation really is.", "score": 678},
                {"body": "The industry playbook is identical to fossil fuels. Delay, deny, deflect to recycling (which doesn't work at scale), and lobby against binding targets.", "score": 567},
                {"body": "Voluntary commitments have never worked for any environmental crisis. Not acid rain (took regulation), not ozone (took Montreal Protocol), not plastic.", "score": 445},
                {"body": "What we need is undeniable, real-time evidence. A map that shows exactly how bad it is, updated continuously. Make it impossible to look away.", "score": 389},
            ],
        },
    ],
    "MachineLearning": [
        {
            "title": "[R] Deep learning model achieves 86% accuracy detecting ocean plastic from Sentinel-2 satellite imagery",
            "selftext": "New paper presents a CNN architecture for detecting floating plastic aggregations in multispectral satellite imagery. Trained on a novel dataset of 12,000 annotated Sentinel-2 patches. Key innovation is a spectral attention module that learns to weight near-infrared bands where plastic has distinctive signatures. Code and weights available on GitHub.",
            "score": 2345,
            "comments": [
                {"body": "The spectral attention module is clever. Plastic has a known SWIR signature around 1700nm that's distinct from water, algae, and foam. Learning to weight those bands automatically makes sense.", "score": 567},
                {"body": "86% precision is good for coarse mapping but you'd need higher recall for monitoring. What's the false negative rate? Missing accumulation zones is worse than false positives for policy use.", "score": 445},
                {"body": "This is great applied ML work. The real challenge is scaling from patches to continuous global monitoring. Has anyone tried this with the new high-cadence satellite constellations?", "score": 398},
                {"body": "I worked on a similar problem for algal bloom detection. The challenge with ocean surface detection is cloud cover and sun glint. How does the model handle those?", "score": 356},
                {"body": "The practical impact of this could be huge. If you can generate real-time density maps of plastic concentration, that changes environmental policy from guesswork to evidence-based.", "score": 312},
            ],
        },
        {
            "title": "[D] What's the state of AI for environmental monitoring? Seems like a high-impact application area",
            "selftext": "I'm interested in applying ML to environmental problems but most of the work I see is small-scale academic projects. Is anyone doing this at scale? Specifically interested in ocean monitoring, deforestation detection, and pollution tracking.",
            "score": 1876,
            "comments": [
                {"body": "Ocean plastic detection from satellite imagery is probably the most mature application. Several groups are working on it. The main bottleneck is training data — annotating plastic in satellite imagery is expensive and requires domain expertise.", "score": 534},
                {"body": "The gap between academic papers and deployed systems is huge in this space. Plenty of 90% accuracy papers, very few operational monitoring systems.", "score": 456},
                {"body": "I think the highest-impact application would be real-time density mapping of ocean plastic. Combine satellite imagery, drone data, and ship-based sensors with a unified ML pipeline. The data would be immediately useful for policy and cleanup operations.", "score": 398},
                {"body": "The environmental monitoring space needs more ML engineers. The domain experts (oceanographers, marine biologists) have the data but often lack the ML infrastructure to process it at scale.", "score": 345},
                {"body": "Computer vision for satellite imagery is where most progress is happening. Object detection and semantic segmentation on multispectral data. Transfer learning from ImageNet surprisingly works okay as a starting point.", "score": 312},
            ],
        },
        {
            "title": "[P] Built a pipeline for detecting microplastic concentrations from satellite data — feedback welcome",
            "selftext": "I built a computer vision pipeline that takes Sentinel-2 multispectral imagery and estimates surface microplastic concentration. Uses a U-Net variant for segmentation followed by a regression head for density estimation. Trained on synthetic data augmented with real annotations from beach cleanup surveys. Would love feedback on the approach.",
            "score": 1234,
            "comments": [
                {"body": "Using synthetic training data is smart given the annotation bottleneck. How do you validate against real-world observations? Any ground truth comparisons?", "score": 398},
                {"body": "The regression head for density is the key innovation here. Most work stops at detection (is plastic present?) but density mapping (how much?) is what policymakers actually need.", "score": 345},
                {"body": "Have you tried this on the known accumulation zones like the North Pacific Gyre? Would be interesting to see if your density estimates match the ship-based sampling surveys.", "score": 289},
                {"body": "This kind of pipeline deployed at scale could be transformative. The gap between what we know about ocean plastic and what we can see in real time is massive.", "score": 267},
            ],
        },
    ],
}


def generate_posts():
    """Generate all posts with metadata."""
    all_posts = []

    for subreddit, posts in POSTS_BY_SUBREDDIT.items():
        for i, post in enumerate(posts):
            # Generate realistic timestamps spread over the past year
            days_ago = random.randint(7, 365)
            created = datetime.now() - timedelta(days=days_ago)

            post_data = {
                "subreddit": subreddit,
                "query": "ocean plastic",
                "title": post["title"],
                "selftext": post["selftext"],
                "score": post["score"],
                "num_comments": len(post["comments"]) + random.randint(10, 100),
                "created_utc": created.isoformat(),
                "url": f"https://reddit.com/r/{subreddit}/comments/{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=6))}/",
                "permalink": f"https://reddit.com/r/{subreddit}/comments/{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=6))}/",
                "comments": post["comments"],
            }
            all_posts.append(post_data)

    output = {
        "source": "reddit_sample",
        "note": "Sample Reddit data for portfolio purposes. Structure mirrors PRAW output. Can be replaced with real API data.",
        "subreddits": SUBREDDITS,
        "queries": ["ocean plastic", "microplastics", "plastic pollution", "AI ocean monitoring"],
        "post_count": len(all_posts),
        "collected_at": datetime.now().isoformat(),
        "posts": all_posts,
    }

    output_path = RAW_DIR / "reddit_posts.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Generated {len(all_posts)} sample posts across {len(SUBREDDITS)} subreddits")
    print(f"Saved to {output_path}")
    return output


if __name__ == "__main__":
    generate_posts()
