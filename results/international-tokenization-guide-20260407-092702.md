# FK Analysis Result

**Article:** International Tokenization Guide
**Date:** 07 April 2026 09:27
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: International Tokenization Guide

SCORE: 10.1
Reading Level: High School
Target Audience: Readers with a high school education or above, comfortable with moderately complex technical content

Summary: This article reads at a 10th-grade level, which is appropriate for technical documentation and falls within the recommended target of Grade 12 or below.

FK RECOMMENDATIONS:
The content meets the readability target. Here are three specific suggestions to improve it further:

1. **Break down compound sentences with multiple clauses.** For example: "Datavant's tokenization engine creates tokens, or de-identified patient keys, from different permutations of patient demographics, such as name, date of birth, gender, and social security number" could be split into two sentences: "Datavant's tokenization engine creates tokens (de-identified patient keys). These tokens are generated from patient demographics such as name, date of birth, gender, and social security number."

2. **Simplify the operation definitions.** The three operations (tokenize, transform-tokens to, transform-tokens from) are described in very dense sentences with semicolons. Each definition should be its own short paragraph with the action separated from the context. For example, split "creates transit tokens by transforming tokens from a site-specific encryption key to a transit encryption key that is specific to the sender and intended recipient; run by sites prior to sending any tokens outside their environment to partners" into two sentences.

3. **Replace technical phrases with simpler alternatives where possible.** For instance, "appropriately sized" could be "large enough," and "accessible outbound over port 443" could be explained more plainly as "accessible for outgoing connections on port 443."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Heavy use of technical jargon without upfront definitions. Terms like "transit encryption key," "site-specific encryption key," "de-identification operations," and "downstream linking" appear without context or explanation.

Sentence Length: **Pass with caution** - Most sentences are under 25 words due to good average sentence length (14.0 words). However, several complex sentences exist, such as: "The tokenization engine comes in several modes that, depending on your requirements and use case, can be deployed on-premise or in the Datavant cloud" (24 words but densely packed).

Jargon: **Needs Attention** - Unexplained technical terms include: "tokenization engine," "de-identified patient keys," "patient demographics," "transit tokens," "site-specific encryption key," "transit encryption key," "CLI," "batch mode," "on-premise," "proxy server," "pass-through mode," "cryptographic secrets," "master salt."

Active Voice: **Pass** - The article predominantly uses active voice ("creates tokens," "run by sites," "install the CLI"). Minimal passive constructions found.

Heading Clarity: **Good** - Headings like "Determine How to Use the Datavant Tokenization Engine" and "Step 1. Complete technical pre-requisites for on-premise software" clearly indicate content that follows.

Link Text: **Cannot assess** - The cleaned prose text doesn't indicate how links are formatted in the original article (e.g., "refer to Use Datavant CLI in Batch Mode" may be a link but context is unclear).

Abbreviations: **Needs Attention** - "CLI" is defined on first use (Command Line Interface), but "OS" is not defined. "RAM," "GHz," and version abbreviations ("v18.04.6") are used without explanation.

Overall WCAG Writing Score: **Needs Attention**