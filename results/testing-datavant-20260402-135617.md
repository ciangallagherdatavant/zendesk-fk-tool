# FK Analysis Result

**Article:** Testing Datavant
**Date:** 02 April 2026 13:56
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Testing Datavant

SCORE: 12.8
Reading Level: High School Advanced (approaching College level)
Target Audience: Readers with advanced high school to early college reading ability; technical professionals

Summary: This article is just slightly above the ideal target range for technical documentation and may challenge some readers due to complex sentence structures and technical density.

FK RECOMMENDATIONS:

The score of 12.8 is close to the Grade 12 target but slightly elevated. Here are three specific suggestions to bring it down:

1. **Break down long conditional sentences**: The sentence "If you maintain separate testing and production environments: Datavant can be deployed in both, allowing you to validate your setup end-to-end before running production jobs" (24 words) could be split: "Do you maintain separate testing and production environments? If yes, Datavant can be deployed in both. This allows you to validate your setup end-to-end before running production jobs."

2. **Simplify the multi-clause recommendation statement**: "Datavant does not recommend creating or maintaining separate testing parameters (for example, a "test site" vs. a "production site" or a "test configuration" vs. a "production configuration")" is complex. Revise to: "Datavant does not recommend separate testing parameters. For example, avoid creating separate test sites and production sites. Also avoid separate test configurations and production configurations."

3. **Shorten the reason-heavy sentence**: "In addition to creating additional overhead and maintenance costs, using separate sites or configurations for testing does not improve testing outcomes, since the key variable for testing quality is whether your test data accurately represents the data you expect to process in production" (42 words). Break into two sentences: "Using separate sites or configurations creates overhead and maintenance costs. More importantly, it does not improve testing outcomes. Testing quality depends on whether your test data accurately represents your production data."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several phrases could be simpler: "native test mode" could be "built-in test mode"; "validate your setup end-to-end" could be "test your complete setup"; "representative test data" could be "test data that matches your real data"

Sentence Length: **Flag** - One sentence exceeds 25 words significantly:
- "In addition to creating additional overhead and maintenance costs, using separate sites or configurations for testing does not improve testing outcomes, since the key variable for testing quality is whether your test data accurately represents the data you expect to process in production." (42 words)

Jargon: **Needs Attention** - Several technical terms lack explanation:
- "tokenization" (first use should be briefly explained)
- "token transformation"
- "transit key transformation"
- "connect key transformation"
- "synthetic datasets"
- "encoding"

Active Voice: **Pass** - Most sentences use active voice effectively ("Datavant does not provide," "You can still test," "Confirm that")

Heading Clarity: **Pass** - Headings are clear and descriptive ("Validate Input and Output Data," "Test the Command," "Recommended Testing Workflow")

Link Text: **Needs Attention** - The article text shows a navigation path ("Configurations > View Configuration > Download Test Input File") but no actual link context is provided in the cleaned text to fully assess

Abbreviations: **Flag** - "prod" is used without first spelling out "production": "If using separate test/prod environments"

Overall WCAG Writing Score: **Needs Attention**