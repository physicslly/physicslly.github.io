# Tilanou Blog Instructions

## Project Context

This repository is a Jekyll Chirpy Starter blog.

Production URL:

https://physicslly.github.io/

This is a GitHub Pages user site, not a project site.

Keep these settings in `_config.yml`:

```yaml
url: "https://physicslly.github.io"
baseurl: ""
```

Do not use a custom domain.

Do not create or modify `CNAME`.

Do not edit `_site/` because it is generated output.

## Blog Identity

Blog name:

Tilanou

Tagline:

Theory of Everything

Niche:

Physics, theoretical physics, mathematical physics, quantum field theory, general relativity, quantum gravity, cosmology, gauge theory, topology, geometry, renormalization, effective field theory, and the search for unification.

Important positioning:

The phrase "Theory of Everything" is used as a thematic direction, not as a solved claim.

Never claim that this blog has solved the Theory of Everything.

Treat the Theory of Everything as an open research direction involving unification, quantum gravity, quantum field theory, geometry, cosmology, and mathematical physics.

## Protected Files

Do not modify these unless explicitly asked:

- `privacy-policy.md`
- `disclaimer.md`
- `_includes/footer.html`
- `ads.txt`
- `robots.txt`
- sitemap configuration
- AdSense script
- GitHub Actions workflow
- `CNAME`
- `_site/`

## Article Style

All new articles must be written in research-paper style.

Every article should feel like advanced theoretical physics lecture notes, a mini review paper, or a research-style exposition.

Use an academic tone:

- precise
- formal
- rigorous
- careful
- no hype
- no clickbait
- no fake certainty
- no fake citations
- no fake DOI
- no fake arXiv IDs
- no fake journal metadata
- no unsupported research claims

Do not write shallow popular-science summaries.

Do not claim that open research problems are solved.

## Article Structure

Every new Physics article must include:

```md
## Abstract

## Keywords

## 1. Introduction

## 2. Preliminaries and Notation

## 3. Theoretical Framework

## 4. Main Derivation

## 5. Interpretation of the Main Equations

## 6. Consistency Checks and Limiting Cases

## 7. Discussion

## 8. Relation to the Theory of Everything

## 9. Common Pitfalls

## 10. Conclusion

## References
```

## Depth Requirements

Each article should be suitable for advanced graduate or PhD-level readers.

Each article must include:

- precise definitions
- assumptions
- notation
- mathematical setup
- at least one serious derivation
- key equations
- term-by-term interpretation of important equations
- consistency checks or limiting cases
- advanced conceptual discussion
- relation to the Theory of Everything
- common pitfalls
- references

Target article length:

3000–5000 words.

Do not add filler just to reach word count.

## Front Matter Template

Use this front matter style for every new article:

```yaml
---
title: "Article Title"
date: 2026-06-23 10:00:00 +0700
categories: [Physics, Theory]
tags: [physics, theoretical-physics, theory-of-everything]
description: "A concise technical description of the article."
math: true
---
```

Rules:

- Use Physics-focused categories only.
- Use lowercase tags only.
- Do not use old tech/Linux/cybersecurity tags.
- Do not use future dates.
- Preserve valid Chirpy front matter.
- Always include `math: true`.

## Math Rendering Rules

This blog uses Jekyll/Chirpy math rendering. Math must be written carefully so formulas render correctly in the browser.

Every Physics post must include:

```yaml
math: true
```

Use inline math only for short expressions:

```md
The coupling $g(\mu)$ runs with the scale $\mu$.
```

Use display math for important equations:

```md
The beta function is defined as

$$
\beta(g)
=
\mu \frac{dg}{d\mu}.
$$

This expression describes the response of the coupling to a change of scale.
```

Use `aligned` for long or multi-line equations:

```md
$$
\begin{aligned}
S
&=
S_{\mathrm{SM}}
+
S_{\mathrm{EH}}
+
S_{\mathrm{beyond}}, \\
S_{\mathrm{EH}}
&=
\frac{c^3}{16\pi G}
\int d^4x\,\sqrt{-g}\,(R-2\Lambda).
\end{aligned}
$$
```

Strict math rules:

