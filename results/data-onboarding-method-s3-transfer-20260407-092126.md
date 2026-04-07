# FK Analysis Result

**Article:** Data Onboarding Method: S3 Transfer
**Date:** 07 April 2026 09:21
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Data Onboarding Method: S3 Transfer

SCORE: 9.3
Reading Level: High School
Target Audience: High school students and general professionals with moderate technical background

Summary: This article is written at a 9th-grade reading level, making it accessible to most adult readers and well within the recommended range for technical documentation.

FK RECOMMENDATIONS:
The content meets the readability target and is appropriate for the technical audience. Here are three specific suggestions to improve it further:

1. **Break up compound sentences with multiple clauses.** For example: "In this process, customers can provision an AWS IAM User within the customer's AWS account, and provide Datavant the AWS Account ID in the Datavant Connect platform" could be split into: "First, customers provision an AWS IAM User within their AWS account. Then, they provide Datavant the AWS Account ID in the Datavant Connect platform."

2. **Simplify technical explanations.** The sentence "Datavant only supports AWS IAM Roles owned by Datavant, and 'assumed' by a customer through a customer's AWS IAM User" could be rewritten as: "Datavant only supports AWS IAM Roles that Datavant owns. Customers access these roles through their AWS IAM User."

3. **Use more concrete action verbs.** Replace passive constructions like "S3 IAM roles have default permissions to make any action" with active phrasing: "S3 IAM roles can perform any action within your customer path by default."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several complex technical phrases could be simplified: "provision an AWS IAM User," "assume (an AWS IAM operation) into the IAM role," and "implement credentials" use unnecessarily formal language.

Sentence Length: **Pass** - Most sentences are well under 25 words. The average of 15.3 words per sentence is excellent for readability.

Jargon: **Needs Attention** - Multiple technical terms lack explanation:
- IAM (defined only as "AWS IAM")
- ARN (mentioned as "Role ARN" with no definition)
- Lambda function (mentioned without context)
- CLI and API (used without expansion)

Abbreviations: **Needs Attention** - Several abbreviations are not expanded on first use:
- S3 (never defined)
- AWS (never defined, though commonly known)
- ARN (never defined)
- CLI (never defined)
- API (never defined)

Active Voice: **Needs Attention** - Multiple passive constructions found:
- "can be used to assume"
- "would then be used to assume"
- "is set"
- "are generated"

Heading Clarity: **Good** - Headings like "Overview," "Generate an S3 IAM Role," and "Option #1" / "Option #2" are clear and descriptive.

Link Text: **Cannot assess** - The cleaned prose text shows a reference to "Read more about using External IDs here" but link implementation cannot be evaluated from this format.

Overall WCAG Writing Score: **Needs Attention**