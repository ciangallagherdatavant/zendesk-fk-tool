# FK Analysis Result

**Article:** Send Distributed Data to a Partner
**Date:** 02 April 2026 15:20
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Send Distributed Data to a Partner

SCORE: 12.2
Reading Level: High School Advanced
Target Audience: Advanced high school readers and college-level audiences with strong reading comprehension skills

Summary: This article is just slightly above the ideal target range for technical documentation, requiring college-level reading skills that may challenge some users.

FK RECOMMENDATIONS:
The content is marginally above the Grade 12 target (by 0.2 points), but improvements can still enhance accessibility:

1. **Break down complex conditional sentences**: The sentence "While Datavant performs some basic format checks on the fields that are processed, some fields (e.g. clinical values) may be configured to pass through without modification" contains multiple clauses. Simplify to: "Datavant performs basic format checks on processed fields. However, some fields (like clinical values) may pass through without modification."

2. **Simplify compound warning statements**: The sentence "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file" uses passive-adjacent construction. Revise to: "Incorrectly placing PHI values in pass-through fields can leak data into the output file."

3. **Reduce prepositional phrase chains**: "If your Company Profile is visible and you would like to indicate to other partners you have loaded one or more complete data tables..." can become: "If your Company Profile is visible, you can show partners that you have complete data tables ready to distribute."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some bureaucratic phrasing found: "must be approved if the Distribution tool can be enabled for your use case" could be simplified to "must be approved for your project."

Sentence Length: **Pass** - While some sentences approach the limit, most stay under 25 words. The longest is manageable at approximately 35 words (the PHI leakage warning), but consider splitting it.

Jargon: **Needs Attention** - Several unexplained technical terms:
- "PHI values" (not defined on first use)
- "pass-through fields" (technical concept not explained)
- "remediations" (unclear in this context)
- "site keys" (not defined)
- "ingestion" (technical term not explained)

Abbreviations: **Needs Attention** - "PHI" is used without expansion on first use (should be "Protected Health Information (PHI)")

Active Voice: **Needs Attention** - Several passive constructions found:
- "Data must be onboarded" → "You must onboard data"
- "must be certified" → "You must certify data tables"
- "may be configured" → "Datavant may configure some fields"
- "can only be enabled by Datavant" → "Only Datavant can enable distributions"
- "Files will be distributed" → "The system distributes files"

Heading Clarity: **Pass** - Step-based headings are clear and follow a logical sequence. Consider making them more action-oriented (e.g., "Step 1: Onboard Data" instead of "Step 1. Onboard Data...")

Link Text: **Pass** - Link text appears descriptive ("Understanding Distributions," "General Onboarding User Guide," "Managing Users For Your Company")

Overall WCAG Writing Score: **Needs Attention**

The article would benefit most from defining technical terms on first use, converting passive voice to active voice, and simplifying complex warning statements. These changes would also likely bring the FK score comfortably below 12.0.

---