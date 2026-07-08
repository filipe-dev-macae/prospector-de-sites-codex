#!/usr/bin/env python3
"""Inject the Prospector visual editor block into a standalone HTML file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EDITOR_BLOCK_RE = re.compile(
    r"\n?<!-- PROSPECTOR-EDITOR-START -->.*?<!-- PROSPECTOR-EDITOR-END -->\n?",
    re.DOTALL,
)


def load_editor_block(reference_path: Path) -> str:
    text = reference_path.read_text(encoding="utf-8")
    marker = re.search(
        r"<!-- PROSPECTOR-EDITOR-START -->.*?<!-- PROSPECTOR-EDITOR-END -->",
        text,
        re.DOTALL,
    )
    if marker:
        return marker.group(0).strip()

    fenced = re.search(r"```html\s*(.*?)\s*```", text, re.DOTALL)
    if fenced:
        return fenced.group(1).strip()

    raise ValueError(f"Editor block not found in {reference_path}")


def inject_editor(source_html: str, editor_block: str) -> str:
    clean_html = EDITOR_BLOCK_RE.sub("\n", source_html).rstrip()
    body_match = re.search(r"</body\s*>", clean_html, re.IGNORECASE)
    if not body_match:
        raise ValueError("HTML must contain a closing </body> tag")

    insert_at = body_match.start()
    return clean_html[:insert_at].rstrip() + "\n" + editor_block + "\n" + clean_html[insert_at:]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Final client HTML file")
    parser.add_argument("output", type=Path, help="Editor HTML output file")
    parser.add_argument(
        "--editor-reference",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "skills"
        / "redesign-premium"
        / "references"
        / "editor-visual.md",
        help="Path to editor-visual.md",
    )
    args = parser.parse_args()

    source_html = args.source.read_text(encoding="utf-8")
    editor_block = load_editor_block(args.editor_reference)
    output_html = inject_editor(source_html, editor_block)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output_html, encoding="utf-8", newline="\n")
    print(f"Editor generated: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
