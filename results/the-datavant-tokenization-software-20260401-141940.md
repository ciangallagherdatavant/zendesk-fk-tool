# FK Analysis Result

**Article:** The Datavant Tokenization Software
**Date:** 01 April 2026 14:19
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: The Datavant Tokenization Software

SCORE: 12.9
Reading Level: High School Advanced (approaching College level)
Target Audience: Readers with advanced high school to early college education; professionals comfortable with technical documentation

Summary: This article requires a college-level reading ability, which is just slightly above the ideal target of Grade 12 or below for technical documentation.

FK RECOMMENDATIONS:

The article is very close to the target threshold (only 0.9 points above Grade 12), but could benefit from minor simplification to reach a broader technical audience. Here are three specific suggestions:

1. **Break down complex noun phrases**: Change "Creates site-specific tokens using a site-specific encryption key derived from patient demographics" to "Creates site-specific tokens. These tokens use an encryption key. The key is derived from patient demographics." This separates one complex idea into three simpler sentences.

2. **Simplify purpose statements**: The phrase "Applies de-identification operations to identified data, run by sites on their own first-party data" could become "Sites run this operation on their own first-party data to remove identifying information."

3. **Use simpler connectors**: Change "Creates transit tokens by transforming tokens from a site-specific encryption key into a transit encryption key that is unique to both the sender and the intended recipient" to "Creates transit tokens. It transforms tokens from a site-specific key to a transit key. This transit key is unique to the sender and recipient."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- Heavy use of technical compound phrases: "site-specific encryption key," "de-identification operations," "transit encryption key"
- The phrase "The original underlying PII tokenized in your site are equal to the transform received tokens result in your site" is particularly unclear and grammatically awkward
- Consider adding a glossary or defining key terms inline

**Sentence Length:** Pass
- Most sentences are under 25 words
- Average of 18.1 words per sentence is good
- No problematic run-on sentences detected

**Jargon:** Needs Attention
Unexplained technical terms include:
- "tokens" (defined as "de-identified patient keys" but concept needs clearer explanation)
- "PII" (not spelled out as Personally Identifiable Information)
- "site-specific encryption key"
- "transit tokens" vs "site tokens"
- "first-party data"
- "Datavant Connect," "Assess," "Ecosystem Explorer," "Segment Builder" (product names used without context)

**Active Voice:** Needs Attention
Several passive constructions found:
- "is available on limited release"
- "is highlighted in purple callout boxes"
- "It's required for the following purposes"
- "are carried out through three core operations"
- "are used in a simple matching use case"

**Heading Clarity:** Pass
Headings are descriptive and hierarchical ("Overview," "About the Datavant Tokenization Software," "Tokenize and transform"). However, "Deployment Methods" section appears incomplete in the provided text.

**Link Text:** Needs Attention
- "see the General Onboarding User Guide" - acceptable but generic
- "see Defining the Configuration Output Operations" - acceptable
- The incomplete sentence at the end suggests there may be links missing from the cleaned text

**Abbreviations:** Needs Attention
- "PII" appears without being spelled out on first use
- "CLI" appears in the callout but is spelled out as "CLI-specific" without defining what CLI means (Command Line Interface)

Overall WCAG Writing Score: Needs Attention

The article has good sentence structure and organization but needs work on plain language, jargon explanation (especially PII and CLI), and reducing passive voice. The awkward sentence about "original underlying PII" should be rewritten for clarity and grammatical correctness.

---