# FK Analysis Result

**Article:** Export Tokens from Assess
**Date:** 07 April 2026 09:20
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Export Tokens from Assess

SCORE: 9.2
Reading Level: High School
Target Audience: High school students and above; moderately complex but accessible to general business users

Summary: This article reads at a 9th-grade level, making it accessible to most users and well within the ideal target range for technical documentation.

FK RECOMMENDATIONS:
The content successfully meets the target readability level. Here are three specific suggestions to improve it further:

1. **Break down compound instructions**: The sentence "If your partner ran the Overlap report using tables you shared, you cannot create a token export" combines a conditional clause with a restriction. Consider splitting this: "Your partner may run Overlap reports using tables you shared. In these cases, you cannot create a token export."

2. **Simplify technical phrases**: The phrase "tokens encrypted with the <your-site-name>-datavant transit encryption key" uses multiple technical modifiers. Consider: "tokens encrypted with your transit key (called <your-site-name>-datavant)" to reduce cognitive load.

3. **Reduce prepositional phrase chains**: "Follow the instructions in the How to Pick Up Distributed Data article to access this environment and retrieve files using SFTP or an S3 Transfer" stacks multiple prepositional phrases. Break into two sentences: "Follow the instructions in the How to Pick Up Distributed Data article. This will help you access the environment and retrieve files using SFTP or S3 Transfer."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some unnecessarily complex phrases found: "securely download token exports from the Datavant Connect platform" could be "download token exports securely from Datavant Connect"; "analyses that can't be done in Assess" could specify what types of analyses.

Sentence Length: **Pass** - All sentences are well under 25 words. The longest sentence is approximately 20 words, which is excellent for accessibility.

Jargon: **Needs Attention** - Several technical terms lack explanation:
- "SFTP" (not defined)
- "S3 Transfer" (not defined)
- "S3 directory" (not explained)
- "site-specific encryption key" (assumed knowledge)
- "transit encryption key" (not distinguished from site-specific key)

Active Voice: **Pass** - Article predominantly uses active voice. One passive construction found: "Token Exports are stored in an S3 directory" - could be "Datavant stores Token Exports in an S3 directory," though passive voice is acceptable here.

Heading Clarity: **Pass** - Headings are clear, descriptive, and follow a logical task-based structure (What/How/Step-by-step format).

Link Text: **Pass** - Link text is descriptive ("Share a Table or Segment article," "How to Pick Up Distributed Data article," "Use Datavant Desktop").

Abbreviations: **Needs Attention** - Several unexplained abbreviations:
- "SFTP" (should be "SFTP (Secure File Transfer Protocol)" on first use)
- "S3" (should be "S3 (Simple Storage Service)" on first use)
- "AWS" (should be "AWS (Amazon Web Services)" on first use)
- "CLI" (should be "CLI (Command Line Interface)" on first use)
- "OS" (should be "OS (Operating System)" on first use)
- "ECS, EKS, EC2" (all unexplained)

Overall WCAG Writing Score: **Needs Attention**

The article has strong structure and sentence length control, but requires better support for technical terms and abbreviations to meet full WCAG 2.2 accessibility standards.

---