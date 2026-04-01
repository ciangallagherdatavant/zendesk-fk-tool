# FK Analysis Result

**Article:** Network Errors and Diagnostic Mode
**Date:** 01 April 2026 15:08
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Network Errors and Diagnostic Mode

SCORE: 12.5
Reading Level: High School Advanced (approaching College level)
Target Audience: Readers with advanced high school to early college-level reading ability; may be challenging for general technical users

Summary: This article is just above the recommended maximum complexity for technical documentation and should be simplified to improve accessibility for a broader technical audience.

FK RECOMMENDATIONS:

While the score of 12.5 is close to the target threshold, it exceeds the Grade 12 maximum recommended for technical writing. Here are 3 specific suggestions to lower complexity:

1. **Break down long technical sentences**: The opening sentence contains 29 words with multiple embedded clauses: "The Datavant CLI and Datavant Desktop are unable to function without successfully connecting to a series of Datavant owned endpoints (sec.datavant.com; auth.datavant.com; api.datavant.com)." Revise to: "The Datavant CLI and Datavant Desktop require connection to Datavant endpoints. These include sec.datavant.com, auth.datavant.com, and api.datavant.com."

2. **Simplify technical phrasing**: "This diagnostic suite is also invoked automatically on connection failure to help users service failures" uses complex passive construction. Revise to: "The tool runs automatically when a connection fails. This helps you fix the problem."

3. **Use simpler vocabulary**: Replace "obstructing" with "blocking," "surfaced" with "shown," "yielded" with "returned," and "invocation" with "use" to reduce syllable count and improve clarity.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Contains unnecessarily complex phrases like "invoked automatically," "surfaced in the test output," "subsequent network connectivity tests," and "resolutions are failing to produce an IP."

**Sentence Length:** Needs Attention - Several sentences exceed 25 words:
- Opening sentence: 29 words
- "v4.2+ of the CLI ships with a network diagnostic mode that allows users the ability to run a series of automated checks to verify connectivity." (26 words)
- "If you know there to be network proxies in your system, but do not see them being surfaced in the test output, consider specifying them in your environment or within your invocation of the CLI." (35 words)

**Jargon:** Needs Attention - Technical terms lacking context or explanation:
- TCP handshake
- DNS
- TLS connection
- Pass-through mode
- Self-signed certificate
- SSL certificate
- Public vs. private IP addresses

**Active Voice:** Needs Attention - Multiple passive constructions found:
- "is also invoked automatically"
- "If network proxies are required and are not found"
- "If these resolutions are failing"
- "Ensure any proxy server is set to pass-through mode"
- "ensure it is configured to pass through"

**Heading Clarity:** Pass - Article would benefit from subheadings to break up diagnostic steps (proxy check, DNS resolution, TCP handshake, TLS connection).

**Link Text:** Pass - References to "Technical Requirements for On-Premise Software" and "support@datavant.com" are descriptive.

**Abbreviations:** Needs Attention - Several abbreviations lack first-use explanation:
- CLI (explained in context but not explicitly defined)
- DNS (not explained)
- TCP (not explained)
- TLS (not explained)
- SSL (not explained)
- IP (not explained)

Overall WCAG Writing Score: Needs Attention

---