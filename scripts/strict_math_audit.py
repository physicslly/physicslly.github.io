#!/usr/bin/env python3
r"""
Strict Math Rendering Audit for Jekyll Chirpy Blog Posts.

Audits Markdown posts in _posts/ for common math rendering issues:
  - Raw LaTeX commands outside math mode ($...$ or $$...$$)
  - Banned \(...\) and \[...\] delimiters (use $...$ and $$...$$ instead)
  - Display math placed inline inside prose ($$ on same line as text)
  - Unbalanced inline dollar signs
  - Long inline math expressions (over 80 chars inside a single $...$)
  - Too many inline math segments in one long prose line
  - Inline math with too many LaTeX commands
  - Display math without blank lines around $$ delimiters
  - Dangling math subscripts/superscripts (_ or ^ without a following token)
  - Fragile star subscript notation such as \gamma_*
  - Fragile raw ket notation such as |0\rangle
  - \left / \right mismatch
  - Accidental indented math that becomes a Markdown code block

Usage:
    python scripts/strict_math_audit.py              # audit all posts
    python scripts/strict_math_audit.py --all        # audit all posts
    python scripts/strict_math_audit.py --changed-only  # audit only changed/new posts
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


MAX_INLINE_MATH_CHARS = 80
MAX_INLINE_MATH_SEGMENTS = 4
MAX_INLINE_MATH_SEGMENT_LINE_CHARS = 120
MAX_INLINE_LATEX_COMMANDS = 2

# LaTeX commands that must appear inside math mode
LATEX_CMD_PATTERN = re.compile(
    r"\\(frac|sum|int|ell|mu|nu|alpha|beta|gamma|delta|theta|lambda|partial|"
    r"nabla|mathcal|mathrm|operatorname|langle|rangle|left|right|begin|end|"
    r"sqrt|Lambda|Omega|rho|phi|psi|Gamma|sigma|equiv|cdot|times|infty|leq|"
    r"geq|Delta|Phi|Psi)"
)

# Banned LaTeX delimiters — should use $...$ and $$...$$ instead
BANNED_DELIMITERS = re.compile(r"\\\(|\\\)|\\\[|\\\]")

# A math script marker must be followed by a real script token, not whitespace,
# punctuation, a closing delimiter, or end-of-segment.
DANGLING_SCRIPT_PATTERN = re.compile(r"(?<!\\)([_^])(?=($|\s|[=,.;:\)\]\}]))")

# Star subscripts can be parsed as Markdown emphasis before MathJax sees them.
FRAGILE_STAR_SUBSCRIPT_PATTERN = re.compile(r"(\\gamma_\*|(?<!\\)_\*)")

# Prefer explicit LaTeX delimiters for kets in Markdown math.
FRAGILE_KET_PATTERN = re.compile(
    r"(?<!\\)\|[^|$\n]*\\rangle|\\langle[^|$\n]*(?<!\\)\|"
)

# Count LaTeX commands in inline math. Three or more usually belongs in display math.
LATEX_COMMAND_IN_MATH_PATTERN = re.compile(r"\\[A-Za-z]+")

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


def math_segments(line, in_display):
    """Yield Markdown math segments from *line*."""
    if in_display:
        yield line
        return

    parts = line.split("$")
    for i in range(1, len(parts), 2):
        yield parts[i]


def inline_math_segments(line):
    """Yield inline $...$ math segments from *line*."""
    parts = line.split("$")
    for i in range(1, len(parts), 2):
        yield parts[i]


def has_blank_line(lines, index):
    """Return True when *index* is outside the file or points to a blank line."""
    return index < 0 or index >= len(lines) or lines[index].strip() == ""


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
            if not in_display:
                if not has_blank_line(lines, n - 2):
                    report.append(
                        f"DISPLAY_MATH_BLANK_LINE {path}:{n}: opening $$ must be preceded by a blank line"
                    )
            else:
                if not has_blank_line(lines, n):
                    report.append(
                        f"DISPLAY_MATH_BLANK_LINE {path}:{n}: closing $$ must be followed by a blank line"
                    )
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

        # --- Check 5: long inline math (>80 chars inside actual $...$ segments) ---
        if not in_display:
            parts = line.split("$")
            inline_count = (len(parts) - 1) // 2

            # Odd indexes are actual inline math segments:
            # text $math$ text $math$ text
            # parts[0] text, parts[1] math, parts[2] text, parts[3] math
            for segment in inline_math_segments(line):
                if len(segment) > MAX_INLINE_MATH_CHARS:
                    report.append(
                        f"LONG_INLINE_MATH {path}:{n}: ${segment[:240]}$"
                    )

            if (
                inline_count > MAX_INLINE_MATH_SEGMENTS
                and len(line) > MAX_INLINE_MATH_SEGMENT_LINE_CHARS
            ):
                report.append(
                    f"MANY_INLINE_MATH_SEGMENTS {path}:{n}: {line[:240]}"
                )

        # --- Check 6: too many LaTeX commands in inline math ---
        if not in_display:
            for segment in inline_math_segments(line):
                command_count = len(LATEX_COMMAND_IN_MATH_PATTERN.findall(segment))
                if command_count >= MAX_INLINE_LATEX_COMMANDS + 1:
                    report.append(
                        f"MULTI_COMMAND_INLINE_MATH {path}:{n}: ${segment[:240]}$"
                    )
                    break

        # --- Check 7: fragile star subscript notation ---
        for segment in math_segments(line, in_display):
            if FRAGILE_STAR_SUBSCRIPT_PATTERN.search(segment):
                report.append(
                    f"FRAGILE_STAR_SUBSCRIPT {path}:{n}: {line[:240]}"
                )
                break

        # --- Check 8: fragile raw ket notation ---
        for segment in math_segments(line, in_display):
            if FRAGILE_KET_PATTERN.search(segment):
                report.append(
                    f"FRAGILE_KET_NOTATION {path}:{n}: {line[:240]}"
                )
                break

        # --- Check 9: dangling math subscript/superscript ---
        for segment in math_segments(line, in_display):
            if DANGLING_SCRIPT_PATTERN.search(segment):
                report.append(
                    f"DANGLING_SUBSCRIPT_OR_SUPERSCRIPT {path}:{n}: {line[:240]}"
                )
                break

        # --- Check 10: \left / \right mismatch ---
        if line.count("\\left") != line.count("\\right"):
            report.append(
                f"LEFT_RIGHT_MISMATCH {path}:{n}: {line[:240]}"
            )

        # --- Check 11: accidental code block from indented math ---
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
    parser.add_argument(
        "--all",
        action="store_true",
        help="Audit all posts under _posts/. This is the default.",
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
