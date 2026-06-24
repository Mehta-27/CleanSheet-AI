<div align="center">
  <br>
  <h1>🧹 CleanSheet AI</h1>
  <p><strong>Your Data, Perfectly Clean.</strong></p>
  <p>Upload a messy CSV → Auto-detect issues → Clean with one click → Download.</p>
  <p>No coding. No sign-up. No cost.</p>
  <br>
  <p>
    <a href="https://cleansheet-ai.streamlit.app" target="_blank">
      <img src="https://img.shields.io/badge/Try%20Free-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Try Free">
    </a>
    &nbsp;
    <a href="https://7388507084353.gumroad.com/l/tqqra" target="_blank">
      <img src="https://img.shields.io/badge/Pro-%249%20on%20Gumroad-36A9AE?style=for-the-badge&logo=gumroad&logoColor=white" alt="Pro on Gumroad">
    </a>
  </p>
  <p>
    <img src="https://img.shields.io/github/license/Mehta-27/CleanSheet-AI?style=flat-square" alt="License">
    &nbsp;
    <img src="https://img.shields.io/badge/python-3.11%2B-purple?style=flat-square&logo=python" alt="Python">
    &nbsp;
    <img src="https://img.shields.io/badge/tests-41%2F41-passing-brightgreen?style=flat-square" alt="Tests">
    &nbsp;
    <img src="https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?style=flat-square&logo=streamlit" alt="Streamlit Cloud">
  </p>
  <br>
</div>

---

## ✨ Features

| Feature | Free | Pro |
|---|---|---|
| CSV & TSV upload | ✅ Up to 5 MB | ✅ Up to 500 MB |
| Auto data profiling (missing, duplicates, outliers, types) | ✅ | ✅ |
| Missing value handling (mean, median, mode, custom, drop) | ✅ | ✅ |
| Duplicate removal | ✅ | ✅ |
| Text standardization (strip, case, special chars) | ✅ | ✅ |
| Type conversion (int, float, string, datetime, category) | ✅ | ✅ |
| Interactive preview & Plotly charts | ✅ | ✅ |
| Cleaning history log | ✅ | ✅ |
| **Excel (.xlsx) import/export** | ❌ | ✅ |
| **AI-powered cleaning suggestions** | ❌ | ✅ |
| **Data quality score (0–100)** | ❌ | ✅ |
| **PDF quality report** | ❌ | ✅ |
| **Outlier detection & IQR filtering** | ❌ | ✅ |
| **Column renaming** | ❌ | ✅ |
| **Constant column detection** | ❌ | ✅ |
| **Runs locally — no limits** | ❌ | ✅ |

---

## 🚀 Pro — $9 (one-time)

Everything in Free plus Excel, AI suggestions, PDF reports, outlier detection, and more.

**[Buy on Gumroad →](https://7388507084353.gumroad.com/l/tqqra)**

### Who needs Pro?
- **Analysts** cleaning weekly reports
- **Small businesses** managing customer data, inventory, sales CSVs
- **Data journalists** preparing datasets for investigation
- **Students & researchers** prepping data for projects
- **Anyone** who regularly works with dirty spreadsheets

---

## 🖼️ Screenshots

> *Coming soon — screenshots of the upload, profiling, cleaning, and export flows.*

---

## 🛠️ Tech Stack

| Layer | Stack |
|---|---|
| **Frontend** | [Streamlit](https://streamlit.io) |
| **Language** | Python 3.11+ |
| **Data** | pandas, numpy |
| **Charts** | Plotly |
| **Analysis** | scipy |
| **Pro — PDF** | fpdf2 |
| **Pro — Excel** | openpyxl, XlsxWriter |

---

## 🧪 Development

```bash
# Clone
git clone https://github.com/Mehta-27/CleanSheet-AI.git
cd CleanSheet-AI

# Setup
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate

# Install
pip install -r requirements.txt

# Run
streamlit run app.py
```

### Tests

```bash
pytest tests/ -v
```

41 tests — all passing.

### Build Pro EXE

See [`BUILD_FOR_GUMROAD.md`](BUILD_FOR_GUMROAD.md) for the full packaging guide.

---

## 📁 Project Structure

```
CleanSheet-AI/
├── app.py                  # Free version entry point
├── app_pro.py              # Pro version entry point
├── components/
│   ├── upload.py           # File upload & hero section
│   ├── overview.py         # Data preview & stats
│   ├── issue_panel.py      # Issue detection UI
│   ├── action_panel.py     # Cleaning actions UI
│   └── export_page.py      # Download & export
├── components_pro/         # Pro-only features
├── src/
│   ├── cleaner.py          # Cleaning logic
│   ├── loader.py           # File loading & validation
│   ├── profiler.py         # Data profiling
│   ├── exporter.py         # Export logic
│   ├── analytics.py        # Google Analytics
│   ├── styles.py           # Design system (CSS)
│   └── utils.py            # Shared utilities
├── tests/                  # 41 test cases
├── sample_data/            # Messy CSV for testing
└── build/                  # PyInstaller output
```

---

## 📄 License

- **CleanSheet Free** — available for public use
- **CleanSheet Pro** — proprietary; contact for licensing

---

<div align="center">
  <p>
    Built with ❤️ by <a href="https://github.com/Mehta-27">Rishit Mehta</a>
  </p>
  <p>
    <a href="https://cleansheet-ai.streamlit.app">Try it Free</a>
    &nbsp;·&nbsp;
    <a href="https://7388507084353.gumroad.com/l/tqqra">Buy Pro</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/Mehta-27/CleanSheet-AI/issues">Report Bug</a>
  </p>
</div>
