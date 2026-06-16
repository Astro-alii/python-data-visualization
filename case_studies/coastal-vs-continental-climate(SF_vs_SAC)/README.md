# 🌊 Coastal vs Inland Climate
## San Francisco vs Sacramento — Temperature Analysis (2000–2025)

> *Two cities. 90 miles apart. Completely different weather stories.*

---

## 📌 Overview

This case study investigates how **geography shapes local climate** by comparing 25 years of daily temperature records from two Californian cities that sit less than 90 miles apart yet inhabit entirely different climate worlds:

- **San Francisco** — a coastal city on the Pacific Ocean peninsula, heavily moderated by marine influence and the famous summer fog layer
- **Sacramento** — an inland city in California's Central Valley, fully exposed to continental temperature extremes with no oceanic buffer

Using **9,130+ daily records per city** spanning 2000–2025, this analysis applies six distinct visualization techniques across two Python libraries to quantify the difference between coastal and inland climates — and to understand the geography that drives it.

---

## 🔬 Hypothesis

Four testable predictions were made before examining the data:

1. Sacramento summer highs will be significantly greater than San Francisco's
2. Sacramento winter lows will be significantly colder than San Francisco's
3. Sacramento's diurnal temperature range (daily swing) will be far greater across all months
4. San Francisco temperatures will remain remarkably stable and consistent year-round

**All four hypotheses were confirmed by the data.**

---

## 📊 Key Findings

| Metric | San Francisco | Sacramento | Difference |
|--------|--------------|------------|------------|
| Average July High | ~66°F | ~93°F | **+27°F** |
| Average January Low | ~47°F | ~39°F | **−8°F** |
| Annual Temperature Range | ~23°F | ~54°F | **+31°F** |
| Peak Diurnal Range | ~15°F (Sep) | ~33°F (Jul) | **+18°F** |
| Std Dev of Daily High | ~8°F | ~18°F | **2.25× greater** |

Sacramento's annual temperature range is **more than double** San Francisco's — despite the two cities being less than 90 minutes apart by car.

---

## 📂 Repository Structure

```
coastal-vs-continental-climate(SF_vs_SAC)/
│
├── coastal_vs_inland_climate_case_study.ipynb   ← Full case study notebook
│
├── graph_code/                                   ← Individual graph scripts
│   ├── graph1_daily_highlow_sf_matplotlib.py
│   ├── graph1_daily_highlow_sac_matplotlib.py
│   ├── graph1b_daily_highlow_combined_plotly.py
│   ├── graph2_monthly_avg_bar_matplotlib.py
│   ├── graph2_monthly_avg_line_plotly.py
│   ├── graph3_temp_range_matplotlib.py
│   ├── graph4_heatmap_matplotlib.py
│   ├── graph5_boxplot_matplotlib.py
│   └── graph6_annual_trend_plotly.py
│
├── matplotlib_all_graphs/                        ← Saved PNG outputs
│   ├── graph1_daily_highlow_sf.png
│   ├── graph1_daily_highlow_sac.png
│   ├── graph2_monthly_avg_bar.png
│   ├── graph3_diurnal_temp_range.png
│   ├── graph4_heatmap.png
│   └── graph5_boxplot.png
│
├── Plotly_all_graphs/                            ← Interactive HTML outputs
│   ├── graph1b_daily_highlow_combined_rolling.html
│   ├── graph2_monthly_avg_line.html
│   └── graph6_annual_trend.html
│
└── raw_data_files/                               ← Source data
    ├── san_francisco_data_2000_2025.csv
    └── sacramento_data_2000_2025.csv
```

---

## 📈 Graphs Produced

### Graph 1a — Daily High & Low Temperatures (Matplotlib)
Raw daily temperatures plotted across five 5-year panels per city. Shows the structural difference in temperature volatility between the two cities at the daily scale.

![SF Daily High & Low](matplotlib_all_graphs/graph1_daily_highlow_sf.png)
![SAC Daily High & Low](matplotlib_all_graphs/graph1_daily_highlow_sac.png)

---

### Graph 1b — Interactive 25-Year Rolling Average (Plotly)
30-day rolling average applied to all four temperature series, rendered as an interactive chart with a range slider. Allows exploration of any specific time window across the full 25-year dataset.

📂 [View Interactive Chart](Plotly_all_graphs/graph1b_daily_highlow_combined_rolling.html)

---

### Graph 2 — Monthly Average Temperatures (Matplotlib + Plotly)
25 years of data collapsed into 12 monthly averages per city. Shows the seasonal arc of each location — Sacramento's dramatic mountain curve vs San Francisco's remarkably flat profile.

