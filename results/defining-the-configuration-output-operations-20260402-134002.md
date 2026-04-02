# FK Analysis Result

**Article:** Defining the Configuration Output Operations
**Date:** 02 April 2026 13:40
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Defining the Configuration Output Operations

SCORE: 12.7
Reading Level: High School Advanced (bordering College level)
Target Audience: Readers with advanced high school education or some college experience, familiar with technical healthcare data concepts

Summary: This article is just above the ideal target range for technical documentation and may be challenging for some readers due to complex sentence structures and dense technical explanations.

FK RECOMMENDATIONS:

The content is slightly above the Grade 12 target. Here are three specific suggestions to improve readability:

1. **Break down the long warning paragraph**: The second paragraph beginning with "While remediations can remove personal information..." contains 67 words in a single sentence. Split this into shorter sentences:
   - Current: "While Datavant performs some basic format checks on the fields that are processed, some fields (e.g. clinical values) may be configured to pass through without modification."
   - Suggested: "Datavant performs basic format checks on processed fields. However, some fields (such as clinical values) may pass through without modification."

2. **Simplify the Expert Determination example**: The sentence "For example, a common de-identifying operation per the Expert Determination method of HIPAA requires the Date of Birth field to use both Convert to Year of Date and Limit Max Age" is 32 words and contains nested concepts. Rewrite as: "For example, HIPAA's Expert Determination method commonly requires two operations on Date of Birth: Convert to Year of Date and Limit Max Age."

3. **Clarify the Null Low Population Zip3 description**: The explanation runs 37 words with embedded census terminology. Break it into two sentences with clearer structure.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "Remediations are operations that transform PII contained within your table into a less precise form" - uses abstract phrasing
- "certified as 'de-identified' under HIPAA by expert determination or Global Safe Harbor" - multiple unexplained technical concepts in one phrase
- "incorrectly placing PHI values in these pass-through fields could result in leakage into the output file" - "leakage" is jargon in this context

**Sentence Length:** Needs Attention
- Several sentences exceed 25 words:
  - "While Datavant performs some basic format checks..." (40 words)
  - "For example, a common de-identifying operation..." (32 words)
  - "The Safe Harbor provision requires..." (37 words)
  - Opening sentence in Overview (19 words - acceptable but dense)

**Jargon:** Needs Attention - Unexplained terms:
- PII (defined as "personally identifiable information" - good)
- PHI (not defined, different from PII)
- HIPAA (not defined)
- Expert Determination (capitalized but not explained)
- Global Safe Harbor (not explained)
- Safe Harbor provision (mentioned separately from Global Safe Harbor, unclear relationship)
- ZCTA (defined as "ZIP Code Tabulation Area" - good)
- Decennial Census (could say "10-year census")
- ICD9, ICD10, ZIP3 (not defined)

**Active Voice:** Needs Attention
- "it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage" (passive construction)
- "this is done by clicking" (passive)
- "Periods in the ICD code are not included" (passive)
- Most operation descriptions use passive voice: "is replaced with NULL," "are applied"

**Heading Clarity:** Pass
- Clear section headings: "Overview" and "Output Operations"
- Table structure provides clear organization of operations

**Link Text:** Unable to assess
- No link text appears in the cleaned prose text provided

**Abbreviations:** Needs Attention
- PHI - not defined (different from PII which is defined)
- HIPAA - not defined
- ICD - not defined (appears as ICD9, ICD10)
- ZIP3, ZCTA - ZIP3 not defined, ZCTA is defined
- NULL - technical term not explained for non-technical readers

Overall WCAG Writing Score: Needs Attention

---