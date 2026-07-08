#!/usr/bin/env python3
"""Export the first Markdown table in leads.md to CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(set(cell.replace(":", "").strip()) <= {"-"} for cell in cells)


def parse_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def extract_first_table(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    in_table = False
    for line in markdown.splitlines():
        row = parse_row(line)
        if row:
            in_table = True
            if not is_separator(row):
                rows.append(row)
            continue
        if in_table:
            break
    if len(rows) < 2:
        raise ValueError("No Markdown table with header and rows found")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="leads.md path")
    parser.add_argument("output", type=Path, help="leads.csv path")
    args = parser.parse_args()

    rows = extract_first_table(args.input.read_text(encoding="utf-8"))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)
    print(f"CSV exported: {args.output} ({len(rows) - 1} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
