# FK Analysis Result

**Article:** Datavant CLI Commands and Optional Arguments
**Date:** 02 April 2026 09:11
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Datavant CLI Commands and Optional Arguments

SCORE: 12.8
Reading Level: High School Advanced (approaching College level)
Target Audience: Advanced high school readers or those with some technical/college education

Summary: This content is slightly above the ideal target for technical documentation and may be difficult for general business users without technical backgrounds.

FK RECOMMENDATIONS:

While the score of 12.8 is only marginally above the Grade 12 target, reducing complexity would make this technical reference more accessible:

1. **Break down long compound sentences** - Example: "When using the Datavant CLI in batch, server, or streaming mode, you must enter commands in the CLI to run tokenize and transform" could become: "You can use the Datavant CLI in three modes: batch, server, or streaming. In each mode, you must enter commands to run tokenize and transform."

2. **Simplify technical explanations** - Example: "If you're tokenizing using the Desktop Application, you may select tokenizing identified data and transforming tokens to send to a partner, which generates both a tokenized and transformed output in a single workflow" contains nested concepts. Break this into: "The Desktop Application offers a simpler option. You can tokenize and transform in a single workflow. This creates both outputs at once."

3. **Add brief definitions for key terms** - Words like "tokenize," "transform," and "streaming mode" appear without context. Add one-line definitions: "Tokenize (replace sensitive data with tokens)" on first use to reduce cognitive load.

FK RECOMMENDATIONS:

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Heavy use of technical jargon without initial explanation. Terms like "tokenize," "transform-tokens," "batch mode," "streaming mode," and "credentials filename" are used without definition. While appropriate for technical documentation, brief explanations would improve accessibility.

Sentence Length: **Pass** - Most sentences are concise. The breakdown shows average of 9.8 words per sentence, well below the 25-word threshold. However, a few sentences approach complexity: "If you're tokenizing using the Desktop Application, you may select tokenizing identified data and transforming tokens to send to a partner, which generates both a tokenized and transformed output in a single workflow" (33 words).

Jargon: **Needs Attention** - Unexplained technical terms include:
- CLI (explained as acronym but "Command Line Interface" not spelled out)
- tokenize/tokenizing
- transform/transform-tokens
- batch mode
- streaming mode
- server mode
- credentials filename
- PowerShell vs cmd
- pipe operator (|)

Abbreviations: **Needs Attention**
- CLI - used throughout but never spelled out as "Command Line Interface"
- OS - spelled out once as "operating system" (good)
- v5 - "version 5" would be clearer

Active Voice: **Pass** - Mostly uses active voice and imperative commands appropriate for technical instructions ("cat," "type," "connect with"). Some passive constructions exist but are acceptable: "is available on limited release," "is highlighted in purple callout boxes."

Heading Clarity: **Good** - Headings are descriptive and follow clear patterns (OS, then command type). Consider adding a brief introductory line under "Building your commands for batch mode" to orient users.

Link Text: **Cannot Assess** - The cleaned prose text doesn't show the actual link text formatting, only mentions references to other articles. Ensure links use descriptive text rather than "click here" patterns.

Overall WCAG Writing Score: **Needs Attention**

The article is well-structured with clear examples, but lacks definitions for technical terms and abbreviation expansions that would help users with cognitive disabilities or those using screen readers. Adding a brief glossary section or first-use definitions would significantly improve accessibility.

---