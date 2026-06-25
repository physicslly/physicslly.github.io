Read and follow `CLAUDE.md`.

Task:
Create exactly 1 new PhD-level theoretical physics article.

Scope:

- Audit existing posts in `_posts/` before choosing a topic.
- Avoid duplicate topics.
- Do not read full existing posts.
- Inspect only filenames, front matter titles, tags, and headings.
- Create exactly one new `_posts/*.md` file.
- Do not edit `_site/`.
- Do not edit existing posts.
- Do not edit protected files.

Article requirements:

- Write around 1800-2500 words.
- Use valid Chirpy front matter.
- Include `math: true`.
- Use Asia/Singapore time with `+0800`.
- Do not use a future timestamp.
- Use Physics-focused categories.
- Use lowercase kebab-case tags only.
- Do not use spaces or uppercase letters in tags.
- Use research-paper style suitable for PhD-level theoretical physics readers.
- Treat Theory of Everything as an open research direction, not a solved claim.
- Do not invent fake references, DOI values, arXiv IDs, authors, or journal metadata.

Math requirements:

- Follow the math rules in `CLAUDE.md`.
- Never leave raw LaTeX outside math mode.
- Do not use `\(...\)` or `\[...\]`.
- Do not put equations in code fences.
- Do not indent equations with four spaces.
- Use display math for important or long equations.
- Use `aligned` for long multi-line equations.
- Do not report success if raw LaTeX remains outside math mode.

After writing:

- Stop after writing and verification.
- Run `git status --short _posts`.
- Confirm exactly one new `_posts/*.md` file was created.
- Fail and report clearly if no post file was created.
- Fail and report clearly if more than one post file was created.
- Fail and report clearly if raw LaTeX remains outside math mode.

Final response:
Report the created file, title, word count, topic-deduplication basis, and math audit result.
