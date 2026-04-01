# FK Analysis Result

**Article:** Token Selection Rationale
**Date:** 01 April 2026 14:18
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Token Selection Rationale

SCORE: 14.5
Reading Level: College level
Target Audience: Readers with college-level education or specialized technical training

Summary: This article requires a college-level reading ability, which is above the recommended Grade 12 target for technical documentation and may exclude some intended users.

FK RECOMMENDATIONS:

Since the score exceeds Grade 12, here are three specific suggestions to improve readability:

1. **Break down long, complex sentences**: The sentence "Confident standardization and fuzzy standardization both handle variations in how names are written. Confident standardization is stricter, matching only name variations that are closely similar, which leads to higher precision. Fuzzy standardization, however, is more flexible." contains multiple clauses and could be simplified to shorter, clearer statements like: "Confident standardization handles name variations. It is stricter. It matches only closely similar names. This gives higher precision."

2. **Simplify technical explanations**: The phrase "Different tokens produce different false positive and false negative rates when used to match records across tables" uses complex statistical terminology without context. Revise to: "Different tokens vary in accuracy. Some may match records that don't belong together (false positives). Others may miss records that should match (false negatives)."

3. **Reduce average sentence length**: With an average of 24.3 words per sentence, aim to break longer sentences into shorter ones. For example, the 35-word sentence "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched" should be split: "Probabilistic matching uses values that may not be unique. When combined, these values provide a high probability of matching the correct individual."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language**: Needs Attention - Multiple instances of complex technical language without sufficient plain-language alternatives: "cascading or hierarchical token matching," "theoretically 100% unique," "higher precision than probabilistic matching"

**Sentence Length**: Needs Attention - Several sentences exceed 25 words:
- "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched." (30 words)
- "In practice, this often involves using names, birth dates, and other identifying values together to improve match accuracy." (18 words - acceptable)
- Multiple technical token descriptions contain compound structures pushing boundaries

**Jargon**: Needs Attention - Several unexplained or inadequately explained terms:
- "Soundex" and "Metaphone" (mentioned but not clearly explained)
- "zip3" (no explanation provided)
- "false positive and false negative rates" (used before adequate context)
- "DOB" (abbreviated without first spelling out)

**Active Voice**: Pass - Most sentences use active voice appropriately ("You should prioritize," "We recommend selecting")

**Heading Clarity**: Pass - Headings clearly describe content ("Use deterministic tokens first," "Use probabilistic tokens from common fields")

**Link Text**: Cannot assess - No link text present in cleaned prose

**Abbreviations**: Needs Attention:
- "PII" - explained on first use ✓
- "SSN" - explained on first use ✓
- "DOB" - never spelled out as "Date of Birth"
- "zip3" - never explained

Overall WCAG Writing Score: Needs Attention

---