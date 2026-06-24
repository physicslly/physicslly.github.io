Read and follow CLAUDE.md.

Main task:
Review existing Physics posts first, identify topic gaps, then create exactly 1 new PhD-level theoretical physics article that does not duplicate existing articles.

This prompt is intended for GitHub Actions automation.
One workflow run should create exactly 1 article.
If the workflow runs every 12 hours, the expected output is 2 articles per 24 hours.

Requirements:
- Do not edit `_site/`.
- Do not modify protected files listed in CLAUDE.md.
- Only create or edit Markdown posts inside `_posts/`.
- Use valid Chirpy front matter.
- Use `math: true`.
- Use Physics-focused categories only.
- Use lowercase tags only.
- Do not use future dates.
- Write in research-paper style.
- Target 3000–5000 words.
- Include equations, derivations, notation, consistency checks, discussion, relation to the Theory of Everything, common pitfalls, conclusion, and references.
- Treat the Theory of Everything as an open research direction, not a solved claim.
- Do not invent fake references, fake DOI, fake arXiv IDs, fake authors, fake journals, or unsupported claims.

Before choosing the topic:
1. Audit all existing published Physics posts in `_posts/`.
2. Create a topic inventory.
3. Identify already-covered topics, equations, frameworks, and references.
4. Identify missing topic gaps.
5. Choose exactly 1 topic that does not substantially overlap with existing articles.

Math rendering requirements:
- Use inline math only for short expressions like `$g(\mu)$`.
- Use display math for important equations.
- Use `aligned` for long or multi-line equations.
- Never leave LaTeX commands outside math mode.
- Never put `$$...$$` inside a paragraph line.
- `$$` must be alone on its own line.
- Add blank lines before and after display equations.
- Do not indent equations or normal paragraphs with four spaces.
- Do not wrap equations in code blocks.
- Avoid malformed LaTeX.
- Avoid horizontal overflow.
- Every `\begin{aligned}` must have matching `\end{aligned}`.
- Every `\left` must have matching `\right`.

After writing:
1. Run a clean Jekyll build.
2. Run the math-rendering audit scripts from CLAUDE.md.
3. Fix all real LaTeX/rendering issues.
4. Rebuild after fixes.
5. Rerun the math audits.
6. Do not finish while real math-rendering errors remain.
7. If there are false positives, explain why they are false positives.
8. Recommend which article pages need manual browser review for heavy equations.

Final response must include:
1. Existing topic inventory summary.
2. Missing topic candidates.
3. Chosen topic and why it is not duplicate.
4. Created file.
5. Article title.
6. Word count.
7. Main equations included.
8. References used.
9. Whether `math: true` was added.
10. Build result.
11. Math audit result.
12. Remaining warnings or false positives.
13. Recommended manual browser review pages.
14. Local preview command:
   `bundle exec jekyll serve`
15. Local preview URL:
   `http://127.0.0.1:4000/`
