# FK Analysis Result

**Article:** Reviewing the Tokenization Software Output and Log Files
**Date:** 07 April 2026 09:24
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Reviewing the Tokenization Software Output and Log Files

SCORE: 9.7
Reading Level: High School
Target Audience: High school students and general adult readers with moderate technical familiarity

Summary: This article reads at a 10th-grade level, making it accessible to most professional audiences and well within the target range for technical documentation.

FK RECOMMENDATIONS:
The content successfully meets the target grade level of 12 or below. To improve readability further, consider these specific refinements:

1. **Break down compound sentences with multiple clauses.** For example, "The output from transform-tokens from is a file (or files) in which the tokens have been transformed, or re-encrypted, from a transit encryption key that is shared between your site and your partner site, to your site-specific encryption key" contains multiple embedded clauses. Split this into: "The output from transform-tokens from is a file (or files) with transformed tokens. These tokens have been re-encrypted from a transit encryption key to your site-specific encryption key. The transit key is shared between your site and your partner site."

2. **Simplify technical compound nouns.** Phrases like "site-specific encryption key" and "transit encryption key" appear repeatedly. Consider introducing a shorthand after first use (e.g., "site key" and "transit key") or creating a glossary box to reduce cognitive load.

3. **Make the "Overview" section more scannable.** The opening paragraph contains several distinct ideas (recommendation to review output, error handling, article purpose, troubleshooting resources). Break this into 2-3 shorter paragraphs with clear topic sentences to improve comprehension.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some sentences use complex constructions. Example: "Note that the output from the on-premise application depends on which operation you've run, and any errors will be sent to the console (if console output is enabled) and will also be visible in the dev log" could be simplified to separate ideas more clearly.

Sentence Length: **Needs Attention** - Several sentences exceed 25 words:
- "Datavant always recommends reviewing the output after running the Datavant tokenization software as it's important to check the appropriate remediations are applied and ensure high-quality and valid tokens are included in the output file(s)." (32 words)
- "While Datavant performs some basic format checks on the fields that are processed, some fields (e.g. clinical values) may be configured to pass through without modification." (28 words)
- "The output from transform-tokens from is a file (or files) in which the tokens have been transformed, or re-encrypted, from a transit encryption key that is shared between your site and your partner site, to your site-specific encryption key." (42 words)

Jargon: **Needs Attention** - Several technical terms lack explanation on first use:
- "remediations" (used multiple times without definition)
- "tokenization" (assumed knowledge)
- "PHI values" (acronym explained nowhere in the visible text)
- "transit encryption key" vs "site-specific encryption key" (the distinction is unclear)
- "dev log" (abbreviation of "development"?)

Active Voice: **Needs Attention** - Multiple passive constructions found:
- "is available on limited release" → "we offer on limited release"
- "will be sent to the console" → "the system sends to the console"
- "has had remediations applied to it" → "includes applied remediations"
- "has been transformed appropriately" → "you have transformed appropriately"

Heading Clarity: **Pass** - Headings clearly describe content sections (Outputs, Tokenize, Transform-tokens to/from, Dev Log File)

Link Text: **Pass** - Email addresses are descriptive (support@datavant.com). Reference to "available troubleshooting articles" could be more specific if it's an actual link.

Abbreviations: **Needs Attention** - Unexplained abbreviations found:
- "PHI" (Protected Health Information - should be spelled out on first use)
- "CLI" (Command Line Interface - mentioned but not explained)
- "v5" (version 5 - clear from context but could be spelled out)

Overall WCAG Writing Score: **Needs Attention**

---