# ============================================
# FK Readability Analysis Tool
# Built by Cian Gallagher - Datavant
# Architecture: Hybrid Python + Claude
# Python handles FK calculation precisely
# Claude handles recommendations and WCAG
# Google Sheets handles article queue
# Supports full URLs or just article IDs
# Datavant brand colours applied
# ============================================

import os
import re
import glob
import json
import urllib3
import textstat
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from dotenv import load_dotenv
import requests
import anthropic

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ZENDESK_SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
ZENDESK_EMAIL = os.getenv("ZENDESK_EMAIL")
ZENDESK_API_TOKEN = os.getenv("ZENDESK_API_TOKEN")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS")

ANALYSIS_PROMPT = """
You are a technical writing assistant helping a technical writing
team improve their Zendesk help centre documentation.

You have been given:
1. The cleaned prose text of a Zendesk article
2. A pre-calculated Flesch-Kincaid Grade Level score
   calculated by Python using the textstat library

Your job is to:
1. Accept the pre-calculated FK score as the official score
2. Explain what the score means in plain English
3. Give specific FK readability recommendations
4. Give WCAG 2.2 writing accessibility notes

## Reading Level Guide
- Grade 1 to 6 = Elementary, very easy to read
- Grade 7 to 8 = Middle School, easy and ideal for most audiences
- Grade 9 to 10 = High School, moderate complexity
- Grade 11 to 12 = High School Advanced, becoming complex
- Grade 13 and above = College level, too complex for most audiences

Technical writing should ideally target Grade 12 or below.

## How to Present Your Response
Use this exact format every time:

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: [title]

SCORE: [use the pre-calculated score provided to you]
Reading Level: [level based on score]
Target Audience: [description of who can read this comfortably]

Summary: [one clear sentence explaining what this score means]

FK RECOMMENDATIONS:
[Always give 3 specific suggestions to improve readability further.
If Grade 12 or below: start by acknowledging the content meets
the target then give 3 specific suggestions to improve it further.
If above Grade 12: give 3 specific suggestions to bring the
score below 12. Always reference specific examples from the
actual article text in your suggestions]

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: [Pass or flag with specific examples from the text]
Sentence Length: [Pass or flag any sentences over 25 words]
Jargon: [Pass or list unexplained technical terms found]
Active Voice: [Pass or flag passive constructions with examples]
Heading Clarity: [Pass or suggestions based on content]
Link Text: [Pass or flag vague link text found]
Abbreviations: [Pass or list unexplained abbreviations found]

Overall WCAG Writing Score: [Good / Needs Attention / Needs Significant Work]
---
"""


def extract_id_from_input(input_value):
    input_value = input_value.strip()
    input_value = input_value.strip('"').strip("'")
    if 'http' in input_value or 'zendesk' in input_value or 'datavant.com' in input_value:
        id_match = re.search(r'/articles/(\d+)', input_value)
        if id_match:
            article_id = id_match.group(1)
            name_match = re.search(r'/articles/\d+-(.+?)(?:\?|$)', input_value)
            if name_match:
                name_hint = name_match.group(1).replace('-', ' ').title()
            else:
                name_hint = None
            return article_id, name_hint
        return None, None
    clean_id = re.sub(r'[^0-9]', '', input_value)
    if clean_id and clean_id.isdigit():
        return clean_id, None
    return None, None


def get_google_sheet():
    print("\nConnecting to Google Sheets...")
    try:
        creds_json = GOOGLE_SHEETS_CREDENTIALS
        if not creds_json:
            print("No Google Sheets credentials found")
            return None
        creds_dict = json.loads(creds_json)
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_info(
            creds_dict, scopes=scopes
        )
        client = gspread.authorize(creds)
        sheet = client.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sheet.get_worksheet(0)
        print("Connected to Google Sheets successfully")
        return worksheet
    except Exception as e:
        print(f"Could not connect to Google Sheets: {e}")
        return None


def get_pending_articles(worksheet):
    print("\nChecking for pending articles in Google Sheet...")
    try:
        all_rows = worksheet.get_all_values()
        pending = []
        done_ids = set()
        for i, row in enumerate(all_rows):
            if i == 0:
                continue
            if not row or not row[0]:
                continue
            raw_input = row[0].strip()
            status = row[2].strip() if len(row) > 2 else ''
            if not raw_input:
                continue
            article_id, _ = extract_id_from_input(raw_input)
            if not article_id:
                continue
            if status.lower() == 'done' or status.lower() == 'n/a':
                done_ids.add(article_id)
        for i, row in enumerate(all_rows):
            if i == 0:
                continue
            if not row or not row[0]:
                continue
            raw_input = row[0].strip()
            article_name = row[1].strip() if len(row) > 1 else ''
            status = row[2].strip() if len(row) > 2 else ''
            if not raw_input:
                continue
            if status.lower() == 'done' or status.lower() == 'n/a':
                continue
            article_id, name_hint = extract_id_from_input(raw_input)
            if not article_id:
                print(f"Could not extract ID from row {i+1}: {raw_input}")
                continue
            if article_id in done_ids:
                print(f"Skipping row {i+1}: Article {article_id} already analysed")
                worksheet.update_cell(i + 1, 3, 'Done (duplicate)')
                continue
            if not article_name and name_hint:
                article_name = name_hint
            pending.append({
                'row': i + 1,
                'article_id': article_id,
                'article_name': article_name,
                'raw_input': raw_input
            })
        print(f"Found {len(pending)} pending articles")
        return pending
    except Exception as e:
        print(f"Error reading sheet: {e}")
        return []


