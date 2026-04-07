# FK Analysis Result

**Article:** Data Onboarding Method: Databricks Transfer
**Date:** 07 April 2026 09:19
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Data Onboarding Method: Databricks Transfer

SCORE: 9.0
Reading Level: High School
Target Audience: High school students and general business users with moderate technical familiarity

Summary: This article reads at a 9th-grade level, making it accessible to most technical users and well within the ideal range for technical documentation.

FK RECOMMENDATIONS:
The content meets the target grade level effectively. To improve readability further:

1. **Break down multi-clause sentences**: While average sentence length is good at 13.2 words, some sentences contain multiple instructions in one. For example, "From the Download page in Connect, go to the S3 Credentials section and create a new IAM Role" could become two sentences: "From the Download page in Connect, go to the S3 Credentials section. Create a new IAM Role."

2. **Simplify technical phrases**: Replace phrases like "integrating a Datavant-owned IAM Role to a customer Databricks account" with "connecting a Datavant IAM Role to your Databricks account." Use "connecting" instead of "integrating" and "your" instead of "a customer's" for directness.

3. **Reduce syllable-heavy words**: The phrase "Copy the Role ARN that is generated in this step" could become "Copy the Role ARN created in this step" (replacing "generated" with "created" saves a syllable and maintains clarity).

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several instances of complex phrasing exist: "There is no risk of writing data to the wrong S3 prefix, as Datavant manages the IAM Role" could be simplified to "Datavant manages the IAM Role to prevent data from going to the wrong location."

Sentence Length: **Pass** - Most sentences are concise. One borderline example: "This works by integrating a Datavant-owned IAM Role to a customer Databricks account so Databricks can write directly to the Datavant S3 bucket" (24 words - acceptable but could be split).

Jargon: **Needs Attention** - Several unexplained technical terms:
- IAM Role (first mention needs expansion)
- S3 bucket/prefix
- ARN
- External ID
- External Location
- Schema
- Catalog

Abbreviations: **Needs Attention** - Unexplained abbreviations found:
- IAM (never spelled out)
- ARN (never spelled out)
- S3 (never spelled out)
- AWS (never spelled out)
- ID (used extensively without expansion)

Active Voice: **Pass** - Strong use of active voice and imperative commands throughout ("Create," "Select," "Copy," "Enter").

Heading Clarity: **Good** - Step numbers are clear and descriptive (e.g., "Step 1. Create an IAM Role").

Link Text: **Cannot assess** - No link text present in cleaned prose version.

Overall WCAG Writing Score: **Needs Attention**