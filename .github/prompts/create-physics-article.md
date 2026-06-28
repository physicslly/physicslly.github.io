Follow the relevant article rules in `CLAUDE.md`.

Task:
Create exactly 1 new PhD-level theoretical physics article.

Turn-budget rules:

- Finish the task within the available Claude Code turn budget.
- Do not over-plan.
- Do not repeatedly inspect the same files.
- Do not perform broad repository exploration.
- Do not read full existing posts.
- Do not run full-site audits inside the article-generation prompt.
- Do not run `bundle exec jekyll build`; the GitHub Actions workflow handles the build.
- Do not run `python scripts/strict_math_audit.py --all`; use only `--changed-only` after writing.
- Create exactly one article, run the minimal required verification, and stop.

Scope:

- Inspect existing post metadata before choosing a topic.
- Avoid duplicate topics.
- Do not read full existing posts.
- Inspect only filenames, front matter titles, tags, and headings.
- Create exactly one new `_posts/*.md` file.
- Do not edit `_site/`.
- Do not edit existing posts.
- Do not edit protected files.

Repository inspection before writing:

Before choosing a topic, inspect only:

- `CLAUDE.md` headings or relevant short sections
- `_config.yml` front matter / permalink / timezone settings
- existing `_posts/*.md` filenames
- existing post titles and tags using grep/head/sed

Do not read full existing posts.
Do not inspect unrelated files.
Do not inspect `_site/`.

Topic selection:

Choose a topic quickly based on filenames, front matter titles, tags, and headings only.

Avoid duplicate topics, but do not perform a full literature review of the repository.

PhD-level topic selection:

- Choose a narrow technical topic, not a broad textbook overview.
- Avoid generic introductory topics unless framed around a specific theorem, derivation, obstruction, or technical problem.
- The article must have a central technical question.
- Prefer topics that support a real derivation, consistency checks, and limitations.

Article requirements:

- Write around 1600-2200 words.
- Use valid Chirpy front matter.
- Include `math: true`.
- Use Asia/Singapore time with `+0800`.
- Do not use a future timestamp.
- Use Physics-focused categories.
- Use lowercase kebab-case tags only.
- Do not use spaces or uppercase letters in tags.
- Use research-paper style suitable for PhD-level theoretical physics readers.
- Frame the article around one central technical question.
- Include assumptions and notation.
- Include precise definitions before heavy use of symbols.
- Include one main derivation with intermediate steps.
- Interpret the main equation term by term.
- Include consistency checks or limiting cases.
- Include limitations or open problems.
- Include canonical references and use in-text citation markers like `[1]`, `[2]`.
- Avoid broad textbook-style summaries.
- Treat Theory of Everything as an open research direction, not a solved claim.
- Do not invent fake references, DOI values, arXiv IDs, authors, or journal metadata.

Abstract and keywords requirements:

- The `## Abstract` section must start with a normal abstract paragraph.
- Do not put `**Keywords:**` immediately after `## Abstract`.
- Put exactly one `**Keywords:**` line after the abstract paragraph.
- Do not use a separate `## Keywords` heading.
- The order must be:

```md
## Abstract

Abstract paragraph.

**Keywords:** keyword one, keyword two, keyword three

## 1. Introduction
```

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

Research-depth requirements:

The article must include at least six of the following elements:

- central technical question
- assumptions and scope
- notation and conventions
- precise definitions
- proposition, theorem, lemma, or proof sketch
- main derivation
- term-by-term equation interpretation
- consistency checks
- limiting cases
- worked technical example
- comparison with related formulations
- limitations or open problems
- in-text citation markers tied to canonical references

Do not force a Mermaid diagram. Diagrams are optional.

Diagram requirements:

- Mermaid is optional.
- Include a Mermaid diagram only if it clearly improves the article and can be written simply.
- If including Mermaid, use exactly one small diagram with 4-7 nodes.
- Prefer `flowchart TD`.
- Use plain English labels only.
- Do not put LaTeX or `$...$` inside Mermaid.
- If a Mermaid block is included, add `mermaid: true` to front matter.
- If no Mermaid block is included, do not add `mermaid: true`.
- If adding a diagram would slow the task down, skip the diagram.

After writing:

- Run `python scripts/strict_math_audit.py --changed-only` once.
- Run `git status --short _posts`.
- Confirm the article is not a generic textbook overview.
- Confirm the article states a central technical question.
- Confirm the article includes assumptions or notation.
- Confirm the article includes a real derivation.
- Confirm the article includes consistency checks, limiting cases, or limitations.
- Confirm references are canonical and include in-text citation markers.
- Confirm exactly one new `_posts/*.md` file was created.
- Confirm there are no modified existing posts.
- Confirm the audit reports `TOTAL_STRICT_MATH_ISSUES=0`.
- Confirm `## Abstract` is followed by an abstract paragraph before the `**Keywords:**` line.
- Confirm there is exactly one `**Keywords:**` line.
- Confirm there is no `## Keywords` heading.
- Stop.

Final response:
Report the created file, title, word count, topic-deduplication basis, and math audit result.
