# FK Analysis Result

**Article:** Use Datavant Natively on AWS EKS
**Date:** 07 April 2026 09:28
**Calculated by:** Python textstat library

---
FLESCH-KINCAID GRADE LEVEL ANALYSIS

Article Title: Use Datavant Natively on AWS EKS

SCORE: 10.3
Reading Level: High School
Target Audience: High school students and adults with secondary education; technical users comfortable with cloud infrastructure and API concepts

Summary: This article reads at a 10th-grade level, making it accessible to most technical audiences, though some simplification could broaden its reach.

FK RECOMMENDATIONS:
The content meets the target readability threshold (below Grade 12), which is appropriate for technical documentation. Here are three specific ways to improve readability further:

1. **Break down compound technical sentences.** For example, "The AWS Native Tokenization is a docker container built to be deployed on either ECS or EKS" could become two sentences: "The AWS Native Tokenization is a docker container. You can deploy it on either ECS or EKS." This separates the definition from the deployment information.

2. **Simplify prepositional phrases.** The phrase "It has added functionality to directly read from and write to S3 buckets in the account that the docker container is running in" contains nested prepositional phrases. Revise to: "It can read from and write to S3 buckets in your account."

3. **Front-load action verbs in instructions.** Change "Ensure any proxy server is set to pass-through mode" to "Set any proxy server to pass-through mode." This makes instructions more direct and reduces syllable count.

WCAG 2.2 WRITING ACCESSIBILITY NOTES:

Plain Language: **Needs Attention** - Several instances of complex phrasing: "endpoints are accessible outbound over port 443," "pass through the incoming SSL certificate," "configured to pass back its own self-signed certificate." Consider defining or simplifying these technical phrases.

Sentence Length: **Pass** - Most sentences stay under 25 words. One borderline example: "If you have a proxy server, ensure it is configured to pass through the incoming SSL certificate from Datavant's endpoints, as opposed to passing back its own self-signed certificate" (30 words) - consider splitting.

Jargon: **Needs Attention** - Multiple unexplained technical terms: ECS, EKS, docker container, S3 buckets, SSL certificate, proxy server, pass-through mode, self-signed certificate, port 443, master salt, encryption keys. Consider adding brief definitions or linking to a glossary.

Active Voice: **Pass** - Generally uses active voice well in instructions ("Ensure," "Verify," "Create," "Click").

Heading Clarity: **Good** - Step-by-step headings are clear and action-oriented (e.g., "Step 1. Complete technical pre-requisites").

Link Text: **Cannot assess** - The cleaned prose doesn't show actual link text implementation, only references like "Download page" and "Configurations user guide."

Abbreviations: **Needs Attention** - AWS, ECS, EKS, CLI, SSL - none are defined on first use. Should expand: "Amazon Web Services (AWS)," "Elastic Container Service (ECS)," "Elastic Kubernetes Service (EKS)," "Command Line Interface (CLI)," "Secure Sockets Layer (SSL)."

Overall WCAG Writing Score: **Needs Attention**

---