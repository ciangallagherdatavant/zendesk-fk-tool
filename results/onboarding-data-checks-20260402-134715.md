# FK Analysis Result

**Article:** Onboarding Data Checks
**Date:** 02 April 2026 13:47
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Onboarding Data Checks

SCORE: 12.1
Reading Level: High School Advanced
Target Audience: Readers with near-college level reading ability; may be challenging for general audiences

Summary: This article requires a high school advanced reading level (Grade 12.1), which is at the upper threshold of acceptable technical documentation and may present comprehension barriers for some users.

FK RECOMMENDATIONS:
The content just slightly exceeds the Grade 12 target (by 0.1), but is close to acceptable. However, improvements would benefit a broader audience:

1. **Break down complex compound sentences**: The sentence "Data that does not comply will cause file failures during ingestion which will need to be resolved before attempting to re-ingest again" could be simplified to "Data that does not comply will cause file failures. Resolve these failures before re-ingesting."

2. **Simplify technical phrasing**: Replace "data being ingested into the Datavant Portal" with "data uploaded to the Datavant Portal" and "data checks are performed when" with "we check data when."

3. **Restructure the opening paragraph**: The explanation about general onboarding vs. Privacy Hub tables uses complex nested clauses. Consider bullet points: "General onboarding data tables are:
   - Onboarded to the Datavant portal
   - Already certified under an existing expert determination
   - All tables onboarded before February 2023"

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "certified under an existing expert determination" - consider explaining or simplifying
- "ingested into" - use "uploaded to" or "loaded into"
- "Unenclosed double quotes" - consider "double quotes without enclosures" or provide example

**Sentence Length:** Pass
No sentences exceed 25 words. Average of 17.7 words per sentence is good.

**Jargon:** Needs Attention
Unexplained technical terms:
- "expert determination" (legal/compliance term)
- "transform tokens"
- "token-specified columns"
- "Multiline Detection"
- SNOMED CUIs (Concept Unique Identifiers) - partially explained but appears cut off

**Active Voice:** Pass
Most sentences use active voice appropriately ("data checks are performed" could be "we perform data checks" but is acceptable in context)

**Heading Clarity:** Needs Attention
- "Background" heading could be more descriptive: "Why Data Checks Are Required" or "Data Check Requirements"
- Missing visible headings for the data type requirements section (dates of birth, diagnosis codes, etc.)

**Link Text:** Insufficient Information
Reference to "Privacy Hub Data Upload User Guide" appears to be link text but context is unclear from cleaned prose

**Abbreviations:** Needs Attention
Several abbreviations lack first-use explanation:
- HIPAA (appears without expansion)
- ICD-9, ICD-10 (industry standard but should define)
- CPT/HCPCS, DRG, NPI, LOINC, NDC (listed without explanation)
- SNOMED CT (partially explained later but not at first use)

Overall WCAG Writing Score: Needs Attention

---