#!/usr/bin/env python3
"""Remove parenthesized Source references from raw Markdown files."""

import argparse
from pathlib import Path
import re


SOURCE_START = re.compile(r"\(Source\s*:", re.IGNORECASE)


def preprocess(text: str, start_pattern: re.Pattern = SOURCE_START) -> tuple[str, int]:
    """Remove Source citations (or other labels matching start_pattern), including nested parentheses and emphasis."""
    count = 0
    position = 0
    while match := start_pattern.search(text, position):
        start = match.start()
        end = match.end()
        depth = 1
        while end < len(text) and depth:
            if text[end] == "(":
                depth += 1
            elif text[end] == ")":
                depth -= 1
            end += 1
        if depth:
            position = match.end()
            continue
        for wrapper in ("**", "__", "*", "_"):
            if text[:start].endswith(wrapper) and text[end:].startswith(wrapper):
                start -= len(wrapper)
                end += len(wrapper)
                break
        # Consume preceding spaces without joining separate lines.
        while start > 0 and text[start - 1] in " \t":
            start -= 1
        text = text[:start] + text[end:]
        position = start
        count += 1
    return text, count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, default=Path("smoke_run_data/raw"))
    parser.add_argument("--output", type=Path, default=Path("smoke_run_data/processed"))
    args = parser.parse_args()
    source = args.input.resolve()
    output = args.output.resolve()
    if not source.is_dir():
        parser.error(f"Input directory does not exist: {source}")
    if output == source or source in output.parents:
        parser.error("Output must be outside the input directory.")
    files = sorted(source.rglob("*.md"))
    if not files:
        parser.error(f"No Markdown files found in {source}")
    total = 0
    for path in files:
        cleaned, count = preprocess(path.read_text(encoding="utf-8"))
        destination = output / path.relative_to(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(cleaned, encoding="utf-8")
        total += count
    print(f"Processed {len(files)} Markdown files; removed {total} references. Output: {output}")


if __name__ == "__main__":
    main()
