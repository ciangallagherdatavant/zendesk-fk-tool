# FK Analysis Result

**Article:** Introduction to Datavant Tokens
**Date:** 02 April 2026 15:11
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Introduction to Datavant Tokens

SCORE: 12.0
Reading Level: High School Advanced
Target Audience: Readers with advanced high school education or higher; professionals working with healthcare data systems

Summary: This article sits at the maximum acceptable complexity level for technical documentation and would be challenging for general audiences without specialized knowledge.

FK RECOMMENDATIONS:
✓ Content meets the Grade 12 target threshold. Well done! The article successfully balances technical accuracy with readability, maintaining an average of 15.6 words per sentence and 1.82 syllables per word. This is appropriate for a technical healthcare security topic. To maintain or improve this score, continue using clear examples (like "John Smith, Male, 03/27/1968") and breaking complex processes into numbered steps.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention**
- "Tokens are encrypted" - sentence appears incomplete at the end
- "Master Token is encrypted with a site-specific key to generate the final encrypted patient token" contains nested technical concepts that could be simplified
- Consider: "The Master Token is then encrypted using a unique key for each site. This creates the final patient token."

Sentence Length: **Pass**
- Longest sentence is 24 words ("Identical patient information always produces the same Master Token, but site-specific encryption ensures each site creates a unique token, or a site-specific token, for the same patient")
- Most sentences are well under 25 words

Jargon: **Needs Attention**
- "PII" - abbreviated on first use without definition
- "soundex" - unexplained technical term
- "SHA-256 irreversible hash function" - technical term without plain language explanation
- "de-identified" - used before clear definition
- "Master Token" - concept introduced but could use simpler explanation

Active Voice: **Pass**
- Good use of active voice throughout ("Tokens allow organizations to link," "Tokens are generated in three steps")
- Passive constructions used appropriately for technical processes

Heading Clarity: **Pass**
- Clear hierarchical structure with descriptive headings
- "What are Datavant tokens?" directly answers user questions
- Process steps clearly numbered and labeled

Link Text: **Good**
- "Token Error Log File" is descriptive
- "Required Data Pre-Processing" is specific and clear
- No vague "click here" or "read more" links found

Abbreviations: **Needs Attention**
- "PII" - used extensively but never defined in the provided text
- "CLI" - defined contextually as "Datavant CLI v5" but acronym not spelled out
- "v4" and "v5" - version abbreviations are acceptable

Overall WCAG Writing Score: **Needs Attention**

Primary issues: Define PII on first use, explain technical terms like "soundex" and "SHA-256 hash function" in plain language, and complete the final incomplete sentence about token encryption.