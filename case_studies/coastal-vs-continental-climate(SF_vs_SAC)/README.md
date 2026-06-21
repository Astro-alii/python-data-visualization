# 🌊 Coastal vs. Inland Climate

### San Francisco vs. Sacramento — A Data Visualization Case Study (2000–2025)

> *Two cities. 90 miles apart. Completely different weather stories.*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=flat-square)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4C72B0?style=flat-square)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/python/)

[← Back to portfolio overview](../../README.md)

---

## 📌 Introduction

Geography is one of the most powerful forces shaping local climate. Cities near large bodies of water experience mild, stable temperatures year-round, moderated by the ocean's enormous thermal capacity. Cities further inland, shielded from that oceanic influence, are exposed to full seasonal extremes — scorching summers and freezing winters.

This case study examines **25 years of daily temperature data (2000–2025)** from two Californian cities that sit just **90 miles apart** but inhabit entirely different climate worlds:

| | **San Francisco** | **Sacramento** |
|---|---|---|
| **Type** | Coastal city | Inland city |
| **Geography** | Pacific Ocean peninsula | Central Valley |
| **Ocean influence** | Strong — marine layer, cold current | None — surrounded by land |
| **Climate classification** | Mediterranean coastal | Hot-summer Mediterranean |

San Francisco is famously cool and foggy, its temperatures buffered by the cold California Current offshore and the daily marine layer rolling in from the Pacific. Sacramento sits deep in the Central Valley, insulated from the coast by the Coast Range mountains — fully exposed to continental heating and cooling cycles.

---

## 🔬 Hypothesis

Four specific, testable predictions were stated before any data was examined:

1. **Sacramento summer highs** will be significantly greater than San Francisco's — driven by inland solar heating with no oceanic buffer
2. **Sacramento winter lows** will be significantly colder than San Francisco's — driven by rapid inland radiative cooling on clear nights
3. **Sacramento's diurnal temperature range** (daily high minus daily low) will be far greater than San Francisco's across all months
4. **San Francisco temperatures** will remain remarkably stable and consistent throughout the year — the signature of coastal climate moderation

All four are tested against the visualizations below.

---

## 📂 Dataset

| Property | Details |
|---|---|
| **Source** | NOAA Climate Data Online (GHCN Daily) |
| **Period** | January 1, 2000 — December 31, 2025 |
| **Variables** | Daily High (`TMAX`), Daily Low (`TMIN`), Daily Average (`TAVG`) — °F |
| **Cities** | San Francisco, CA · Sacramento, CA |
| **Records** | ~9,130 daily entries per city (~18,260 total) |
| **Raw columns** | `STATION`, `NAME`, `DATE`, `TAVG`, `TMAX`, `TMIN` |

Raw files: [`san_francisco_data_2000_2025.csv`](raw_data_files/san_francisco_data_2000_2025.csv) · [`sacramento_data_2000_2025.csv`](raw_data_files/sacramento_data_2000_2025.csv)

---

## 📈 Visualizations

| # | Chart | Technique | Library |
|---|---|---|---|
| 1a | Daily High & Low, 5-year windows (SF & SAC separately) | Multi-panel grid, raw daily series | Matplotlib |
| 1b | Interactive 25-year overview | 30-day rolling average, range slider | Plotly |
| 2 | Monthly average temperatures | Grouped aggregation, bar + line | Matplotlib, Plotly |
| 3 | Monthly diurnal temperature range | Derived metric (high − low) | Matplotlib |
| 4 | Temperature heatmap (month × year) | 2D heatmap | Seaborn |
| 5 | Monthly temperature distribution | Box plot | Seaborn |
| 6 | Annual average trend (2000–2025) | Linear regression trendline | Plotly, NumPy |

Scripts for each chart live in [`scripts/`](scripts/). The full walkthrough — code, charts, and written interpretation together — is in the [Jupyter notebook](notebook/coastal_vs_inland_climate_case_study.ipynb). Pre-rendered interactive exports are in [`exports/`](exports/) for viewing without running anything.

---

## 🔍 Key Findings

### San Francisco — stability and restraint
- High and low lines stay consistently close together across all 25 years — the gap rarely exceeds 15°F
- The 2000–2004 pattern looks almost identical to 2020–2025 — SF's climate has been extraordinarily consistent
- SF's warmest months are **September and October**, not July/August — the marine layer suppresses summer highs, then burns off in fall

