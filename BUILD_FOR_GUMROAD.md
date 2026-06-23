# 🚀 CleanSheet Pro — Build for Gumroad Distribution

This guide explains how to package CleanSheet Pro into a standalone Windows EXE
for sale on Gumroad.

## Prerequisites

- Python 3.11+ installed
- All dependencies installed
- PyInstaller (`pip install pyinstaller`)

## Step 1: Prepare the Pro Build

We build a single EXE that includes ALL features (Free + Pro).
Pro features are enabled by default in the downloadable version.

```bash
pip install pyinstaller
```

## Step 2: Build the EXE

### Important: The entry point is `app_pro.py`, NOT `app.py`.
`app_pro.py` includes all Pro features (Excel, AI suggestions, PDF reports, etc.).

```bash
pyinstaller ^
    --onefile ^
    --name "CleanSheet_AI_Pro" ^
    --add-data "sample_data;sample_data" ^
    app_pro.py
```

### Explanation:
- `--onefile`: Single EXE for easy distribution
- `--name`: "CleanSheet_AI_Pro" — the product name buyers see
- `--add-data`: Includes sample data for first-time users
- Entry point is `app_pro.py` (includes all Free + Pro features)

### How the EXE works when a buyer double-clicks it:
1. A terminal window opens briefly while Streamlit starts up
2. Your default browser automatically opens to `http://localhost:8501`
3. The full CleanSheet Pro UI appears — all features unlocked
4. Close the terminal window to stop the app
5. No installation, no admin rights, no registry changes. Runs portably (even from USB).

## Step 3: Test the EXE

```bash
dist\CleanSheet_AI_Pro.exe
```

The app will start Streamlit and open in your default browser.
Test all features before uploading to Gumroad.

## Step 4: Prepare for Gumroad

1. Create a Gumroad account at https://gumroad.com
2. Create a new product:
   - **Name:** CleanSheet AI Pro
   - **Price:** $9.99 (one-time)
   - **Description:** Copy from README.md Pro section
   - **File:** Upload `dist\CleanSheet_AI_Pro.exe`
   - **License:** Enable Gumroad license keys (optional)

3. **Product images:** Take screenshots:
   - Upload screen with demo data
   - Data profiling dashboard
   - Cleaning panel with AI suggestions
   - Export/download page
   - Quality score dashboard

4. **Sales page highlights:**
   ```
   Clean messy CSV data in 60 seconds.
   
   ✓ No coding required
   ✓ No sign-up or account needed
   ✓ Runs 100% offline on your machine
   ✓ Unlimited file size
   ✓ Excel support, AI suggestions, PDF reports
   ✓ One-time payment — no subscription
   ```

## Step 5: Marketing

### Where to promote:
- **Reddit:** r/datasets, r/dataanalysis, r/excel, r/datascience
- **Product Hunt:** Launch as a free tool with Pro upgrade
- **Twitter/X:** Share before/after examples
- **LinkedIn:** Post about the tool in data communities
- **Indie Hackers:** Share your journey building it

### Free users → Pro buyers pipeline:
1. User finds the free hosted version (Streamlit Cloud)
2. Free version has "Get Pro" buttons in sidebar + export page
3. User hits free limits (50MB, no Excel, no PDF)
4. User clicks → Gumroad → $9.99 → downloads Pro EXE

## Pricing Strategy

| | Free (Hosted) | Pro (EXE) |
|---|---|---|
| Price | $0 | $9.99 one-time |
| Where | streamlit.cloud | gumroad.com |
| Users | Everyone | Power users |
| Strategy | Traffic + lead gen | Revenue |

## Optional: Custom Icon

Generate a `icon.ico` from any PNG:
```bash
pip install pillow
python -c "
from PIL import Image
img = Image.open('icon.png')
img.save('icon.ico', format='ICO', sizes=[(256,256)])
"
```

## Optional: Version Updates

When you release updates:
1. Increment version in `pyproject.toml`
2. Rebuild with PyInstaller
3. Replace file on Gumroad
4. Notify buyers via Gumroad's email tool

---

## Quick Reference

```bash
# Full build command (copy-paste ready)
pip install pyinstaller
pyinstaller --onefile --name "CleanSheet_AI_Pro" --add-data "sample_data;sample_data" --copy-metadata streamlit app_pro.py

# Output: dist/CleanSheet_AI_Pro.exe (~130 MB)
```
