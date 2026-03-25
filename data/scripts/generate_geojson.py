"""
Pelagic IntelX — Synthetic Ocean Plastic Density GeoJSON Generator
Generates realistic but synthetic density data based on known accumulation zones.
Output: data/processed/plastic_density.geojson
"""

import json
import math
import random
from pathlib import Path

PROCESSED_DIR = Path(__file__).parent.parent / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

random.seed(42)

# Known ocean plastic accumulation zones
# Based on published research on gyral accumulation patterns
ACCUMULATION_ZONES = [
    # North Pacific Gyre (Great Pacific Garbage Patch) — highest concentration
    {"name": "North Pacific Gyre Center", "lat": 32.0, "lon": -145.0, "intensity": 0.95, "spread": 8.0},
    {"name": "North Pacific Gyre East", "lat": 30.0, "lon": -135.0, "intensity": 0.85, "spread": 6.0},
    {"name": "North Pacific Gyre West", "lat": 35.0, "lon": -155.0, "intensity": 0.75, "spread": 5.0},

    # South Pacific Gyre
    {"name": "South Pacific Gyre", "lat": -30.0, "lon": -110.0, "intensity": 0.55, "spread": 7.0},

    # North Atlantic Gyre (Sargasso Sea area)
    {"name": "North Atlantic Gyre", "lat": 30.0, "lon": -45.0, "intensity": 0.65, "spread": 6.0},

    # South Atlantic Gyre
    {"name": "South Atlantic Gyre", "lat": -32.0, "lon": -15.0, "intensity": 0.45, "spread": 5.0},

    # Indian Ocean Gyre
    {"name": "Indian Ocean Gyre", "lat": -28.0, "lon": 75.0, "intensity": 0.55, "spread": 6.0},

    # Coastal Southeast Asia — high input zones
    {"name": "South China Sea", "lat": 12.0, "lon": 114.0, "intensity": 0.80, "spread": 4.0},
    {"name": "Java Sea", "lat": -5.0, "lon": 110.0, "intensity": 0.75, "spread": 3.5},
    {"name": "Bay of Bengal", "lat": 15.0, "lon": 88.0, "intensity": 0.70, "spread": 4.0},

    # Mediterranean micro-concentrations
    {"name": "Western Mediterranean", "lat": 38.0, "lon": 5.0, "intensity": 0.60, "spread": 2.5},
    {"name": "Eastern Mediterranean", "lat": 34.0, "lon": 28.0, "intensity": 0.55, "spread": 2.0},

    # Arctic entry points
    {"name": "Barents Sea", "lat": 72.0, "lon": 30.0, "intensity": 0.35, "spread": 3.0},

    # Coastal hotspots
    {"name": "East China Coast", "lat": 28.0, "lon": 122.0, "intensity": 0.70, "spread": 2.5},
    {"name": "West Africa Coast", "lat": 5.0, "lon": -2.0, "intensity": 0.45, "spread": 3.0},
    {"name": "US East Coast", "lat": 35.0, "lon": -72.0, "intensity": 0.40, "spread": 2.5},
]


def gaussian_density(lat, lon, zone):
    """Calculate density contribution from a single accumulation zone using Gaussian spread."""
    dlat = lat - zone["lat"]
    dlon = lon - zone["lon"]
    # Adjust for longitude compression at higher latitudes
    dlon *= math.cos(math.radians(lat))
    distance_sq = dlat**2 + dlon**2
    spread_sq = zone["spread"]**2
    return zone["intensity"] * math.exp(-distance_sq / (2 * spread_sq))


def compute_density(lat, lon):
    """Compute total plastic density at a given point from all accumulation zones."""
    total = 0.0
    for zone in ACCUMULATION_ZONES:
        total += gaussian_density(lat, lon, zone)

    # Add realistic noise (10-20% variance)
    noise = random.gauss(0, 0.05)
    total = max(0, total + noise)

    # Clamp to [0, 1]
    return min(1.0, total)


def generate_density_grid():
    """Generate a grid of density points across the world's oceans."""
    features = []

    # Generate points on a grid
    lat_step = 2.0
    lon_step = 3.0

    lat = -60.0
    while lat <= 75.0:
        lon = -180.0
        while lon <= 180.0:
            density = compute_density(lat, lon)

            # Only include points with meaningful density (> 0.02)
            if density > 0.02:
                # Add slight position jitter for natural appearance
                jlat = lat + random.uniform(-0.5, 0.5)
                jlon = lon + random.uniform(-0.75, 0.75)

                # Density category for styling
                if density > 0.7:
                    category = "extreme"
                elif density > 0.4:
                    category = "high"
                elif density > 0.2:
                    category = "moderate"
                elif density > 0.08:
                    category = "low"
                else:
                    category = "trace"

                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [round(jlon, 4), round(jlat, 4)],
                    },
                    "properties": {
                        "density": round(density, 4),
                        "category": category,
                        "particles_per_km2": int(density * 580000),  # Scale to realistic units
                    },
                }
                features.append(feature)

            lon += lon_step
        lat += lat_step

    # Add extra detail points around high-concentration zones
    for zone in ACCUMULATION_ZONES:
        if zone["intensity"] > 0.6:
            for _ in range(30):
                dlat = random.gauss(0, zone["spread"] * 0.6)
                dlon = random.gauss(0, zone["spread"] * 0.6)
                pt_lat = zone["lat"] + dlat
                pt_lon = zone["lon"] + dlon
                density = compute_density(pt_lat, pt_lon)

                if density > 0.05:
                    if density > 0.7:
                        category = "extreme"
                    elif density > 0.4:
                        category = "high"
                    elif density > 0.2:
                        category = "moderate"
                    else:
                        category = "low"

                    feature = {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [round(pt_lon, 4), round(pt_lat, 4)],
                        },
                        "properties": {
                            "density": round(density, 4),
                            "category": category,
                            "particles_per_km2": int(density * 580000),
                        },
                    }
                    features.append(feature)

    return features


def main():
    print("Generating synthetic ocean plastic density data...")
    print(f"Accumulation zones: {len(ACCUMULATION_ZONES)}")

    features = generate_density_grid()
    print(f"Generated {len(features)} data points")

    # Summary stats
    densities = [f["properties"]["density"] for f in features]
    categories = {}
    for f in features:
        cat = f["properties"]["category"]
        categories[cat] = categories.get(cat, 0) + 1

    print(f"\nDensity range: {min(densities):.4f} - {max(densities):.4f}")
    print("Category distribution:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} points")

    geojson = {
        "type": "FeatureCollection",
        "metadata": {
            "source": "pelagic_intelx_synthetic",
            "description": "Simulated ocean plastic density data for portfolio purposes",
            "methodology": (
                "Gaussian spread functions seeded at known accumulation zones "
                "(NOAA, Jambeck et al. 2015). Variance tuned to match published "
                "accumulation models. NOT real observational data."
            ),
            "units": "particles_per_km2 (estimated scale)",
            "accumulation_zones": [z["name"] for z in ACCUMULATION_ZONES],
            "generated_seed": 42,
        },
        "features": features,
    }

    output_path = PROCESSED_DIR / "plastic_density.geojson"
    with open(output_path, "w") as f:
        json.dump(geojson, f, indent=2)

    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"\nSaved to {output_path} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
