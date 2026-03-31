# ============================================
# FK Readability Analysis Tool
# Built by Cian Gallagher - Datavant
# ============================================

import os
import re
import glob
import urllib3
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

FK_PROMPT = """
You are a technical writing assistant that performs
Flesch-Kincaid Grade Level (FKGL) readability assessments
and WCAG 2.2 writing accessibility checks
on Zendesk help content.

You help a technical writing team ensure their documentation
is clear, accessible and easy to understand.

## What is Flesch-Kincaid Grade Level
The Flesch-Kincaid Grade Level formula measures how easy or
hard text is to read. It looks at average sentence length and
average number of syllables per word. The result maps to a US
school grade level.

Reading level guide:
- Grade 1 to 6 = Elementary, very easy to read
- Grade 7 to 8 = Middle School, easy and ideal for most audiences
- Grade 9 to 10 = High School, moderate complexity
- Grade 11 to 12 = High School Advanced, becoming complex
- Grade 13 and above = College level, too complex for most audiences

Technical writing should ideally target Grade 12 or below.

The formula is:
(0.39 x average words per sentence) +
(11.8 x average syllables per word) - 15.59

## EXCLUSION CRITERIA
Remove all of the following before scoring:
- Titles, headings, and subheadings
- Bullet points and numbered lists
- Code blocks and programming syntax
- Images and media references
- URLs and web addresses
- Technical identifiers and CamelCase words
- Product and team names like Tokenization

## Sentence Eligibility Rule
Only include text that:
1. Appears in paragraph form
2. Contains complete grammatical sentences
3. Uses natural language syntax
4. Is intended for reader comprehension

## How to Present Results
Use this exact format every time:

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: [title]

SCORE: [number]
Reading Level: [level]
Target Audience: [description]

Summary: [one sentence explanation]

SCORE BREAKDOWN:
- Eligible sentences analysed: [number]
- Eligible words analysed: [number]
- Eligible syllables analysed: [number]
- Average words per sentence: [number]
- Average syllables per word: [number]
- Formula applied: [show the calculation]

CONTENT EXCLUDED FROM SCORING:
- Headings: [yes/no and count]
- Lists: [yes/no and count]
- Code blocks: [yes/no and count]
- Images: [yes/no and count]
- Product names noted: [list any found]

FK RECOMMENDATIONS:
[If Grade 12 or below: confirm content meets target]
[If above Grade 12: give 3 specific suggestions]

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: [Pass or flag with specific examples]
Sentence Length: [Pass or flag sentences over 25 words]
Jargon: [Pass or list unexplained terms found]
Active Voice: [Pass or flag passive constructions]
Heading Clarity: [Pass or suggestions]
Link Text: [Pass or flag vague link text]
Abbreviations: [Pass or list unexplained abbreviations]

Overall WCAG Writing Score: [Good / Needs Attention / Needs Significant Work]
---
"""


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


def analyse_with_claude(title, content):
    print(f"\nSending article to Claude for FK and WCAG analysis...")
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=3000,
        messages=[
            {
                "role": "user",
                "content": f"{FK_PROMPT}\n\nARTICLE TO ANALYSE:\n\nTitle: {title}\n\n{content}"
            }
        ]
    )
    result = message.content[0].text
    print("Analysis complete")
    return result


def save_result(title, result):
    print(f"\nSaving result...")
    clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    clean_title = clean_title.replace(' ', '-').lower()
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"results/{clean_title}-{timestamp}.md"
    with open(filename, 'w') as f:
        f.write(f"# FK Analysis Result\n\n")
        f.write(f"**Article:** {title}\n")
        f.write(f"**Date:** {datetime.now().strftime('%d %B %Y %H:%M')}\n\n")
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


