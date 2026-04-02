# FK Analysis Result

**Article:** Technical Requirements for the Datavant CLI and Datavant Desktop
**Date:** 02 April 2026 15:23
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Technical Requirements for the Datavant CLI and Datavant Desktop

SCORE: 13.1
Reading Level: College level
Target Audience: Readers with a college-level education; too complex for general technical users

Summary: This article requires college-level reading ability, which exceeds the ideal target of Grade 12 or below for technical documentation.

FK RECOMMENDATIONS:

1. **Break down complex noun phrases into simpler constructions**
   - Current: "Datavant's maintenance policy for the Datavant Tokenization application and deployments"
   - Suggested: "How Datavant maintains the Tokenization application"

2. **Simplify technical explanations with shorter, more direct phrasing**
   - Current: "Any proxy server passes through the incoming SSL certificate from Datavant's endpoints, rather than replacing it with a self-signed certificate."
   - Suggested: "Your proxy server must pass through SSL certificates from Datavant. It must not replace them with self-signed certificates."

3. **Use bulleted lists to break up dense information clusters**
   - Current: "It checks DNS resolution, TCP connectivity, and SSL/TLS validation to confirm that your machine can reach the required services."
   - Suggested: Transform into a bulleted list: "It checks three things: DNS resolution, TCP connectivity, and SSL/TLS validation"

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Contains unexplained technical concepts like "pass-through mode," "hash salt," "encryption keys," and "transit key" without context.

**Sentence Length:** Pass - Most sentences are under 25 words, though one sentence at 26 words could be shortened: "Any proxy server passes through the incoming SSL certificate from Datavant's endpoints, rather than replacing it with a self-signed certificate."

**Jargon:** Needs Attention - Multiple unexplained technical terms: "hash salt," "transit key," "connect key," "pass-through mode," "self-signed certificate," "DNS resolution," "TCP connectivity," "SSL/TLS validation"

**Active Voice:** Pass - Generally uses active voice well throughout the document.

**Heading Clarity:** Pass - Headings are descriptive and well-structured (Overview, Compatible Operating Systems, Network Connectivity, etc.)

**Link Text:** Pass - No vague link text detected; references are specific (e.g., "Client Versions and Support Policy," "Network Errors and Diagnostics Mode")

**Abbreviations:** Needs Attention - Several abbreviations lack first-use expansion: CLI (appears in title without expansion), SSL, TLS, TCP, DNS, HTTPS, AWS

Overall WCAG Writing Score: Needs Attention