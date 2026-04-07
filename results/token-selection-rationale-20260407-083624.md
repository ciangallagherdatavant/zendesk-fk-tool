# FK Analysis Result

**Article:** Token Selection Rationale
**Date:** 07 April 2026 08:36
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Token Selection Rationale

SCORE: 14.5
Reading Level: College level
Target Audience: College-educated readers with technical background or specialized training in data matching concepts

Summary: This article requires a college-level reading ability and is too complex for the general audience, exceeding the recommended Grade 12 maximum for technical documentation.

FK RECOMMENDATIONS:

This content exceeds the Grade 12 target. Here are 3 specific suggestions:

1. **Break down complex compound sentences**: The sentence "Confident standardization is stricter, matching only name variations that are closely similar, which leads to higher precision" (19 words) combines multiple concepts. Split into: "Confident standardization is stricter. It matches only name variations that are closely similar. This leads to higher precision."

2. **Simplify technical explanations**: The phrase "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched" is dense. Rewrite as: "Probabilistic matching uses multiple data points together. Each point alone may not be unique. But combining them helps identify the correct person."

3. **Reduce multi-clause sentences**: The sentence "Errors can occur due to data entry mistakes (such as a mistyped SSN) or limitations in the dataset (for example, SSNs may be missing from many records)" contains nested examples. Simplify to: "Errors can happen. Data entry mistakes like mistyped SSNs cause problems. Missing data also reduces accuracy."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Heavy use of technical terminology without sufficient context for non-experts. Terms like "cascading or hierarchical token matching," "false positive and false negative rates," and "zip3" assume specialized knowledge.

Sentence Length: **Needs Attention** - Multiple sentences exceed 25 words:
- "Different tokens produce different false positive and false negative rates when used to match records across tables." (17 words - acceptable)
- "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched." (29 words - **too long**)
- "Confident standardization is stricter, matching only name variations that are closely similar, which leads to higher precision." (17 words - acceptable)
- Several token description bullets contain parenthetical information that increases cognitive load

Jargon: **Needs Attention** - Unexplained or insufficiently explained terms:
- "PII" (defined in parentheses, good practice)
- "cascading or hierarchical token matching" (not defined)
- "false positive and false negative rates" (not defined)
- "zip3" (not defined - unclear what this means)
- "Soundex" (not defined)
- "Metaphone" (not defined)
- "metaphone standardization" (partial explanation at end, but comes after first use)
- "Administrative Gender" (not defined)
- "precision" vs "recall" (used without definition)

Active Voice: **Pass with minor concerns** - Mostly active voice used effectively. One passive construction: "Errors can occur due to data entry mistakes" could be "Data entry mistakes cause errors."

Heading Clarity: **Pass** - Headings are clear and descriptive ("Use deterministic tokens first," "Use probabilistic tokens from common fields")

Link Text: **Cannot assess** - No link text present in the cleaned prose provided

Abbreviations: **Needs Attention**:
- "PII" - expanded on first use ✓
- "SSN" - expanded on first use ✓
- "DOB" - **never expanded** (used extensively throughout)
- "zip3" - **never explained**

Overall WCAG Writing Score: **Needs Attention**

The article makes good structural choices with clear headings and some definitions, but requires work on sentence complexity, comprehensive jargon definitions (especially DOB and zip3), and reducing technical density for broader accessibility.

---