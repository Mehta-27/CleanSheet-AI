# 🧹 CleanSheet AI

**Your Data, Perfectly Clean.**

Clean messy CSV files in **under 60 seconds** — no coding, no sign-up, no cost.

---

## Free Version (Hosted)

Upload your CSV → Auto-detect issues → Clean with one click → Download.

**Use it now:** [cleansheet-ai.streamlit.app](https://cleansheet-ai.streamlit.app)

### Free features:
- ✅ CSV & TSV upload (up to 5MB)
- ✅ Automatic data profiling (missing values, duplicates, outliers, types)
- ✅ Missing value handling (mean, median, mode, custom value, drop)
- ✅ Duplicate removal (all columns or selected subset)
- ✅ Text standardization (strip whitespace, case conversion, special chars)
- ✅ Type conversion (int, float, string, datetime, category)
- ✅ Interactive data preview and visualizations
- ✅ Download cleaned CSV
- ✅ Cleaning history log

---

## 🚀 CleanSheet Pro — $9.99

**Everything in Free + advanced features for power users.**

Grab it on Gumroad: [7388507084353.gumroad.com/l/tqqra](https://7388507084353.gumroad.com/l/tqqra)

### Pro features:
| Feature | Free | Pro |
|---|---|---|
| File size limit | 50 MB | 500 MB |
| CSV / TSV | ✅ | ✅ |
| Excel (.xlsx) import/export | ❌ | ✅ |
| AI-powered cleaning suggestions | ❌ | ✅ |
| Data quality score (0-100) | ❌ | ✅ |
| PDF quality report | ❌ | ✅ |
| Batch processing (multiple files) | ❌ | ✅ |
| Outlier detection & filtering | ❌ | ✅ |
| Constant column detection | ❌ | ✅ |
| Column renaming | ❌ | ✅ |
| Priority email support | ❌ | ✅ |
| Runs locally (no limits) | ❌ | ✅ |

### Who needs Pro?
- **Analysts** cleaning weekly reports
- **Small businesses** managing customer data, inventory, sales CSVs
- **Data journalists** cleaning messy datasets before analysis
- **Students & researchers** preparing data for projects
- **Anyone** who regularly works with dirty spreadsheets

### Why pay?
Pro pays for itself in the first use. Instead of spending 30+ minutes fixing data in Excel, you get a clean dataset in **under 60 seconds**.

---

## Why CleanSheet AI?

| Problem | CleanSheet AI |
|---|---|
| "My CSV has missing values everywhere" | Auto-detect + fill with mean/median/mode |
| "Names are in ALL CAPS, lowercase, mixed" | One-click text standardization |
| "I have duplicate rows" | Remove in one click |
| "Dates are in wrong format" | Auto type conversion |
| "Numbers have $ signs" | Smart parsing |
| "I don't know what's wrong with my data" | Auto profiling tells you exactly |

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python 3.11+
- **Data:** pandas, numpy
- **Charts:** plotly
- **Pro PDF:** fpdf2
- **Pro Excel:** openpyxl, XlsxWriter

---

## Development

```bash
git clone https://github.com/Mehta-27/cleansheet-ai.git
cd cleansheet-ai
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run app.py
```

### Run tests
```bash
pytest tests/ -v
```

### Build Pro EXE
See [BUILD_FOR_GUMROAD.md](BUILD_FOR_GUMROAD.md)

---

## Roadmap

### v1.0 (current)
- Free: Core CSV cleaning
- Pro: AI + Excel + PDF + Batch

### v2.0 (planned)
- AI cleaning suggestions via Gemini/GPT
- Schema validation (define expected columns/types)
- Data merging (join multiple CSVs)
- Custom cleaning pipeline templates
- API endpoint for programmatic access

### v3.0 (future)
- Cloud storage integration (Google Drive, Dropbox)
- Scheduled auto-cleaning
- Team collaboration
- Data dictionary generation

---

## License

CleanSheet Free is available for public use.
CleanSheet Pro is proprietary — contact for licensing.

---

*Built by [Rishit Mehta](https://github.com/Mehta-27) · [Buy me a coffee](https://buymeacoffee.com)*
