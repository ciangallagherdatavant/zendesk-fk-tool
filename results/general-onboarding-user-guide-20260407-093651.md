# FK Analysis Result

**Article:** General Onboarding User Guide
**Date:** 07 April 2026 09:36
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: General Onboarding User Guide

SCORE: 12.0
Reading Level: High School Advanced
Target Audience: High school seniors and college-level readers with technical familiarity

Summary: This article sits at the maximum acceptable complexity threshold for technical documentation and would benefit from simplification to reach a broader audience.

FK RECOMMENDATIONS:
The content meets the Grade 12 target threshold, but here are three specific suggestions to improve readability further:

1. **Break down complex compound sentences**: The sentence "Data uploaded to the platform must either: Have an expert determination certifying it as de-identified Adhere to Datavant's pre-certified Profile Model, or Not be covered by HIPAA" combines multiple conditions in a way that increases cognitive load. Split this into separate, clearly numbered requirements (1. Have an expert determination... 2. Adhere to Datavant's... 3. Not be covered by HIPAA).

2. **Simplify technical explanations**: The definition "Flattened Parquet files remove nested structures and arrays by transforming data into a single-level format" uses abstract technical language. Rewrite as: "Flattened Parquet files convert complex, multi-layered data into a simple, single-level table format."

3. **Reduce multi-clause sentences**: The sentence "Nested fields are flattened into dot-delimited keys (e.g., Address.Street), while arrays are either combined into a single string (e.g.,"Lupus, Rheumatoid Arthritis, Psoriasis") or expanded into multiple rows" contains 28 words with multiple subordinate clauses. Break into two sentences: "Nested fields become dot-delimited keys (e.g., Address.Street). Arrays are either combined into a single string or expanded into multiple rows."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Terms like "deidentified, tokenized data table," "overlap stack," "flat and delimited," and "dot-delimited keys" appear without initial explanation. The phrase "datavant-[your_site] transit encryption key" assumes substantial prior knowledge.

Sentence Length: **Needs Attention** - One sentence exceeds 25 words: "Nested fields are flattened into dot-delimited keys (e.g., Address.Street), while arrays are either combined into a single string (e.g.,"Lupus, Rheumatoid Arthritis, Psoriasis") or expanded into multiple rows" (28 words).

Jargon: **Needs Attention** - Unexplained technical terms include: "tokenized," "deidentified," "overlap stack," "profile reporting," "flat and delimited," "nested data," "dot-delimited keys," "transit encryption key," "CLI," "millisecond/second timestamps," and "microsecond and nanosecond timestamps."

Active Voice: **Pass** - The article primarily uses active voice constructions. Minor passive uses are appropriate in context (e.g., "Data must be certified").

Heading Clarity: **Pass** - Headings are descriptive and informative ("Onboarding Requirements," "Important Considerations on Parquet Files," "File Size Limitations").

Link Text: **Needs Attention** - The phrase "access it here" is vague link text. Should specify destination like "access the onboarding demo video."

Abbreviations: **Needs Attention** - "HIPAA," "CLI," ".csv," ".parquet," ".xml," ".pdf" appear without first spelling out the full term. "CLI" particularly needs explanation as "Command Line Interface."

Overall WCAG Writing Score: **Needs Attention**