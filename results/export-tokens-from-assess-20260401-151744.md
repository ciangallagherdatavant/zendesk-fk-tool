# FK Analysis Result

**Article:** Export Tokens from Assess
**Date:** 01 April 2026 15:17
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Export Tokens from Assess

SCORE: 9.2
Reading Level: High School
Target Audience: High school students and general adult readers with moderate reading ability

Summary: This article scores at a 9th-grade reading level, which is well within the ideal range for technical documentation and accessible to most professional audiences.

FK RECOMMENDATIONS:
✓ **Content meets target readability standards** - Well done! 

This article achieves strong readability with a Grade 9.2 score, comfortably below the Grade 12 threshold. The writing uses short sentences (average 12.1 words) and relatively simple vocabulary (average 1.7 syllables per word), making complex technical concepts accessible. The step-by-step structure and clear headings further enhance comprehension. Continue this approach in future articles.

---

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Pass
The article uses straightforward, direct language. Technical concepts are introduced with context (e.g., "A token export is a file containing the overlapping records from an Overlap report").

**Sentence Length:** Pass
All sentences stay well under the 25-word threshold. The longest sentences are appropriately complex for technical instructions while remaining clear and scannable.

**Jargon:** Needs Attention
- "Token export" - explained ✓
- "Overlap report" - used without definition
- "SFTP" - unexplained abbreviation
- "S3 Transfer" - unexplained
- "AWS S3 environment" - unexplained
- "transit encryption key" - unexplained technical concept
- "site-specific encryption key" - unexplained technical concept
- "subscription tier" - used without context

**Active Voice:** Pass with minor note
Predominantly active voice throughout. One passive construction found: "Token Exports are stored in an S3 directory" - could be rewritten as "Datavant stores Token Exports in an S3 directory."

**Heading Clarity:** Pass
Headings are clear, descriptive, and follow a logical task-based structure. The "How to Create a Token Export" section uses numbered steps effectively.

**Link Text:** Needs Attention
- "Share a Table or Segment article" - Good, descriptive ✓
- "How to Pick Up Distributed Data article" - Good, descriptive ✓
- "Datavant CLI Commands and Optional Arguments article" - Good, descriptive ✓
- "Use Datavant Desktop" - Good, descriptive ✓
- Generic references like "See Use Datavant Natively on Snowflake for more information" appear twice with different contexts (Snowflake and Databricks), which may cause confusion.

**Abbreviations:** Needs Attention
Unexplained abbreviations:
- SFTP (Secure File Transfer Protocol)
- S3 (Simple Storage Service)
- AWS (Amazon Web Services)
- CLI (Command Line Interface)
- OS (Operating System)
- ECS, EKS, EC2 (AWS service abbreviations)

Overall WCAG Writing Score: **Needs Attention**

The article has excellent structure and readability, but would benefit from defining technical acronyms on first use and providing brief explanations for specialized terms like "encryption key" and "Overlap report."