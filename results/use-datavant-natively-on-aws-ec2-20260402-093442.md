# FK Analysis Result

**Article:** Use Datavant Natively on AWS EC2
**Date:** 02 April 2026 09:34
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Use Datavant Natively on AWS EC2

SCORE: 12.1
Reading Level: High School Advanced
Target Audience: Readers with advanced high school education or higher; technical professionals comfortable with cloud infrastructure terminology

Summary: This article is just slightly above the ideal target for technical documentation and may challenge readers without college-level reading skills or cloud computing experience.

FK RECOMMENDATIONS:

The content is slightly above the Grade 12 target (by 0.1), indicating minor complexity issues. Here are three specific suggestions:

1. **Break down long technical sentences**: The sentence "The AWS Native Tokenization is a docker container built to be deployed on either EC2, ECS, or EKS" could be split: "The AWS Native Tokenization is a docker container. You can deploy it on EC2, ECS, or EKS."

2. **Simplify conditional phrasing**: The sentence "If you are interested in this Datavant implementation and have not received an AWS Marketplace Private Listing, please reach out to your Customer Success Lead or Cloud-Integrations@datavant.com" could be shortened to: "Interested in this implementation? Contact your Customer Success Lead or Cloud-Integrations@datavant.com if you need an AWS Marketplace Private Listing."

3. **Convert explanatory clauses to separate sentences**: The sentence "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate" could become: "Do you have a proxy server? Configure it to pass through the incoming SSL certificate from Datavant's endpoints. It should not pass back its own self-signed certificate."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some phrases could be simplified:
- "appropriately sized" → "large enough"
- "as opposed to" → "instead of"
- "Verify network connectivity" → "Check your network connection"

Sentence Length: **Needs Attention** - Several sentences exceed 25 words:
- "This product enables customers to generate, transform, and onboard directly all from within your personal AWS Cloud tenant." (17 words - Pass)
- "It has added functionality to directly read from and write to S3 buckets in the account that the docker container is running in." (24 words - Pass)
- "If you are interested in this Datavant implementation and have not received an AWS Marketplace Private Listing, please reach out to your Customer Success Lead or Cloud-Integrations@datavant.com." (29 words - **Flag**)
- "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate." (31 words - **Flag**)
- "A direct SSL connection is required with the endpoints listed above to ensure that the Datavant application and sensitive data are protected." (24 words - Pass)

Jargon: **Needs Attention** - Several technical terms lack explanation on first use:
- "docker container" (not explained)
- "EC2, ECS, EKS" (not explained; abbreviations)
- "S3 buckets" (not explained)
- "instance type" (not explained)
- "master salt and encryption keys" (not explained)
- "pass-through mode" (not explained)
- "self-signed certificate" (not explained)

Active Voice: **Pass** - Most content uses active voice effectively ("Ensure your machine...", "Click Download File...", "Do not skip this step...")

Heading Clarity: **Pass** - Headings are clear and action-oriented (Step 1, Step 2, etc.), though "Step 4" appears truncated in the provided text

Link Text: **Needs Attention** - Generic link text found:
- "here" (in "You can see all of the EC2 types that AWS provides here") - Should specify "View AWS EC2 instance types"

Abbreviations: **Needs Attention** - Multiple unexplained abbreviations:
- AWS (appears to be assumed knowledge)
- EC2, ECS, EKS (not defined)
- S3 (not defined)
- OS (not defined)
- CLI (not defined)
- SSL (not defined)

Overall WCAG Writing Score: **Needs Attention**

---