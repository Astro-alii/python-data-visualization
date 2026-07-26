# Exoplanet Demographic Survey

A data science case study analyzing ~6,300 confirmed exoplanets from the NASA Exoplanet Archive, investigating what the current data reveals about detection bias, planetary composition, and the search for Earth-like worlds.

## Thesis

Using the population of confirmed exoplanets, this project tests three claims:

1. **Detection bias, not nature, shapes what we've found.** The distribution of discovered planets isn't a fair sample of what's actually out there — it's a fingerprint of *how* we're able to detect them (transit method favors big planets close to their star; radial velocity favors massive planets).
2. **Mass and radius aren't independent — they follow a physical law, not a scatter.** Planets cluster into distinct regimes (rocky, gas dwarf, gas giant) based on composition, not random size.
3. **The search for Earth-like planets is still an edge case, not the norm.** Very few confirmed planets fall within a size and temperature range resembling Earth.

## Data Source

**Dataset:** NASA Exoplanet Archive — Planetary Systems (PS) table
**Downloaded:** July 18, 2026
**Filter applied:** `default_flag = 1` (one row per planet, not per publication)
**Row count:** 6,324 planets

**Reproduce this query:**
```
https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,discoverymethod,disc_year,pl_orbper,pl_orbsmax,pl_rade,pl_bmasse,pl_insol,pl_eqt,st_teff,st_rad,st_mass,sy_dist+from+ps+where+default_flag=1&format=csv
```

Full column documentation is preserved in `data/SOURCE.md`.

## Data Cleaning

- Loaded with `comment='#'` to skip the archive's header documentation block
- Dropped rows with missing values in the specific columns each graph required (not a blanket drop — a planet missing its mass can still be used for a discovery-year chart)
- Filtered out non-positive values before applying log scales, where relevant
- Verified discovery method counts and total row counts against the raw file at each stage

## Graphs

### 1. Exoplanet Discoveries Over Time by Detection Method
**Matplotlib** — stacked bar chart, discovery year vs. planet count, segmented by detection method, with Kepler (2009) and TESS (2018) launch years annotated.

Discovery counts jump sharply in 2014 and 2016 — batch confirmations of Kepler candidates, not a natural increase in the rate of planet formation. Radial Velocity dominates the pre-2009 era; Transit takes over almost completely once Kepler comes online. The shape of this timeline is a history of telescopes, not a history of the universe.

### 2. Exoplanet Discoveries by Detection Method
**Matplotlib** — horizontal bar chart ranking all 11 detection methods by total planets found.

| Method | Count | Share |
|---|---|---|
| Transit | 4,667 | 73.8% |
| Radial Velocity | 1,195 | 18.9% |
| Microlensing | 281 | 4.4% |
| Imaging | 98 | 1.5% |
| Transit Timing Variations | 40 | 0.6% |
| Eclipse Timing Variations | 17 | 0.3% |
| Orbital Brightness Modulation | 9 | 0.1% |
| Pulsar Timing | 8 | 0.1% |
| Astrometry | 6 | 0.1% |
| Pulsation Timing Variations | 2 | 0.0% |
| Disk Kinematics | 1 | 0.0% |

Transit and Radial Velocity alone account for ~93% of every confirmed exoplanet — a direct measure of how lopsided detection capability is across methods.

### 3. Exoplanet Mass-Radius Relationship
**Plotly (interactive)** — log-log scatter of planet mass vs. radius, colored by detection method, with Earth/Neptune/Jupiter marked as reference points and full hover detail per planet.

Planets trace a tight diagonal band from roughly 0.1 to 10 Earth masses, then flatten into a plateau around 10–13 Earth radii from ~10 Earth masses up into the thousands. That flattening is visual proof that gravitational compression, not simple mass accumulation, governs giant planet structure — past a certain point, adding more mass barely makes a planet bigger.

### 4. Orbital Period vs. Semi-Major Axis — Verifying Kepler's Third Law
**Matplotlib** — log-log scatter of real exoplanet orbital data with a theoretical Kepler's Third Law curve (P = a^1.5) overlaid.

The observed data tracks the theoretical prediction almost exactly across six orders of magnitude in orbital distance — confirming that a relationship derived 400 years ago from six solar system planets holds for thousands of planets orbiting entirely different stars.

### 5. Exoplanet Habitable Zone Candidates
**Plotly (interactive)** — scatter of equilibrium temperature vs. planet radius, colored by detection method, with a shaded "roughly Earth-like" reference zone.

Out of thousands of confirmed planets, very few fall inside or near the Earth-like zone — reinforcing that current detection capability, not the absence of such planets, is the limiting factor in finding true Earth analogs.

## Stack

Python · pandas · NumPy · Matplotlib · Plotly

## Repository Structure

```
exoplanet-demographic-survey/
|__exoplanet__demographic_survey.ipynb
|
├── data/
│   ├── exoplanets_raw.csv
├── graph_code/
│   ├── graph1_discoveries_over_time_matplotlib.py
│   ├── graph2_detection_methods_matplotlib.py
│   ├── graph3_mass_radius_plotly.py
│   ├── graph4_keplers_law_matplotlib.py
│   └── graph5_habitable_zone_plotly.py
├── Matplotlib_graphs/
│   ├── graph1_discoveries_over_time.png
│   ├── graph2_detection_methods.png
│   └── graph4_keplers_law.png
├── Plotly_graphs/
│   ├── graph3_mass_radius.html
│   └── graph5_Earth_like_planets.html
└── README.md
```

## Notes

This case study intentionally splits chart types by purpose rather than personal preference: Matplotlib for static, single-conclusion arguments (timeline shape, a fitted regression line), and Plotly for dense, exploratory scatter plots where hovering over individual planets adds real value.

A sixth graph (a stellar/planetary correlation heatmap) was planned but not completed in this iteration.
