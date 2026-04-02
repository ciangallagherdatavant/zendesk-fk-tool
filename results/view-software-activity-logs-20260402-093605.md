# FK Analysis Result

**Article:** View Software Activity Logs
**Date:** 02 April 2026 09:36
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: View Software Activity Logs

SCORE: 16.6
Reading Level: College level
Target Audience: Readers with college-level education or advanced reading skills

Summary: This article is written at a college level (Grade 16.6), which is significantly above the recommended Grade 12 target for technical documentation and may be difficult for many users to understand quickly.

FK RECOMMENDATIONS:

1. **Break up extremely long sentences** - Your average sentence length is 32.2 words, which is far too long. For example, this 50+ word sentence needs to be split:
   - Current: "In other words, any time tokenization occurs using a site owned by your company, any time transformation occurs using a site owned by your company, and any time transformation occurs for a site that is linked with a partner, a log entry will be posted."
   - Suggested: "A log entry is posted when: tokenization occurs using your company's site, transformation occurs using your company's site, or transformation occurs for a partner-linked site."

2. **Simplify dense introductory sentence** - The opening sentence is overly complex:
   - Current: "The software activity log page displays logs that indicate each time one of your company's encryption keys is accessed."
   - Suggested: "The software activity log shows when your encryption keys are accessed."

3. **Create a bulleted list instead of comma-separated conditions** - The three scenarios where logs are posted should be formatted as a list rather than strung together with "any time" repetitions, which will reduce cognitive load and sentence length.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Phrases like "indicate each time one of your company's encryption keys is accessed" could be simplified to "show when your encryption keys are used."

Sentence Length: **Flag** - Multiple sentences exceed 25 words. The second sentence contains 50+ words and desperately needs breaking up. Average sentence length of 32.2 words is well above the recommended 20-25 word maximum.

Jargon: **Needs Attention** - Technical terms used without explanation:
- "tokenization" (not defined)
- "transformation" (not defined)
- "encryption keys" (assumed knowledge)
- "partner-linked site" (relationship not explained)

Active Voice: **Flag** - Several passive constructions found:
- "logs that indicate" (could be "logs show")
- "a log entry will be posted" (could be "the system posts a log entry")
- "logs are only captured" (could be "the system only captures logs")

Heading Clarity: **Pass** - "Understanding the Software Activity Logs" is clear and descriptive.

Link Text: **Pass** - No links present in the cleaned text to evaluate.

Abbreviations: **Needs Attention** - "&gt;" appears to be an encoding issue for ">" symbol in "Settings &gt; Activity"

Overall WCAG Writing Score: **Needs Significant Work**

---