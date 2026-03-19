# ============================================
# FK Readability Analysis Tool
# Built by Cian Gallagher - Datavant
# ============================================
# What this script does:
# 1. Connects to Zendesk using API credentials
# 2. Fetches an article by its ID
# 3. Sends the article to Claude for FK analysis
# 4. Saves the result to the results folder
# ============================================

import os
import re
from datetime import datetime
from dotenv import load_dotenv
import requests
import anthropic

# ============================================
# LOAD SECRET CREDENTIALS
# Reads your .env file and loads all
# your API keys safely into the script
# Nobody can see these values
# ============================================
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ZENDESK_SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
ZENDESK_EMAIL = os.getenv("ZENDESK_EMAIL")
ZENDESK_API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

# ============================================
# YOUR FK ANALYSIS PROMPT
# This is the brain of the tool
# Tells Claude exactly what to do
# Nobody using the tool can edit this
# It is locked inside the script
# ============================================
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
Use this exact format:

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
# Goes into Zendesk and retrieves the
# article text using the article ID
# ============================================
def get_zendesk_article(article_id):
    print(f"\nFetching article {article_id} from Zendesk...")
    
    url = f"https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/help_center/articles/{article_id}"
    
    auth = (
        f"{ZENDESK_EMAIL}/token",
        ZENDESK_API_TOKEN
    )
    
    response = requests.get(url, auth=auth)
    
    if response.status_code != 200:
        print(f"Error fetching article: {response.status_code}")
        print(f"Message: {response.text}")
        return None, None
    
    data = response.json()
    title = data['article']['title']
    body = data['article']['body']
    
    # Remove HTML tags from the article body
    # Zendesk stores articles in HTML format
    # We need plain text for the analysis
    clean_body = re.sub('<[^<]+?>', '', body)
    
    print(f"Article fetched successfully: {title}")
    return title, clean_body

# ============================================
# ANALYSE WITH CLAUDE
# Sends the article text to Claude
# with your FK prompt and gets score back
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
# Saves the FK score result as a file
# in your results folder automatically
# ============================================
def save_result(title, result):
    print(f"\nSaving result...")
    
    # Create a clean filename from the article title
    clean_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
    clean_title = clean_title.replace(' ', '-').lower()
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = f"results/{clean_title}-{timestamp}.md"
    
    # Write the result file
    with open(filename, 'w') as f:
        f.write(f"# FK Analysis Result\n\n")
        f.write(f"**Article:** {title}\n")
        f.write(f"**Date:** {datetime.now().strftime('%d %B %Y %H:%M')}\n\n")
        f.write(result)
    
    print(f"Result saved to: {filename}")
    return filename

# ============================================
# MAIN FUNCTION
# This runs when you start the script
# Asks for article ID then runs everything
# ============================================
def main():
    print("========================================")
    print("  FK Readability Analysis Tool")
    print("  Datavant Technical Writing Team")
    print("========================================")
    
    # Ask the user for the article ID
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
    
    # Step 3: Save result
    filename = save_result(title, result)
    
    # Step 4: Print result to screen
    print("\n========================================")
    print("  ANALYSIS COMPLETE")
    print("========================================")
    print(result)
    print(f"\nResult saved to: {filename}")

# This line means the script only runs
# when you directly execute it
if __name__ == "__main__":
    main()