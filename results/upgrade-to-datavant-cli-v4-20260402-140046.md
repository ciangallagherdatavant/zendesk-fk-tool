# FK Analysis Result

**Article:** Upgrade to Datavant CLI v4
**Date:** 02 April 2026 14:00
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Upgrade to Datavant CLI v4

SCORE: 15.8
Reading Level: College level
Target Audience: Readers with college-level reading ability; too complex for general technical audiences

Summary: This article requires a college-level reading ability (nearly 16th grade), which exceeds the recommended Grade 12 maximum for technical documentation.

FK RECOMMENDATIONS:

This content exceeds the Grade 12 target and needs simplification. Here are 3 specific suggestions:

1. **Break down complex sentences with multiple clauses**
   - Current: "As with previous versions, Datavant v4 and above require the ability to make an outbound network connection over port 443."
   - Suggested: "Datavant v4 requires an outbound network connection. Use port 443."

2. **Simplify technical explanations**
   - Current: "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information."
   - Suggested: "These connections let the application access encryption keys and configuration information."

3. **Reduce compound sentences and split information**
   - Current: "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime."
   - Suggested: "Do you run DeID or Link in an automated pipeline? See Configure Datavant CLI in an Automated Pipeline. This guide shows how to stagger credential use and prevent downtime."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention - Contains complex phrasing like "deprecated," "cryptographic secrets," "staggering credential use," and "site-specific password is needed" (passive construction)

**Sentence Length:** Flag - Several sentences exceed 25 words:
- "As with previous versions, Datavant v4 and above require the ability to make an outbound network connection over port 443." (21 words - acceptable)
- "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information." (18 words - acceptable)
- "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime." (30 words - TOO LONG)

**Jargon:** Needs Attention - Multiple unexplained terms:
- "deprecated" (not defined for non-technical users)
- "command-line interface" (used but CLI abbreviation explained)
- "outbound network connection"
- "cryptographic secrets"
- "master salt"

**Active Voice:** Flag - Passive constructions found:
- "a site-specific password is needed" → should be "you need a site-specific password"
- "Command syntax changes are highlighted in red below" → should be "Red text highlights command syntax changes"

**Heading Clarity:** Pass - Headings are clear and action-oriented (Step 1, Step 2, etc.)

**Link Text:** Needs Attention - Some vague references:
- "For more information, see v4 Upgrade FAQs" - acceptable but generic
- Link destinations are mentioned but context could be clearer

**Abbreviations:** Pass - Most abbreviations explained on first use (CLI = command line interface, DeID, v3/v4 contextually clear)

Overall WCAG Writing Score: Needs Attention

---