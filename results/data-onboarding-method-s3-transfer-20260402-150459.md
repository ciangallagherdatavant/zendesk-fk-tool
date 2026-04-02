# FK Analysis Result

**Article:** Data Onboarding Method: S3 Transfer
**Date:** 02 April 2026 15:04
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Data Onboarding Method: S3 Transfer

SCORE: 9.3
Reading Level: High School
Target Audience: High school students and above with moderate reading ability

Summary: This article is written at a 9th-grade reading level, making it moderately easy to read and well-suited for a general technical audience.

FK RECOMMENDATIONS:
✓ Content meets target readability standard - Well done!

This article scores 9.3, which is comfortably below the Grade 12 threshold for technical writing. The average sentence length of 15.3 words and 1.6 syllables per word contribute to good readability. The content successfully balances technical accuracy with accessibility.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention**
- "provision an AWS IAM User" - use "create" or "set up" instead of "provision"
- "assume (an AWS IAM operation) into the IAM role" - this technical phrasing needs simplification or a clearer explanation upfront
- "authenticates the environment" - use "verifies your system's access" or similar

Sentence Length: **Flagged**
- "In this process, customers can provision an AWS IAM User within the customer's AWS account, and provide Datavant the AWS Account ID in the Datavant Connect platform." (28 words)
- "Datavant will then provision an AWS IAM role within the Datavant AWS account." (13 words) - Consider combining differently to break up the 28-word sentence above
- "Through this role, customers can download and upload data from and to the customer's S3 bucket within Datavant AWS account, using the AWS CLI or AWS API." (28 words)

Jargon: **Needs Attention**
- "AWS IAM Roles" - explained contextually but not defined
- "AWS IAM User" - not explicitly defined
- "assume" (as AWS operation) - mentioned as operation but not explained
- "Lambda function" - no explanation provided
- "Role ARN" - not defined
- "AWS CLI" and "AWS API" - abbreviations used without definition

Active Voice: **Pass**
The article primarily uses active voice effectively (e.g., "Customers must push data," "You will need to retrieve").

Heading Clarity: **Pass**
Headings are clear and descriptive ("Generate an S3 IAM Role," "Option #1," "Option #2").

Link Text: **Cannot Assess**
One link reference found ("Read more about using External IDs here") - text is clear and descriptive.

Abbreviations: **Needs Attention**
- S3 - not defined on first use
- AWS - not defined on first use
- IAM - not defined on first use
- CLI - not defined (appears as "AWS CLI")
- API - not defined (appears as "AWS API")
- ARN - not defined (appears as "Role ARN")

Overall WCAG Writing Score: **Needs Attention**

The article has good structural clarity and sentence length (mostly), but needs work on defining technical terms and abbreviations on first use, and simplifying some technical jargon for better accessibility.

---