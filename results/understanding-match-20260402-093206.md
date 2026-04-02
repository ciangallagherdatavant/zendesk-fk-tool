# FK Analysis Result

**Article:** Understanding Match
**Date:** 02 April 2026 09:32
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Understanding Match

SCORE: 12.1
Reading Level: High School Advanced
Target Audience: Readers with advanced high school or early college-level reading ability

Summary: This article is just slightly above the ideal complexity target for technical documentation and may be challenging for some general business users.

FK RECOMMENDATIONS:

The content is very close to the Grade 12 target (only 0.1 points over), which is commendable. However, minor refinements could bring it to the ideal range:

1. **Break down complex definitions**: The sentence "Datavant Match provides precise Privacy-Preserving Record Linkage (PPRL) by securely connecting data at the patient level" combines technical terminology with abstract concepts. Consider: "Datavant Match connects patient records securely. This is called Privacy-Preserving Record Linkage (PPRL)."

2. **Simplify the DVID explanation**: "Match assigns a consistent, locally encrypted Datavant ID (DVID) to each tokenized patient record" contains multiple technical layers. Try: "Match assigns each patient record a unique Datavant ID (DVID). This ID is encrypted and stays consistent across your data."

3. **Clarify the data pool concept**: "Each Match run creates its own unique data pool...the resulting DVIDs will differ from those in other runs and cannot be linked to DVIDs from previous or future Match runs" could be simplified to: "Each Match run creates its own data pool. The DVIDs from one run are unique to that run. You cannot link them to DVIDs from other runs."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several instances of unnecessary complexity:
- "resolves these different tokens into the same Datavant ID" (jargon-heavy)
- "locally encrypted Datavant ID" (technical without explanation)
- "enabling enterprise-wide identification resolution" (business jargon)

Sentence Length: **Pass** - Most sentences are well under 25 words. The average of 16.4 words per sentence is excellent.

Jargon: **Needs Attention** - Several technical terms lack immediate explanation:
- "tokenized records" (used before adequate explanation)
- "precision and recall" (statistical terms not defined)
- "referential data" (mentioned but not explained in the truncated text)
- "de-identified" (assume knowledge)
- "matching thresholds" (not defined until mentioned in context)

Active Voice: **Pass** - Predominantly uses active voice. Examples: "Match assigns," "Datavant distributes," "Match offers."

Heading Clarity: **Good** - Headings are clear and descriptive ("What is Match?", "Key benefits", "Perform a Match job")

Link Text: **Pass** - Link references are contextual: "see Understanding Distributions" and "see How to Run Match" provide clear navigation cues.

Abbreviations: **Needs Attention**:
- PPRL (expanded on first use ✓)
- DVID (expanded on first use ✓)
- PII (not expanded - mentioned once without definition)

Overall WCAG Writing Score: **Needs Attention**

The article demonstrates good structure and sentence length control but would benefit from simpler explanations of technical concepts and ensuring all jargon is defined before use, especially for readers who may be new to data matching concepts.

---