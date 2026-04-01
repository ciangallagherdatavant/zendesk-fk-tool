# FK Analysis Result

**Article:** Use Datavant Natively on AWS EC2
**Date:** 01 April 2026 15:12
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Use Datavant Natively on AWS EC2

SCORE: 12.1
Reading Level: High School Advanced
Target Audience: Readers with advanced high school to early college reading ability; technical professionals

Summary: This article just slightly exceeds the ideal readability target for technical documentation, requiring an advanced high school reading level due to technical terminology and sentence complexity.

FK RECOMMENDATIONS:
The content is very close to the target threshold (12.0 or below) and only marginally exceeds it. Here are three specific suggestions to bring it under Grade 12:

1. **Break down compound sentences with multiple clauses**: 
   - Current: "The AWS Native Tokenization is a docker container built to be deployed on either EC2, ECS, or EKS."
   - Simpler: "The AWS Native Tokenization is a docker container. You can deploy it on EC2, ECS, or EKS."

2. **Simplify technical explanations**:
   - Current: "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate."
   - Simpler: "If you have a proxy server, configure it to pass through the SSL certificate from Datavant's endpoints. Do not let it pass back its own self-signed certificate."

3. **Reduce prepositional phrases**:
   - Current: "It has added functionality to directly read from and write to S3 buckets in the account that the docker container is running in."
   - Simpler: "It can read from and write to S3 buckets in your account."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "appropriately sized" is vague (what does this mean?)
- "pass-through mode" assumes technical knowledge
- "intercepting the incoming SSL certificate" could be simplified to "blocking the SSL certificate"

**Sentence Length:** Pass
No sentences exceed 25 words. Average sentence length is well-controlled at 17.3 words.

**Jargon:** Needs Attention
Unexplained technical terms include:
- Docker container (not explained for non-technical readers)
- EC2, ECS, EKS (AWS services mentioned without context)
- S3 buckets (AWS term not defined)
- M5.xlarge (instance type not explained)
- OS (operating system abbreviation)
- AWS CLI (command line interface not spelled out)
- Port 443 (technical networking term)
- SSL certificate (security term not explained)
- Self-signed certificate (advanced concept)
- Master salt and encryption keys (cryptographic terms)

**Active Voice:** Pass
Most sentences use active voice effectively. One flagged example:
- "is a docker container built to be deployed" (passive) → could be "is a docker container you deploy"

**Heading Clarity:** Pass
Step-based headings are clear and action-oriented (Step 1, Step 2, etc.)

**Link Text:** Needs Attention
- "here" is vague link text (should be "view all EC2 instance types" or similar)
- "the below command" references content not shown in provided text

**Abbreviations:** Needs Attention
- AWS (defined in title context but not in body)
- EC2, ECS, EKS (not spelled out)
- OS (not spelled out)
- CLI (not spelled out)
- SSL (not spelled out)

Overall WCAG Writing Score: Needs Attention

---