![Monthly Average Bar](matplotlib_all_graphs/graph2_monthly_avg_bar.png)

📂 [View Interactive Version](Plotly_all_graphs/graph2_monthly_avg_line.html)

---

### Graph 3 — Monthly Diurnal Temperature Range (Matplotlib)
The average difference between daily high and daily low per month. Sacramento's diurnal range peaks at ~33°F in July — nearly 3× San Francisco's ~11°F.

![Diurnal Range](matplotlib_all_graphs/graph3_diurnal_temp_range.png)

---

### Graph 4 — Temperature Heatmap: Month × Year (Matplotlib + Seaborn)
A 12×25 grid where each cell represents the average daily high for a specific month in a specific year. Color intensity reveals temperature — deeper red = hotter, deeper blue = cooler. Sacramento's consistent red summer band vs SF's uniform mild palette tells the whole story in one image.

![Heatmap](matplotlib_all_graphs/graph4_heatmap.png)

---

### Graph 5 — Monthly Temperature Distribution (Matplotlib + Seaborn)
Box plots showing the full statistical distribution of daily highs per month — median, interquartile range, and outliers. Sacramento's tall summer boxes vs San Francisco's consistently compact boxes visualize not just the temperature difference but the volatility difference.

![Box Plot](matplotlib_all_graphs/graph5_boxplot.png)

---

### Graph 6 — Annual Average Temperature Trend (Plotly)
Annual mean temperatures with linear trendlines fitted using polynomial regression. Both cities show a positive warming trend over 25 years, with Sacramento warming at a faster rate — consistent with broader observations of inland areas warming faster than coastal ones.

📂 [View Interactive Chart](Plotly_all_graphs/graph6_annual_trend.html)

---

## 🛠️ Libraries Used

| Library | Version | Purpose |
|---------|---------|---------|
| `pandas` | ≥2.0 | Data loading, cleaning, groupby aggregations, date parsing |
| `matplotlib` | ≥3.7 | Static line charts, bar charts, subplots |
| `seaborn` | ≥0.12 | Heatmaps, box plots |
| `plotly` | ≥5.0 | Interactive line charts, range slider, trendlines |
| `numpy` | ≥1.24 | Bar positioning, polynomial regression for trendlines |

---

## ⚙️ Setup & Installation

### Requirements
- Python 3.11 (recommended)

### Install dependencies
```bash
pip install pandas matplotlib seaborn plotly numpy
```

### Run individual graphs
```bash
cd graph_code
python graph1_daily_highlow_sf_matplotlib.py
```

### Run the full case study
Open `coastal_vs_inland_climate_case_study.ipynb` in VS Code or Jupyter and run all cells. The notebook loads data, generates all graphs inline, and presents the full written analysis.

---

## 📁 Data Source

**NOAA Climate Data Online — Global Historical Climatology Network Daily (GHCN-D)**

- Variables: `TMAX` (daily high, °F), `TMIN` (daily low, °F)
- Period: January 1, 2000 — December 31, 2025
- Records: ~9,130 per city

---

## 🌍 The Geography Behind the Data

**Why is San Francisco so mild?**
SF sits on a peninsula surrounded by the Pacific Ocean and San Francisco Bay. The cold California Current keeps ocean surface temperatures low year-round. The marine layer — a coastal fog driven by offshore upwelling — acts as a natural air conditioner, suppressing summer highs. The ocean's enormous thermal mass (specific heat ~4× that of land) resists rapid temperature change in either direction.

**Why does Sacramento swing so wildly?**
Sacramento sits in the Central Valley, separated from the coast by the Coast Range mountains. These mountains block marine influence almost entirely. Without an oceanic buffer, Sacramento's temperature is driven by solar radiation alone — land heats and cools approximately 4× faster than water. Clear skies year-round mean intense daytime solar heating and rapid nighttime radiative cooling — producing the large diurnal swings visible throughout this analysis.

---

## 📝 Case Study Format

The full analysis is presented as a **Jupyter Notebook** (`coastal_vs_inland_climate_case_study.ipynb`) combining:
- Written analysis and hypothesis testing in Markdown cells
- Reproducible graph code in executable Python cells
- Inline graph outputs rendered directly in the notebook
- Interactive Plotly charts that render live in the notebook environment

Individual graph scripts are maintained separately in `graph_code/` for reference and reproducibility.

---

*Part of a Python Data Visualization portfolio — building real case studies with real data.*

*Libraries: Pandas · Matplotlib · Seaborn · Plotly · NumPy*
