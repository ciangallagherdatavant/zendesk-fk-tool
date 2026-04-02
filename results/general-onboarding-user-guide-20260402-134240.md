# FK Analysis Result

**Article:** General Onboarding User Guide
**Date:** 02 April 2026 13:42
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: General Onboarding User Guide

SCORE: 12.0
Reading Level: High School Advanced
Target Audience: Advanced high school readers or college-level readers; acceptable for technical documentation but at the upper limit of recommended complexity.

Summary: This article sits exactly at the Grade 12 threshold, making it accessible to most technical users but leaving no margin for further complexity.

FK RECOMMENDATIONS:
✓ Content meets the Grade 12 target threshold—well done! However, since you're at the maximum recommended level with no buffer, consider these refinements to improve accessibility:

1. **Break down compound sentences with multiple clauses.** For example: "If you are onboarding data to receive an Expert Determination from Privacy Hub, refer to the Privacy Hub Data Upload User Guide if you need to tokenize your data, or the Streamlined Privacy Hub Onboarding Flow if you do not need to tokenize your data" could be split into separate sentences for each condition.

2. **Simplify technical definitions.** The explanation "Flattened Parquet files remove nested structures and arrays by transforming data into a single-level format" uses multiple technical concepts in one sentence. Consider: "Flattened Parquet files have a simple, single-level format. They convert nested data structures into flat columns."

3. **Use shorter introductory phrases.** Replace "Data Onboarding is the process of uploading a deidentified, tokenized data table to the Datavant Connect Platform for the following purposes:" with "Data Onboarding uploads deidentified, tokenized data tables to Datavant Connect. Use it for:"

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "deidentified, tokenized data table" appears without initial explanation
- "expert determination certifying it as de-identified" uses legal jargon without context
- "flat and delimited" assumes technical knowledge

**Sentence Length:** Flagged
- "If you are onboarding data to receive an Expert Determination from Privacy Hub, refer to the Privacy Hub Data Upload User Guide if you need to tokenize your data, or the Streamlined Privacy Hub Onboarding Flow if you do not need to tokenize your data." (46 words)
- "To onboard a tokenized data table to the Datavant Connect platform, tokens must be first converted to a datavant transit encryption key." (22 words - acceptable but dense)

**Jargon:** Flagged - unexplained terms include:
- "tokenized" (first use)
- "deidentified" (first use)
- "transit encryption key"
- "CLI" (mentioned but not expanded in visible text)
- "nested structures and arrays"
- "dot-delimited keys"
- "millisecond/second timestamps vs microsecond and nanosecond timestamps"

**Active Voice:** Needs Attention
- "Data uploaded to the platform must either..." (passive)
- "Tokens must be in the datavant..." (passive)
- "tokens must be first converted to..." (passive)
- Consider: "You must convert tokens to..." or "Convert tokens to..."

**Heading Clarity:** Pass
Headings are descriptive and scannable (Overview, Onboarding Requirements, File Size Limitations)

**Link Text:** Needs Attention
- "access it here" is vague and non-descriptive
- Better: "access the onboarding demo video here"

**Abbreviations:** Flagged
- "CLI" appears without expansion on first use (Desktop App is spelled out, CLI should be too: "Command Line Interface (CLI)")
- File extensions (.csv, .parquet, etc.) are standard and acceptable

Overall WCAG Writing Score: Needs Attention

**Priority fixes:** Expand "CLI" on first use, replace "access it here" with descriptive link text, define "tokenized" and "deidentified" at first mention, and break the 46-word sentence into multiple sentences.

---