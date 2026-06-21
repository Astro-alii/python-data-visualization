# 🏔️ Sitka, Alaska — Temperature Analysis

### A Single-Year Deep Dive into Coastal Alaskan Climate (2021)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=flat-square)](https://matplotlib.org/)

[← Back to portfolio overview](../../README.md)

---

## 📌 Introduction

Sitka is a coastal city in Southeast Alaska, situated on Baranof Island along the Pacific Ocean. Its climate is classified as **oceanic** — mild, wet winters and cool summers, with the Pacific moderating temperature extremes year-round. This makes Sitka significantly warmer in winter than interior Alaskan cities, while keeping summers cooler than most of the continental US.

This case study examines a full year of daily high and low temperature data for Sitka, using it as a focused, single-city study in seasonal pattern, temperature extremes, and the relationship between daily highs and lows.

This was also the first case study in this portfolio built around a multi-panel `GridSpec` layout — a technique later reused at larger scale in the [coastal vs. inland climate comparative study](../coastal-vs-inland-climate/README.md).

---

## 📂 Dataset

| Property | Details |
|---|---|
| **Location** | Sitka, Alaska, US |
| **Period** | Full year, 2021 (365 days) |
| **Variables** | Daily High and Daily Low temperature, °F |
| **Format** | CSV |

Raw files: [`sitka_weather_2021_simple.csv`](data_files/sitka_weather_2021_simple.csv) · [`sitka_weather_07-2021.csv`](data_files/sitka_weather_07-2021.csv)

---

## 📈 Visualization

A single 2×2 grid figure built with `matplotlib.gridspec`:

| Panel | Content |
|---|---|
| Top-left | Daily high temperature, full year |
| Top-right | Daily low temperature, full year |
| Bottom (full width) | High and low combined, with shaded diurnal range (`fill_between`) |

Script: [`sitka_weather_analysis.py`](scripts/sitka_weather_analysis.py)
Full write-up with all three figures: [`sitka_weather_2021_case_study.pdf`](report/sitka_weather_2021_case_study.pdf)

---

## 🔍 Key Findings

### Daily highs
The daily high temperature traces a smooth, well-defined seasonal curve. The year opened with highs in the low-to-mid 40s°F, held steady through February and March, then climbed from May onward. The peak of the year was recorded in **mid-July at approximately 78°F**, with summer highs (June–August) consistently in the 55–75°F range. By December, highs had fallen back into the mid-to-upper 20s°F.

A notable anomaly: in **late February**, the daily high briefly dropped to near **18°F** — a sharp departure from trend, likely driven by an arctic air intrusion pushing cold continental air into the coastal region.

### Daily lows
Daily lows followed a broadly similar arc but with more pronounced winter extremes. January opened with lows in the upper 30s°F, before a dramatic plunge in late February brought lows to approximately **12°F — the coldest value of the entire year**. Summer lows peaked near 58–60°F in July and August, reflecting long daylight hours and warm sea surface temperatures. The year closed with a steady decline, finishing near 15°F by early January 2022 — mirroring the late-February anomaly and bookending the year with two unusually cold periods.

### Combined high vs. low
Plotting both series together exposes the **diurnal temperature range** — the gap between daily high and low. This gap is relatively wide in winter and narrows noticeably in summer, when long Alaskan days and cloudy maritime conditions keep overnight temperatures from dropping far below afternoon peaks. The most dramatic divergence occurs around the late-February cold event, where the low (12°F) and high (upper teens) nearly converge at the bottom of the year's range — a near-freezing day standing out clearly against the rest of the trend.

---

## 📊 Summary Table

| Metric | Value |
|---|---|
| Warmest day | ~78°F (mid-July) |
| Coldest low | ~12°F (late February — arctic intrusion) |
| Summer highs (Jun–Aug) | 55–75°F, consistently |
| Summer lows (Jul–Aug) | Peaked near 58–60°F |
| Annual high range | ~27°F (Dec) → ~78°F (Jul) — 51°F spread |
| Annual low range | ~12°F (Feb) → ~60°F (Aug) — 48°F spread |
| Climate character | Classic oceanic — mild, maritime, rare extremes |

---

## ✅ Conclusion

Sitka's 2021 temperature record paints a picture of a stable, maritime climate shaped by its coastal geography. The year followed a predictable seasonal arc, punctuated by one notable cold anomaly in late February. Summers were mild and pleasant; winters cool but rarely severe. The narrow diurnal range in summer and the moderating influence of the Pacific Ocean throughout the year are hallmarks of Sitka's climate — distinguishing it sharply from the more extreme conditions found in Alaska's interior.

---

## ⚙️ Running This Case Study

```bash
cd case_studies/sitka-alaska-weather-2021/scripts
python sitka_weather_analysis.py
```

---

## 📄 Files in This Case Study

```
sitka-alaska-weather-2021/
├── README.md                              ← this file
├── scripts/
│   └── sitka_weather_analysis.py
├── data_files/
│   ├── sitka_weather_2021_simple.csv
│   └── sitka_weather_07-2021.csv
└── report/
    └── sitka_weather_2021_case_study.pdf
```

---

*Libraries used: Matplotlib (`gridspec`) · csv (stdlib) · datetime (stdlib)*

[← Back to portfolio overview](../../README.md)
