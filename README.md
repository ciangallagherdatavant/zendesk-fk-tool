# Zendesk FK Readability Analysis Tool

## What This Tool Does
This tool performs automated Flesch-Kincaid Grade Level (FKGL) 
readability assessments on Zendesk help centre content.

It is designed for the Datavant technical writing team to quickly 
assess and improve the readability of their documentation.

## How it Works
1. Zendesk article content is exported and stored in the content folder
2. The content is pasted into Claude Console Workbench
3. Claude applies the FK formula using the official exclusion criteria
4. A full grade level score and breakdown is returned in seconds
5. Results are saved to the results folder for record keeping

## Target Score
All content should aim for Grade 8 or below on the 
Flesch-Kincaid Grade Level scale.

## Repository Structure
- content/ - Zendesk articles for analysis
- prompts/ - Claude analysis prompt and exclusion criteria
- results/ - Saved FK analysis outputs

## How to Use
See HOW-TO-USE.md for full instructions

## Tool Location
Claude Console Workbench - FK Readability Analysis Tool
platform.claude.com

## Built By
Cian Gallagher - Intern Engineer
