# FK Analysis Result

**Article:** Request an External File Push
**Date:** 07 April 2026 09:22
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Request an External File Push

SCORE: 9.4
Reading Level: High School
Target Audience: High school students and general adult readers with moderate technical knowledge

Summary: This article reads at a 9th-10th grade level, making it accessible to most adult users and well within the recommended target for technical documentation.

FK RECOMMENDATIONS:
The content already meets the readability target of Grade 12 or below, which is excellent for technical documentation. To improve it further:

1. **Break down compound technical sentences**: The sentence "Copy and paste this text and replace the bracketed {BUCKET_NAME} and {BUCKET_PATH} in both instances under 'Resource'" contains multiple instructions in one sentence. Split this into: "Copy and paste this text. Then replace the bracketed {BUCKET_NAME} and {BUCKET_PATH} in both instances under 'Resource'."

2. **Simplify the trust policy introduction**: "Create an IAM role in your AWS account into which Datavant can assume" uses complex prepositional phrasing. Revise to: "Create an IAM role in your AWS account. Datavant will assume this role."

3. **Clarify the cloud targets sentence**: "For Cloud targets like Snowflake, Azure, Databricks, or GCP: Customers are responsible for building the ingest pipeline on their side once the data lands in S3" could be simplified to: "For cloud targets (Snowflake, Azure, Databricks, or GCP): You must build the ingest pipeline after data lands in S3."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some phrases could be simpler. "IAM role in your AWS account into which Datavant can assume" uses unnecessarily complex structure. "Populate the bucket name and path" could be "Enter the bucket name and path."

Sentence Length: **Pass** - All sentences are under 25 words. The average of 12.4 words per sentence is excellent for readability.

Jargon: **Needs Attention** - Several technical terms lack explanation:
- IAM Role (first use should explain: Identity and Access Management)
- Trust policy
- Permissions policy
- ARN (should spell out: Amazon Resource Name)
- Prefix (used without clear context for non-AWS users)
- Ingest pipeline

Abbreviations: **Needs Attention**
- AWS (explained as "Amazon Web Services" on first use would help)
- S3 (should be "Amazon S3" or "S3 storage" for clarity)
- IAM (never expanded)
- ARN (never expanded)
- GCP (never expanded as "Google Cloud Platform")

Active Voice: **Pass** - Most content uses active voice effectively ("Create an IAM role," "Copy and paste this text," "Provide these details").

Heading Clarity: **Good** - Step-by-step headings are clear and action-oriented. The "Overview" section properly sets context.

Link Text: **Pass** - The link "Understanding Distributions" is descriptive and meaningful. Email addresses are appropriately formatted.

Overall WCAG Writing Score: **Needs Attention**

The article has good structure and sentence length, but would benefit from expanding abbreviations on first use and providing brief explanations for technical terms that may be unfamiliar to users new to AWS or cloud storage concepts.

---