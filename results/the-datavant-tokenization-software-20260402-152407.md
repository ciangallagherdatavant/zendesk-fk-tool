# FK Analysis Result

**Article:** The Datavant Tokenization Software
**Date:** 02 April 2026 15:24
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: The Datavant Tokenization Software

SCORE: 12.9
Reading Level: High School Advanced (approaching College level)
Target Audience: Readers with advanced high school to college-level reading ability, comfortable with technical content

Summary: This article narrowly exceeds the Grade 12 target for technical documentation and would benefit from simplification to reach a broader technical audience.

FK RECOMMENDATIONS:

While the score of 12.9 is very close to the target threshold, it still exceeds Grade 12. Here are three specific suggestions to bring it below 12:

1. **Break down compound sentences with multiple clauses:**
   - Current: "Creates transit tokens by transforming tokens from a site-specific encryption key into a transit encryption key that is unique to both the sender and the intended recipient."
   - Suggested: "Creates transit tokens. This transforms tokens from a site-specific encryption key. The new transit encryption key is unique to both the sender and recipient."

2. **Simplify technical definitions:**
   - Current: "Datavant's tokenization software generates tokens, or de-identified patient keys, using different combinations of patient demographic information such as name, date of birth, administrative gender, and social security number."
   - Suggested: "Datavant's tokenization software creates tokens (de-identified patient keys). It uses patient information like name, date of birth, gender, and social security number."

3. **Reduce nested explanatory phrases:**
   - Current: "Transform tokens for use within Datavant tools such as Assess, Ecosystem Explorer, Segment Builder, Match, or Distribution."
   - Suggested: "Transform tokens for Datavant tools. These tools include Assess, Ecosystem Explorer, Segment Builder, Match, and Distribution."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- Phrases like "transit encryption key that is unique to both the sender and the intended recipient" and "site-specific encryption key derived from patient demographics" are complex
- Consider defining "transit tokens" and "site-specific tokens" earlier with simpler language

**Sentence Length:** Pass
- Average of 18.1 words per sentence is well within acceptable range
- No sentences appear to significantly exceed 25 words

**Jargon:** Needs Attention
- "Tokenizing" - explained with context
- "First-party data" - not explained
- "Transit tokens" - used before clear definition
- "Site-specific encryption key" - technical term not simplified
- "De-identification operations" - not explained
- "PII" - abbreviation used but not defined on first use

**Active Voice:** Pass with minor flags
- Most content uses active voice effectively
- One passive construction: "These functions are carried out through three core operations" (could be: "Three core operations carry out these functions")

**Heading Clarity:** Pass
- Headings are descriptive and hierarchical
- "About the Datavant Tokenization Software" clearly introduces the topic
- "Tokenize and transform" effectively summarizes the section content

**Link Text:** Needs Attention
- "see the General Onboarding User Guide" - acceptable but generic
- "see Defining the Configuration Output Operations" - acceptable
- Consider making link text more descriptive of what users will find

**Abbreviations:** Needs Attention
- "CLI" - explained in context (Command Line Interface implied)
- "PII" - used in heading "Creating Tokens from PII" but never defined (should be "Personally Identifiable Information")

Overall WCAG Writing Score: Needs Attention

The article has good structural elements and reasonable sentence length, but would benefit from defining technical terms more clearly, explaining all abbreviations on first use (especially PII), and simplifying complex technical phrases for broader accessibility.

---