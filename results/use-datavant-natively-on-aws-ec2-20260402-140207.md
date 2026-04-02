# FK Analysis Result

**Article:** Use Datavant Natively on AWS EC2
**Date:** 02 April 2026 14:02
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Use Datavant Natively on AWS EC2

SCORE: 12.1
Reading Level: High School Advanced
Target Audience: Readers with advanced high school to early college reading ability, likely technical professionals

Summary: This article just exceeds the ideal technical writing target and requires a high school senior level reading ability to understand comfortably.

FK RECOMMENDATIONS:
The content is very close to the Grade 12 target (only 0.1 above), but minor improvements would make it more accessible:

1. **Break down compound technical sentences**: "The AWS Native Tokenization is a docker container built to be deployed on either EC2, ECS, or EKS" could become: "The AWS Native Tokenization is a docker container. You can deploy it on EC2, ECS, or EKS."

2. **Simplify nested clauses**: "It has added functionality to directly read from and write to S3 buckets in the account that the docker container is running in" could be: "It can read from and write to S3 buckets in your account. This happens in the same account where the docker container runs."

3. **Reduce sentence complexity in warnings**: "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate" could be split: "Do you have a proxy server? Ensure it passes through the incoming SSL certificate from Datavant's endpoints. It should not pass back its own self-signed certificate."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some sentences use unnecessarily complex constructions. Example: "appropriately sized" could be "large enough"; "accessible outbound over port 443" could be simplified to "accessible through port 443."

Sentence Length: **Pass** - Average sentence length is 17.3 words, which is excellent. No problematic sentences over 25 words detected in the sample.

Jargon: **Needs Attention** - Several technical terms lack explanation or context:
- "docker container" (not explained for non-technical readers)
- "EC2, ECS, or EKS" (AWS services not defined)
- "M5.xlarge" (instance type not explained)
- "pass-through mode" (not defined)
- "master salt and encryption keys" (cryptographic terms unexplained)
- "self-signed certificate" (not explained)

Abbreviations: **Needs Attention** - Multiple abbreviations appear without first being spelled out:
- AWS (Amazon Web Services)
- EC2, ECS, EKS (not expanded)
- OS (Operating System)
- CLI (Command Line Interface)
- SSL (Secure Sockets Layer)

Active Voice: **Pass** - Most instructions use active voice and direct commands ("Ensure your machine," "Click Download," "Do not skip").

Heading Clarity: **Good** - Step-based headings are clear and action-oriented. Consider making "Step 2" more specific: "Step 2. Create a configuration for tokenization" instead of the parenthetical qualifier.

Link Text: **Needs Attention** - "here" is used as link text ("You can see all of the EC2 types that AWS provides here"), which is not descriptive. Should be: "view all AWS EC2 instance types" or similar.

Overall WCAG Writing Score: **Needs Attention**

The article has good structure and sentence length, but needs work on explaining technical terms, expanding abbreviations on first use, and improving link text descriptiveness.

---