def update_sheet_status(worksheet, row_number, article_name, score):
    try:
        today = datetime.now().strftime('%d %B %Y %H:%M')
        worksheet.update_cell(row_number, 2, article_name)
        worksheet.update_cell(row_number, 3, 'Done')
        worksheet.update_cell(row_number, 4, today)
        worksheet.update_cell(row_number, 5, str(score))
        print(f"Sheet updated for row {row_number}")
    except Exception as e:
        print(f"Could not update sheet: {e}")


def get_zendesk_article(article_id):
    print(f"\nFetching article {article_id} from Zendesk...")
    url = f"https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/help_center/articles/{article_id}"
    auth = (f"{ZENDESK_EMAIL}/token", ZENDESK_API_TOKEN)
    response = requests.get(url, auth=auth, verify=False)
    if response.status_code != 200:
        print(f"Error fetching article: {response.status_code}")
        return None, None
    data = response.json()
    title = data['article']['title']
    body = data['article']['body']
    clean_body = re.sub('<[^<]+?>', '', body)
    print(f"Article fetched successfully: {title}")
    return title, clean_body


def clean_text_for_fk(text):
    lines = text.split('\n')
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if len(line) < 20:
            continue
        if line.startswith('http'):
            continue
        if re.match(r'^[\d\s\.\-\*\#\>\|]+$', line):
            continue
        symbol_count = len(re.findall(r'[^a-zA-Z\s]', line))
        if symbol_count > len(line) * 0.4:
            continue
        word_count = len(line.split())
        if word_count < 4:
            continue
        clean_lines.append(line)
    return ' '.join(clean_lines)


def calculate_fk_score(clean_text):
    if not clean_text or len(clean_text.split()) < 10:
        return None
    score = textstat.flesch_kincaid_grade(clean_text)
    score = round(score, 1)
    word_count = textstat.lexicon_count(clean_text)
    sentence_count = textstat.sentence_count(clean_text)
    syllable_count = textstat.syllable_count(clean_text)
    print(f"FK Score calculated by Python: {score}")
    print(f"Words: {word_count} | Sentences: {sentence_count} | Syllables: {syllable_count}")
    return {
        'score': score,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'syllable_count': syllable_count,
        'avg_words_per_sentence': round(word_count / sentence_count, 1) if sentence_count > 0 else 0,
        'avg_syllables_per_word': round(syllable_count / word_count, 2) if word_count > 0 else 0
    }


def get_reading_level(score):
    if score <= 6:
        return "Elementary"
    elif score <= 8:
        return "Middle School"
    elif score <= 10:
        return "High School"
    elif score <= 12:
        return "High School Advanced"
    else:
        return "College level"


def analyse_with_claude(title, clean_text, fk_data):
    print(f"\nSending to Claude for recommendations and WCAG analysis...")
    score = fk_data['score']
    reading_level = get_reading_level(score)
    prompt_with_data = f"""
{ANALYSIS_PROMPT}

---
ARTICLE INFORMATION:

Title: {title}

Pre-calculated FK Score: {score}
Reading Level: {reading_level}

Score Breakdown (calculated by Python textstat):
- Eligible words analysed: {fk_data['word_count']}
- Eligible sentences analysed: {fk_data['sentence_count']}
- Eligible syllables analysed: {fk_data['syllable_count']}
- Average words per sentence: {fk_data['avg_words_per_sentence']}
- Average syllables per word: {fk_data['avg_syllables_per_word']}

CLEANED PROSE TEXT FOR WCAG ANALYSIS:
{clean_text[:3000]}
---

Please use the pre-calculated score of {score} as the official score.
Do not recalculate. Focus your response on recommendations and WCAG notes.
"""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=3000,
        messages=[{"role": "user", "content": prompt_with_data}]
    )
    result = message.content[0].text
    print("Claude analysis complete")
    return result


def save_result(title, result, fk_data):
    print(f"\nSaving result...")
    clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    clean_title = clean_title.replace(' ', '-').lower()
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"results/{clean_title}-{timestamp}.md"
    with open(filename, 'w') as f:
        f.write(f"# FK Analysis Result\n\n")
        f.write(f"**Article:** {title}\n")
        f.write(f"**Date:** {datetime.now().strftime('%d %B %Y %H:%M')}\n")
        f.write(f"**Calculated by:** Python textstat library\n\n")
        f.write(result)
    print(f"Result saved to: {filename}")
    return filename


