# FK Analysis Result

**Article:** International Transform Tokens User Guide
**Date:** 02 April 2026 15:11
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: International Transform Tokens User Guide

SCORE: 10.8
Reading Level: High School (upper level)
Target Audience: Readers with high school level education and above, comfortable with moderate complexity text

Summary: This article achieves a grade 10.8 reading level, which falls within the acceptable range for technical documentation and should be accessible to most professional audiences.

FK RECOMMENDATIONS:
✓ **Content meets target readability level** - Well done! With a score of 10.8, this article sits comfortably below the Grade 12 threshold, making it accessible to the intended technical audience. The short average sentence length (11.0 words) contributes positively to readability. Continue maintaining concise sentences and clear structure in future revisions.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- "client-partner_TOKEN_ENCRYPTION_KEY" appears without explanation of what this format means
- "linkable to your own site key" assumes technical knowledge without context
- "Run the transform tokens from command" uses technical language that could be clearer (e.g., "Run the following command to transform tokens")

**Sentence Length:** Pass
All sentences are well under 25 words. The average of 11.0 words per sentence is excellent for accessibility.

**Jargon:** Needs Attention
- TOKEN_ENCRYPTION_KEY - not explained
- SFTP - appears multiple times without expansion on first use
- S3 - not explained (Amazon S3 bucket)
- CLI - mentioned in heading without expansion
- "site key" - technical term used without definition
- "tokenization" - used but concept not explained in this article

**Active Voice:** Pass
Most instructions use clear active voice commands ("Run," "Ensure," "Pull," "Share").

**Heading Clarity:** Needs Attention
- "Step 3. Run Datavant CLI to Transform Tokens" and "Step 3. Run Transform Tokens From" - two different Step 3s creates confusion
- Missing clear section breaks between "Sharing Data Out" and "Receiving Data In" processes
- "Receiving Data In" section lacks numbered step headings for Step 1

**Link Text:** Needs Attention
- "Receiving Data In" - link destination unclear (is this within the same article or external?)
- "Onboarding User Guide" - acceptable but could specify what aspects it covers
- "Tokenization User Guide" - acceptable

**Abbreviations:** Needs Attention
- SFTP - not expanded on first use
- S3 - not expanded
- CLI - not expanded (appears only in heading)
- &amp; - HTML entity not properly rendered (should be "&")

Overall WCAG Writing Score: Needs Attention

**Priority fixes:** Expand abbreviations on first use (SFTP, S3, CLI), fix duplicate step numbering, add brief explanations for technical terms like "site key" and "TOKEN_ENCRYPTION_KEY," and correct the "&amp;" HTML rendering error.

---