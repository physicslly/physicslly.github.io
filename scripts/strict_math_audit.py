#!/usr/bin/env python3
r"""
Strict Math Rendering Audit for Jekyll Chirpy Blog Posts.

Audits Markdown posts in _posts/ for common math rendering issues:
  - Raw LaTeX commands outside math mode ($...$ or $$...$$)
  - Banned \(...\) and \[...\] delimiters (use $...$ and $$...$$ instead)
  - Display math placed inline inside prose ($$ on same line as text)
  - Unbalanced inline dollar signs
  - Long inline math expressions (over 100 chars inside a single $...$)
  - \left / \right mismatch
  - Accidental indented math that becomes a Markdown code block

Usage:
    python scripts/strict_math_audit.py              # audit all posts
    python scripts/strict_math_audit.py --changed-only  # audit only changed/new posts
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


# LaTeX commands that must appear inside math mode
LATEX_CMD_PATTERN = re.compile(
    r"\\(frac|sum|int|ell|mu|nu|alpha|beta|gamma|delta|theta|lambda|partial|"
    r"nabla|mathcal|mathrm|operatorname|langle|rangle|left|right|begin|end|"
    r"sqrt|Lambda|Omega|rho|phi|psi|Gamma|sigma|equiv|cdot|times|infty|leq|"
    r"geq|Delta|Phi|Psi)"
)

# Banned LaTeX delimiters — should use $...$ and $$...$$ instead
BANNED_DELIMITERS = re.compile(r"\\\(|\\\)|\\\[|\\\]")

# For detecting accidental code blocks from indented math
CODE_BLOCK_PATTERNS = [
    re.compile(r"^\s{4,}.*\\"),
    re.compile(r"^\t+.*\\"),
    re.compile(r"^\s{4,}.*\$"),
    re.compile(r"^\t+.*\$"),
    re.compile(r"^\s{4,}.*\btheta\b"),
    re.compile(r"^\s{4,}.*\blambda\b"),
    re.compile(r"^\s{4,}.*\bell\b"),
    re.compile(r"^\s{4,}.*\bmu\b"),
    re.compile(r"^\s{4,}.*\bnu\b"),
    re.compile(r"^\s{4,}.*\bDelta\b"),
    re.compile(r"^\s{4,}.*\bmathcal\b"),
]

POSTS_DIR = Path("_posts")


def get_changed_posts():
    """Return set of filenames for changed/new posts under _posts/."""
    try:
        result = subprocess.run(
            ["git", "status", "--short", "_posts"],
            capture_output=True,
            text=True,
            check=True,
            cwd=os.getcwd(),
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Not in a git repo or git unavailable — exit cleanly
        return None

    changed = set()
    for raw_line in result.stdout.splitlines():
        if not raw_line.strip():
            continue
        # Git status short format: "XY filename"
        # X = staging area status (space for unmodified)
        # Y = working tree status
        # ?? = untracked file
        # Filename starts at index 3 for standard entries, index 3 for ?? entries
        if raw_line.startswith("??"):
            # Untracked file — line is "?? filename"
            filename = raw_line[3:].strip()
        else:
            # Tracked file — line is "XY filename" (each char may be space)
            filename = raw_line[3:].strip()
        # Only care about files under _posts/
        if filename.startswith("_posts/") and filename.endswith(".md"):
            changed.add(filename)

    return changed


def strip_front_matter(text):
    """Remove YAML front matter from Markdown text."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def outside_inline_segments(line):
    """Yield segments of *line* that are outside $...$ inline math."""
    parts = line.split("$")
    for i, part in enumerate(parts):
        if i % 2 == 0:
            yield part


def audit_file(path, report):
    """Audit a single Markdown file. Append issues to *report*."""
    text = path.read_text(encoding="utf-8")
    text = strip_front_matter(text)

    in_code = False
    in_display = False
    lines = text.splitlines()

    for n, line in enumerate(lines, 1):
        stripped = line.strip()

        # Track fenced code blocks
        if stripped.startswith("```"):
            in_code = not in_code
            continue

        if in_code:
            continue

        # Track display math ($$ on its own line)
        if stripped == "$$":
            in_display = not in_display
            continue

        # --- Check 1: display math embedded inline in prose ---
        if "$$" in line and stripped != "$$":
            report.append(
                f"INLINE_DISPLAY_MATH {path}:{n}: {line[:240]}"
            )
            continue

        # --- Check 2: unbalanced dollar signs (outside display math) ---
        if not in_display and line.count("$") % 2 == 1:
            report.append(
                f"UNBALANCED_DOLLAR {path}:{n}: {line[:240]}"
            )

        # --- Check 3: banned LaTeX delimiters \( \) \[ \] ---
        if not in_display and BANNED_DELIMITERS.search(line):
            report.append(
                f"BANNED_LATEX_DELIMITER {path}:{n}: {line[:240]}"
            )

        # --- Check 4: raw LaTeX commands outside math mode ---
        if not in_display:
            for segment in outside_inline_segments(line):
                if LATEX_CMD_PATTERN.search(segment):
                    report.append(
                        f"RAW_LATEX_OUTSIDE_MATH {path}:{n}: {line[:240]}"
                    )
                    break

        # --- Check 5: long inline math (>100 chars inside $...$) ---
        for m in re.finditer(r"\$([^$]{100,})\$", line):
            report.append(
                f"LONG_INLINE_MATH {path}:{n}: {m.group(0)[:240]}"
            )

        # --- Check 6: \left / \right mismatch ---
        if line.count("\\left") != line.count("\\right"):
            report.append(
                f"LEFT_RIGHT_MISMATCH {path}:{n}: {line[:240]}"
            )

        # --- Check 7: accidental code block from indented math ---
        for pat in CODE_BLOCK_PATTERNS:
            if pat.search(line):
                report.append(
                    f"POSSIBLE_CODE_BLOCK_MATH {path}:{n}: {line[:240]}"
                )
                break


def main():
    parser = argparse.ArgumentParser(
        description="Strict math rendering audit for Jekyll Chirpy blog posts."
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Only audit files changed or new in working tree under _posts/.",
    )
    args = parser.parse_args()

    # Determine which posts to audit
    if args.changed_only:
        changed = get_changed_posts()
        if changed is None:
            print("::warning:: Git not available — falling back to full audit.")
            posts = sorted(POSTS_DIR.glob("*.md"))
        elif not changed:
            print("No changed posts to audit. Exiting cleanly.")
            sys.exit(0)
        else:
            posts = [POSTS_DIR / Path(f).name for f in changed]
            # Only keep files that actually exist
            posts = [p for p in posts if p.exists()]
            if not posts:
                print("Changed files no longer on disk. Exiting cleanly.")
                sys.exit(0)
            print(f"Auditing {len(posts)} changed/new post(s):")
            for p in posts:
                print(f"  {p}")
    else:
        posts = sorted(POSTS_DIR.glob("*.md"))
        if not posts:
            print("No posts found in _posts/. Exiting cleanly.")
            sys.exit(0)
        print(f"Auditing all {len(posts)} post(s):")
        for p in posts:
            print(f"  {p}")

    print()

    # Run audit
    report = []
    for post in posts:
        audit_file(post, report)

    # Report results
    total = len(report)
    if total == 0:
        print(f"TOTAL_STRICT_MATH_ISSUES=0 — no issues found.")
        sys.exit(0)
    else:
        print(f"\n--- Found {total} issue(s) ---\n")
        for entry in report:
            print(entry)
        print(f"\nTOTAL_STRICT_MATH_ISSUES={total}")
        sys.exit(1)


if __name__ == "__main__":
    main()