def read_all_results():
    print("\nReading all result files...")
    result_files = glob.glob('results/*.md')
    result_files = [f for f in result_files if '.gitkeep' not in f]
    result_files = [f for f in result_files if 'sample-article' not in f]
    all_by_title = {}
    for filepath in result_files:
        with open(filepath, 'r') as f:
            content = f.read()
        title_match = re.search(r'\*\*Article:\*\* (.+)', content)
        title = title_match.group(1).strip() if title_match else 'Unknown Article'
        date_match = re.search(r'\*\*Date:\*\* (.+)', content)
        date = date_match.group(1).strip() if date_match else 'Unknown Date'
        score_match = re.search(r'\*?\*?SCORE:\*?\*?\s*\*?\*?(\d+\.?\d*)', content)
        score = float(score_match.group(1)) if score_match else 0
        level_match = re.search(r'Reading Level:\s*\*?\*?(.+)', content)
        level = level_match.group(1).strip() if level_match else 'Unknown'
        level = re.sub(r'\*', '', level).strip()
        summary_match = re.search(r'Summary:\s*\*?\*?(.+)', content)
        summary = summary_match.group(1).strip() if summary_match else ''
        summary = re.sub(r'\*', '', summary).strip()
        fk_rec_match = re.search(
            r'FK RECOMMENDATIONS:\s*\n(.*?)(?=WCAG 2\.2 WRITING|---|$)',
            content, re.DOTALL
        )
        fk_recommendations = fk_rec_match.group(1).strip() if fk_rec_match else ''
        fk_recommendations = re.sub(r'\*\*', '', fk_recommendations)
        if not fk_recommendations:
            rec_match = re.search(
                r'RECOMMENDATIONS:\s*\n(.*?)(?=WCAG|---|$)',
                content, re.DOTALL
            )
            fk_recommendations = rec_match.group(1).strip() if rec_match else ''
            fk_recommendations = re.sub(r'\*\*', '', fk_recommendations)
        wcag_match = re.search(
            r'WCAG 2\.2 WRITING ACCESSIBILITY NOTES:\s*\n(.*?)(?=---|$)',
            content, re.DOTALL
        )
        wcag_notes = wcag_match.group(1).strip() if wcag_match else ''
        wcag_notes = re.sub(r'\*\*', '', wcag_notes)
        entry = {
            'title': title,
            'date': date,
            'score': score,
            'level': level,
            'summary': summary,
            'fk_recommendations': fk_recommendations,
            'wcag_notes': wcag_notes,
            'filepath': filepath
        }
        if title not in all_by_title:
            all_by_title[title] = []
        all_by_title[title].append(entry)
    results = []
    for title, entries in all_by_title.items():
        entries.sort(key=lambda x: datetime.strptime(x['date'].strip()[:20], '%d %B %Y %H:%M') if len(x['date'].strip()) > 11 else datetime.strptime(x['date'].strip(), '%d %B %Y'))
        latest = entries[-1]
        history = entries[:-1]
        first_score = entries[0]['score'] if len(entries) > 1 else None
        improvement = None
        if first_score and first_score != latest['score']:
            improvement = round(first_score - latest['score'], 1)
        latest['history'] = history
        latest['first_score'] = first_score
        latest['improvement'] = improvement
        results.append(latest)
    results.sort(key=lambda x: x['score'], reverse=True)
    print(f"Found {len(results)} unique articles")
    return results


def get_status(score):
    if score <= 12.0:
        return 'good', '✅ Meets Target'
    elif score <= 14.9:
        return 'warning', '⚠️ Needs Improvement'
    else:
        return 'bad', '🔴 Needs Significant Work'


def get_progress_width(score):
    capped = min(score, 20)
    return int((capped / 20) * 100)


def build_history_rows_html(history, current_score, current_date):
    all_entries = history + [{'date': current_date, 'score': current_score}]
    rows = ''
    for entry in reversed(all_entries):
        h_status, _ = get_status(entry['score'])
        label = 'Latest' if entry['date'] == current_date else ''
        rows += f"""
        <div class="history-row">
            <span class="history-date">{entry['date']}</span>
            <span class="history-score {h_status}">{entry['score']}</span>
            {f'<span class="history-label">Latest</span>' if label else ''}
        </div>
        """
    return rows


