# FK Analysis Result

**Article:** Upgrade to Datavant CLI v4
**Date:** 02 April 2026 15:28
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Upgrade to Datavant CLI v4

SCORE: 15.8
Reading Level: College level
Target Audience: Readers with college-level reading ability; too complex for general technical audiences

Summary: This article requires a college-level education to read comfortably, which is above the recommended target for technical documentation.

FK RECOMMENDATIONS:

This content exceeds the Grade 12 target and needs simplification. Here are three specific suggestions:

1. **Break down long, multi-clause sentences** - Example: "As with previous versions, Datavant v4 and above require the ability to make an outbound network connection over port 443." 
   - Simplify to: "Datavant v4 needs an outbound network connection. Use port 443."

2. **Simplify technical explanations** - Example: "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information."
   - Simplify to: "These connections let the application access secrets (master salt and encryption keys) and configuration information."

3. **Use shorter sentences in the overview** - Example: "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime."
   - Break into: "Do you run DeID or Link in an automated pipeline? See Configure Datavant CLI in an Automated Pipeline. It shows how to stagger credential use. This prevents unplanned downtime."

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Phrases like "cryptographic secrets," "staggering credential use," and "site-specific password is needed" could be simplified or explained more clearly for non-expert users.

Sentence Length: **Needs Attention** - Several sentences exceed 25 words:
- "As with previous versions, Datavant v4 and above require the ability to make an outbound network connection over port 443." (21 words - acceptable)
- "These connections enable the application to access cryptographic secrets (master salt, encryption keys), as well as configuration information." (18 words - acceptable)
- "If you run DeID or Link in an automated pipeline, refer to Configure Datavant CLI in an Automated Pipeline for recommendations on staggering credential use to prevent unplanned downtime." (30 words - **too long**)

Jargon: **Needs Attention** - Multiple unexplained technical terms:
- "master salt" (explained in parentheses but not defined)
- "encryption keys" (mentioned but not defined)
- "outbound network connection"
- "port 443" (no context for why this specific port)
- "authentication file" vs "authentication_file" (inconsistent)

Active Voice: **Pass** - Most sentences use active voice effectively ("Download," "Retrieve," "Modify")

Heading Clarity: **Pass** - Step-based headings are clear and action-oriented (Step 1. Configure your network, Step 2. Download the v4 application, etc.)

Link Text: **Needs Attention** - Some link references are vague:
- "For more information, see v4 Upgrade FAQs" (acceptable)
- "Refer to Use Datavant CLI in Batch Mode" (acceptable)
- "refer to Configure Datavant CLI in an Automated Pipeline" (acceptable but could be more specific about what readers will learn)

Abbreviations: **Needs Attention** - Several unexplained abbreviations:
- "CLI" (explained on second use but not on first mention in title)
- "DeID" (not spelled out; appears to mean "de-identification")
- "v3" and "v4" (clear from context but not explicitly defined as "version")
- "FAQs" (common abbreviation but not spelled out)

Overall WCAG Writing Score: **Needs Attention**

---