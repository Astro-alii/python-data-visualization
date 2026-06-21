<div align="center">

# 📊 Python Data Visualization Portfolio

**A growing collection of independent data visualization case studies — from raw data to publication-ready insight.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=flat-square)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4C72B0?style=flat-square)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 📌 About This Repository

This repository collects independent **data visualization case studies**, each one taking a real-world dataset from raw form through to a fully narrated, insight-driven analysis. The focus is on visualization technique — multi-panel layouts, rolling averages, heatmaps, distribution plots, trend analysis — paired with written interpretation of what each chart actually reveals, rather than charts presented without context.

This is an ongoing portfolio. New case studies are added as standalone projects under `case_studies/`, each with its own data, code, and write-up. Datasets and domains vary by study — climate, and others to follow — but every case study follows the same underlying process, described below.

---

## 🗂️ Repository Structure

```
python-data-visualization/
│
├── README.md                          ← you are here (portfolio overview)
│
└── case_studies/
    │
    ├── coastal-vs-inland-climate/         # SF vs Sacramento, 2000–2025
    │   ├── notebook/
    │   ├── scripts/
    │   ├── raw_data_files/
    │   ├── exports/
    │   └── README.md                      ← case study-specific write-up
    │
    ├── sitka-alaska-weather-2021/         # Sitka, AK, single-year deep dive
    │   ├── scripts/
    │   ├── data_files/
    │   ├── report/
    │   └── README.md                      ← case study-specific write-up
    │
    └── (more case studies added over time)
```

Each case study folder is fully self-contained — its own data, scripts/notebook, outputs, and README — so the repo scales cleanly as new studies are added without touching prior work. **Start at this README for the overview, then open a case study's own README for the full analysis and findings.**

---

## 🔬 Case Studies

| Case Study | Domain | Description | Stack |
|---|---|---|---|
| [Coastal vs. Inland Climate](case_studies/coastal-vs-inland-climate/README.md) | Climate · Comparative | 25-year temperature comparison, San Francisco vs. Sacramento, testing whether ocean proximity measurably moderates climate | pandas, matplotlib, seaborn, plotly |
| [Sitka, Alaska — 2021](case_studies/sitka-alaska-weather-2021/README.md) | Climate · Single-city | Single-year deep dive into daily high/low temperatures for a coastal Alaskan town | matplotlib (gridspec) |

More case studies will be added to this table as they're completed.

---

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.11+ |
| **Data handling** | pandas, NumPy, csv (stdlib) |
| **Static visualization** | Matplotlib, Seaborn |
| **Interactive visualization** | Plotly |
| **Environment** | Jupyter Notebook |

Specific data sources vary by case study and are documented in each one's own README.

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.11 or later
- pip

### Installation

```bash
git clone https://github.com/Astro-alii/python-data-visualization.git
cd python-data-visualization
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### `requirements.txt`

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.13.0
plotly>=5.18.0
jupyter>=1.0.0
```

### Running a case study

Each case study is independently runnable. Navigate into its folder and follow the instructions in its own README — for example:

```bash
cd case_studies/coastal-vs-inland-climate
jupyter notebook notebook/coastal_vs_inland_climate_case_study.ipynb
```

---

## 📐 Methodology

Every case study in this repo follows the same five-stage process:

1. **State a hypothesis first.** Before any chart is drawn, specific and falsifiable predictions are written down — this keeps the analysis honest rather than chart-then-narrate.
2. **Clean and structure the data.** Raw data is parsed and transformed once into a structure that's reused across all visualizations in the study.
3. **Visualize at multiple scales.** Different granularities and chart types expose different layers of signal in the same underlying data.
4. **Interpret, don't just display.** Every chart is followed by a written breakdown of what it actually shows and why, grounded in the underlying cause.
5. **Conclude against the hypothesis.** Findings are checked back against the original predictions — confirmed, rejected, or partially supported — rather than left as an open-ended set of charts.

---

## 🗺️ Roadmap

- [x] Sitka, Alaska — single-city seasonal analysis
- [x] Coastal vs. inland climate comparative study
- [ ] Additional case study (TBD)
- [ ] Shared plotting utilities module (reduce duplication across case studies)
- [ ] Automated data-refresh pipeline for live data sources

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 🔗 Connect

**GitHub:** [@Astro-alii](https://github.com/Astro-alii)

---

<div align="center">
<sub>An ongoing Python data visualization learning journey — clean code, honest interpretation, real datasets.</sub>
</div>
