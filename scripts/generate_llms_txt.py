#!/usr/bin/env python3
"""Generate root-level llms.txt from Jekyll post metadata.

The parser intentionally handles only the simple YAML subset used by this site:
top-level scalar keys, inline arrays, booleans, and quoted strings.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "_config.yml"
POSTS_DIR = ROOT / "_posts"
OUTPUT_PATH = ROOT / "llms.txt"


@dataclass(frozen=True)
class Post:
    title: str
    url: str
    description: str
    categories: list[str]
    tags: list[str]
    math: bool
    sort_date: datetime
    source: Path


def strip_inline_comment(value: str) -> str:
    in_single = False
    in_double = False
    escaped = False

    for index, char in enumerate(value):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "'" and not in_double:
            in_single = not in_single
            continue
        if char == '"' and not in_single:
            in_double = not in_double
            continue
        if char == "#" and not in_single and not in_double:
            return value[:index].rstrip()
    return value.strip()


def parse_scalar(value: str) -> object:
    value = strip_inline_comment(value).strip()
    if not value:
        return ""
    if value in {"true", "false"}:
        return value == "true"
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part) for part in inner.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_simple_yaml(text: str) -> dict[str, object]:
    data: dict[str, object] = {}
    lines = text.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index]
        index += 1

        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()

        if raw_value in {">-", ">", "|-", "|"}:
            block_lines: list[str] = []
            while index < len(lines):
                next_line = lines[index]
                if next_line and not next_line.startswith((" ", "\t")):
                    break
                stripped = next_line.strip()
                if stripped:
                    block_lines.append(stripped)
                index += 1
            data[key] = " ".join(block_lines)
            continue

        data[key] = parse_scalar(raw_value)

    return data


def read_config() -> dict[str, str]:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Missing required config file: {CONFIG_PATH}")

    raw = parse_simple_yaml(CONFIG_PATH.read_text(encoding="utf-8"))
    url = str(raw.get("url") or "").rstrip("/")
    if not url:
        raise RuntimeError("Missing required url in _config.yml.")

    return {
        "url": url,
        "baseurl": str(raw.get("baseurl") or "").strip("/"),
        "title": str(raw.get("title") or "physicslly"),
        "tagline": str(raw.get("tagline") or ""),
    }


def parse_front_matter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    return parse_simple_yaml(parts[1])


def parse_sort_date(path: Path, metadata: dict[str, object]) -> datetime:
    raw_date = str(metadata.get("date") or "")
    if raw_date:
        normalized = re.sub(r" ([+-]\d{2})(\d{2})$", r"\1:\2", raw_date)
        try:
            return datetime.fromisoformat(normalized)
        except ValueError:
            pass

    match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.name)
    if not match:
        return datetime.min
    return datetime.fromisoformat(match.group(1))


def title_from_slug(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("-"))


def markdown_text(value: object, fallback: str) -> str:
    text = str(value or fallback).strip()
    text = re.sub(r"\s+", " ", text)
    return text.replace("[", "\\[").replace("]", "\\]")


def list_text(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if value:
        return [str(value).strip()]
    return []


def site_url(config: dict[str, str], path: str) -> str:
    base = config["url"]
    baseurl = config["baseurl"]
    if baseurl:
        return f"{base}/{baseurl}{path}"
    return f"{base}{path}"


def load_posts(config: dict[str, str]) -> list[Post]:
    if not POSTS_DIR.exists():
        raise FileNotFoundError("Missing required _posts/ directory.")

    post_paths = sorted(POSTS_DIR.glob("*.md"))
    if not post_paths:
        raise RuntimeError("No Markdown posts found in _posts/.")

    posts: list[Post] = []
    for path in post_paths:
        match = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.md$", path.name)
        if not match:
            continue

        slug = match.group(1)
        metadata = parse_front_matter(path)
        title = markdown_text(metadata.get("title"), title_from_slug(slug))
        description = markdown_text(
            metadata.get("description"),
            "Theoretical physics article.",
        )
        posts.append(
            Post(
                title=title,
                url=site_url(config, f"/posts/{slug}/"),
                description=description,
                categories=list_text(metadata.get("categories")),
                tags=list_text(metadata.get("tags")),
                math=bool(metadata.get("math")),
                sort_date=parse_sort_date(path, metadata),
                source=path,
            )
        )

    if not posts:
        raise RuntimeError("No valid dated Markdown posts found in _posts/.")

    return sorted(posts, key=lambda post: (post.sort_date, post.source.name), reverse=True)


def generate_llms_txt(config: dict[str, str], posts: list[Post]) -> str:
    title = markdown_text(config.get("title"), "physicslly")
    home = site_url(config, "/")
    archives = site_url(config, "/archives/")
    categories = site_url(config, "/categories/")
    tags = site_url(config, "/tags/")
    sitemap = site_url(config, "/sitemap.xml")

    lines = [
        f"# {title}",
        "",
        "> physicslly is a theoretical physics blog focused on quantum field theory, general relativity, quantum gravity, holography, gauge theory, topology, cosmology, black holes, and the search for deeper unifying structures in fundamental physics.",
        "",
        "## Important Pages",
        "",
        f"- [Home]({home}): Main entry point for the site.",
        f"- [Archives]({archives}): Chronological archive of all posts.",
        f"- [Categories]({categories}): Topic-based navigation.",
        f"- [Tags]({tags}): Tag-based navigation.",
        "",
        "## Articles",
        "",
    ]

    for post in posts:
        lines.append(f"- [{post.title}]({post.url}): {post.description}")

    lines.extend(
        [
            "",
            "## Sitemap",
            "",
            f"- [XML Sitemap]({sitemap})",
            "",
        ]
    )

    return "\n".join(lines)


def validate_output(output: str) -> None:
    if not output.strip():
        raise RuntimeError("Generated llms.txt output is empty.")
    if "## Articles" not in output:
        raise RuntimeError("Generated llms.txt does not contain ## Articles.")
    if "sitemap.xml" not in output:
        raise RuntimeError("Generated llms.txt does not contain sitemap.xml.")


def main() -> int:
    try:
        config = read_config()
        posts = load_posts(config)
        output = generate_llms_txt(config, posts)
        validate_output(output)
        OUTPUT_PATH.write_text(output, encoding="utf-8")
        print(f"Generated llms.txt with {len(posts)} posts.")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
