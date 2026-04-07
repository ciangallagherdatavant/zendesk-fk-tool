# FK Analysis Result

**Article:** Token Selection Rationale
**Date:** 07 April 2026 08:21
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Token Selection Rationale

SCORE: 14.5
Reading Level: College level
Target Audience: Readers with some college education or specialized technical training

Summary: This article requires a college-level reading ability, which exceeds the recommended Grade 12 target for technical documentation and may be challenging for some users.

FK RECOMMENDATIONS:

This content exceeds the Grade 12 target and should be simplified. Here are three specific suggestions:

1. **Break down complex technical sentences**: The sentence "Confident standardization is stricter, matching only name variations that are closely similar, which leads to higher precision" (19 words) combines multiple concepts. Split it: "Confident standardization is stricter. It matches only name variations that are closely similar. This leads to higher precision."

2. **Simplify nested explanations**: The sentence "Errors can occur due to data entry mistakes (such as a mistyped SSN) or limitations in the dataset (for example, SSNs may be missing from many records)" (27 words) contains embedded examples. Revise to: "Errors can occur due to data entry mistakes, such as a mistyped SSN. Errors also happen when SSNs are missing from records."

3. **Front-load key information**: The sentence "Datavant's software can generate multiple types of tokens from PII (Personally Identifiable Information) in a table" buries the PII definition. Revise to: "PII is Personally Identifiable Information. Datavant's software can generate multiple types of tokens from PII in a table."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Heavy use of technical terminology without upfront definitions (e.g., "cascading or hierarchical token matching," "false positive and false negative rates," "Soundex," "metaphone," "zip3")

Sentence Length: **Flagged** - One sentence exceeds 25 words:
- "Errors can occur due to data entry mistakes (such as a mistyped SSN) or limitations in the dataset (for example, SSNs may be missing from many records)." (27 words)

Jargon: **Needs Attention** - Multiple unexplained technical terms:
- "cascading or hierarchical token matching"
- "Soundex" (explained later but used in token lists first)
- "metaphone" (explained later but used in token lists first)
- "zip3"
- "recall" vs "precision" (precision explained, recall not defined)

Active Voice: **Pass** - Mostly uses active voice effectively ("We recommend," "You should prioritize")

Heading Clarity: **Pass** - Headings are clear and descriptive ("Use deterministic tokens first," "Use probabilistic tokens from common fields")

Link Text: **Cannot assess** - No link text present in cleaned prose

Abbreviations: **Needs Attention** - Some abbreviations defined well (PII, SSN, DOB), but:
- "zip3" is never explained
- Abbreviations used in token descriptions without consistent definition placement

Overall WCAG Writing Score: **Needs Attention**