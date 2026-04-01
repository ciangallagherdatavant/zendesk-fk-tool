# FK Analysis Result

**Article:** Performance Benchmarking for Desktop
**Date:** 01 April 2026 15:14
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Performance Benchmarking for Desktop

SCORE: 18.7
Reading Level: College Graduate level
Target Audience: Readers with advanced graduate-level education or specialized technical training

Summary: This article requires a college graduate reading level (grade 18.7), which is significantly above the recommended maximum of grade 12 for technical documentation and will exclude many users.

FK RECOMMENDATIONS:

**1. Break down extremely long sentences (average 44.6 words per sentence)**
   - Current example: The opening sentence "We recommend that you use the Datavant CLI (Command Line Interface) when working with large data files" flows into what appears to be a massive run-on sentence containing all the benchmark data
   - Recommendation: Split benchmark data into separate sentences or use bullet points. For example: "We recommend using the Datavant CLI when working with large data files. The following sections show performance benchmarks for different operations. Results may vary based on your system."

**2. Add explanatory context and transition sentences**
   - Current: The text jumps directly from a recommendation into dense benchmark numbers with minimal explanation
   - Recommendation: Add brief sentences to introduce each benchmark section. Example: "DeID performance varies based on token count. These tests used 500,000 to 2 million records."

**3. Convert data tables from prose to structured format**
   - Current: Performance numbers are embedded in continuous text, creating extremely long sentences
   - Recommendation: Use actual tables or clearly separated list items instead of embedding "7200 records per second 8400 records per second" within sentences. This will dramatically reduce sentence length and improve readability.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

**Plain Language:** Needs Attention
- The continuous stream of numbers without clear separators makes the content difficult to parse
- Recommendation: Add descriptive labels and context for each benchmark result

**Sentence Length:** FAIL
- Average sentence length is 44.6 words (target: under 25 words)
- The benchmark data appears to form 5 extremely long sentences containing multiple data points
- Recommendation: Each benchmark result should be its own sentence or list item

**Jargon:** Needs Attention
- "DeID" - not defined (appears to mean de-identification)
- "tokens" - technical term used without explanation
- "Link" - unclear if this refers to data linking, record matching, or another operation
- CLI is explained on first use (good practice)

**Active Voice:** Pass
- Opening recommendation uses active voice appropriately
- Most content is data presentation rather than action-oriented prose

**Heading Clarity:** Needs Attention
- No headings are present in the cleaned text
- Recommendation: Add headings like "macOS Performance," "Windows Performance," "DeID Operations," and "Link Operations" to structure the benchmark data

**Link Text:** Cannot assess
- No link text present in the provided cleaned prose

**Abbreviations:** Partial Pass
- "CLI" is expanded on first use ✓
- "DeID" is not expanded ✗
- "v3.6.0" appears without context (version of what?)
- "M" and "k" used for millions/thousands without confirmation readers understand these conventions

Overall WCAG Writing Score: Needs Significant Work

**Priority Actions:**
1. Restructure benchmark data into proper tables or bulleted lists
2. Define all abbreviations (DeID, tokens)
3. Add section headings to organize different benchmark categories
4. Break content into sentences under 25 words each