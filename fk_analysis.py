# ============================================
# FK Readability Analysis Tool
# Built by Cian Gallagher - Datavant
# Architecture: Hybrid Python + Claude
# Python handles FK calculation precisely
# Claude handles recommendations and WCAG
# Google Sheets handles article ID queue
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
   (headings, lists, code blocks and images have already been removed)
2. A pre-calculated Flesch-Kincaid Grade Level score
   calculated by Python using the textstat library

Your job is to:
1. Accept the pre-calculated FK score as the official score
   Do not recalculate it yourself
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
[If Grade 12 or below: confirm content meets target and say well done]
[If above Grade 12: give 3 very specific suggestions with actual
examples from the article text provided]

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


def get_google_sheet():
    """
    Connects to Google Sheets using service account credentials
    Returns the worksheet object
    """
    print("\nConnecting to Google Sheets...")
    try:
        creds_json = GOOGLE_SHEETS_CREDENTIALS
        if not creds_json:
            print("No Google Sheets credentials found")
            return None

        creds_dict = json.loads(creds_json)
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets'
        ]
        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=scopes
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
    """
    Reads the Google Sheet and returns articles
    that have not been analysed yet
    Column A = Article ID
    Column B = Article Name
    Column C = Status (blank = pending, Done = complete)
    """
    print("\nChecking for pending articles in Google Sheet...")
    try:
        all_rows = worksheet.get_all_values()
        pending = []

        for i, row in enumerate(all_rows):
            if i == 0:
                continue

            if not row or not row[0]:
                continue

            article_id = row[0].strip()
            article_name = row[1].strip() if len(row) > 1 else ''
            status = row[2].strip() if len(row) > 2 else ''

            if not article_id.isdigit():
                continue

            if status.lower() != 'done':
                pending.append({
                    'row': i + 1,
                    'article_id': article_id,
                    'article_name': article_name
                })

        print(f"Found {len(pending)} pending articles")
        return pending
    except Exception as e:
        print(f"Error reading sheet: {e}")
        return []


