# FK Analysis Result

**Article:** Use Datavant Natively on AWS EC2
**Date:** 02 April 2026 15:29
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Use Datavant Natively on AWS EC2

SCORE: 12.1
Reading Level: High School Advanced
Target Audience: Advanced high school readers or entry-level college readers with some technical background

Summary: This content just exceeds the recommended readability target for technical documentation and would benefit from minor simplification to reach a broader technical audience.

FK RECOMMENDATIONS:

While the score of 12.1 is very close to the target threshold, here are three specific suggestions to bring it below Grade 12:

1. **Break down compound technical sentences**: The sentence "The AWS Native Tokenization is a docker container built to be deployed on either EC2, ECS, or EKS" (17 words) could be split: "The AWS Native Tokenization is a docker container. You can deploy it on EC2, ECS, or EKS."

2. **Simplify the proxy server instruction**: "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate" (30 words) could become: "If you have a proxy server, configure it to pass through the SSL certificate from Datavant's endpoints. Do not let it pass back its own self-signed certificate."

3. **Clarify credential timing statement**: "Once you generate the credential, you can't view it again" could be: "After you generate the credential, you cannot view it again. Save it immediately."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some phrases are unnecessarily complex: "appropriately sized," "pass-through mode," "configured to pass through the incoming SSL certificate." Consider: "correctly sized," "pass-through setting," "set to accept the SSL certificate."

Sentence Length: **Flag** - One sentence exceeds 25 words:
- "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate." (30 words)

Jargon: **Needs Attention** - Multiple technical terms lack explanation or definition:
- "docker container" (not explained for non-DevOps audiences)
- "master salt" (cryptographic term not defined)
- "pass-through mode" (not defined)
- "self-signed certificate" (not explained)
- "SSL certificate" (acronym used but not expanded on first use)

Active Voice: **Pass** - Most instructions use clear active voice ("Ensure your machine," "click Generate," "Do not share").

Heading Clarity: **Pass** - Step-based headings are clear and actionable, though "Step 2" could specify "(for tokenization only)" in the heading itself rather than in parentheses.

Link Text: **Flag** - Contains vague link text:
- "here" (in "You can see all of the EC2 types that AWS provides here") should be descriptive like "view AWS EC2 instance types"
- Generic references to other guides without clear link text context

Abbreviations: **Needs Attention** - Several abbreviations lack first-use expansion:
- OS (Operating System)
- SSL (Secure Sockets Layer)
- CLI (Command Line Interface)
- AWS is used throughout but never expanded to "Amazon Web Services"

Overall WCAG Writing Score: **Needs Attention**

---