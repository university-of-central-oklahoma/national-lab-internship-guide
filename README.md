# National Laboratory Internship Guide

A MkDocs Material site for students, faculty and the Research Internship Advisory Committee. Includes a shared opportunity-spreadsheet link, application checklist, planning guides and downloadable templates.

## Build and preview

```powershell
cd C:\Users\jhrhe\Downloads\CHATGPT\national-lab-guide
.\.venv\Scripts\python.exe -m mkdocs build --strict
.\.venv\Scripts\python.exe -m mkdocs serve
```

Open http://127.0.0.1:8000. Press Ctrl+C to stop. Generated static output is in `dist/`.

If you need to install dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Maintain content

Edit guide pages in `docs/`. Maintain listings directly in the [shared spreadsheet](https://docs.google.com/spreadsheets/d/1XfAbQf3lic7tOpiT_JgilAPFzAPPrtLPZBIZlM1TGBk/edit?usp=sharing); spreadsheet edits do not require rebuilding the site. There is no directory generator or fixed opportunity count. The homepage, toolkit, eligibility, committee and FAQ pages link to the spreadsheet.

Run `python verify_build.py` after building to check local references and the spreadsheet link. Serve `dist/` on any static host. Sites hosting is configured in `.openai/hosting.json`.

## Content boundaries

Initial research reviewed November 9, 2026. This is an independent educational guide, not a lab hiring portal. Confirm live openings, eligibility, deadlines and funding with each program. Checklist state stays in the visitor's browser. Spreadsheet access follows its Google sharing settings.

Committee members and professional contact details are listed directly on the committee webpage. Preserve the Sites audience unless explicitly changing its access settings.
