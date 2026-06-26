# 🧹 CleanSheet AI — No-Code Data Cleaning, Delivered

**Clean messy CSVs in seconds — with zero code. Free tier or Pro.**

[![Try Free](https://img.shields.io/badge/Live_Demo-🧹_CleanSheet_AI-6366F1?style=for-the-badge&logo=streamlit&logoColor=white)](https://cleansheet-ai.streamlit.app)
[![Get Pro](https://img.shields.io/badge/Get_Pro-$9_one--time-F59E0B?style=for-the-badge&logo=gumroad&logoColor=white)](https://7388507084353.gumroad.com/l/tqqra)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-111827?style=for-the-badge&logo=python&logoColor=white)]()
[![Tests](https://img.shields.io/badge/Tests-41_✅-22C55E?style=for-the-badge)]()

---

## ✨ What is CleanSheet AI?

CleanSheet AI is a **privacy-first, no-code data cleaning tool** that turns messy spreadsheets into analysis-ready datasets. Built with Streamlit, it replaces pandas wrangling with a visual 5‑step workflow — upload, inspect, detect issues, clean, and export.

> **No Python. No Jupyter. Just clean data.**

---

## 🎯 The 5‑Step Workflow

```
📤 Upload  →  📊 Overview  →  🚩 Issues  →  🧹 Clean  →  📥 Export
```

| Step | What You Get |
|------|-------------|
| **📤 Upload** | Drag & drop CSV, TSV, or TXT (up to **5 MB** free / **500 MB** Pro) |
| **📊 Overview** | Instant profile: row count, missing cells, duplicates, dtypes, memory, completeness %, numeric distributions, outlier candidates |
| **🚩 Issues** | Auto‑detected: missing values, duplicate rows, constant columns, potential outliers — all with visual indicators |
| **🧹 Clean** | Remove duplicates · fill/drop missing values · standardize text (strip, case, special chars) · convert dtypes · filter outliers |
| **📥 Export** | Download cleaned CSV · before/after comparison · cleaning summary |

---

## 🆚 Free vs Pro

| Feature | Free | Pro ($9) |
|---------|:----:|:--------:|
| CSV / TSV / TXT import | ✅ | ✅ |
| Excel (.xlsx) import & export | ❌ | ✅ |
| File size limit | 5 MB | 500 MB |
| Dark / Light mode | ✅ | ✅ |
| Data quality scoring | ❌ | QualityScore™ radar & metrics |
| AI‑powered cleaning suggestions | ❌ | Rule‑based smart suggestions |
| PDF quality reports | ❌ | Beautiful A4 reports |
| Outlier detection & filtering | ✅ IQR‑based | ✅ IQR‑based |
| Export to CSV | ✅ | ✅ |
| Export to Excel | ❌ | ✅ |
| Deployment | Streamlit Cloud | Local EXE (PyInstaller) |

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────┐
│                   Streamlit UI                   │
│  app.py / app_pro.py (+ components/)             │
├─────────────────────────────────────────────────┤
│              session_state (df, log)              │
├─────────────────────────────────────────────────┤
│  src/                                            │
│  ├── loader.py      CSV detection & loading      │
│  ├── profiler.py    Dataset profiling (fast!)     │
│  ├── cleaner.py     All cleaning operations      │
│  ├── exporter.py    CSV / Excel / Markdown        │
│  ├── styles.py      Dark/light CSS design system  │
│  └── analytics.py   Optional GA4 analytics        │
└─────────────────────────────────────────────────┘
```

### Pro‑Only Add‑ons (`components_pro/`)
- **AI Assistant** — rule‑based cleaning suggestions (zero API cost, instant)
- **Quality Dashboard** — 4‑dimension scoring (completeness, uniqueness, consistency, validity) with radar chart
- **PDF Reporter** — generate & download A4 PDF reports with fpdf2

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit 1.36+ |
| **Data** | pandas 2.0+, numpy 1.24+ |
| **Visualization** | Plotly 5.18+ |
| **Pro PDF** | fpdf2 2.7+ |
| **Pro EXE** | PyInstaller (PyPI) |
| **Deployment** | Streamlit Cloud (free) + Gumroad (Pro) |
| **Code Quality** | Python 3.11+, mypy strict, ruff |

---

## 🚀 Quick Start

```bash
git clone https://github.com/Mehta-27/CleanSheet-AI.git
cd CleanSheet-AI
python -m venv .venv && source .venv/bin/activate   # or .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open **http://localhost:8501** and upload a CSV to start cleaning.

---

## 🧪 Testing

```bash
pytest tests/ -v
```

| Module | Tests | What's Verified |
|--------|:-----:|-----------------|
| `loader` | 8 | Delimiter detection, encoding inference, CSV/Excel loading |
| `profiler` | 11 | Row counts, missing values, duplicates, dtypes, numeric stats |
| `cleaner` | 18 | Duplicate removal, missing fill strategies, text ops, type conversion |
| `exporter` | 4 | CSV bytes, Excel bytes, Markdown preview |

**41 tests — all passing in 0.67s.**

---

## 📁 Project Structure

```
CleanSheet-AI/
├── app.py                 # Free version entry point
├── app_pro.py             # Pro version entry point (PyInstaller-ready)
├── components/            # Free UI pages
│   ├── upload.py
│   ├── overview.py
│   ├── issue_panel.py
│   ├── action_panel.py
│   └── export_page.py
├── components_pro/        # Pro‑only UI
│   ├── ai_assistant.py
│   ├── quality_score.py
│   └── pdf_reporter.py
├── src/                   # Pure business logic (no Streamlit imports)
│   ├── cleaner.py
│   ├── exporter.py
│   ├── loader.py
│   ├── profiler.py
│   ├── styles.py
│   └── utils.py
├── tests/                 # 41 pytest tests
├── sample_data/           # messy_sales.csv (25 rows with deliberate issues)
└── requirements.txt
```

---

## 💜 Support

Loving CleanSheet? Even a small contribution helps keep the free version alive.

```
🇮🇳  UPI:  mehtarishit108@oksbi
💳  PayPal:  coming soon
```

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/Mehta-27">Rishit Mehta</a><br>
  <sub>Free for everyone · Pro for power users · Privacy first, always</sub>
</p>
