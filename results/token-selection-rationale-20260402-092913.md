# FK Analysis Result

**Article:** Token Selection Rationale
**Date:** 02 April 2026 09:29
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Token Selection Rationale

SCORE: 14.5
Reading Level: College level
Target Audience: Readers with college-level education; too complex for general technical audiences

Summary: This article requires a college sophomore reading level, which exceeds the recommended Grade 12 maximum for technical documentation and may exclude many legitimate users from understanding critical token selection guidance.

FK RECOMMENDATIONS:

This content exceeds the Grade 12 target. Here are three specific suggestions:

1. **Break down long, complex sentences**: The sentence "Confident standardization is stricter, matching only name variations that are closely similar, which leads to higher precision" (17 words) can be split: "Confident standardization is stricter. It matches only name variations that are closely similar. This leads to higher precision."

2. **Simplify terminology introductions**: The phrase "Different tokens produce different false positive and false negative rates when used to match records across tables" uses technical jargon without definition. Revise to: "Different tokens have different accuracy levels. Some may match records that shouldn't match (false positives). Others may miss records that should match (false negatives)."

3. **Reduce sentence complexity in definitions**: The sentence "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched" (29 words) should be: "Probabilistic matching uses values that aren't unique on their own. When combined, these values create a high probability of finding the correct match."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Terms like "cascading or hierarchical token matching," "theoretically 100% unique," and "metaphone standardization" are introduced without sufficient explanation for non-expert readers.

Sentence Length: **Flag** - Several sentences exceed 25 words:
- "Different tokens produce different false positive and false negative rates when used to match records across tables." (18 words - acceptable)
- "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched." (29 words - **exceeds limit**)
- "Errors can occur due to data entry mistakes (such as a mistyped SSN) or limitations in the dataset (for example, SSNs may be missing from many records)." (27 words - **exceeds limit**)

Jargon: **Needs Attention** - Unexplained or under-explained terms:
- "Cascading or hierarchical token matching" (no definition)
- "Metaphone" (mentioned but explanation appears cut off)
- "zip3" (abbreviation not explained)
- "Soundex" (technical term not defined)
- "Recall" vs "precision" (used in definition but assumes prior knowledge)

Active Voice: **Pass** - Most sentences use active voice appropriately. One minor instance: "Errors can occur" could be "Data entry mistakes can cause errors."

Heading Clarity: **Pass** - Headings are clear and action-oriented ("Use deterministic tokens first," "Use probabilistic tokens from common fields").

Link Text: **Cannot assess** - No link text present in the cleaned prose provided.

Abbreviations: **Needs Attention**:
- "PII" - defined on first use ✓
- "SSN" - defined on first use ✓
- "DOB" - **not defined** (Date of Birth assumed)
- "zip3" - **not defined**

Overall WCAG Writing Score: **Needs Attention**

---