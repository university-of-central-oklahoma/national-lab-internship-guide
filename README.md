# LabPath — national laboratory internship guide

A real MkDocs Material site for students, faculty and department ambassadors. Includes 30 curated program/research pathways, an eligibility-aware directory with browser-local saves, application checklist, planning guides and downloadable templates.

## Build

Python 3.10+ recommended. On Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe build_content.py
.\.venv\Scripts\python.exe -m mkdocs build --strict
.\.venv\Scripts\python.exe -m mkdocs serve
```

On other systems use `python3 -m venv .venv` and `.venv/bin/python` for the same commands. Generated static output is in `dist/`. Serve that folder on any static host. Sites hosting is configured in `.openai/hosting.json`.

Edit guide pages in `docs/`. Directory records are maintained in `build_content.py`; running it generates `data/opportunities.json`, directory Markdown, source register and the CSV download together. Use the existing guide formats and preserve official source URLs and review dates.

## Content boundaries

Research reviewed November 9, 2026. This is an independent educational guide, not a lab hiring portal. The 30 routes are curated, not ranked; live openings, eligibility, deadlines and funding must be confirmed with each program. Some routes are fellowships or faculty collaborations, labeled accordingly. No live deadline feed, email submission or department database is implemented. Local saves/checklist state stay in the visitor's browser.

Department contacts were not supplied: fill the blank downloadable roster with approved contacts before announcing campus support. New Sites deployment remains owner-private unless explicitly shared through Sites access settings.
