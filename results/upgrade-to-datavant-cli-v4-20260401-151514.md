# FK Analysis Result

**Article:** Upgrade to Datavant CLI v4
**Date:** 01 April 2026 15:15
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Upgrade to Datavant CLI v4

SCORE: 15.8
Reading Level: College level
Target Audience: Readers with college-level reading ability; too complex for general technical audiences

Summary: This article requires a college-level reading ability (nearly 16th grade), which exceeds the recommended maximum of Grade 12 for technical documentation and may prevent many users from understanding critical upgrade instructions.

FK RECOMMENDATIONS:

This content significantly exceeds the Grade 12 target and needs simplification. Here are 3 specific suggestions:

1. **Break down compound sentences with multiple clauses:**
   - Current: "As with previous versions, Datavant v4 and above require the ability to make an outbound network connection over port 443."
   - Suggested: "Datavant v4 requires an outbound network connection. Use port 443."

2. **Simplify technical explanations:**
   - Current: "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information."
   - Suggested: "These connections let the application access: cryptographic secrets (master salt and encryption keys) and configuration information."

3. **Reduce noun clusters and prepositional phrases:**
   - Current: "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime."
   - Suggested: "Do you run DeID or Link in an automated pipeline? See Configure Datavant CLI in an Automated Pipeline. This guide shows how to stagger credentials and avoid downtime."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "deprecated" could be "stopped supporting" or "ended support for"
- "staggering credential use" is vague—clarify as "rotating between multiple credentials"
- "outbound network connection" could be simplified to "connection to external servers"

**Sentence Length:** Needs Attention
- "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime." (30 words)
- "As with previous versions, Datavant v4 and above require the ability to make an outbound network connection over port 443." (20 words, but dense with technical content)

**Jargon:** Needs Attention - Several unexplained terms:
- CLI (explained as "command-line interface" later, but not at first use)
- DeID (not defined)
- Link (not defined as a process/product)
- "master salt" (cryptographic term without explanation)
- "deprecated" (technical term)
- "authentication file" (not explained)

**Active Voice:** Pass
Most sentences use active voice appropriately. Minor exception: "black text are replacements commands" (grammatically incorrect passive construction).

**Heading Clarity:** Pass
Headings are clear and action-oriented ("Step 1. Configure your network", "Step 2. Download the v4 application").

**Link Text:** Pass
Link text appears descriptive ("v4 Upgrade FAQs", "Configure Datavant CLI in an Automated Pipeline", "Use Datavant CLI in Batch Mode").

**Abbreviations:** Needs Attention
- CLI: defined on second use, should be defined at first use in Overview
- v3, v4: not spelled out (could use "version 3" and "version 4" at first mention)
- DeID: never defined
- FAQs: commonly understood but could spell out

Overall WCAG Writing Score: Needs Attention

---