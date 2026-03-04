# How to Use the FK Readability Analysis Tool

## What You Need
- Access to Claude Console Workbench
- Your Zendesk article content in text format

## Steps to Analyse an Article

### Step 1 - Export Your Zendesk Content
- Open your Zendesk article
- Copy all the text content from the article
- You do not need to worry about formatting, 
  the tool handles that automatically

### Step 2 - Open Claude Console Workbench
- Go to platform.claude.com
- Click on Workbench in the left menu
- Open the saved prompt called FK Readability Analysis Tool

### Step 3 - Paste Your Article
- The System Prompt box at the top is already filled in
- Do not change or delete the System Prompt
- Click inside the User box
- Delete any previous article that is in there
- Paste your new Zendesk article text into the User box

### Step 4 - Run the Analysis
- Click the black Run button in the top right
- Wait approximately 10 to 15 seconds
- The results appear on the right side of the screen

### Step 5 - Read Your Results
The tool will return:
- A Grade Level Score
- A Reading Level label
- A full breakdown of what was analysed
- A list of everything that was excluded from scoring
- Specific recommendations if the score is above Grade 8

### Step 6 - Save Your Results (Optional)
- Copy the results from the right side panel
- Create a new file in the results folder of the 
  zendesk-fk-tool GitHub repository
- Name it after the article for example: 
  how-to-reset-password-result.md
- Paste the results in and commit to GitHub

---

## What the Score Means

| Grade Level | Reading Level | What it Means |
|---|---|---|
| 1 to 6 | Elementary | Very easy, ideal |
| 7 to 8 | Middle School | Easy, meets target |
| 9 to 10 | High School | Moderate, needs work |
| 11 to 12 | High School Advanced | Complex, simplify |
| 13 and above | College | Too complex, rewrite |

## Target Score
All Zendesk content should aim for Grade 8 or below

---

## What the Tool Automatically Ignores
You do not need to manually remove any of the following 
before pasting your article. The tool handles all of this:

- Headings and subheadings
- Bullet point and numbered lists
- Code blocks and programming syntax
- Images and media references
- URLs and web addresses
- Technical identifiers
- Product and team names like Tokenization

---

## Repository Structure
All project files are stored at:
github.com/ciangallagherdatavant/zendesk-fk-tool

- content/ stores Zendesk articles for testing
- prompts/ stores the Claude analysis prompt
- results/ stores all FK analysis outputs