- Never leave LaTeX commands outside math mode.
- Never use long inline equations.
- Never put `$$...$$` inside a paragraph line.
- `$$` must appear alone on its own line.
- Always add a blank line before and after display equations.
- Do not indent equations with four spaces.
- Do not indent normal paragraphs with four spaces.
- Do not wrap equations in backticks.
- Do not place equations inside code blocks unless explaining literal syntax.
- Use `aligned` for wide equations.
- Avoid horizontal overflow.
- Avoid malformed LaTeX.
- Every `\begin{aligned}` must have matching `\end{aligned}`.
- Every `\left` must have matching `\right`.

Bad:

```md
The equation is $$G_{\mu\nu}=8\pi GT_{\mu\nu}$$ and it means curvature.
```

Good:

```md
The equation is

$$
G_{\mu\nu}
=
\frac{8\pi G}{c^4}
T_{\mu\nu}.
$$

It relates spacetime curvature to stress-energy.
```

Bad:

```md
The expansion becomes θ

    → −∞ at finite affine parameter \lambda \le 3/\theta_0.
```

Good:

```md
The expansion becomes $\theta \to -\infty$ at a finite affine parameter,

$$
\lambda
\leq
\frac{3}{|\theta_0|}.
$$

This implies that nearby null geodesics develop a caustic within finite affine parameter whenever $\theta_0 < 0$.
```

## Reference Rules

Every article must include a `## References` section.

Use numbered references:

```md
[1] Author, _Book or Paper Title_, Publisher or Journal, Year.
```

Use in-text citations like `[1]`, `[2]`, `[3]`.

Rules:

- Do not cite Wikipedia.
- Do not cite random websites.
- Prefer canonical textbooks, foundational papers, and standard review-style references.
- Do not invent fake DOI.
- Do not invent fake arXiv IDs.
- Do not invent fake authors.
- Do not invent fake journal metadata.
- If exact metadata is uncertain, keep it conservative.

## Topic Selection Rules

Before creating a new article:

1. Audit all existing published Physics posts in `_posts/`.
2. Create a topic inventory.
3. Identify already-covered frameworks, equations, and conceptual focus.
4. Propose missing topic gaps.
5. Choose a topic that does not duplicate existing articles.

A topic is duplicate if it substantially overlaps in:

- title
- framework
- equations
- references
- conceptual focus
- intended reader takeaway

Prefer advanced missing topics such as:

- quantum anomalies
- supersymmetry
- spinors and Clifford algebras
- conformal field theory
- AdS/CFT correspondence
- black hole thermodynamics
- holographic principle
- BRST symmetry
- instantons
- canonical quantization
- Hamiltonian formulation of general relativity
- singularity theorems
- causal structure and Penrose diagrams
- Noether currents and Ward identities
- vacuum structure in QFT
- geometric quantization
- path integral measure and anomalies
- modular Hamiltonians
- tensor networks and holography
- asymptotic symmetries
- spontaneous symmetry breaking
- Higgs mechanism
- neutrino masses and beyond Standard Model physics

## Build Verification

After creating or editing articles, always run:

```bash
rm -rf .jekyll-cache _site
bundle exec jekyll build 2>&1 | tee /tmp/jekyll-build.log
```

Then check:

```bash
grep -Ei "Conflict|Skipping|Error|Warning" /tmp/jekyll-build.log || true
find _site -maxdepth 4 -type f -name "index.html" | grep "/posts/" | wc -l
grep -c "<loc>" _site/sitemap.xml
grep -RIn "math: true" _posts | wc -l
```

Expected:

- No build errors.
- No future-date skipping.
- No conflict warnings.
- Sitemap updates correctly.
- New articles appear in `_site`.

## Required Math Audit After Writing

After creating or editing an article, run this audit to detect likely math rendering problems:

````bash
python - <<'PY'
from pathlib import Path
import re

latex_cmd = re.compile(
    r'\\(frac|sum|int|ell|mu|nu|alpha|beta|gamma|delta|theta|lambda|partial|nabla|mathcal|mathrm|operatorname|langle|rangle|left|right|begin|end|sqrt|Lambda|Omega|rho|phi|psi|Gamma|sigma|equiv|cdot|times|infty|leq|geq)'
)

def strip_front_matter(text):
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[2]
    return text

