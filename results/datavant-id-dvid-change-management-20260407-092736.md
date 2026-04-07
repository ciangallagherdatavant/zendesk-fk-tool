# FK Analysis Result

**Article:** Datavant ID (DVID) Change Management
**Date:** 07 April 2026 09:27
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Datavant ID (DVID) Change Management

SCORE: 10.2
Reading Level: High School
Target Audience: High school students and adults with at least a 10th-grade reading level

Summary: This article requires a high school reading level (grade 10) and is accessible to most general audiences, though it could be simplified further for broader reach.

FK RECOMMENDATIONS:
The content meets the target of Grade 12 or below. Here are three specific suggestions to improve readability further:

1. **Break down complex compound sentences**: The sentence "When an associated data table is updated with new records, either incrementally or in a full refresh, the Match run automatically runs to process the newly added records and to distribute DVIDs through the active distribution subscription" contains multiple clauses and ideas. Split this into two sentences: "When an associated data table is updated with new records (either incrementally or in a full refresh), the Match run automatically processes them. It then distributes DVIDs through the active distribution subscription."

2. **Simplify technical explanations**: The phrase "Match retains old records and their DVID assignments from previous dataset versions to minimize changes to existing DVIDs" could be rewritten more simply as "Match keeps old records and their DVID assignments. This minimizes changes to existing DVIDs."

3. **Use bulleted lists for procedural information**: The two-step process under "How does Match handle data updates?" ("If a match is found... If no match is found...") would be clearer as a numbered list format, making the logic flow more scannable and digestible.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Some phrases are unnecessarily complex. Examples: "onboarding new records to a Match run with an active distribution" (use "adding"), "net new records" (use "new records"), "associated data table" (consider "linked data table").

Sentence Length: **Pass** - Most sentences are under 25 words. The longest is 32 words ("When an associated data table is updated with new records, either incrementally or in a full refresh, the Match run automatically runs to process the newly added records and to distribute DVIDs through the active distribution subscription") but this is an isolated case.

Jargon: **Needs Attention** - Several technical terms lack immediate explanation: "data pool" (explained in context), "incremental" and "full refresh" (defined), "tokens" (not explained), "SFTP location" (not explained), "ingestion pipelines" (not explained). Consider adding brief explanations for tokens, SFTP, and ingestion pipelines.

Active Voice: **Good** - The article predominantly uses active voice. Examples: "Match aims to preserve," "Match identifies net new records," "Datavant distributes updated DVIDs." One passive construction appears: "updates are delivered as a separate file" but this is acceptable in context.

Heading Clarity: **Good** - Headings are descriptive and action-oriented: "Add data to a Match data pool," "How does Match handle data updates?" These clearly indicate content that follows.

Link Text: **Pass** - The article references "Understanding Match" and "support@datavant.com" which are appropriately descriptive. No vague "click here" or "read more" links present.

Abbreviations: **Good** - Abbreviations are properly introduced: "Datavant IDs (DVIDs)" on first use, then DVID throughout. "SFTP" appears without expansion and should be defined as "Secure File Transfer Protocol" on first use.

Overall WCAG Writing Score: **Needs Attention**