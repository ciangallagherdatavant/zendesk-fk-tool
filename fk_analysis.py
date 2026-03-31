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
[If above Grade 12: give 3 specific suggestions to improve the score]

WCAG 2.2 WRITING ACCESSIBILITY NOTES:
Check the content against these WCAG 2.2 writing guidelines
and provide specific findings for each:

1. Plain Language (WCAG 3.1.5)
   Is the content written in plain language?
   Flag any unnecessarily complex words or phrases
   and suggest simpler alternatives

2. Sentence and Paragraph Length
   Are sentences under 20 words where possible?
   Are paragraphs focused on one idea?
   Flag any sentences exceeding 25 words

3. Jargon and Technical Terms (WCAG 3.1.3)
   Are technical terms explained on first use?
   List any unexplained jargon found

4. Active Voice
   Is the content written in active voice?
   Flag any passive voice constructions
   and suggest active alternatives

5. Heading and Structure Clarity
   Based on the content structure
   are headings clear and descriptive?
   Do they accurately describe the content below?

6. Link Text Quality (WCAG 2.4.6)
   Are any links described with vague text
   like click here or read more?
   Flag these and suggest descriptive alternatives

7. Abbreviations and Acronyms (WCAG 3.1.4)
   Are abbreviations and acronyms
   spelled out on first use?
   List any that are not explained

Format the WCAG section like this:

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
    seen_titles = {}
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
            content,
            re.DOTALL
        )
        fk_recommendations = fk_rec_match.group(1).strip() if fk_rec_match else ''
        fk_recommendations = re.sub(r'\*\*', '', fk_recommendations)
        wcag_match = re.search(
            r'WCAG 2\.2 WRITING ACCESSIBILITY NOTES:\s*\n(.*?)(?=---|$)',
            content,
            re.DOTALL
        )
        wcag_notes = wcag_match.group(1).strip() if wcag_match else ''
        wcag_notes = re.sub(r'\*\*', '', wcag_notes)
        if not fk_recommendations:
            rec_match = re.search(
                r'RECOMMENDATIONS:\s*\n(.*?)(?=---|$)',
                content,
                re.DOTALL
            )
            fk_recommendations = rec_match.group(1).strip() if rec_match else ''
            fk_recommendations = re.sub(r'\*\*', '', fk_recommendations)
        if title in seen_titles:
            existing_date = seen_titles[title]['date']
            if date > existing_date:
                seen_titles[title] = {
                    'title': title,
                    'date': date,
                    'score': score,
                    'level': level,
                    'summary': summary,
                    'fk_recommendations': fk_recommendations,
                    'wcag_notes': wcag_notes,
                    'filepath': filepath
                }
        else:
            seen_titles[title] = {
                'title': title,
                'date': date,
                'score': score,
                'level': level,
                'summary': summary,
                'fk_recommendations': fk_recommendations,
                'wcag_notes': wcag_notes,
                'filepath': filepath
            }
    results = list(seen_titles.values())
    results.sort(key=lambda x: x['score'], reverse=True)
    print(f"Found {len(results)} unique articles")
    return results