def build_dashboard(results):
    print("\nUpdating dashboard...")
    total = len(results)
    good_count = len([r for r in results if r['score'] <= 12.0])
    warning_count = len([r for r in results if 12.0 < r['score'] <= 14.9])
    bad_count = len([r for r in results if r['score'] > 14.9])
    avg_score = round(
        sum(r['score'] for r in results) / total, 1
    ) if total > 0 else 0
    today = datetime.now().strftime('%d %B %Y')

    cards_html = ""
    history_cards_html = ""

    for i, r in enumerate(results):
        status, status_text = get_status(r['score'])
        progress = get_progress_width(r['score'])
        delay = round(0.1 + (i * 0.05), 2)

        fk_rec_lines = r['fk_recommendations'].split('\n')
        fk_rec_html = ""
        for line in fk_rec_lines:
            line = line.strip()
            if line:
                fk_rec_html += f"<p>{line}</p>"
        if not fk_rec_html:
            fk_rec_html = "<p>Re-run this article to generate FK recommendations.</p>"

        wcag_lines = r.get('wcag_notes', '').split('\n')
        wcag_html = ""
        for line in wcag_lines:
            line = line.strip()
            if line:
                wcag_html += f"<p>{line}</p>"
        if not wcag_html:
            wcag_html = "<p>Re-run this article to generate WCAG accessibility notes.</p>"

        cards_html += f"""
        <div class="article-card {status}" data-status="{status}" data-title="{r['title'].lower()}" data-score="{r['score']}" data-date="{r['date']}" style="animation-delay:{delay}s">
            <div class="card-header">
                <div class="article-title">{r['title']}</div>
                <div class="score-badge {status}">{r['score']}</div>
            </div>
            <div class="progress-bar-wrap">
                <div class="progress-bar {status}" style="width:{progress}%"></div>
            </div>
            <div class="reading-level">{r['level']}</div>
            <span class="status-pill {status}">{status_text}</span>
            <div class="summary-text">{r['summary']}</div>
            <div class="card-meta">Tested: {r['date']} · Score calculated by Python textstat</div>
            <button class="rec-toggle" onclick="toggleSection('fk-{i}', this)">
                <span>📊 FK Recommendations</span><span>▼</span>
            </button>
            <div class="recommendations" id="fk-{i}">
                <div class="rec-section-title">Flesch-Kincaid Recommendations</div>
                {fk_rec_html}
            </div>
            <button class="rec-toggle wcag-toggle" onclick="toggleSection('wcag-{i}', this)">
                <span>♿ WCAG Accessibility Notes</span><span>▼</span>
            </button>
            <div class="recommendations wcag-rec" id="wcag-{i}">
                <div class="rec-section-title">WCAG 2.2 Writing Accessibility</div>
                {wcag_html}
            </div>
        </div>
"""

        history = r.get('history', [])
        improvement = r.get('improvement')

        if improvement is not None:
            if improvement > 0:
                trend_class = 'trend-good'
                trend_text = f'↓ Improved by {improvement} points'
            elif improvement < 0:
                trend_class = 'trend-bad'
                trend_text = f'↑ Declined by {abs(improvement)} points'
            else:
                trend_class = 'trend-neutral'
                trend_text = '→ No change'
        else:
            trend_class = 'trend-neutral'
            trend_text = 'Only tested once'

        history_rows = build_history_rows_html(
            history, r['score'], r['date']
        )

        history_cards_html += f"""
        <div class="history-card {status}" style="animation-delay:{delay}s">
            <div class="history-card-header">
                <div class="article-title">{r['title']}</div>
                <div class="score-badge {status}">{r['score']}</div>
            </div>
            <div class="progress-bar-wrap">
                <div class="progress-bar {status}" style="width:{progress}%"></div>
            </div>
            <div class="trend-badge {trend_class}">{trend_text}</div>
            <div class="history-entries">
                {history_rows}
            </div>
        </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datavant Readability Tool</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #ECEAE4;
            color: #020202;
        }}

        header {{
            background: #020202;
            color: white;
            padding: 24px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 20px rgba(2,2,2,0.3);
        }}

        header h1 {{
            font-size: 22px;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: white;
        }}

        header h1 span {{
            color: #14E7E8;
        }}

        header p {{
            font-size: 12px;
            opacity: 0.5;
            margin-top: 4px;
            color: white;
        }}

        .target-badge {{
            background: rgba(20,231,232,0.15);
            border: 1px solid rgba(20,231,232,0.3);
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 12px;
            color: #14E7E8;
            font-weight: 600;
        }}

        .stats-bar {{
            background: #FFFFFF;
            padding: 20px 40px;
            display: flex;
            gap: 0;
            border-bottom: 1px solid #D9D7D1;
            box-shadow: 0 2px 8px rgba(2,2,2,0.06);
        }}

        .stat {{
            text-align: center;
            flex: 1;
            padding: 8px 0;
            border-right: 1px solid #ECEAE4;
            transition: transform 0.2s;
        }}

        .stat:last-child {{ border-right: none; }}
        .stat:hover {{ transform: translateY(-2px); }}

        .stat-number {{
            font-size: 30px;
            font-weight: 800;
            color: #020202;
            line-height: 1;
        }}

        .stat-label {{
            font-size: 10px;
            color: #9A9A9A;
            margin-top: 4px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            font-weight: 600;
        }}

        .stat-number.good {{ color: #0F3D4C; }}
        .stat-number.warning {{ color: #475FF2; }}
        .stat-number.bad {{ color: #152271; }}

        .main {{ padding: 28px 40px; }}

        .section-title {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 6px;
            color: #020202;
        }}

        .last-updated {{
            font-size: 11px;
            color: #9A9A9A;
            margin-bottom: 20px;
        }}

        .controls-bar {{
            display: flex;
            gap: 12px;
            margin-bottom: 18px;
            flex-wrap: wrap;
            align-items: center;
        }}

        .search-wrap {{
            flex: 1;
            min-width: 200px;
            position: relative;
        }}

        .search-wrap input {{
            width: 100%;
            padding: 10px 16px 10px 40px;
            border: 1.5px solid #D9D7D1;
            border-radius: 8px;
            font-size: 13px;
            outline: none;
            transition: border-color 0.2s;
            background: white;
            font-family: 'DM Sans', sans-serif;
            color: #020202;
        }}

        .search-wrap input:focus {{ border-color: #14E7E8; }}
        .search-icon {{ position: absolute; left: 12px; top: 50%; transform: translateY(-50%); font-size: 15px; color: #9A9A9A; }}
        .search-count {{ position: absolute; right: 12px; top: 50%; transform: translateY(-50%); font-size: 11px; color: #9A9A9A; font-weight: 600; }}

        .sort-wrap {{ display: flex; gap: 6px; flex-wrap: wrap; }}

        .sort-btn {{
            padding: 8px 14px;
            border-radius: 6px;
            border: 1.5px solid #D9D7D1;
            background: white;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            color: #676767;
            white-space: nowrap;
            font-family: 'DM Sans', sans-serif;
        }}

        .sort-btn:hover {{ border-color: #020202; color: #020202; }}
        .sort-btn.active {{ background: #020202; color: white; border-color: #020202; }}

        .filter-bar {{ display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }}

        .filter-btn {{
            padding: 7px 16px;
            border-radius: 20px;
            border: 1.5px solid #D9D7D1;
            background: white;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            color: #676767;
            font-family: 'DM Sans', sans-serif;
        }}

        .filter-btn:hover {{ border-color: #020202; color: #020202; }}
        .filter-btn.active {{ background: #020202; color: white; border-color: #020202; }}
        .filter-btn.good-filter.active {{ background: #0F3D4C; border-color: #0F3D4C; color: #14E7E8; }}
        .filter-btn.warning-filter.active {{ background: #475FF2; border-color: #475FF2; color: white; }}
        .filter-btn.bad-filter.active {{ background: #152271; border-color: #152271; color: #D6D6FF; }}
        .filter-btn.history-filter.active {{ background: #7C8CEF; border-color: #7C8CEF; color: white; }}

        .legend {{
            background: white;
            border-radius: 10px;
            padding: 14px 20px;
            box-shadow: 0 2px 8px rgba(2,2,2,0.06);
            margin-bottom: 20px;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            align-items: center;
            border: 1px solid #F0EEE9;
        }}

        .legend-title {{ font-size: 11px; font-weight: 700; color: #020202; text-transform: uppercase; letter-spacing: 0.8px; }}
        .legend-item {{ display: flex; align-items: center; gap: 8px; font-size: 11px; color: #676767; }}
        .legend-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
        .legend-dot.good {{ background: #14E7E8; }}
        .legend-dot.warning {{ background: #475FF2; }}
        .legend-dot.bad {{ background: #152271; }}

        .no-results {{ text-align: center; padding: 60px 20px; color: #9A9A9A; font-size: 15px; display: none; }}
        .no-results-icon {{ font-size: 48px; margin-bottom: 12px; }}

        .articles-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 16px;
            margin-bottom: 40px;
        }}

        .article-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(2,2,2,0.06);
            border-left: 4px solid #ECEAE4;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            opacity: 0;
            animation: fadeInUp 0.4s ease forwards;
            border-top: 1px solid #F0EEE9;
            border-right: 1px solid #F0EEE9;
            border-bottom: 1px solid #F0EEE9;
        }}

        .article-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(2,2,2,0.1);
        }}

        .article-card.good {{ border-left-color: #14E7E8; }}
        .article-card.warning {{ border-left-color: #475FF2; }}
        .article-card.bad {{ border-left-color: #152271; }}

        .history-card {{
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(2,2,2,0.06);
            border-left: 4px solid #ECEAE4;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            opacity: 0;
            animation: fadeInUp 0.4s ease forwards;
            display: none;
            border-top: 1px solid #F0EEE9;
            border-right: 1px solid #F0EEE9;
            border-bottom: 1px solid #F0EEE9;
        }}

        .history-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(2,2,2,0.1);
        }}

        .history-card.good {{ border-left-color: #14E7E8; }}
        .history-card.warning {{ border-left-color: #475FF2; }}
        .history-card.bad {{ border-left-color: #152271; }}
        .history-card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }}

        .trend-badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 700;
            margin: 8px 0 12px;
        }}

        .trend-good {{ background: #D6FFFF; color: #0F3D4C; }}
        .trend-bad {{ background: #D6D6FF; color: #152271; }}
        .trend-neutral {{ background: #ECEAE4; color: #676767; }}

        .history-entries {{ margin-top: 8px; }}

        .history-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 7px 0;
            border-bottom: 1px solid #F0EEE9;
            font-size: 12px;
        }}

        .history-row:last-child {{ border-bottom: none; }}
        .history-date {{ color: #9A9A9A; }}
        .history-score {{ font-weight: 800; font-size: 13px; }}
        .history-score.good {{ color: #0F3D4C; }}
        .history-score.warning {{ color: #475FF2; }}
        .history-score.bad {{ color: #152271; }}

        .history-label {{
            background: #020202;
            color: #14E7E8;
            font-size: 9px;
            padding: 2px 7px;
            border-radius: 10px;
            font-weight: 700;
            text-transform: uppercase;
        }}

        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(16px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }}

        .article-title {{
            font-size: 13px;
            font-weight: 700;
            color: #020202;
            flex: 1;
            margin-right: 12px;
            line-height: 1.4;
        }}

        .score-badge {{ font-size: 24px; font-weight: 900; line-height: 1; }}
        .score-badge.good {{ color: #0F3D4C; }}
        .score-badge.warning {{ color: #475FF2; }}
        .score-badge.bad {{ color: #152271; }}

        .progress-bar-wrap {{
            height: 3px;
            background: #ECEAE4;
            border-radius: 2px;
            margin: 8px 0 10px;
            overflow: hidden;
        }}

        .progress-bar {{ height: 100%; border-radius: 2px; }}
        .progress-bar.good {{ background: linear-gradient(90deg, #14E7E8, #46C4C3); }}
        .progress-bar.warning {{ background: linear-gradient(90deg, #7C8CEF, #475FF2); }}
        .progress-bar.bad {{ background: linear-gradient(90deg, #475FF2, #152271); }}

        .reading-level {{
            font-size: 10px;
            color: #9A9A9A;
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
        }}

        .status-pill {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 10px;
            font-weight: 700;
            margin-bottom: 8px;
            letter-spacing: 0.3px;
        }}

        .status-pill.good {{ background: #D6FFFF; color: #0F3D4C; }}
        .status-pill.warning {{ background: #D6D6FF; color: #475FF2; }}
        .status-pill.bad {{ background: #D6D6FF; color: #152271; }}

        .summary-text {{
            font-size: 11px;
            color: #676767;
            margin-bottom: 8px;
            line-height: 1.6;
        }}

        .card-meta {{
            font-size: 10px;
            color: #B3B3B3;
            border-top: 1px solid #F0EEE9;
            padding-top: 8px;
            margin-top: 4px;
            margin-bottom: 8px;
        }}

        .rec-toggle {{
            width: 100%;
            padding: 8px 12px;
            background: #F4F2EF;
            border: 1px solid #ECEAE4;
            border-radius: 6px;
            font-size: 11px;
            cursor: pointer;
            text-align: left;
            color: #020202;
            font-weight: 600;
            transition: all 0.2s;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'DM Sans', sans-serif;
        }}

        .rec-toggle:hover {{ background: #ECEAE4; }}

        .wcag-toggle {{
            background: #F0F9FF;
            border-color: #D6FFFF;
            margin-top: 5px;
            color: #0F3D4C;
        }}

        .wcag-toggle:hover {{ background: #D6FFFF; }}

        .recommendations {{
            margin-top: 6px;
            padding: 0 12px;
            background: #F4F2EF;
            border-radius: 6px;
            border-left: 3px solid #020202;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease, padding 0.3s ease;
        }}

        .recommendations.open {{ max-height: 2000px; padding: 12px; }}
        .wcag-rec {{ background: #F0F9FF; border-left-color: #14E7E8; }}

        .rec-section-title {{
            font-size: 9px;
            font-weight: 800;
            color: #9A9A9A;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }}

        .recommendations p {{
            font-size: 11px;
            color: #353535;
            margin-bottom: 7px;
            line-height: 1.7;
        }}

        .recommendations p:last-child {{ margin-bottom: 0; }}

        .analyse-section {{
            background: white;
            border-radius: 10px;
            padding: 24px;
            box-shadow: 0 2px 8px rgba(2,2,2,0.06);
            margin-bottom: 24px;
            border: 1px solid #F0EEE9;
        }}

        .analyse-section h2 {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 4px;
            color: #020202;
        }}

        .analyse-section p {{
            font-size: 12px;
            color: #9A9A9A;
            margin-bottom: 16px;
            line-height: 1.6;
        }}

        .sheets-link {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background: #020202;
            color: #14E7E8;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.2s;
            margin-top: 4px;
            font-family: 'DM Sans', sans-serif;
        }}

        .sheets-link:hover {{
            background: #0F3D4C;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(2,2,2,0.2);
        }}

        .sheets-info {{
            background: #F4F2EF;
            border-radius: 8px;
            padding: 14px 18px;
            border-left: 3px solid #14E7E8;
            font-size: 12px;
            color: #353535;
            line-height: 1.8;
            margin-top: 14px;
        }}

        .history-intro {{
            background: white;
            border-radius: 10px;
            padding: 14px 20px;
            box-shadow: 0 2px 8px rgba(2,2,2,0.06);
            margin-bottom: 20px;
            font-size: 12px;
            color: #676767;
            display: none;
            border-left: 3px solid #7C8CEF;
            border-top: 1px solid #F0EEE9;
            border-right: 1px solid #F0EEE9;
            border-bottom: 1px solid #F0EEE9;
        }}

        .datavant-badge {{
            display: inline-block;
            background: #020202;
            color: #14E7E8;
            font-size: 9px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 10px;
            margin-left: 6px;
            letter-spacing: 0.5px;
        }}

        footer {{
            text-align: center;
            padding: 20px;
            font-size: 11px;
            color: #9A9A9A;
            border-top: 1px solid #D9D7D1;
            background: white;
        }}

        .hidden {{ display: none !important; }}
    </style>
</head>
<body>

<header>
    <div>
        <h1>Datavant <span>Readability</span> Tool</h1>
        <p>Technical Writing Team · Powered by Python textstat and Claude AI</p>
    </div>
    <div class="target-badge">🎯 Target: Grade 12 or below</div>
</header>

<div class="stats-bar">
    <div class="stat">
        <div class="stat-number">{total}</div>
        <div class="stat-label">Total Articles</div>
    </div>
    <div class="stat">
        <div class="stat-number good">{good_count}</div>
        <div class="stat-label">Meets Target</div>
    </div>
    <div class="stat">
        <div class="stat-number warning">{warning_count}</div>
        <div class="stat-label">Needs Improvement</div>
    </div>
    <div class="stat">
        <div class="stat-number bad">{bad_count}</div>
        <div class="stat-label">Needs Significant Work</div>
    </div>
    <div class="stat">
        <div class="stat-number">{avg_score}</div>
        <div class="stat-label">Average Score</div>
    </div>
</div>

<div class="main">

    <div class="analyse-section">
        <h2>Analyse a New Article</h2>
        <p>
            Paste a Zendesk article URL into the Google Sheet to queue it for analysis.
            The tool runs automatically and updates this dashboard within 4 hours.
        </p>
        <a class="sheets-link" href="https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}" target="_blank">
            📊 Open FK Articles Google Sheet
        </a>
        <div class="sheets-info">
            <strong>How to add a new article:</strong><br>
            1. Open the article in Zendesk and copy the URL<br>
            2. Click the button above to open the Google Sheet<br>
            3. Paste the URL in column A of a new row<br>
            4. Leave column C blank — the analysis runs automatically
        </div>
    </div>

    <div class="section-title">All Article Results</div>
    <div class="last-updated">Last updated: {today}</div>

    <div class="controls-bar" id="controls-bar">
        <div class="search-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="searchInput" placeholder="Search articles..." oninput="handleSearch()" />
            <span class="search-count" id="searchCount"></span>
        </div>
        <div class="sort-wrap">
            <button class="sort-btn active" onclick="sortCards('score-high', this)">Score ↓</button>
            <button class="sort-btn" onclick="sortCards('score-low', this)">Score ↑</button>
            <button class="sort-btn" onclick="sortCards('date-new', this)">Newest</button>
            <button class="sort-btn" onclick="sortCards('date-old', this)">Oldest</button>
            <button class="sort-btn" onclick="sortCards('alpha', this)">A → Z</button>
        </div>
    </div>

    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterCards('all', this)">All Articles ({total})</button>
        <button class="filter-btn good-filter" onclick="filterCards('good', this)">✅ Meets Target ({good_count})</button>
        <button class="filter-btn warning-filter" onclick="filterCards('warning', this)">⚠️ Needs Improvement ({warning_count})</button>
        <button class="filter-btn bad-filter" onclick="filterCards('bad', this)">🔴 Needs Significant Work ({bad_count})</button>
        <button class="filter-btn history-filter" onclick="filterCards('history', this)">📈 Score History</button>
    </div>

    <div class="legend" id="legend-bar">
        <span class="legend-title">Score Guide:</span>
        <div class="legend-item"><div class="legend-dot good"></div><span>12.0 or below = Meets Target</span></div>
        <div class="legend-item"><div class="legend-dot warning"></div><span>12.1 to 14.9 = Needs Improvement</span></div>
        <div class="legend-item"><div class="legend-dot bad"></div><span>15.0 and above = Needs Significant Work</span></div>
        <div class="legend-item"><span class="datavant-badge">Python</span><span>Consistent mathematical scores</span></div>
    </div>

    <div class="history-intro" id="history-intro">
        📈 <strong>Score History</strong> shows how each article has changed over time.
        Because scores are calculated by Python textstat, any change here reflects
        a genuine article rewrite — not AI variation.
    </div>

    <div class="no-results" id="no-results">
        <div class="no-results-icon">🔍</div>
        <div>No articles found matching your search</div>
    </div>

    <div class="articles-grid" id="articles-grid">
        {cards_html}
    </div>

    <div class="articles-grid" id="history-grid" style="display:none">
        {history_cards_html}
    </div>

</div>

<footer>
    Datavant Readability Tool · Technical Writing Team · Built by Cian Gallagher
</footer>

<script>
let currentFilter = 'all';
let currentSort = 'score-high';
let currentSearch = '';

function toggleSection(id, btn) {{
    const section = document.getElementById(id);
    const arrow = btn.querySelector('span:last-child');
    if (section.classList.contains('open')) {{
        section.classList.remove('open');
        arrow.textContent = '▼';
    }} else {{
        section.classList.add('open');
        arrow.textContent = '▲';
    }}
}}

function handleSearch() {{
    currentSearch = document.getElementById('searchInput').value.toLowerCase();
    applyFiltersAndSort();
}}

function filterCards(status, btn) {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = status;

    const articlesGrid = document.getElementById('articles-grid');
    const historyGrid = document.getElementById('history-grid');
    const legendBar = document.getElementById('legend-bar');
    const historyIntro = document.getElementById('history-intro');
    const controlsBar = document.getElementById('controls-bar');
    const noResults = document.getElementById('no-results');

    if (status === 'history') {{
        articlesGrid.style.display = 'none';
        historyGrid.style.display = 'grid';
        legendBar.style.display = 'none';
        historyIntro.style.display = 'block';
        controlsBar.style.display = 'none';
        noResults.style.display = 'none';
        document.querySelectorAll('.history-card').forEach(card => {{
            card.style.display = 'block';
        }});
    }} else {{
        articlesGrid.style.display = 'grid';
        historyGrid.style.display = 'none';
        legendBar.style.display = 'flex';
        historyIntro.style.display = 'none';
        controlsBar.style.display = 'flex';
        applyFiltersAndSort();
    }}
}}

function sortCards(sortType, btn) {{
    document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentSort = sortType;
    applyFiltersAndSort();
}}

function applyFiltersAndSort() {{
    const grid = document.getElementById('articles-grid');
    const cards = Array.from(grid.querySelectorAll('.article-card'));
    const noResults = document.getElementById('no-results');

    let visibleCount = 0;

    cards.forEach(card => {{
        const matchesFilter = currentFilter === 'all' || card.dataset.status === currentFilter;
        const matchesSearch = currentSearch === '' || card.dataset.title.includes(currentSearch);

        if (matchesFilter && matchesSearch) {{
            card.classList.remove('hidden');
            visibleCount++;
        }} else {{
            card.classList.add('hidden');
        }}
    }});

    const searchCount = document.getElementById('searchCount');
    if (currentSearch) {{
        searchCount.textContent = visibleCount + ' found';
    }} else {{
        searchCount.textContent = '';
    }}

    if (visibleCount === 0) {{
        noResults.style.display = 'block';
        grid.style.display = 'none';
    }} else {{
        noResults.style.display = 'none';
        grid.style.display = 'grid';
    }}

    const visibleCards = cards.filter(c => !c.classList.contains('hidden'));

    visibleCards.sort((a, b) => {{
        if (currentSort === 'score-high') {{
            return parseFloat(b.dataset.score) - parseFloat(a.dataset.score);
        }} else if (currentSort === 'score-low') {{
            return parseFloat(a.dataset.score) - parseFloat(b.dataset.score);
        }} else if (currentSort === 'date-new') {{
            return b.dataset.date.localeCompare(a.dataset.date);
        }} else if (currentSort === 'date-old') {{
            return a.dataset.date.localeCompare(b.dataset.date);
        }} else if (currentSort === 'alpha') {{
            return a.dataset.title.localeCompare(b.dataset.title);
        }}
        return 0;
    }});

    visibleCards.forEach(card => grid.appendChild(card));
}}
</script>

</body>
</html>"""

    with open('index.html', 'w') as f:
        f.write(html)
    print("Dashboard updated successfully")


