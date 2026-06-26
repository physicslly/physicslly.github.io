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

Repository inspection before writing:

Before creating the article, inspect only these files enough to understand the local rendering environment:

- `CLAUDE.md`
- `_config.yml`
- `Gemfile`
- `scripts/strict_math_audit.py`

Determine:

- the Jekyll theme
- active plugins
- timezone
- permalink/baseurl expectations
- Chirpy front matter expectations
- math-rendering constraints
- audit rules that must pass

Do not edit these files during article generation.

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
- Avoid fragile inline math.
- Do not use `\gamma_*`; prefer `\Gamma_{\mathrm{ch}}` or another safe notation.
- Do not use `$|0\rangle$`; use `\lvert 0 \rangle`.
- Convert transformations, field expansions, eigenvalue equations, and long definitions into display math.
- Do not put more than four inline math segments in one prose line.
- Do not use inline math longer than 80 characters.
- Use display math for anything complex.
- Avoid prose lines that mix many formulas and text.
- Ensure the article renders safely in Jekyll Chirpy, not merely as valid LaTeX.
- Never leave raw LaTeX outside math mode.
- Do not use `\(...\)` or `\[...\]`.
- Do not put equations in code fences.
- Do not indent equations with four spaces.
- Use display math for important or long equations.
- Use `aligned` for long multi-line equations.
- Do not report success if raw LaTeX remains outside math mode.

Diagram requirements:

- Include at most one Mermaid diagram when it genuinely clarifies the article.
- Prefer a conceptual flowchart or dependency map.
- Use `flowchart TD` or `graph TD`.
- Put the diagram after the introduction or theoretical framework section.
- If a Mermaid diagram is included, add `mermaid: true` to front matter.
- If no Mermaid diagram is included, do not add `mermaid: true`.
- Do not put LaTeX math inside Mermaid.
- Do not use `$...$`, `$$...$$`, `\frac`, `\mathcal`, `\partial`, Greek-letter commands, or equation syntax inside Mermaid labels.
- Mermaid node labels must be short plain English text.
- Explain the diagram in prose after the block.
- Do not include more than one Mermaid block.

After writing:

- Stop after writing and verification.
- Run `python scripts/strict_math_audit.py --changed-only`.
- Run `git status --short _posts`.
- Confirm exactly one new `_posts/*.md` file was created.
- Confirm there are no modified existing posts.
- Confirm the audit reports `TOTAL_STRICT_MATH_ISSUES=0`.
- If a Mermaid diagram exists, confirm `mermaid: true` exists in front matter.
- If no Mermaid diagram exists, confirm `mermaid: true` is absent.
- Confirm there is at most one Mermaid block.
- Confirm no LaTeX or math delimiters appear inside Mermaid blocks.
- Do not report success if the audit fails.
- Do not report success if the article contains fragile inline math patterns.
- Fail and report clearly if no post file was created.
- Fail and report clearly if more than one post file was created.
- Fail and report clearly if raw LaTeX remains outside math mode.

Final response:
Report the created file, title, word count, topic-deduplication basis, and math audit result.
