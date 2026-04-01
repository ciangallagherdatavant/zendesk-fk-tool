# FK Analysis Result

**Article:** Technical Requirements for the Datavant CLI and Datavant Desktop
**Date:** 01 April 2026 15:06
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Technical Requirements for the Datavant CLI and Datavant Desktop

SCORE: 13.1
Reading Level: College level
Target Audience: College-educated readers with technical background

Summary: This article requires a college-level reading ability, which exceeds the recommended Grade 12 target for technical documentation and may create barriers for some IT professionals and system administrators.

FK RECOMMENDATIONS:

Since this scores above Grade 12, here are three specific suggestions:

1. **Break down compound technical sentences**: The sentence "Any proxy server passes through the incoming SSL certificate from Datavant's endpoints, rather than replacing it with a self-signed certificate" (19 words) could be simplified to two sentences: "Your proxy server must pass through the incoming SSL certificate from Datavant's endpoints. Do not replace it with a self-signed certificate."

2. **Simplify multi-clause network connectivity explanations**: The phrase "Validate user credentials and confirm permissions" uses formal language. Change to: "Check user credentials and permissions." Similarly, "Reference hash salt and encryption keys" could become "Access hash salt and encryption keys."

3. **Reduce syllable density in action items**: Replace "troubleshoot any connectivity problems you may be experiencing" with "fix connection problems" and "checks DNS resolution, TCP connectivity, and SSL/TLS validation to confirm" with "tests DNS resolution, TCP connectivity, and SSL/TLS validation to check."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Terms like "pass-through mode," "self-signed certificate," "intercepting," and "secrets management system" assume high technical literacy. While some jargon is necessary for this audience, consider adding brief explanations in parentheses.

Sentence Length: **Pass** - Most sentences are well under 25 words. The longest is 23 words ("In Datavant Desktop, you can select diagnosing network issues menu option to troubleshoot any connectivity problems you may be experiencing"), which is acceptable.

Jargon: **Needs Attention** - Unexplained technical terms include: "batch/server/streaming mode," "hash salt," "encryption keys," "transit key," "connect key," "DNS resolution," "TCP connectivity," "SSL/TLS validation," "pass-through mode," and "self-signed certificate." Consider a glossary or hover-text definitions.

Active Voice: **Needs Attention** - Several passive constructions found:
- "information is highlighted in purple callout boxes"
- "valid transit key or connect key is in place"
- "following three endpoints must be allowed"
- "Any proxy server is set to pass-through mode"

Heading Clarity: **Pass** - Headings are descriptive and action-oriented: "Compatible Operating Systems," "Network Connectivity," and "Minimum Specifications" clearly indicate section content.

Link Text: **Good** - Link text is descriptive: "Client Versions and Support Policy" and "Network Errors and Diagnostics Mode" tell users what to expect.

Abbreviations: **Needs Attention** - Several abbreviations lack first-use expansion:
- CLI (Command Line Interface) - appears in title unexpanded
- AWS (Amazon Web Services)
- HTTPS (defined by context but not explicitly)
- DNS, TCP, SSL/TLS (used without expansion)

Overall WCAG Writing Score: **Needs Attention**

---