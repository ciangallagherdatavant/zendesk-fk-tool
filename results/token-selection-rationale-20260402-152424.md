# FK Analysis Result

**Article:** Token Selection Rationale
**Date:** 02 April 2026 15:24
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Token Selection Rationale

SCORE: 14.5
Reading Level: College level
Target Audience: Readers with college-level education or specialized technical training

Summary: This article requires a college-level reading ability, which is above the recommended Grade 12 target for technical documentation and may be difficult for many users to understand.

FK RECOMMENDATIONS:

**1. Break down complex sentences with multiple clauses**
- Current example: "Confident standardization and fuzzy standardization both handle variations in how names are written."
- Improved: "Confident standardization handles name variations. Fuzzy standardization also handles name variations. However, they work differently."

**2. Simplify technical explanations by using shorter, clearer sentences**
- Current example: "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched."
- Improved: "Probabilistic matching uses values that may not be unique. These values work together. Combined, they give a high probability of a correct match."

**3. Replace or define complex terminology upfront**
- Current example: "Tokens 1, 2, 5, and 101–111" appears before readers understand what tokens are
- Improved: Add a brief definition box at the top: "Token: A coded representation of personal information used for matching records"

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- Heavy use of unexplained technical concepts (deterministic, probabilistic, soundex, metaphone)
- Complex phrasing: "theoretically 100% unique" could be "always unique"
- "In priority order" could be "most important first"

**Sentence Length:** Needs Attention
- "Datavant's software can generate multiple types of tokens from PII (Personally Identifiable Information) in a table." (16 words - Pass)
- "Probabilistic matching is matching that uses values that may not be unique, however when used in combination, they provide a high probability that the correct individual is matched." (30 words - **Flag**)
- "Confident standardization is stricter, matching only name variations that are closely similar, which leads to higher precision." (17 words - Pass, but complex structure)

**Jargon:** Needs Attention
- Unexplained or under-explained terms: "cascading or hierarchical token matching," "Soundex," "metaphone," "zip3," "recall," "precision"
- PII is defined on first use (Good)
- SSN defined on first use (Good)

**Active Voice:** Pass with minor flags
- Mostly uses active voice effectively
- One passive example: "calculated by Python textstat" (though this is in metadata, not article)

**Heading Clarity:** Good
- "Use deterministic tokens first" - clear and actionable
- "Use probabilistic tokens from common fields" - clear and actionable
- "Introduction to token selection" - descriptive

**Link Text:** Unable to assess
- No link text present in cleaned prose to evaluate

**Abbreviations:** Needs Attention
- PII - defined ✓
- SSN - defined ✓
- DOB - **not defined** (appears in Token 5 description without explanation)
- zip3 - **not defined**

Overall WCAG Writing Score: Needs Attention

---