def get_status(score):
    if score <= 12.0:
        return 'good', '✅ Meets Target', '#27ae60'
    elif score <= 14.9:
        return 'warning', '⚠️ Needs Improvement', '#f39c12'
    else:
        return 'bad', '🔴 Needs Significant Work', '#e74c3c'


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
        status, status_text, status_colour = get_status(r['score'])

        fk_rec_lines = r['fk_recommendations'].split('\n')
        fk_rec_html = ""
        for line in fk_rec_lines:
            line = line.strip()
            if line:
                fk_rec_html += f"<p>{line}</p>"

        wcag_lines = r.get('wcag_notes', '').split('\n')
        wcag_html = ""
        for line in wcag_lines:
            line = line.strip()
            if line:
                wcag_html += f"<p>{line}</p>"

        cards_html += f"""
        <div class="article-card {status}">
            <div class="card-header">
                <div class="article-title">{r['title']}</div>
                <div class="score-badge {status}">{r['score']}</div>
            </div>
            <div class="reading-level">{r['level']}</div>
            <span class="status-pill {status}">{status_text}</span>
            <div class="summary-text">{r['summary']}</div>
            <div class="card-meta">Tested: {r['date']}</div>
            <button class="rec-toggle" onclick="toggleSection('fk-{i}', this)">
                📊 FK Recommendations ▼
            </button>
            <div class="recommendations" id="fk-{i}" style="display:none">
                <div class="rec-section-title">Flesch-Kincaid Recommendations</div>
                {fk_rec_html if fk_rec_html else '<p>No FK recommendations available for this article yet. Re-run the analysis to generate them.</p>'}
            </div>
            <button class="rec-toggle wcag-toggle" onclick="toggleSection('wcag-{i}', this)" style="margin-top:6px;">
                ♿ WCAG Accessibility Notes ▼
            </button>
            <div class="recommendations wcag-rec" id="wcag-{i}" style="display:none">
                <div class="rec-section-title">WCAG 2.2 Writing Accessibility</div>
                {wcag_html if wcag_html else '<p>No WCAG notes available for this article yet. Re-run the analysis to generate them.</p>'}
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
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f7fa; color: #333; }}
        header {{ background: #1a1a2e; color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }}
        header h1 {{ font-size: 22px; font-weight: 600; }}
        header p {{ font-size: 13px; opacity: 0.7; margin-top: 4px; }}
        .target-badge {{ background: #16213e; border: 1px solid #0f3460; padding: 8px 16px; border-radius: 20px; font-size: 13px; }}
        .stats-bar {{ background: white; padding: 20px 40px; display: flex; gap: 40px; border-bottom: 1px solid #e0e0e0; flex-wrap: wrap; }}
        .stat {{ text-align: center; }}
        .stat-number {{ font-size: 28px; font-weight: 700; color: #1a1a2e; }}
        .stat-label {{ font-size: 12px; color: #888; margin-top: 2px; }}
        .stat-number.good {{ color: #27ae60; }}
        .stat-number.warning {{ color: #f39c12; }}
        .stat-number.bad {{ color: #e74c3c; }}
        .main {{ padding: 30px 40px; }}
        .section-title {{ font-size: 16px; font-weight: 600; margin-bottom: 8px; color: #1a1a2e; }}
        .last-updated {{ font-size: 11px; color: #aaa; margin-bottom: 20px; }}
        .legend {{ background: white; border-radius: 10px; padding: 20px 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 24px; display: flex; gap: 24px; flex-wrap: wrap; align-items: center; }}
        .legend-title {{ font-size: 13px; font-weight: 600; color: #1a1a2e; margin-right: 8px; }}
        .legend-item {{ display: flex; align-items: center; gap: 8px; font-size: 12px; color: #555; }}
        .legend-dot {{ width: 12px; height: 12px; border-radius: 50%; }}
        .legend-dot.good {{ background: #27ae60; }}
        .legend-dot.warning {{ background: #f39c12; }}
        .legend-dot.bad {{ background: #e74c3c; }}
        .articles-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; margin-bottom: 40px; }}
        .article-card {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #ccc; }}
        .article-card.good {{ border-left-color: #27ae60; }}
        .article-card.warning {{ border-left-color: #f39c12; }}
        .article-card.bad {{ border-left-color: #e74c3c; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }}
        .article-title {{ font-size: 14px; font-weight: 600; color: #1a1a2e; flex: 1; margin-right: 10px; }}
        .score-badge {{ font-size: 22px; font-weight: 800; }}
        .score-badge.good {{ color: #27ae60; }}
        .score-badge.warning {{ color: #f39c12; }}
        .score-badge.bad {{ color: #e74c3c; }}
        .reading-level {{ font-size: 12px; color: #888; margin-bottom: 8px; }}
        .status-pill {{ display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; margin-bottom: 8px; }}
        .status-pill.good {{ background: #eafaf1; color: #27ae60; }}
        .status-pill.warning {{ background: #fef9e7; color: #f39c12; }}
        .status-pill.bad {{ background: #fdf0ed; color: #e74c3c; }}
        .summary-text {{ font-size: 12px; color: #666; margin-bottom: 8px; line-height: 1.5; }}
        .card-meta {{ font-size: 11px; color: #aaa; border-top: 1px solid #f0f0f0; padding-top: 8px; margin-top: 8px; margin-bottom: 8px; }}
        .rec-toggle {{ width: 100%; padding: 8px; background: #f5f7fa; border: 1px solid #e0e0e0; border-radius: 6px; font-size: 12px; cursor: pointer; text-align: left; color: #1a1a2e; font-weight: 600; }}
        .rec-toggle:hover {{ background: #e8eaf0; }}
        .wcag-toggle {{ background: #f0f7ff; border-color: #c0d8f0; }}
        .wcag-toggle:hover {{ background: #ddeeff; }}
        .recommendations {{ margin-top: 8px; padding: 12px; background: #f9f9f9; border-radius: 6px; border-left: 3px solid #1a1a2e; }}
        .wcag-rec {{ background: #f0f7ff; border-left-color: #3498db; }}
        .rec-section-title {{ font-size: 11px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }}
        .recommendations p {{ font-size: 12px; color: #444; margin-bottom: 8px; line-height: 1.6; }}
        .recommendations p:last-child {{ margin-bottom: 0; }}
        .analyse-section {{ background: white; border-radius: 10px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 40px; }}
        .analyse-section h2 {{ font-size: 16px; font-weight: 600; margin-bottom: 8px; color: #1a1a2e; }}
        .analyse-section p {{ font-size: 13px; color: #888; margin-bottom: 16px; }}
        .input-row {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .input-row input {{ flex: 1; padding: 10px 16px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; min-width: 200px; }}
        .input-row button {{ padding: 10px 24px; background: #1a1a2e; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; font-weight: 600; }}
        .input-row button:hover {{ background: #0f3460; }}
        .notice {{ margin-top: 16px; padding: 16px; background: #f0f7ff; border-radius: 8px; border-left: 4px solid #1a1a2e; font-size: 13px; color: #333; line-height: 1.8; }}
        footer {{ text-align: center; padding: 20px; font-size: 12px; color: #aaa; border-top: 1px solid #e0e0e0; }}
    </style>
</head>
<body>

<header>
    <div>
        <h1>FK Readability Dashboard</h1>
        <p>Datavant Technical Writing Team</p>
    </div>
    <div class="target-badge">Target: Grade 12 or below</div>
</header>

<div class="stats-bar">
    <div class="stat">
        <div class="stat-number">{total}</div>
        <div class="stat-label">Total Articles Tested</div>
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
        <p>Enter a Zendesk article ID below and click Analyse Article to run a new FK readability analysis</p>
        <div class="input-row">
            <input type="text" id="articleId" placeholder="Enter Zendesk Article ID e.g. 26609721445140" />
            <button onclick="analyseArticle()">Analyse Article</button>
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

    <div class="legend">
        <span class="legend-title">Score Guide:</span>
        <div class="legend-item">
            <div class="legend-dot good"></div>
            <span>12.0 or below = Meets Target</span>
        </div>
        <div class="legend-item">
            <div class="legend-dot warning"></div>
            <span>12.1 to 14.9 = Needs Improvement</span>
        </div>
        <div class="legend-item">
            <div class="legend-dot bad"></div>
            <span>15.0 and above = Needs Significant Work</span>
        </div>
    </div>

    <div class="articles-grid">
        {cards_html}
    </div>
</div>

<footer>
    FK Readability Dashboard - Datavant Technical Writing Team -
    Built by Cian Gallagher
</footer>

<script>
function toggleSection(id, btn) {{
    const section = document.getElementById(id);
    if (section.style.display === 'none') {{
        section.style.display = 'block';
        btn.textContent = btn.textContent.replace('▼', '▲');
    }} else {{
        section.style.display = 'none';
        btn.textContent = btn.textContent.replace('▲', '▼');
    }}
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