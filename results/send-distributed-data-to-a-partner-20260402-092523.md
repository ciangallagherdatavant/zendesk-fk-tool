# FK Analysis Result

**Article:** Send Distributed Data to a Partner
**Date:** 02 April 2026 09:25
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Send Distributed Data to a Partner

SCORE: 12.2
Reading Level: High School Advanced
Target Audience: Readers with advanced high school or some college-level reading ability

Summary: This article is just above the ideal target range for technical documentation, requiring a near-college reading level that may challenge some users.

FK RECOMMENDATIONS:
The content is slightly above the Grade 12 target (by 0.2 points), which puts it at the threshold of acceptability. Here are 3 specific suggestions to bring it comfortably below Grade 12:

1. **Break down compound sentences with multiple clauses.** Example: "If your Company Profile is visible and you would like to indicate to other partners you have loaded one or more complete data tables and are ready/willing to distribute to partners when needed, go to your Company Settings to turn the tag on." (41 words) → Split into: "Does your Company Profile show to others? You can indicate you are ready to distribute data. Go to your Company Settings to turn this tag on."

2. **Simplify technical explanations.** Example: "While Datavant performs some basic format checks on the fields that are processed, some fields (e.g. clinical values) may be configured to pass through without modification." → "Datavant checks some fields for format errors. However, some fields (like clinical values) pass through without any checks."

3. **Reduce word density in warning statements.** Example: "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file." (21 words) → "Warning: If you place PHI values in pass-through fields, they may leak into the output file." (16 words)

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some phrases are unnecessarily complex: "onboarded to" (use "uploaded to"), "remediations applied" (use "fixes applied" or "corrections made"), "distributions can only be enabled by Datavant" (use "only Datavant can enable distributions")

Sentence Length: **Flagged** - Two sentences exceed 25 words:
- "If your Company Profile is visible and you would like to indicate to other partners you have loaded one or more complete data tables and are ready/willing to distribute to partners when needed, go to your Company Settings to turn the tag on." (41 words)
- "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file." (21 words - acceptable but at limit)

Jargon: **Needs Attention** - Several terms lack immediate explanation:
- "PHI" (only appears in warning, never defined - should be "PHI (Protected Health Information)")
- "site keys" (never explained)
- "segment" (used without definition)
- "ingestion" (technical term that could be simplified to "upload")

Active Voice: **Flagged** - Multiple passive constructions found:
- "Data must be onboarded" → "You must onboard data"
- "Data tables must be certified" → "You must certify data tables"
- "some fields may be configured" → "Datavant may configure some fields"
- "Distributions can only be enabled" → "Only Datavant can enable distributions"
- "Files will be distributed" → "The system distributes files"

Heading Clarity: **Pass** - Step-based headings are clear and actionable, though "Step 2 (Optional)" could be "Step 2 (Optional): Show You're Ready to Distribute"

Link Text: **Pass** - Link text appears descriptive ("Understanding Distributions", "General Onboarding User Guide", "Manage your Company Profile in Explore")

Abbreviations: **Flagged** - "PHI" is used without being spelled out on first use. In a security-critical context, this abbreviation must be defined.

Overall WCAG Writing Score: **Needs Attention**

The article has good structure but requires work on plain language, passive voice reduction, and jargon explanation to meet accessibility standards. The slightly elevated FK score aligns with these accessibility concerns.

---