# FK Analysis Result

**Article:** Data Onboarding Method: S3 Transfer
**Date:** 02 April 2026 13:37
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Data Onboarding Method: S3 Transfer

SCORE: 9.3
Reading Level: High School
Target Audience: High school level readers with basic technical knowledge; accessible to most professional audiences

Summary: This article achieves a grade 9 reading level, making it appropriately accessible for general business and technical audiences without being overly complex.

FK RECOMMENDATIONS:
✓ **Content meets target readability** - Well done! The article scores at grade 9.3, which is comfortably below the grade 12 threshold for technical writing. The average sentence length of 15.3 words and average syllable count of 1.6 per word both contribute to good readability. Continue maintaining this clarity in future updates.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention**
- Heavy use of unexplained technical jargon (see below) assumes expert knowledge
- Example: "assume the Datavant role only when pushing data to Datavant's S3 folder" - the verb "assume" is AWS-specific terminology that may confuse non-AWS users

Sentence Length: **Pass**
- Most sentences are well-structured and concise
- One flagged sentence (47 words): "In this process, customers can provision an AWS IAM User within the customer's AWS account, and provide Datavant the AWS Account ID in the Datavant Connect platform. Datavant will then provision an AWS IAM role within the Datavant AWS account."
- Consider breaking this into shorter segments

Jargon: **Needs Attention**
The following technical terms lack explanation or context:
- S3 bucket/transfer
- AWS IAM Roles/User
- Lambda function
- Role ARN
- AWS CLI/API
- External ID (partially explained via link)
- IAM Principal
Recommendation: Add a glossary section or inline tooltips for first use of each term

Active Voice: **Needs Attention**
Passive constructions found:
- "Uploading data through an S3 transfer is one of the most common ways..."
  Suggested: "Many customers upload data through an S3 transfer..."
- "customers can provision an AWS IAM User"
  Better as: "provision an AWS IAM User"
- "credentials generated after entering"
  Better as: "the system generates credentials after you enter"

Heading Clarity: **Pass**
- Clear descriptive headings ("Overview," "Generate an S3 IAM Role")
- Option #1 and Option #2 clearly delineate different pathways

Link Text: **Needs Attention**
- "Read more about using External IDs here" - the word "here" is not descriptive
  Better: "Read more about External ID best practices" or "Learn when to use External IDs"

Abbreviations: **Needs Significant Work**
Unexplained abbreviations:
- S3 (never spelled out)
- AWS (never spelled out)
- IAM (never spelled out)
- API (never spelled out)
- CLI (never spelled out)
- ARN (never spelled out)
Best practice: Spell out on first use, e.g., "Amazon Web Services (AWS)"

Overall WCAG Writing Score: **Needs Attention**

The article achieves good readability scores but requires improved accessibility through defining technical terms, expanding abbreviations, and providing context for AWS-specific concepts. These improvements would make the content accessible to a broader audience including those new to AWS services.

---