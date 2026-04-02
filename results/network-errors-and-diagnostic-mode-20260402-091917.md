# FK Analysis Result

**Article:** Network Errors and Diagnostic Mode
**Date:** 02 April 2026 09:19
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Network Errors and Diagnostic Mode

SCORE: 12.5
Reading Level: High School Advanced (approaching College level)
Target Audience: Readers with advanced high school education or above; comfortable with technical documentation

Summary: This article is at the upper threshold of acceptable readability for technical documentation and would benefit from simplification to reach a broader technical audience.

FK RECOMMENDATIONS:

While the score of 12.5 is just above the Grade 12 target, some targeted improvements can bring this content to a more accessible level:

1. **Break down complex sentences with multiple clauses**: The opening sentence contains 28 words with nested parenthetical information: "The Datavant CLI and Datavant Desktop are unable to function without successfully connecting to a series of Datavant owned endpoints (sec.datavant.com; auth.datavant.com; api.datavant.com)." Consider breaking this into two sentences: "The Datavant CLI and Datavant Desktop must connect to Datavant endpoints to function. These endpoints include sec.datavant.com, auth.datavant.com, and api.datavant.com."

2. **Simplify vocabulary where possible**: Replace phrases like "subsequently" with "next," "yields" with "produces," and "invocation" with "use" to reduce syllable count without losing technical accuracy.

3. **Remove redundant phrasing**: The phrase "This diagnostic suite is also invoked automatically on connection failure to help users service failures on v4.2+ of the CLI" contains repetitive "failure" references. Simplify to: "The diagnostic suite runs automatically when connection fails on CLI v4.2 and later."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Some unnecessarily complex phrasing such as "invoked automatically," "yields," and "surfaced in the test output" could be simplified to more common terms.

**Sentence Length:** Flag - One sentence exceeds 25 words: "The Datavant CLI and Datavant Desktop are unable to function without successfully connecting to a series of Datavant owned endpoints (sec.datavant.com; auth.datavant.com; api.datavant.com)" at 28 words. Break this into shorter segments.

**Jargon:** Pass with note - Technical terms like "TCP handshake," "TLS connection," "DNS," and "proxy servers" are appropriate for the technical audience, though brief contextual explanations could help (e.g., "TCP handshake (initial connection test)").

**Active Voice:** Flag - Several passive constructions found:
- "are unable to function" → "cannot function"
- "is also invoked automatically" → "also runs automatically"
- "are not obstructing" → "do not obstruct"
- "are required and are not found" → "you require proxies but the CLI cannot find them"

**Heading Clarity:** Pass - The article would benefit from visible section headings to break up troubleshooting steps (DNS checks, TCP checks, TLS checks, etc.), though the content logically progresses through diagnostics.

**Link Text:** Pass - References to "Technical Requirements for On-Premise Software" is descriptive; email address is clear.

**Abbreviations:** Needs Attention - "CLI," "DNS," "TCP," "TLS," and "IP" appear without first-use expansion. First mention should spell out: "Command Line Interface (CLI)," "Domain Name System (DNS)," etc.

Overall WCAG Writing Score: Needs Attention