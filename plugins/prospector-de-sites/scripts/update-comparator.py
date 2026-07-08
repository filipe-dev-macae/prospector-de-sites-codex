#!/usr/bin/env python3
"""Merge client entries into comparar.html from the bundled template."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


CLIENTES_RE = re.compile(r"var\s+CLIENTES\s*=\s*(\[.*?\])\s*;\s*var\s+tabs", re.DOTALL)


def load_existing(output_path: Path) -> list[dict[str, Any]]:
    if not output_path.exists():
        return []
    text = output_path.read_text(encoding="utf-8")
    match = CLIENTES_RE.search(text)
    if not match:
        return []
    return json.loads(match.group(1))


def normalize_client(raw: str) -> dict[str, Any]:
    client = json.loads(raw)
    if not isinstance(client, dict):
        raise ValueError("--client must be a JSON object")
    for key in ("nome", "slug"):
        if not client.get(key):
            raise ValueError(f"--client missing required key: {key}")
    client.setdefault("old", None)
    return client


def merge_clients(existing: list[dict[str, Any]], new_clients: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    seen: set[str] = set()
    for client in new_clients + existing:
        slug = str(client.get("slug", "")).strip()
        if not slug or slug in seen:
            continue
        seen.add(slug)
        merged.append(client)
    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, required=True, help="comparador-template.html")
    parser.add_argument("--output", type=Path, required=True, help="comparar.html output path")
    parser.add_argument(
        "--client",
        action="append",
        default=[],
        help='Client JSON, e.g. {"nome":"Cliente","slug":"cliente","old":"https://..."}',
    )
    args = parser.parse_args()

    template = args.template.read_text(encoding="utf-8")
    if "__CLIENTES__" not in template:
        raise ValueError("Template must contain __CLIENTES__")

    new_clients = [normalize_client(raw) for raw in args.client]
    clients = merge_clients(load_existing(args.output), new_clients)
    clients_json = json.dumps(clients, ensure_ascii=False, indent=2)
    output = template.replace("__CLIENTES__", clients_json)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8", newline="\n")
    print(f"Comparator updated: {args.output} ({len(clients)} clients)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