def build_history_html(history, first_score, improvement, current_score):
    if not history:
        return ''

    trend_html = ''
    if improvement is not None:
        if improvement > 0:
            trend_html = f'<span class="trend-good">↓ Improved by {improvement} points</span>'
        elif improvement < 0:
            trend_html = f'<span class="trend-bad">↑ Declined by {abs(improvement)} points</span>'
        else:
            trend_html = f'<span class="trend-neutral">→ No change</span>'

    history_rows = ''
    all_entries = history + [{'date': 'Current', 'score': current_score}]
    for entry in reversed(history):
        h_status, _ = get_status(entry['score'])
        history_rows += f"""
        <div class="history-row">
            <span class="history-date">{entry['date']}</span>
            <span class="history-score {h_status}">{entry['score']}</span>
        </div>
        """

    return f"""
    <div class="progression-section">
        <div class="progression-header">
            📈 Score History {trend_html}
        </div>
        {history_rows}
    </div>
    """


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

        history_html = build_history_html(
            r.get('history', []),
            r.get('first_score'),
            r.get('improvement'),
            r['score']
        )

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
            {history_html}
            <div class="card-meta">Tested: {r['date']}</div>
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
        .progression-section {{ background: #f8f9fa; border-radius: 8px; padding: 12px; margin-bottom: 10px; border-left: 3px solid #6c757d; }}
        .progression-header {{ font-size: 12px; font-weight: 700; color: #555; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 4px; }}
        .trend-good {{ color: #27ae60; font-size: 11px; font-weight: 700; }}
        .trend-bad {{ color: #e74c3c; font-size: 11px; font-weight: 700; }}
        .trend-neutral {{ color: #999; font-size: 11px; font-weight: 700; }}
        .history-row {{ display: flex; justify-content: space-between; align-items: center; padding: 4px 0; border-bottom: 1px solid #eee; font-size: 11px; }}
        .history-row:last-child {{ border-bottom: none; }}
        .history-date {{ color: #999; }}
        .history-score {{ font-weight: 700; }}
        .history-score.good {{ color: #27ae60; }}
        .history-score.warning {{ color: #f39c12; }}
        .history-score.bad {{ color: #e74c3c; }}
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
        .analyse-section p {{ font-size: 13px; color: #999; margin-bottom: 18px; }}
        .input-row {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .input-row input {{ flex: 1; padding: 12px 18px; border: 2px solid #eee; border-radius: 10px; font-size: 14px; min-width: 200px; transition: border-color 0.2s; outline: none; }}
        .input-row input:focus {{ border-color: #1a1a2e; }}
        .input-row button {{ padding: 12px 28px; background: linear-gradient(135deg, #1a1a2e, #0f3460); color: white; border: none; border-radius: 10px; font-size: 14px; cursor: pointer; font-weight: 700; transition: all 0.2s; letter-spacing: 0.3px; }}
        .input-row button:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(15,52,96,0.4); }}
        .notice {{ margin-top: 16px; padding: 16px 20px; background: #f0f7ff; border-radius: 10px; border-left: 4px solid #3498db; font-size: 13px; color: #333; line-height: 1.8; }}
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
        <p>Enter a Zendesk article ID below and click Analyse Article to run a new FK and WCAG readability analysis</p>
        <div class="input-row">
            <input type="text" id="articleId" placeholder="Enter Zendesk Article ID e.g. 26609721445140" />
            <button onclick="analyseArticle()">Analyse Article →</button>
        </div>
        <div class="notice" id="instructions" style="display:none">
            <strong>GitHub Actions is opening in a new tab</strong><br><br>
            Your article ID has been copied to your clipboard. Follow these steps:<br><br>
            <ol style="margin-left:16px;margin-top:8px;">
                <li style="margin-bottom:6px;">In the new tab click the green <strong>Run workflow</strong> button</li>
                <li style="margin-bottom:6px;">Paste your article ID into the box</li>
                <li style="margin-bottom:6px;">Click the green <strong>Run workflow</strong> button</li>
                <li style="margin-bottom:6px;">Wait about 30 seconds for it to complete</li>
                <li style="margin-bottom:6px;">Come back to this page and refresh</li>
                <li style="margin-bottom:6px;">Your new score will appear automatically</li>
                <li style="margin-bottom:6px;color:#856404;"><strong>Note:</strong> The dashboard can take 2 to 3 minutes to update after the action completes. If you do not see your result yet simply refresh the page again.</li>
            </ol>
        </div>
    </div>

    <div class="section-title">All Article Results</div>
    <div class="last-updated">Last updated: {today}</div>

    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterCards('all', this)">All Articles</button>
        <button class="filter-btn good-filter" onclick="filterCards('good', this)">✅ Meets Target</button>
        <button class="filter-btn warning-filter" onclick="filterCards('warning', this)">⚠️ Needs Improvement</button>
        <button class="filter-btn bad-filter" onclick="filterCards('bad', this)">🔴 Needs Significant Work</button>
    </div>

    <div class="legend">
        <span class="legend-title">Score Guide:</span>
        <div class="legend-item"><div class="legend-dot good"></div><span>12.0 or below = Meets Target</span></div>
        <div class="legend-item"><div class="legend-dot warning"></div><span>12.1 to 14.9 = Needs Improvement</span></div>
        <div class="legend-item"><div class="legend-dot bad"></div><span>15.0 and above = Needs Significant Work</span></div>
    </div>

    <div class="articles-grid" id="articles-grid">
        {cards_html}
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
    document.querySelectorAll('.article-card').forEach(card => {{
        if (status === 'all' || card.dataset.status === status) {{
            card.classList.remove('hidden');
        }} else {{
            card.classList.add('hidden');
        }}
    }});
}}

function analyseArticle() {{
    const id = document.getElementById('articleId').value.trim();
    if (!id) {{
        alert('Please enter a Zendesk Article ID first');
        return;
    }}
    navigator.clipboard.writeText(id).then(function() {{
        document.getElementById('instructions').style.display = 'block';
        setTimeout(function() {{
            window.open(
                'https://github.com/ciangallagherdatavant/zendesk-fk-tool/actions/workflows/analyse.yml',
                '_blank'
            );
        }}, 1000);
    }}).catch(function() {{
        document.getElementById('instructions').style.display = 'block';
        setTimeout(function() {{
            window.open(
                'https://github.com/ciangallagherdatavant/zendesk-fk-tool/actions/workflows/analyse.yml',
                '_blank'
            );
        }}, 1000);
    }});
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


def main():
    print("========================================")
    print("  FK Readability Analysis Tool")
    print("  Datavant Technical Writing Team")
    print("========================================")

    article_id = input("\nEnter the Zendesk article ID: ").strip()

    if not article_id.isdigit():
        print("Error: Please enter a valid article ID number")
        return

    title, content = get_zendesk_article(article_id)
    if not title:
        return

    result = analyse_with_claude(title, content)
    filename = save_result(title, result)
    all_results = read_all_results()
    build_dashboard(all_results)
    push_to_github(title)

    print("\n========================================")
    print("  ANALYSIS COMPLETE")
    print("========================================")
    print(result)
    print(f"\nResult saved to: {filename}")
    print("\nDashboard updated and pushed to GitHub automatically")


if __name__ == "__main__":
    main()