def push_to_github(article_title):
    print("\nPushing to GitHub...")
    try:
        import subprocess
        subprocess.run(
            ['git', 'config', '--global', 'user.email', 'action@github.com'],
            check=True
        )
        subprocess.run(
            ['git', 'config', '--global', 'user.name', 'GitHub Action'],
            check=True
        )
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(
            ['git', 'commit', '-m',
             f'FK analysis: {article_title} - {datetime.now().strftime("%d %b %Y")}'],
            check=True
        )
        subprocess.run(['git', 'push'], check=True)
        print("Successfully pushed to GitHub")
        print("Dashboard will update in about 2 minutes")
    except Exception as e:
        print(f"Could not auto push: {e}")
        print("Please push manually using GitHub Desktop")


def run_sheets_mode():
    print("========================================")
    print("  Datavant Readability Tool")
    print("  Running in Google Sheets mode")
    print("========================================")

    worksheet = get_google_sheet()
    if not worksheet:
        print("Could not connect to Google Sheets")
        return

    pending = get_pending_articles(worksheet)

    if not pending:
        print("No pending articles found in Google Sheet")
        print("Rebuilding dashboard with existing results...")
        all_results = read_all_results()
        build_dashboard(all_results)
        push_to_github("scheduled update")
        return

    print(f"\nProcessing {len(pending)} pending articles...")

    for item in pending:
        article_id = item['article_id']
        row = item['row']

        print(f"\nProcessing article ID: {article_id}")

        title, content = get_zendesk_article(article_id)
        if not title:
            print(f"Could not fetch article {article_id}")
            continue

        clean_text = clean_text_for_fk(content)
        fk_data = calculate_fk_score(clean_text)

        if not fk_data:
            print(f"Not enough content in article {article_id}")
            continue

        result = analyse_with_claude(title, clean_text, fk_data)
        save_result(title, result, fk_data)
        update_sheet_status(worksheet, row, title, fk_data['score'])

        print(f"Completed: {title} - Score: {fk_data['score']}")

    print("\nAll pending articles processed")
    print("Rebuilding dashboard...")
    all_results = read_all_results()
    build_dashboard(all_results)
    push_to_github("Google Sheets batch analysis")
    print("\nDone! Dashboard updated.")


