# FK Analysis Result

**Article:** Send Distributed Data to a Partner
**Date:** 01 April 2026 15:19
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Send Distributed Data to a Partner

SCORE: 12.2
Reading Level: High School Advanced
Target Audience: Readers with advanced high school to college-level reading skills, comfortable with technical documentation

Summary: This article sits just above the ideal target for technical documentation and may present moderate reading challenges for some users due to sentence complexity and technical density.

FK RECOMMENDATIONS:

While close to the Grade 12 target, this article would benefit from minor simplification:

1. **Break down complex sentences with multiple clauses** - Example: "While Datavant performs some basic format checks on the fields that are processed, some fields (e.g. clinical values) may be configured to pass through without modification." Split this into two sentences: "Datavant performs some basic format checks on the fields that are processed. However, some fields (e.g. clinical values) may be configured to pass through without modification."

2. **Simplify multi-part conditional statements** - Example: "If your Company Profile is visible and you would like to indicate to other partners you have loaded one or more complete data tables and are ready/willing to distribute to partners when needed, go to your Company Settings to turn the tag on." Break into steps or shorter sentences with clearer action points.

3. **Reduce prepositional phrase stacking** - Example: "Distributions can only be enabled by Datavant and must be approved if the Distribution tool can be enabled for your use case." Simplify to: "Datavant must enable and approve the Distribution tool for your use case."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Some sentences are overly complex. Example: "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file" could be simplified to "If you incorrectly place PHI values in these pass-through fields, they may leak into the output file."

**Sentence Length:** Flag - Several sentences exceed 25 words:
- "If your Company Profile is visible and you would like to indicate to other partners you have loaded one or more complete data tables and are ready/willing to distribute to partners when needed, go to your Company Settings to turn the tag on." (43 words)
- "While Datavant performs some basic format checks on the fields that are processed, some fields (e.g. clinical values) may be configured to pass through without modification." (28 words)
- "Therefore, it is possible that incorrectly placing PHI values in these pass-through fields could result in leakage into the output file." (23 words - acceptable but near limit)

**Jargon:** Needs Attention - Several technical terms lack explanation:
- PHI (appears without definition)
- Site keys
- Segment (in data context)
- Pass-through fields
- Remediations

**Active Voice:** Flag - Multiple passive constructions found:
- "Data must be onboarded" (consider: "You must onboard data")
- "Distributions can only be enabled by Datavant" (consider: "Datavant must enable distributions")
- "Files will be distributed" (consider: "The system distributes files")

**Heading Clarity:** Pass - Headings are clear, numbered, and action-oriented (Step 1, Step 2, etc.)

**Link Text:** Pass - Link text is descriptive ("Understanding Distributions," "General Onboarding User Guide," "Manage your Company Profile in Explore")

**Abbreviations:** Flag - "PHI" is used without first defining it as "Protected Health Information (PHI)"

Overall WCAG Writing Score: Needs Attention

---