def in_inline_math(line, idx):
    before = line[:idx]
    return before.count('$') % 2 == 1

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

        if not in_display and line.count("$") % 2 == 1:
            print(f"UNBALANCED_DOLLAR {path}:{n}: {line[:240]}")
            issues += 1

        if "$$" in line and stripped != "$$":
            print(f"INLINE_DISPLAY_MATH {path}:{n}: {line[:240]}")
            issues += 1

        for m in latex_cmd.finditer(line):
            if not in_display and not in_inline_math(line, m.start()):
                print(f"LATEX_OUTSIDE_MATH {path}:{n}: {line[:240]}")
                issues += 1

        for m in re.finditer(r'\$([^$]{100,})\$', line):
            print(f"LONG_INLINE_MATH {path}:{n}: {m.group(0)[:240]}")
            issues += 1

        if line.count("\\left") != line.count("\\right"):
            print(f"LEFT_RIGHT_MISMATCH {path}:{n}: {line[:240]}")
            issues += 1

print(f"TOTAL_ISSUES={issues}")
PY
````

Also run this audit for accidental Markdown code blocks around math:

```bash
python - <<'PY'
from pathlib import Path
import re

patterns = [
    r'^\s{4,}.*\\',
    r'^\t+.*\\',
    r'^\s{4,}.*\$',
    r'^\t+.*\$',
    r'^\s{4,}.*theta',
    r'^\s{4,}.*lambda',
    r'^\s{4,}.*ell',
    r'^\s{4,}.*mu',
    r'^\s{4,}.*nu',
]

for path in sorted(Path("_posts").glob("*.md")):
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines, 1):
        for pat in patterns:
            if re.search(pat, line):
                print(f"POSSIBLE_CODE_BLOCK_MATH {path}:{i}: {line[:240]}")
PY
```

If issues are found:

- inspect the exact file and line
- fix the source Markdown
- rebuild
- rerun the math audit
- repeat until clean or until only justified false positives remain

## Final Response Requirements

After each task, report:

1. Files created or edited.
2. Article titles created or improved.
3. Topic inventory summary.
4. Why the chosen topic is not duplicate.
5. Whether `math: true` was used.
6. References added.
7. Build result.
8. Math audit result.
9. Any warnings or false positives.
10. Local preview command:

```bash
bundle exec jekyll serve
```

11. Local preview URL:

```text
http://127.0.0.1:4000/
```

## Reusable Article Creation Workflow

When I ask to create a new article, always follow this workflow:

1. Read CLAUDE.md first.
2. Audit existing posts in `_posts/`.
3. Build a topic inventory.
4. Identify already-covered topics and missing topic gaps.
5. Choose only topics that do not duplicate existing articles.
6. Create exactly the number of articles requested.
7. Write each article in research-paper style.
8. Use `math: true`.
9. Use display math for important equations.
10. Use `aligned` for wide equations.
11. Never leave LaTeX commands outside math mode.
12. Never indent normal paragraphs or equations with four spaces.
13. Run a clean build.
14. Run the math audit scripts from CLAUDE.md.
15. Fix all real math-rendering issues before finishing.
16. If the audit reports false positives, explain why they are false positives.
17. Recommend manual browser review for posts with heavy equations.

Standard reusable prompt:

"Read and follow CLAUDE.md. Review existing Physics posts first, identify topic gaps, then create exactly 1 new PhD-level theoretical physics article that does not duplicate existing articles. After writing, build the site and run the math-rendering audits from CLAUDE.md. Fix all real LaTeX/rendering issues before finishing. Recommend which article pages need manual browser review for heavy equations."

## GitHub Actions Article Automation

This repository may use GitHub Actions to run Claude Code automatically.

When Claude is executed from GitHub Actions, follow these rules:

1. Read `CLAUDE.md` first.
2. Treat the repository root as the source of truth.
3. Create exactly 1 new article per workflow run unless the prompt explicitly requests a different number.
4. The scheduled workflow may run every 12 hours, so the expected output is 2 articles per 24 hours.
5. Always audit existing posts before choosing a topic.
6. Build a topic inventory before writing.
7. Never duplicate existing article topics.
8. Never edit `_site/`.
9. Never modify protected files unless explicitly requested.
10. Only create or edit Markdown posts inside `_posts/` during article-generation runs.
11. Use valid Chirpy front matter.
12. Use `math: true` in every new Physics article.
13. Use Physics-focused categories only.
14. Use lowercase tags only.
15. Do not use future dates.
16. Treat the Theory of Everything as an open research direction, not a solved claim.
17. Run the Jekyll build after writing.
18. Run the math-rendering audit scripts from this file.
19. Fix all real LaTeX/rendering issues before finishing.
20. If the audit reports false positives, explain why they are false positives.
21. Recommend manual browser review for equation-heavy posts.
22. Treat the article as a draft that will be reviewed through a Pull Request.
