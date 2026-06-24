Read and follow CLAUDE.md.

Main task:
Review existing Physics posts first, identify topic gaps, then create exactly 1 new PhD-level theoretical physics article that does not duplicate existing articles.

This prompt is intended for GitHub Actions automation.
One workflow run should create exactly 1 article.
If the workflow runs every 12 hours, the expected output is 2 articles per 24 hours.

Date rule:
Use Asia/Singapore time for all new post dates.

The front matter date must use the +0800 timezone offset.

Never use a future timestamp. To avoid Jekyll skipping posts as future-dated, use a timestamp that has definitely already passed, preferably 00:01:00 +0800 on the current Singapore date, or yesterday's date if unsure.

Example:
date: YYYY-MM-DD 00:01:00 +0800

Never use fixed future-prone times like 10:00:00 +0800 unless that time has already passed.

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

## Mandatory Math Rendering Hard Gate

Before finishing any article-generation or article-editing task, perform a strict math rendering check.

This is mandatory. Do not finish, commit, or report success if raw LaTeX remains visible in prose.

Common broken patterns that must be fixed:

- `T_{\mu\nu}` outside math mode
- `\partial^{\mu}` outside math mode
- `\mathcal{O}` outside math mode
- `\Delta_i` outside math mode
- `\ell_i` outside math mode
- `\langle ... \rangle` outside math mode
- `\frac{...}{...}` outside math mode
- equations written directly inside bullet lists without display math
- long formulas written inline
- display equations mixed with prose on the same line
- indented math that becomes a grey code block

Correct examples:

Inline symbols must use `$...$`:

```md
The stress-energy tensor $T_{\mu\nu}$ is conserved, so $\partial^\mu T_{\mu\nu}=0$.
```

Operators must use `$...$`:

```md
A primary operator $\mathcal{O}_i(x)$ has scaling dimension $\Delta_i$ and spin $\ell_i$.
```

Long correlation functions must use display math:

```md
The two-point function takes the form

$$
\langle \mathcal{O}_i(x)\mathcal{O}_j(0)\rangle
=
\frac{\delta_{ij}}{|x|^{2\Delta_i}}.
$$
```

Long three-point functions must use display math and `aligned`:

```md
$$
\begin{aligned}
\langle
\mathcal{O}_i(x_1)
\mathcal{O}_j(x_2)
\mathcal{O}_k(x_3)
\rangle
&=
\frac{C_{ijk}}
{|x_{12}|^{\Delta_i+\Delta_j-\Delta_k}
 |x_{23}|^{\Delta_j+\Delta_k-\Delta_i}
 |x_{13}|^{\Delta_k+\Delta_i-\Delta_j}}.
\end{aligned}
$$
```

Bullet lists must not contain raw LaTeX. Bad:

```md
- Primary operators \mathcal{O}\_i(x) of scaling dimension \Delta_i.
```

Good:

```md
- Primary operators $\mathcal{O}_i(x)$ of scaling dimension $\Delta_i$.
```

Before finishing, run this strict audit:

````bash
python - <<'PY'
from pathlib import Path
import re

latex_cmd = re.compile(
    r'\\(frac|sum|int|ell|mu|nu|alpha|beta|gamma|delta|theta|lambda|partial|nabla|mathcal|mathrm|operatorname|langle|rangle|left|right|begin|end|sqrt|Lambda|Omega|rho|phi|psi|Gamma|sigma|equiv|cdot|times|infty|leq|geq|Delta|Phi|Psi)'
)

banned_delimiters = re.compile(r'\\\(|\\\)|\\\[|\\\]')

def strip_front_matter(text):
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[2]
    return text

def outside_inline_segments(line):
    parts = line.split('$')
    for i, part in enumerate(parts):
        if i % 2 == 0:
            yield part

issues = 0

for path in sorted(Path("_posts").glob("*.md")):
    text = strip_front_matter(path.read_text())
    in_code = False
    in_display = False

    for n, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code = not in_code
            continue

        if in_code:
            continue

        if stripped == "$$":
            in_display = not in_display
            continue

        if "$$" in line and stripped != "$$":
            print(f"INLINE_DISPLAY_MATH {path}:{n}: {line[:240]}")
            issues += 1

        if not in_display and line.count("$") % 2 == 1:
            print(f"UNBALANCED_DOLLAR {path}:{n}: {line[:240]}")
            issues += 1

        if not in_display and banned_delimiters.search(line):
            print(f"BANNED_LATEX_DELIMITER {path}:{n}: {line[:240]}")
            issues += 1

        if not in_display:
            for segment in outside_inline_segments(line):
                if latex_cmd.search(segment):
                    print(f"RAW_LATEX_OUTSIDE_MATH {path}:{n}: {line[:240]}")
                    issues += 1
                    break

        for m in re.finditer(r'\$([^$]{100,})\$', line):
            print(f"LONG_INLINE_MATH {path}:{n}: {m.group(0)[:240]}")
            issues += 1

        if line.count("\\left") != line.count("\\right"):
            print(f"LEFT_RIGHT_MISMATCH {path}:{n}: {line[:240]}")
            issues += 1

        if re.search(r'^\s{4,}.*(\\|\$|theta|lambda|mu|nu|ell|Delta|mathcal)', line):
            print(f"POSSIBLE_CODE_BLOCK_MATH {path}:{n}: {line[:240]}")
            issues += 1

print(f"TOTAL_STRICT_MATH_ISSUES={issues}")

if issues:
    raise SystemExit(1)
PY
````

If the audit fails:

1. Open the exact reported file and line.
2. Convert raw LaTeX symbols into inline math using `$...$`.
3. Convert long formulas into display math.
4. Use `aligned` for long equations.
5. Rebuild the site.
6. Rerun the strict audit.
7. Repeat until `TOTAL_STRICT_MATH_ISSUES=0`.

Do not treat real raw LaTeX as a false positive.

Only false positives inside intentional code examples are allowed.

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