def main():
    print("========================================")
    print("  Datavant Readability Tool")
    print("  Technical Writing Team")
    print("  Scores: Python textstat library")
    print("  Recommendations: Claude AI")
    print("========================================")

    article_id = input("\nEnter the Zendesk article ID or URL: ").strip()

    extracted_id, name_hint = extract_id_from_input(article_id)

    if not extracted_id:
        print("Error: Please enter a valid article ID or Zendesk URL")
        return

    title, content = get_zendesk_article(extracted_id)
    if not title:
        return

    print("\nPre-processing text for FK calculation...")
    clean_text = clean_text_for_fk(content)

    print("\nCalculating FK score with Python textstat...")
    fk_data = calculate_fk_score(clean_text)

    if not fk_data:
        print("Not enough eligible prose content to calculate FK score")
        return

    result = analyse_with_claude(title, clean_text, fk_data)
    filename = save_result(title, result, fk_data)
    all_results = read_all_results()
    build_dashboard(all_results)
    push_to_github(title)

    print("\n========================================")
    print("  ANALYSIS COMPLETE")
    print(f"  FK Score: {fk_data['score']} (Python textstat)")
    print("========================================")
    print(result)
    print(f"\nResult saved to: {filename}")
    print("\nDashboard updated and pushed to GitHub automatically")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--sheets':
        run_sheets_mode()
    else:
        main()