### Sacramento — wide seasonal swings
- High and low lines are far apart, especially in summer — the gap is visible at a glance
- Clear, deep seasonal waves dominate every year — summer peaks soar past 100°F, winter troughs dip into the 30s
- The 2020–2025 window shows some of the highest summer peaks in the dataset, consistent with recent Central Valley heat events

### The headline numbers

| Metric | San Francisco | Sacramento | Difference |
|---|---|---|---|
| Average July high | ~66°F | ~93°F | **+27°F** |
| Average January low | ~47°F | ~39°F | **−8°F** |
| Annual temperature range | ~23°F | ~54°F | **+31°F** |
| Peak diurnal range | ~15°F (Sep) | ~33°F (Jul) | **+18°F** |
| Std. dev. of daily high | ~8°F | ~18°F | **2.25× greater** |
| All-time record high | ~105°F | ~115°F | **+10°F** |

Sacramento's annual temperature range is **more than double** San Francisco's, despite being less than 90 miles away. By July, Sacramento's diurnal swing (33°F) is nearly **3× San Francisco's** (11°F).

### Long-term trend

Both cities show a positive trendline over the 25-year period — but Sacramento's warming rate is steeper, and its year-to-year variability is much higher, consistent with inland climates being inherently less stable than coastal ones.

---

## ✅ Hypothesis Verdict

| Hypothesis | Result |
|---|---|
| H1 — Sacramento summer highs significantly greater | ✅ Confirmed (~27°F hotter in July) |
| H2 — Sacramento winter lows significantly colder | ✅ Confirmed (~8°F colder in January) |
| H3 — Sacramento diurnal range far greater | ✅ Confirmed (~2–3× greater every month) |
| H4 — San Francisco remains stable year-round | ✅ Confirmed (std dev ~8°F vs ~18°F) |

---

## 🌍 The Geography Behind the Data

**San Francisco** sits on a peninsula surrounded by the Pacific Ocean and San Francisco Bay. The cold California Current keeps ocean surface temperatures low year-round, providing a constant source of cool, stable air. The summer marine layer — coastal fog driven by offshore upwelling — acts as a natural air conditioner, suppressing daytime highs even at the height of summer. The ocean's enormous thermal mass (roughly 4× the specific heat capacity of land) prevents rapid temperature change in either direction.

**Sacramento** sits in the Central Valley, separated from the coast by the Coast Range mountains, which block marine influence almost entirely. Without an oceanic buffer, Sacramento's temperature is driven by solar radiation alone — heating rapidly during the day, cooling rapidly at night under clear skies. The valley's flat topography and dry summer conditions amplify both extremes.

---

## ⚙️ Running This Case Study

```bash
cd case_studies/coastal-vs-inland-climate

# Full notebook (code + charts + narrative)
jupyter notebook notebook/coastal_vs_inland_climate_case_study.ipynb

# Or run an individual script
cd scripts
python graph1_daily_highlow_sf_matplotlib.py
```

Interactive Plotly charts open in your default browser. To view results without running anything, open the pre-rendered files in [`exports/`](exports/) directly.

---

## 📄 Files in This Case Study

```
coastal-vs-inland-climate/
├── README.md                                          ← this file
├── notebook/
│   └── coastal_vs_inland_climate_case_study.ipynb
├── scripts/
│   ├── graph1_daily_highlow_sf_matplotlib.py
│   ├── graph1_daily_highlow_sac_matplotlib.py
│   ├── graph1b_daily_highlow_combined_plotly.py
│   ├── graph2_monthly_avg_bar_matplotlib.py
│   ├── graph2_monthly_avg_line_plotly.py
│   ├── graph3_temp_range_matplotlib.py
│   ├── graph4_heatmap_matplotlib.py
│   ├── graph5_boxplot_matplotlib.py
│   └── graph6_annual_trend_plotly.py
├── raw_data_files/
│   ├── san_francisco_data_2000_2025.csv
│   └── sacramento_data_2000_2025.csv
└── exports/
    ├── graph1b_daily_highlow_combined_rolling_plotly.html
    ├── graph2_monthly_avg_line.html
    └── graph6_annual_trend_plotly.html
```

---

*Libraries used: pandas · NumPy · Matplotlib · Seaborn · Plotly*
*Data source: NOAA Climate Data Online — GHCN Daily Records*

[← Back to portfolio overview](../../README.md)
