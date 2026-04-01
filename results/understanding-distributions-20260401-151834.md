# FK Analysis Result

**Article:** Understanding Distributions
**Date:** 01 April 2026 15:18
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Understanding Distributions

SCORE: 14.8
Reading Level: College level
Target Audience: Readers with college-level education; too complex for general business users

Summary: This article requires a college-level reading ability, which is above the recommended Grade 12 target for technical documentation and may exclude many users who need to understand the Distribution tool.

FK RECOMMENDATIONS:

This content exceeds the Grade 12 target and needs simplification. Here are 3 specific suggestions:

1. **Break down complex sentences with multiple clauses**
   - Current: "Distribution enables a simple and efficient process for Datavant partners to deliver and receive data tables using one single integration instead of having to manage multiple integrations with multiple recipients."
   - Suggested: "Distribution simplifies data delivery. Partners can use one single integration to deliver and receive data tables. This replaces managing multiple integrations with multiple recipients."

2. **Simplify technical warnings and explanations**
   - Current: "While Datavant performs some basic format checks on the fields that are processed during data onboarding, some fields (e.g. clinical values) may be configured to pass through without modification."
   - Suggested: "Datavant checks some field formats during data onboarding. However, some fields pass through without modification. For example, clinical values may not be checked."

3. **Use shorter, more direct sentences in procedural sections**
   - Current: "Companies have the ability to set the "Distribution Ready" tag on their visible Company Profile to indicate that they have loaded one or more complete data tables and are ready/willing to distribute to partners when needed."
   - Suggested: "Companies can set a "Distribution Ready" tag on their Company Profile. This tag shows they have complete data tables loaded. It also shows they are ready to distribute to partners."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- Heavy use of product-specific terminology without adequate context (e.g., "certified," "onboarding," "ingestion")
- Compound noun phrases create cognitive load: "Ecosystem Explore page," "visible Company Profile"

**Sentence Length:** Needs Attention
- Several sentences exceed 25 words:
  - "Distribution enables a simple and efficient process for Datavant partners to deliver and receive data tables using one single integration instead of having to manage multiple integrations with multiple recipients." (30 words)
  - "While Datavant performs some basic format checks on the fields that are processed during data onboarding, some fields (e.g. clinical values) may be configured to pass through without modification." (31 words)
  - "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file." (21 words - acceptable but at the limit)
  - "Companies have the ability to set the "Distribution Ready" tag on their visible Company Profile to indicate that they have loaded one or more complete data tables and are ready/willing to distribute to partners when needed." (38 words)

**Jargon:** Needs Attention
- Unexplained terms: "certified" (in context of data tables), "onboarding," "ingestion," "remediated," "Token Export," "PHI," "pass-through fields"
- "Match run results" and "Overlap report" assume prior product knowledge

**Active Voice:** Needs Attention
- Passive constructions found:
  - "Distributions can only be enabled by Datavant"
  - "some fields...may be configured to pass through"
  - "Files are distributed shortly after ingestion"

**Heading Clarity:** Pass
- Main heading "Understanding Distributions" is clear
- Subheading "How to Manage Distributions" is action-oriented and helpful

**Link Text:** Pass
- Link text appears descriptive: "Pick up Distributed Data," "Request an External File Push," "Send Distributed Data to a Partner"

**Abbreviations:** Needs Attention
- "PHI" is not defined on first use (should be "Protected Health Information (PHI)")

Overall WCAG Writing Score: Needs Significant Work

---