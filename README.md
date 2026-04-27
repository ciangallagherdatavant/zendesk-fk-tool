# Datavant Readability Tool

Automated Flesch-Kincaid readability analysis for Datavant's Zendesk
help centre articles.

**Live Dashboard:** https://ciangallagherdatavant.github.io/zendesk-fk-tool/

## What It Does
- Fetches Zendesk articles via the Zendesk API
- Calculates the Flesch-Kincaid Grade Level using Python's `textstat`
  library (consistent, mathematical, no AI variance)
- Uses Claude AI to generate plain-English recommendations and
  WCAG 2.2 writing accessibility notes
- Publishes results to a live dashboard
- Runs automatically every 4 hours via GitHub Actions

## Target Score
Grade 12 or below for all Datavant help centre content.

## How to Add an Article
Paste the Zendesk URL into column A of the linked Google Sheet.
The next scheduled run will analyse it automatically.

Full instructions in [HOW-TO-USE.md](HOW-TO-USE.md).

## Architecture
- `fk_analysis.py` — main script
- `index.html` — auto-generated dashboard
- `results/` — markdown record of every analysis
- `.github/workflows/analyse.yml` — schedule
- `prompts/` — reference copy of Claude prompt

## Built By
Cian Gallagher · Datavant Technical Writing Team