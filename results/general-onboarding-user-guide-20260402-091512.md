# FK Analysis Result

**Article:** General Onboarding User Guide
**Date:** 02 April 2026 09:15
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: General Onboarding User Guide

SCORE: 12.0
Reading Level: High School Advanced
Target Audience: Readers with an advanced high school education or higher; comfortable with complex technical content

Summary: This article sits at the upper limit of acceptable technical writing (Grade 12), meaning it requires a strong reading ability and may challenge some users.

FK RECOMMENDATIONS:
✓ Content meets the Grade 12 target threshold - well done! However, since you're at the maximum acceptable level, consider these refinements to improve accessibility:

1. **Break down dense introductory sentences** - The opening sentence lists five purposes in one go: "Data Onboarding is the process of uploading a deidentified, tokenized data table to the Datavant Connect Platform for the following purposes: Assess: conduct overlaps, overlap comparisons, overlap stack, and profile reporting Ecosystem Explore: showcase a data asset to potential partners..." Consider using a bulleted list after a shorter introduction.

2. **Simplify compound requirements** - "Data uploaded to the platform must either: Have an expert determination certifying it as de-identified Adhere to Datavant's pre-certified Profile Model, or Not be covered by HIPAA" could be split into clearer, standalone statements.

3. **Reduce technical stacking** - Phrases like "deidentified, tokenized data table" and "millisecond/second timestamps" pack multiple technical concepts together. Where possible, introduce concepts separately before combining them.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "tokenized data table," "datavant-[your_site] transit encryption key," and "expert determination" lack explanations
- "Nested data is currently not supported" vs "What is .parquet (flattened only)?" - provide upfront definition
- Consider explaining "de-identified" on first use

**Sentence Length:** Pass
- Average 20.4 words per sentence is well within guidelines
- No flagged sentences over 25 words detected in the sample

**Jargon:** Needs Attention
Unexplained technical terms found:
- tokenized/tokens
- de-identified/deidentified
- expert determination
- transit encryption key
- flat and delimited
- nested data
- parquet files
- dot-delimited keys
- millisecond/second timestamps vs microsecond/nanosecond timestamps

**Active Voice:** Pass
- Primarily uses active constructions ("This article will review," "Run the transform tokens command")
- Passive uses are appropriate ("Data must be certified," "Files must be flat")

**Heading Clarity:** Pass
- Clear hierarchical structure: "Overview," "Onboarding Requirements," "Important Considerations"
- Headings accurately describe content beneath them

**Link Text:** Needs Attention
- "click the play button below or access it here" - "here" is vague link text
- Recommend: "watch the onboarding demo video" or "access the onboarding demo"

**Abbreviations:** Needs Attention
Unexplained abbreviations:
- HIPAA (first use should spell out: Health Insurance Portability and Accountability Act)
- CLI (first use should spell out: Command Line Interface)
- File extensions (.csv, .parquet, etc.) - consider brief expansion on first use

Overall WCAG Writing Score: Needs Attention

**Priority fixes:** Define HIPAA and CLI on first use, replace vague "here" link text, and add brief explanations for core concepts like "tokenized" and "de-identified" early in the article.

---