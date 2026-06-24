Read and follow CLAUDE.md.

Task:
Create exactly 1 new PhD-level theoretical physics article.

Hard requirements:

- Audit existing posts in `_posts/` before choosing the topic.
- Choose a topic that does not duplicate existing posts.
- Create exactly 1 new Markdown file in `_posts/`.
- Do not edit `_site/`.
- Do not modify protected files.
- Use valid Chirpy front matter.
- Use `math: true`.
- Use Asia/Singapore time with `+0800`.
- Do not use a future timestamp.
- Use Physics-focused categories only.
- Use lowercase tags only.
- Write in research-paper style.
- Target 3000–5000 words.
- Include the required article sections from CLAUDE.md.
- Include serious equations, derivations, consistency checks, pitfalls, and references.
- Treat Theory of Everything as an open research direction, not a solved claim.
- Do not invent fake references, fake DOI, fake arXiv IDs, fake authors, or fake journal metadata.

Math rendering:

- Follow all math rendering rules in CLAUDE.md.
- Never leave raw LaTeX outside math mode.
- Use display math for important equations.
- Use `aligned` for long equations.
- Do not use `\(...\)` or `\[...\]`.
- Do not place `$$...$$` inside prose lines.
- Do not indent equations with four spaces.

Before finishing:

- Run `git status --short _posts`.
- Confirm that exactly one new `_posts/*.md` file was created.
- Do not report success if no post file was created.
- Do not report success if raw LaTeX remains visible outside math mode.

Final response:
Report the created file, title, word count, build result, and math audit result.
