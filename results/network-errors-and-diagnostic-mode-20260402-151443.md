# FK Analysis Result

**Article:** Network Errors and Diagnostic Mode
**Date:** 02 April 2026 15:14
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Network Errors and Diagnostic Mode

SCORE: 12.5
Reading Level: High School Advanced / Early College
Target Audience: Readers with advanced high school or some college education

Summary: This content is at the upper limit of acceptable technical writing complexity and would benefit from simplification to improve accessibility for a broader technical audience.

FK RECOMMENDATIONS:

While the score of 12.5 is just slightly above the Grade 12 target, there is room for improvement. Here are three specific suggestions:

1. **Break down complex opening sentence**: The first sentence contains 23 words and multiple concepts. Change from: "The Datavant CLI and Datavant Desktop are unable to function without successfully connecting to a series of Datavant owned endpoints (sec.datavant.com; auth.datavant.com; api.datavant.com)." To: "The Datavant CLI and Datavant Desktop need to connect to Datavant endpoints to function. These endpoints include sec.datavant.com, auth.datavant.com, and api.datavant.com."

2. **Simplify technical explanations**: Change "If these resolutions are failing to produce an IP, or the IP addresses yielded are private..." to "If DNS cannot find an IP address, or if the IP address is private..."

3. **Use shorter, direct instructions**: Change "Provided the domain resolutions are valid, we then attempt a TCP handshake" to "After DNS resolution succeeds, the CLI attempts a TCP handshake."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Several phrases use unnecessarily complex language: "invoked automatically," "surfaced in the test output," "resolutions are failing to produce," "IP addresses yielded are private"

**Sentence Length:** Flag - One sentence exceeds 25 words: "If your networking system relies on proxy servers to redirect traffic, please ensure that they are not obstructing the CLI from running." (23 words - close but acceptable). The opening sentence is 23 words but dense with technical concepts.

**Jargon:** Needs Attention - Several technical terms lack explanation: TCP handshake, TLS connection, DNS, pass-through mode, SSL certificate, self-signed certificate. While the audience is technical, brief explanations or links would improve accessibility.

**Active Voice:** Pass - Most instructions use active voice effectively ("We first check," "We recommend," "Ensure any proxy server")

**Heading Clarity:** Needs Attention - The article appears to lack clear section headings. Adding headings like "What is Diagnostic Mode?", "Running Diagnostic Mode," "Troubleshooting Steps," and "Contacting Support" would improve scannability.

**Link Text:** Pass - The reference to "Technical Requirements for On-Premise Software" is descriptive link text.

**Abbreviations:** Needs Attention - CLI, DNS, TCP, TLS, SSL, IP are used without first defining them (e.g., "Command Line Interface (CLI)," "Domain Name System (DNS)")

Overall WCAG Writing Score: Needs Attention