def update_sheet_status(worksheet, row_number, article_name, score):
    """
    Updates the Google Sheet after analysis is complete
    Sets status to Done and adds the date and score
    """
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
        entries.sort(key=lambda x: x['date'])
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
        delay = round(0.1 + (i * 0.1), 1)

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
        <div class="article-card {status}" data-status="{status}" style="animation-delay:{delay}s">
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
    <title>FK Readability Dashboard - Datavant</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f0f2f5; color: #333; }}
        header {{ background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); color: white; padding: 24px 40px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }}
        header h1 {{ font-size: 24px; font-weight: 700; letter-spacing: -0.5px; }}
        header p {{ font-size: 13px; opacity: 0.6; margin-top: 4px; }}
        .target-badge {{ background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); padding: 8px 18px; border-radius: 20px; font-size: 13px; backdrop-filter: blur(10px); }}
        .stats-bar {{ background: white; padding: 24px 40px; display: flex; gap: 0; border-bottom: 1px solid #e8ecf0; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .stat {{ text-align: center; flex: 1; padding: 8px 0; border-right: 1px solid #f0f0f0; transition: transform 0.2s; }}
        .stat:last-child {{ border-right: none; }}
        .stat:hover {{ transform: translateY(-2px); }}
        .stat-number {{ font-size: 32px; font-weight: 800; color: #1a1a2e; line-height: 1; }}
        .stat-label {{ font-size: 11px; color: #999; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .stat-number.good {{ color: #27ae60; }}
        .stat-number.warning {{ color: #f39c12; }}
        .stat-number.bad {{ color: #e74c3c; }}
        .main {{ padding: 30px 40px; }}
        .section-title {{ font-size: 18px; font-weight: 700; margin-bottom: 8px; color: #1a1a2e; }}
        .last-updated {{ font-size: 11px; color: #aaa; margin-bottom: 20px; }}
        .filter-bar {{ display: flex; gap: 8px; margin-bottom: 24px; flex-wrap: wrap; }}
        .filter-btn {{ padding: 8px 18px; border-radius: 20px; border: 2px solid #e0e0e0; background: white; font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.2s; color: #666; }}
        .filter-btn:hover {{ border-color: #1a1a2e; color: #1a1a2e; }}
        .filter-btn.active {{ background: #1a1a2e; color: white; border-color: #1a1a2e; }}
        .filter-btn.good-filter.active {{ background: #27ae60; border-color: #27ae60; }}
        .filter-btn.warning-filter.active {{ background: #f39c12; border-color: #f39c12; }}
        .filter-btn.bad-filter.active {{ background: #e74c3c; border-color: #e74c3c; }}
        .filter-btn.history-filter.active {{ background: #8e44ad; border-color: #8e44ad; }}
        .legend {{ background: white; border-radius: 12px; padding: 16px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 24px; display: flex; gap: 24px; flex-wrap: wrap; align-items: center; }}
        .legend-title {{ font-size: 12px; font-weight: 700; color: #1a1a2e; text-transform: uppercase; letter-spacing: 0.5px; }}
        .legend-item {{ display: flex; align-items: center; gap: 8px; font-size: 12px; color: #555; }}
        .legend-dot {{ width: 10px; height: 10px; border-radius: 50%; }}
        .legend-dot.good {{ background: #27ae60; }}
        .legend-dot.warning {{ background: #f39c12; }}
        .legend-dot.bad {{ background: #e74c3c; }}
        .articles-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 20px; margin-bottom: 40px; }}
        .article-card {{ background: white; border-radius: 14px; padding: 22px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-left: 5px solid #ccc; transition: transform 0.25s ease, box-shadow 0.25s ease; opacity: 0; animation: fadeInUp 0.5s ease forwards; }}
        .article-card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 30px rgba(0,0,0,0.12); }}
        .article-card.good {{ border-left-color: #27ae60; }}
        .article-card.warning {{ border-left-color: #f39c12; }}
        .article-card.bad {{ border-left-color: #e74c3c; }}
        .history-card {{ background: white; border-radius: 14px; padding: 22px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); border-left: 5px solid #ccc; transition: transform 0.25s ease, box-shadow 0.25s ease; opacity: 0; animation: fadeInUp 0.5s ease forwards; display: none; }}
        .history-card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 30px rgba(0,0,0,0.12); }}
        .history-card.good {{ border-left-color: #27ae60; }}
        .history-card.warning {{ border-left-color: #f39c12; }}
        .history-card.bad {{ border-left-color: #e74c3c; }}
        .history-card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }}
        .trend-badge {{ display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 700; margin: 8px 0 12px; }}
        .trend-good {{ background: #eafaf1; color: #27ae60; }}
        .trend-bad {{ background: #fdf0ed; color: #e74c3c; }}
        .trend-neutral {{ background: #f8f9fa; color: #999; }}
        .history-entries {{ margin-top: 8px; }}
        .history-row {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #f5f5f5; font-size: 12px; }}
        .history-row:last-child {{ border-bottom: none; }}
        .history-date {{ color: #999; }}
        .history-score {{ font-weight: 800; font-size: 14px; }}
        .history-score.good {{ color: #27ae60; }}
        .history-score.warning {{ color: #f39c12; }}
        .history-score.bad {{ color: #e74c3c; }}
        .history-label {{ background: #1a1a2e; color: white; font-size: 9px; padding: 2px 6px; border-radius: 10px; font-weight: 700; text-transform: uppercase; }}
        @keyframes fadeInUp {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }}
        .article-title {{ font-size: 14px; font-weight: 700; color: #1a1a2e; flex: 1; margin-right: 12px; line-height: 1.4; }}
        .score-badge {{ font-size: 26px; font-weight: 900; line-height: 1; }}
        .score-badge.good {{ color: #27ae60; }}
        .score-badge.warning {{ color: #f39c12; }}
        .score-badge.bad {{ color: #e74c3c; }}
        .progress-bar-wrap {{ height: 4px; background: #f0f0f0; border-radius: 2px; margin: 8px 0 10px; overflow: hidden; }}
        .progress-bar {{ height: 100%; border-radius: 2px; transition: width 1s ease; }}
        .progress-bar.good {{ background: #27ae60; }}
        .progress-bar.warning {{ background: #f39c12; }}
        .progress-bar.bad {{ background: #e74c3c; }}
        .reading-level {{ font-size: 11px; color: #999; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.3px; }}
        .status-pill {{ display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; margin-bottom: 10px; letter-spacing: 0.3px; }}
        .status-pill.good {{ background: #eafaf1; color: #27ae60; }}
        .status-pill.warning {{ background: #fef9e7; color: #f39c12; }}
        .status-pill.bad {{ background: #fdf0ed; color: #e74c3c; }}
        .summary-text {{ font-size: 12px; color: #666; margin-bottom: 10px; line-height: 1.6; }}
        .card-meta {{ font-size: 11px; color: #bbb; border-top: 1px solid #f5f5f5; padding-top: 10px; margin-top: 4px; margin-bottom: 10px; }}
        .rec-toggle {{ width: 100%; padding: 9px 12px; background: #f8f9fa; border: 1px solid #eee; border-radius: 8px; font-size: 12px; cursor: pointer; text-align: left; color: #1a1a2e; font-weight: 600; transition: all 0.2s; display: flex; justify-content: space-between; align-items: center; }}
        .rec-toggle:hover {{ background: #e9ecef; border-color: #ddd; }}
        .wcag-toggle {{ background: #f0f7ff; border-color: #daeaf8; margin-top: 6px; }}
        .wcag-toggle:hover {{ background: #ddeeff; }}
        .recommendations {{ margin-top: 8px; padding: 0 14px; background: #f9f9f9; border-radius: 8px; border-left: 3px solid #1a1a2e; max-height: 0; overflow: hidden; transition: max-height 0.4s ease, padding 0.3s ease; }}
        .recommendations.open {{ max-height: 2000px; padding: 14px; }}
        .wcag-rec {{ background: #f0f7ff; border-left-color: #3498db; }}
        .rec-section-title {{ font-size: 10px; font-weight: 800; color: #aaa; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }}
        .recommendations p {{ font-size: 12px; color: #444; margin-bottom: 8px; line-height: 1.7; }}
        .recommendations p:last-child {{ margin-bottom: 0; }}
        .analyse-section {{ background: white; border-radius: 14px; padding: 30px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); margin-bottom: 30px; }}
        .analyse-section h2 {{ font-size: 18px; font-weight: 700; margin-bottom: 6px; color: #1a1a2e; }}
        .analyse-section p {{ font-size: 13px; color: #999; margin-bottom: 18px; line-height: 1.6; }}
        .sheets-link {{ display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; background: #27ae60; color: white; border-radius: 10px; font-size: 14px; font-weight: 700; text-decoration: none; transition: all 0.2s; margin-top: 4px; }}
        .sheets-link:hover {{ background: #219a52; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(39,174,96,0.4); }}
        .sheets-info {{ background: #f0fff4; border-radius: 10px; padding: 16px 20px; border-left: 4px solid #27ae60; font-size: 13px; color: #333; line-height: 1.8; margin-top: 16px; }}
        .history-intro {{ background: white; border-radius: 12px; padding: 16px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 24px; font-size: 13px; color: #666; display: none; border-left: 4px solid #8e44ad; }}
        .python-badge {{ display: inline-block; background: #f0f7ff; color: #3498db; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 6px; border: 1px solid #daeaf8; }}
        footer {{ text-align: center; padding: 24px; font-size: 12px; color: #bbb; border-top: 1px solid #eee; background: white; }}
        .hidden {{ display: none !important; }}
    </style>
</head>
<body>

<header>
    <div>
        <h1>FK Readability Dashboard</h1>
        <p>Datavant Technical Writing Team</p>
    </div>
    <div class="target-badge">🎯 Target: Grade 12 or below</div>
</header>

<div class="stats-bar">
    <div class="stat">
        <div class="stat-number">{total}</div>
        <div class="stat-label">Total Tested</div>
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
            To analyse a new article simply add the Zendesk article ID
            to the FK Articles Google Sheet and it will be analysed
            automatically within the next scheduled run.
        </p>
        <a class="sheets-link" href="https://docs.google.com/spreadsheets/d/{GOOGLE_SHEET_ID}" target="_blank">
            📊 Open FK Articles Google Sheet
        </a>
        <div class="sheets-info">
            <strong>How to add a new article:</strong><br>
            1. Click the button above to open the Google Sheet<br>
            2. Add the article ID in column A<br>
            3. Add the article name in column B<br>
            4. Leave column C blank<br>
            5. The analysis will run automatically and update this dashboard
        </div>
    </div>

    <div class="section-title">All Article Results</div>
    <div class="last-updated">Last updated: {today}</div>

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
        <div class="legend-item"><span class="python-badge">Python</span><span>Scores calculated by textstat library</span></div>
    </div>

    <div class="history-intro" id="history-intro">
        📈 <strong>Score History</strong> shows how each article has changed over time.
        Scores are calculated by the Python textstat library so changes here
        reflect genuine article rewrites not AI variation.
    </div>

    <div class="articles-grid" id="articles-grid">
        {cards_html}
    </div>

    <div class="articles-grid" id="history-grid" style="display:none">
        {history_cards_html}
    </div>

</div>

<footer>
    FK Readability Dashboard · Datavant Technical Writing Team · Built by Cian Gallagher
</footer>

<script>
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

function filterCards(status, btn) {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const articlesGrid = document.getElementById('articles-grid');
    const historyGrid = document.getElementById('history-grid');
    const legendBar = document.getElementById('legend-bar');
    const historyIntro = document.getElementById('history-intro');
    if (status === 'history') {{
        articlesGrid.style.display = 'none';
        historyGrid.style.display = 'grid';
        legendBar.style.display = 'none';
        historyIntro.style.display = 'block';
        document.querySelectorAll('.history-card').forEach(card => {{
            card.style.display = 'block';
        }});
    }} else {{
        articlesGrid.style.display = 'grid';
        historyGrid.style.display = 'none';
        legendBar.style.display = 'flex';
        historyIntro.style.display = 'none';
        document.querySelectorAll('.article-card').forEach(card => {{
            if (status === 'all' || card.dataset.status === status) {{
                card.classList.remove('hidden');
            }} else {{
                card.classList.add('hidden');
            }}
        }});
    }}
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
        subprocess.run(['git', 'config', '--global',
            'user.email', 'action@github.com'], check=True)
        subprocess.run(['git', 'config', '--global',
            'user.name', 'GitHub Action'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m',
            f'FK analysis: {article_title} - {datetime.now().strftime("%d %b %Y")}'],
            check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Successfully pushed to GitHub")
        print("Dashboard will update in about 2 minutes")
    except Exception as e:
        print(f"Could not auto push: {e}")
        print("Please push manually using GitHub Desktop")
            f'FK analysis: {article_title} - {datetime.now().strftime("%d %b %Y")}'],
            check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Successfully pushed to GitHub")
        print("Dashboard will update in about 2 minutes")
    except Exception as e:
        print(f"Could not auto push: {e}")
        print("Please push manually using GitHub Desktop")


def run_sheets_mode():
    """
    Runs in Google Sheets mode
    Reads pending articles from the sheet
    Analyses each one automatically
    Updates the sheet when done
    """
    print("========================================")
    print("  FK Readability Analysis Tool")
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
    print("  FK Readability Analysis Tool")
    print("  Datavant Technical Writing Team")
    print("  Scores: Python textstat library")
    print("  Recommendations: Claude AI")
    print("========================================")

    article_id = input("\nEnter the Zendesk article ID: ").strip()

    if not article_id.isdigit():
        print("Error: Please enter a valid article ID number")
        return

    title, content = get_zendesk_article(article_id)
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