# FK Analysis Result

**Article:** Understanding the Profile Model
**Date:** 02 April 2026 14:00
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Understanding the Profile Model

SCORE: 12.7
Reading Level: High School Advanced (approaching College level)
Target Audience: Readers with advanced high school or some college education; professionals familiar with technical healthcare documentation

Summary: This article is slightly above the ideal target of Grade 12 or below for technical writing, requiring a high level of reading comprehension that may challenge some users in the healthcare data management field.

FK RECOMMENDATIONS:

**1. Break down complex, multi-clause sentences**
Example from text: "Onboarding certain Profile Model fields to the Datavant Connect platform, along with tokens, unlocks extra capabilities."
Suggested revision: "You can onboard certain Profile Model fields to the Datavant Connect platform. Onboard them along with tokens. This unlocks extra capabilities."

**2. Simplify technical terminology clusters**
Example from text: "tables must contain only the variables listed in the Profile Model (or a subset of them) and all required remediations must be applied"
Suggested revision: "Tables must contain only the variables listed in the Profile Model. You may use a subset of these variables. Apply all required remediations."

**3. Use shorter, more direct phrasing**
Example from text: "If your table contains additional variables, they require further review by Expert Determination to either certify the data as de-identified or to confirm that the data is not covered by HIPAA."
Suggested revision: "Does your table contain additional variables? Expert Determination must review them. The review will certify the data as de-identified. Or it will confirm that HIPAA does not cover the data."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "Expert Determination" used repeatedly without initial definition
- "remediations" used as technical jargon without clear explanation
- "de-identified under HIPAA" assumes prior knowledge
- "auto-certification" not explained

**Sentence Length:** Pass with minor concerns
Most sentences are under 25 words. One concern:
- "If your table contains additional variables, they require further review by Expert Determination to either certify the data as de-identified or to confirm that the data is not covered by HIPAA." (32 words)

**Jargon:** Needs Attention
Unexplained technical terms:
- Expert Determination (used throughout, never defined)
- de-identified
- remediations (plural usage unclear)
- tokens/tokenization
- Zip3 (mentioned without explanation)
- PHI (appears at end without definition)
- granular Assess reports
- Match performance
- auto-certification

**Active Voice:** Needs Attention
Passive constructions found:
- "has been certified as de-identified" → suggest "Expert Determination certified as de-identified"
- "are provided in the Profile Model" → suggest "The Profile Model provides details"
- "are available to provide flexibility" → suggest "Four remediation sets provide flexibility"
- "is only considered de-identified" → suggest "We only consider the table de-identified"
- "if PHI is placed in these fields" → suggest "if you place PHI in these fields"

**Heading Clarity:** Pass
Headings are clear and descriptive (Overview, Profile Model fields, How to Use the Profile Model, Step 1/2/3)

**Link Text:** Needs Attention
- "email support@datavant.com" - email address used as link text (acceptable but could be "contact Datavant support")
- Multiple references to "linked at the end of this guide" without descriptive link text visible in the provided content

**Abbreviations:** Needs Attention
Unexplained abbreviations:
- HIPAA (first use should be spelled out)
- ICD-10
- NDC
- CPT
- HCPCS
- PHI (appears only once at end, unexplained)
- "Zip3" (abbreviation of 3-digit Zip code, not explained)

Overall WCAG Writing Score: Needs Attention

**Priority improvements:** Define "Expert Determination" and "remediations" on first use, expand all abbreviations on first mention, convert passive voice to active voice, and add brief explanations for technical terms that are essential to understanding the process.

---