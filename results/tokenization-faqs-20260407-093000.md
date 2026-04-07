# FK Analysis Result

**Article:** Tokenization FAQs
**Date:** 07 April 2026 09:30
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Tokenization FAQs

SCORE: 10.7
Reading Level: High School (upper level)
Target Audience: Readers with high school or higher education; comfortable with technical concepts and moderate complexity

Summary: This content is approaching the upper limit of acceptable complexity for technical documentation and should be simplified to reach a broader audience.

FK RECOMMENDATIONS:

1. **Break down complex sentences with multiple clauses.** For example, "We recommend using the number of threads such that each process is at ~95% CPU usage without exceeding the number of cores on your machine" contains multiple technical conditions in one sentence. Split this into: "We recommend using multiple threads. Each process should run at ~95% CPU usage. Do not exceed the number of cores on your machine."

2. **Simplify technical explanations with shorter, direct statements.** The sentence "Datavant's applications are CPU-intensive, and the token creation and transformation processes are expensive, encryption-based operations" combines three concepts. Revise to: "Datavant's applications use a lot of CPU power. Token creation and transformation use encryption. These are resource-heavy operations."

3. **Replace complex conditional phrasing with simpler alternatives.** Change "When a PII element used to make a token is missing from the input, a valid token will not be generated" to "Missing PII elements result in error tokens, not valid tokens."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several instances of unnecessarily complex phrasing: "environments optimized for heavy computing," "encryption-based operations," "data quality statistics are surfaced in the data quality log"

Sentence Length: **Needs Attention** - Several sentences exceed 25 words:
- "We recommend using the number of threads such that each process is at ~95% CPU usage without exceeding the number of cores on your machine." (27 words)
- "When a PII element used to make a token is missing from the input, a valid token will not be generated." (19 words but grammatically complex)

Jargon: **Needs Attention** - Multiple technical terms lack explanation: "multithreading flag," "command line argument," "CPU-intensive," "encryption-based operations," "Cloud Provider native applications," "Snowflake Warehouse"

Active Voice: **Pass** - Most sentences use active voice effectively ("Ensure your machine is sized appropriately," "Turn off other background processes")

Heading Clarity: **Pass** - Questions are clear and specific, formatted as FAQ entries that directly match user concerns

Link Text: **Needs Attention** - Some link references are vague: "cloud performance articles" (should specify which articles), "the token error log" (could include hint about where to find it)

Abbreviations: **Needs Attention** - Several abbreviations introduced without full explanation on first use: "RAM," "CPU," "PHI/PII" (only used in heading, not explained)

Overall WCAG Writing Score: **Needs Attention**