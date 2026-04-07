# FK Analysis Result

**Article:** Security Architecture and Amazon's Secrets Managers Service
**Date:** 07 April 2026 09:31
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Security Architecture and Amazon's Secrets Managers Service

SCORE: 10.9
Reading Level: High School (approaching High School Advanced)
Target Audience: Readers with a high school education or higher, comfortable with technical security concepts

Summary: This article scores 10.9, indicating high school level complexity that is accessible to most technical audiences and meets the target of Grade 12 or below.

FK RECOMMENDATIONS:
The content successfully meets the readability target. Here are three specific suggestions to improve it further:

1. **Break down compound technical processes**: The sentence "When Datavant's applications request a secret, Secrets Manager: Fetches the encryption key. Transmits the secret securely over TLS." uses a colon-list format that could be clearer as a standard sentence or bulleted list. Consider: "When Datavant's applications request a secret, Secrets Manager performs two actions: it fetches the encryption key and transmits the secret securely over TLS."

2. **Simplify multi-clause sentences**: "Only a small group of Datavant team members can access this environment, and they cannot run Datavant software" could be split for clarity: "Only a small group of Datavant team members can access this environment. These team members cannot run Datavant software."

3. **Add brief definitions for technical terms**: While "TLS" and "encryption key" are standard security terms, consider adding parenthetical explanations on first use to support broader audiences, such as "Transmits the secret securely over TLS (Transport Layer Security, a security protocol)."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several phrases use technical jargon without explanation: "persistent storage," "tokens using a client's encryption scheme," and "TTP environment" (explained later but could be clearer upfront).

Sentence Length: **Pass** - Most sentences are concise. The longest sentence is approximately 22 words ("To communicate with Datavant's TTP AWS environment, you must configure your network when running Datavant CLI or Datavant Desktop"), which is acceptable.

Jargon: **Needs Attention** - Multiple unexplained technical terms: "secrets" (in security context), "TLS," "persistent storage," "tokens," "encryption scheme," "CLI." While appropriate for technical audiences, brief contextual definitions would improve accessibility.

Active Voice: **Pass** - The article predominantly uses active voice effectively: "Datavant uses," "AWS generates," "Secrets Manager encrypts," "Datavant runs."

Heading Clarity: **Pass** - The title clearly indicates the topic. Consider adding subheadings to break up the content (e.g., "How Secrets Manager Works," "Access Controls," "Network Configuration").

Link Text: **Needs Attention** - The phrase "see Technical Requirements to Run Datavant Software" is functional but could be more descriptive, such as "see network setup requirements for Datavant software."

Abbreviations: **Needs Attention** - Several abbreviations lack first-use expansion: "TLS," "AWS" (expanded once but not at first use), "CLI." "TTP" is expanded as "Trusted Third Party" which is good practice.

Overall WCAG Writing Score: **Needs Attention**
---