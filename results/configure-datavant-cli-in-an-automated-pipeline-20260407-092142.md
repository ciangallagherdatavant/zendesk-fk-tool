# FK Analysis Result

**Article:** Configure Datavant CLI in an Automated Pipeline
**Date:** 07 April 2026 09:21
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Configure Datavant CLI in an Automated Pipeline

SCORE: 11.9
Reading Level: High School Advanced
Target Audience: Advanced high school readers or those with similar reading proficiency; approaching college-level complexity

Summary: This article is just below the Grade 12 target threshold, making it accessible to most technical users but with room for simplification.

FK RECOMMENDATIONS:
1. **Break down long compound sentences**: The sentence "You can complete steps 1–3 in this article for service accounts, as long as the account has an associated email address (or alias)" could be split into two simpler sentences: "You can complete steps 1–3 in this article for service accounts. The account must have an associated email address (or alias)."

2. **Simplify technical explanations**: The phrase "Datavant recommends maintaining two active credentials to allow rotation without downtime when one expires" uses the technical term "rotation" without explanation. Revise to: "Datavant recommends keeping two active credentials. This way, you can switch between them without service interruption when one expires."

3. **Reduce syllable-heavy words where possible**: Replace "generate" with "create" throughout (appears 4 times), "retrieve" with "get," and "nears expiration" with "is about to expire." These simpler alternatives maintain meaning while improving readability.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Terms like "rotation without downtime," "user-specific credential," and "UAT pipelines" could be explained more clearly. The phrase "allow rotation without downtime" assumes technical knowledge.

Sentence Length: **Flag** - One sentence exceeds 25 words: "Datavant recommends maintaining two active credentials to allow rotation without downtime when one expires.It is also recommended to create two portal accounts for the production pipeline." (28 words, also contains a punctuation error with missing space after period)

Jargon: **Needs Attention** - Several unexplained technical terms:
- "UAT pipelines" (UAT is explained in Abbreviations, but "pipeline" is not defined)
- "status code 1" (no explanation of what this means)
- "runtime" (could use "when running")
- "rotation" (in credential context)

Active Voice: **Pass** - Most sentences use active voice appropriately. One minor passive construction: "The credentials provided are invalid" in the error message, but this is acceptable for error messages.

Heading Clarity: **Pass** - Headings are clear and action-oriented (Step 1, Step 2, Step 3 with descriptive labels)

Link Text: **Pass** - Link references are descriptive: "Managing Users For Your Company," "Generate Datavant Credentials," "Datavant CLI Commands and Optional Arguments"

Abbreviations: **Flag** - "UAT" appears without explanation. "CLI" appears in title but is not expanded on first use in body text (though it may be defined in parent documentation).

Overall WCAG Writing Score: **Needs Attention**