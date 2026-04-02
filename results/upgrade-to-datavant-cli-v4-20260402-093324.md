# FK Analysis Result

**Article:** Upgrade to Datavant CLI v4
**Date:** 02 April 2026 09:33
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Upgrade to Datavant CLI v4

SCORE: 15.8
Reading Level: College level (Grade 15-16, equivalent to college junior/senior)
Target Audience: Readers with advanced technical education and strong comprehension skills

Summary: This article requires a college-level reading ability, which exceeds the recommended Grade 12 target for technical documentation and may create barriers for some technical users.

FK RECOMMENDATIONS:

This content exceeds Grade 12 and needs simplification. Here are 3 specific suggestions:

1. **Break down complex sentences with multiple clauses**
   - Current: "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information."
   - Suggested: "These connections let the application access cryptographic secrets. This includes master salt and encryption keys. It also includes configuration information."

2. **Simplify technical explanations with embedded parentheticals**
   - Current: "Starting in v4, running Datavant (either the CLI or desktop) requires user-specific credentials (in prior versions, a site-specific password is needed)."
   - Suggested: "Version 4 requires user-specific credentials. This is different from prior versions, which needed a site-specific password. This applies to both the CLI and desktop versions."

3. **Remove unnecessary complexity in instructions**
   - Current: "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime."
   - Suggested: "Do you run DeID or Link in an automated pipeline? See 'Configure Datavant CLI in an Automated Pipeline.' This guide shows you how to stagger credential use. This prevents unplanned downtime."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- Heavy use of compound technical phrases: "user-specific credentials," "outbound network connection," "cryptographic secrets"
- Parenthetical asides interrupt reading flow: "(either the CLI or desktop)" and "(in prior versions, a site-specific password is needed)"
- Consider defining terms before use or using simpler alternatives where possible

**Sentence Length:** Needs Attention
- Several sentences exceed 25 words:
  - "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information." (18 words but complex structure)
  - "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime." (30 words)
  - "Starting in v4, running Datavant (either the CLI or desktop) requires user-specific credentials (in prior versions, a site-specific password is needed)." (23 words but overly complex)

**Jargon:** Needs Attention
Unexplained technical terms:
- "deprecated" (used without definition)
- "command-line interface" (abbreviated to CLI but not defined on first use)
- "outbound network connection"
- "port 443"
- "cryptographic secrets"
- "master salt"
- "encryption keys"
- "automated pipeline"
- "batch mode"

**Active Voice:** Pass
Most instructions use active voice effectively ("Download the v4 application," "Configure your network")

**Heading Clarity:** Pass
Step-based headings are clear and action-oriented (Step 1. Configure your network, Step 2. Download the v4 application)

**Link Text:** Needs Attention
- "v4 Upgrade FAQs" - Good, descriptive
- "Configure Datavant CLI in an Automated Pipeline" - Good, descriptive
- "Use Datavant CLI in Batch Mode" - Good, descriptive
However, ensure these are actual links in the published version

**Abbreviations:** Needs Attention
- "CLI" - used frequently but not defined on first use as "command-line interface (CLI)"
- "DeID" - not defined (appears to mean "de-identification")
- "v3" and "v4" - acceptable in context but spell out "Version" on first use

Overall WCAG Writing Score: Needs Attention

**Priority Actions:**
1. Define all abbreviations on first use
2. Break long sentences into shorter units (aim for under 20 words)
3. Add a glossary or define technical terms inline for users unfamiliar with concepts like "port 443" or "master salt"
4. Reduce parenthetical asides by converting them to separate sentences

---