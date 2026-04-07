# FK Analysis Result

**Article:** Understanding Match
**Date:** 07 April 2026 09:28
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Understanding Match

SCORE: 12.1
Reading Level: High School Advanced (bordering College level)
Target Audience: Readers with advanced high school or some college education; technical professionals familiar with data concepts

Summary: This article just exceeds the Grade 12 target for technical documentation, requiring a high school senior or early college reading level to read comfortably.

FK RECOMMENDATIONS:

1. **Break down compound sentences with multiple clauses.** For example, "When you run selected data tables through a Match job, Datavant Match uses high precision and recall to determine whether two de-identified, tokenized records in the same table, or across multiple tables, represent the same person" (33 words) could be split into: "When you run selected data tables through a Match job, Datavant Match analyzes the records. It determines whether two de-identified, tokenized records represent the same person. These records may be in the same table or across multiple tables."

2. **Replace technical compound phrases with simpler alternatives.** Change "Privacy-Preserving Record Linkage (PPRL)" to "secure record linking" on first reference, and "locally encrypted Datavant ID" to "encrypted Datavant ID" (removing the modifier "locally" which adds complexity without clarity for most users).

3. **Simplify the data pool explanation.** The sentence "Because each Match run creates its own data pool, the resulting DVIDs will differ from those in other runs and cannot be linked to DVIDs from previous or future Match runs" uses complex subordinate structure. Revise to: "Each Match run creates its own data pool. The DVIDs from one run will differ from other runs. You cannot link DVIDs across different Match runs."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Several instances of complex technical phrasing: "Privacy-Preserving Record Linkage (PPRL)," "high precision and recall," "de-identified, tokenized records," "referential data," and "configurable matching thresholds" appear without adequate plain-language explanation.

**Sentence Length:** Mostly Pass - Most sentences are under 25 words. One flagged exception: "When you run selected data tables through a Match job, Datavant Match uses high precision and recall to determine whether two de-identified, tokenized records in the same table, or across multiple tables, represent the same person" (43 words).

**Jargon:** Needs Attention - Multiple unexplained terms: "precision and recall" (data science metrics), "de-identified," "tokenized," "referential data," "data pool," "matching thresholds," "data standardization and quality protocols," and "enterprise-wide identification resolution."

**Active Voice:** Pass - Article predominantly uses active voice ("Datavant Match provides," "Match assigns," "Datavant distributes"). No significant passive constructions detected.

**Heading Clarity:** Pass - Headings are clear and descriptive: "What is Match?", "Key benefits", "Perform a Match job", "Referential Data". They effectively preview content.

**Link Text:** Pass - Link text is descriptive: "Understanding Distributions" and "How to Run Match" clearly indicate destination content.

**Abbreviations:** Needs Attention - PPRL is explained on first use (good), DVID is explained on first use (good), but PII appears in "Even when underlying PII changes" without prior definition or expansion.

Overall WCAG Writing Score: Needs Attention

---