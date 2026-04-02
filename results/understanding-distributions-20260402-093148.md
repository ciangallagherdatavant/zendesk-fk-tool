# FK Analysis Result

**Article:** Understanding Distributions
**Date:** 02 April 2026 09:31
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Understanding Distributions

SCORE: 14.8
Reading Level: College level
Target Audience: Readers with college-level reading ability; too complex for general business users

Summary: This article requires a college-level education to read comfortably, which exceeds the recommended Grade 12 target for technical documentation.

FK RECOMMENDATIONS:

This content scores above the Grade 12 target and needs simplification. Here are 3 specific suggestions:

1. **Break up complex sentences with multiple clauses**
   - Current: "Distribution enables a simple and efficient process for Datavant partners to deliver and receive data tables using one single integration instead of having to manage multiple integrations with multiple recipients."
   - Suggested: "Distribution simplifies data delivery. Datavant partners can deliver and receive data tables using one integration. This eliminates the need to manage multiple integrations with different recipients."

2. **Simplify technical explanations with nested conditions**
   - Current: "While Datavant performs some basic format checks on the fields that are processed during data onboarding, some fields (e.g. clinical values) may be configured to pass through without modification."
   - Suggested: "Datavant performs basic format checks during data onboarding. However, some fields pass through without modification. Examples include clinical values."

3. **Split compound sentences listing multiple items**
   - Current: "Distribution is the default tool when delivering Match results, Token Exports, or receiving remediated Privacy Hub tables."
   - Suggested: "Distribution is the default tool for these tasks: delivering Match results, delivering Token Exports, and receiving remediated Privacy Hub tables."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Multiple instances of complex phrasing such as "remediated Privacy Hub tables," "pass through without modification," and "data tables must be certified in order to distribute data." Consider: "Privacy Hub tables that have been cleaned" and "data tables need certification before you can distribute them."

Sentence Length: **Needs Attention** - Several sentences exceed 25 words:
- "Distribution enables a simple and efficient process for Datavant partners to deliver and receive data tables using one single integration instead of having to manage multiple integrations with multiple recipients." (31 words)
- "While Datavant performs some basic format checks on the fields that are processed during data onboarding, some fields (e.g. clinical values) may be configured to pass through without modification." (31 words)
- "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file." (21 words - borderline)

Jargon: **Needs Attention** - Unexplained technical terms:
- "PHI" (appears without definition; later context suggests Protected Health Information)
- "remediated" (used multiple times without explanation)
- "certified" (in context of data tables)
- "ingestion" (technical database term)
- "Token Exports"
- "Overlap report"
- "trimming a single table"

Active Voice: **Needs Attention** - Multiple passive constructions found:
- "Distributions can only be enabled by Datavant" → "Only Datavant can enable Distributions"
- "some fields...may be configured to pass through" → "we configure some fields to pass through"
- "Files are distributed shortly after ingestion" → "Datavant distributes files shortly after the source partner sends them"

Heading Clarity: **Pass** - The main title "Understanding Distributions" is clear, and the subheading "How to Manage Distributions" accurately describes the section content.

Link Text: **Pass** - Link text appears descriptive: "Pick up Distributed Data," "Request an External File Push," "Send Distributed Data to a Partner."

Abbreviations: **Needs Attention**:
- "PHI" - not defined on first use
- "e.g." - used in parenthetical; spell out as "for example" for better accessibility

Overall WCAG Writing Score: **Needs Attention**

---