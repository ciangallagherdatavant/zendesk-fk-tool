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
on Zendesk help content.

You help a technical writing team ensure their documentation 
is clear and accessible to their intended audience.

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

Technical writing should ideally target Grade 8 or below.

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

RECOMMENDATIONS:
[If Grade 8 or below: confirm content meets target]
[If above Grade 8: give 3 specific suggestions]
---
"""

# ============================================
# FETCH ARTICLE FROM ZENDESK
# ============================================
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

# ============================================
# ANALYSE WITH CLAUDE
# ============================================
def analyse_with_claude(title, content):
    print(f"\nSending article to Claude for FK analysis...")
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2000,
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

# ============================================
# SAVE RESULT
# ============================================
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

# ============================================
# READ ALL RESULTS
# Reads every result file and extracts
# all the key information including
# recommendations for the dashboard
# ============================================
def read_all_results():
    print("\nReading all result files...")
    
    results = []
    result_files = glob.glob('results/*.md')
    result_files = [f for f in result_files if '.gitkeep' not in f]
    result_files = [f for f in result_files if 'sample-article' not in f]
    
    seen_titles = {}
    
    for filepath in result_files:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Extract article title
        title_match = re.search(r'\*\*Article:\*\* (.+)', content)
        title = title_match.group(1).strip() if title_match else 'Unknown Article'
        
        # Extract date
        date_match = re.search(r'\*\*Date:\*\* (.+)', content)
        date = date_match.group(1).strip() if date_match else 'Unknown Date'
        
        # Extract score
        score_match = re.search(r'SCORE:\s*\*?\*?(\d+\.?\d*)', content)
        score = float(score_match.group(1)) if score_match else 0
        
        # Extract reading level
        level_match = re.search(r'Reading Level:\s*\*?\*?(.+)', content)
        level = level_match.group(1).strip() if level_match else 'Unknown'
        level = re.sub(r'\*', '', level).strip()
        
        # Extract summary
        summary_match = re.search(r'Summary:\s*\*?\*?(.+)', content)
        summary = summary_match.group(1).strip() if summary_match else ''
        summary = re.sub(r'\*', '', summary).strip()
        
        # Extract recommendations section
        rec_match = re.search(r'RECOMMENDATIONS:\s*\n(.*?)(?=---|$)', 
                             content, re.DOTALL)
        recommendations = rec_match.group(1).strip() if rec_match else ''
        recommendations = re.sub(r'\*\*', '', recommendations)
        
        # If we have seen this title before keep the most recent
        if title in seen_titles:
            existing_date = seen_titles[title]['date']
            if date > existing_date:
                seen_titles[title] = {
                    'title': title,
                    'date': date,
                    'score': score,
                    'level': level,
                    'summary': summary,
                    'recommendations': recommendations,
                    'filepath': filepath
                }
        else:
            seen_titles[title] = {
                'title': title,
                'date': date,
                'score': score,
                'level': level,
                'summary': summary,
                'recommendations': recommendations,
                'filepath': filepath
            }
    
    results = list(seen_titles.values())
    results.sort(key=lambda x: x['score'], reverse=True)
    
    print(f"Found {len(results)} unique articles")
    return results

# ============================================
# BUILD DASHBOARD
# Rebuilds the full dashboard with
# expandable recommendation sections
# ============================================
def build_dashboard(results):
    print("\nUpdating dashboard...")
    
    total = len(results)
    failing = len([r for r in results if r['score'] > 8])
    passing = len([r for r in results if r['score'] <= 8])
    avg_score = round(sum(r['score'] for r in results) / total, 1) if total > 0 else 0
    today = datetime.now().strftime('%d %B %Y')
    
    cards_html = ""
    for i, r in enumerate(results):
        status = "fail" if r['score'] > 8 else "pass"
        status_text = "❌ Needs Improvement" if r['score'] > 8 else "✅ Meets Target"
        
        # Format recommendations as HTML
        rec_lines = r['recommendations'].split('\n')
        rec_html = ""
        for line in rec_lines:
            line = line.strip()
            if line:
                rec_html += f"<p>{line}</p>"
        
        cards_html += f"""
        <div class="article-card {status}">
            <div class="card-header">
                <div class="article-title">{r['title']}</div>
                <div class="score-badge">{r['score']}</div>
            </div>
            <div class="reading-level">{r['level']}</div>
            <span class="status-pill {status}">{status_text}</span>
            <div class="summary-text">{r['summary']}</div>
            <div class="card-meta">Tested: {r['date']}</div>
            <button class="rec-toggle" onclick="toggleRec({i})">
                View Recommendations ▼
            </button>
            <div class="recommendations" id="rec-{i}" style="display:none">
                {rec_html}
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
        .stat-number.pass {{ color: #27ae60; }}
        .stat-number.fail {{ color: #e74c3c; }}
        .main {{ padding: 30px 40px; }}
        .section-title {{ font-size: 16px; font-weight: 600; margin-bottom: 8px; color: #1a1a2e; }}
        .last-updated {{ font-size: 11px; color: #aaa; margin-bottom: 20px; }}
        .articles-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; margin-bottom: 40px; }}
        .article-card {{ background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 5px solid #ccc; }}
        .article-card.pass {{ border-left-color: #27ae60; }}
        .article-card.fail {{ border-left-color: #e74c3c; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }}
        .article-title {{ font-size: 14px; font-weight: 600; color: #1a1a2e; flex: 1; margin-right: 10px; }}
        .score-badge {{ font-size: 22px; font-weight: 800; color: #e74c3c; }}
        .score-badge.pass {{ color: #27ae60; }}
        .reading-level {{ font-size: 12px; color: #888; margin-bottom: 8px; }}
        .status-pill {{ display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; margin-bottom: 8px; }}
        .status-pill.pass {{ background: #eafaf1; color: #27ae60; }}
        .status-pill.fail {{ background: #fdf0ed; color: #e74c3c; }}
        .summary-text {{ font-size: 12px; color: #666; margin-bottom: 8px; line-height: 1.5; }}
        .card-meta {{ font-size: 11px; color: #aaa; border-top: 1px solid #f0f0f0; padding-top: 8px; margin-top: 8px; margin-bottom: 8px; }}
        .rec-toggle {{ width: 100%; padding: 8px; background: #f5f7fa; border: 1px solid #e0e0e0; border-radius: 6px; font-size: 12px; cursor: pointer; text-align: left; color: #1a1a2e; font-weight: 600; }}
        .rec-toggle:hover {{ background: #e8eaf0; }}
        .recommendations {{ margin-top: 12px; padding: 12px; background: #f9f9f9; border-radius: 6px; border-left: 3px solid #1a1a2e; }}
        .recommendations p {{ font-size: 12px; color: #444; margin-bottom: 8px; line-height: 1.6; }}
        .recommendations p:last-child {{ margin-bottom: 0; }}
        .analyse-section {{ background: white; border-radius: 10px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 40px; }}
        .analyse-section h2 {{ font-size: 16px; font-weight: 600; margin-bottom: 8px; color: #1a1a2e; }}
        .analyse-section p {{ font-size: 13px; color: #888; margin-bottom: 16px; }}
        .input-row {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .input-row input {{ flex: 1; padding: 10px 16px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; min-width: 200px; }}
        .input-row button {{ padding: 10px 24px; background: #1a1a2e; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer; font-weight: 600; }}
        .input-row button:hover {{ background: #0f3460; }}
        .notice {{ margin-top: 12px; padding: 12px 16px; background: #fff8e1; border-radius: 6px; font-size: 12px; color: #856404; }}
        footer {{ text-align: center; padding: 20px; font-size: 12px; color: #aaa; border-top: 1px solid #e0e0e0; }}
    </style>
</head>
<body>

<header>
    <div>
        <h1>FK Readability Dashboard</h1>
        <p>Datavant Technical Writing Team</p>
    </div>
    <div class="target-badge">Target: Grade 8 or below</div>
</header>

<div class="stats-bar">
    <div class="stat">
        <div class="stat-number">{total}</div>
        <div class="stat-label">Total Articles Tested</div>
    </div>
    <div class="stat">
        <div class="stat-number fail">{failing}</div>
        <div class="stat-label">Need Improvement</div>
    </div>
    <div class="stat">
        <div class="stat-number pass">{passing}</div>
        <div class="stat-label">Passing Grade 8</div>
    </div>
    <div class="stat">
        <div class="stat-number">{avg_score}</div>
        <div class="stat-label">Average Score</div>
    </div>
</div>

<div class="main">

    <div class="analyse-section">
        <h2>Analyse a New Article</h2>
        <p>Enter a Zendesk article ID below to run a new FK readability analysis</p>
        <div class="input-row">
            <input type="text" id="articleId" placeholder="Enter Zendesk Article ID e.g. 26609721445140" />
            <button onclick="showInstructions()">Analyse Article</button>
        </div>
        <div class="notice" id="instructions" style="display:none">
            To analyse this article open Terminal and run:<br><br>
            <strong>cd ~/Documents/zendesk-fk-tool/zendesk-fk-tool</strong><br>
            <strong>python3 fk_analysis.py</strong><br><br>
            Then enter your article ID when prompted.
            The dashboard will update automatically after the analysis completes.
        </div>
    </div>

    <div class="section-title">All Article Results</div>
    <div class="last-updated">Last updated: {today}</div>

    <div class="articles-grid">
        {cards_html}
    </div>
</div>

<footer>
    FK Readability Dashboard - Datavant Technical Writing Team -
    Built by Cian Gallagher
</footer>

<script>
function toggleRec(id) {{
    const rec = document.getElementById('rec-' + id);
    const btn = rec.previousElementSibling;
    if (rec.style.display === 'none') {{
        rec.style.display = 'block';
        btn.textContent = 'Hide Recommendations ▲';
    }} else {{
        rec.style.display = 'none';
        btn.textContent = 'View Recommendations ▼';
    }}
}}

function showInstructions() {{
    const id = document.getElementById('articleId').value;
    if (id) {{
        document.getElementById('instructions').style.display = 'block';
    }} else {{
        alert('Please enter an article ID first');
    }}
}}
</script>

</body>
</html>"""
    
    with open('index.html', 'w') as f:
        f.write(html)
    
    print("Dashboard updated successfully")

# ============================================
# PUSH TO GITHUB
# ============================================
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

# ============================================
# MAIN FUNCTION
# ============================================
def main():
    print("========================================")
    print("  FK Readability Analysis Tool")
    print("  Datavant Technical Writing Team")
    print("========================================")
    
    article_id = input("\nEnter the Zendesk article ID: ").strip()
    
    if not article_id.isdigit():
        print("Error: Please enter a valid article ID number")
        return
    
    # Step 1: Fetch from Zendesk
    title, content = get_zendesk_article(article_id)
    if not title:
        return
    
    # Step 2: Analyse with Claude
    result = analyse_with_claude(title, content)
    
    # Step 3: Save result file
    filename = save_result(title, result)
    
    # Step 4: Rebuild dashboard
    all_results = read_all_results()
    build_dashboard(all_results)
    
    # Step 5: Push to GitHub
    push_to_github(title)
    
    # Step 6: Print result
    print("\n========================================")
    print("  ANALYSIS COMPLETE")
    print("========================================")
    print(result)
    print(f"\nResult saved to: {filename}")
    print("\nDashboard updated and pushed to GitHub automatically")

if __name__ == "__main__":
    main()