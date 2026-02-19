#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from typing import List

from validate_csv import validate_frequency_response_csv, CsvIssue
from validate_json import validate_metadata_json, JsonIssue


def _collect_csvs(root: Path) -> List[Path]:
    return [p for p in root.rglob("*.csv") if p.is_file()]


def _collect_metadata(root: Path) -> List[Path]:
    return [p for p in root.rglob("metadata.json") if p.is_file()]


def _is_warning_message(msg: str) -> bool:
    # Treat "recommended" issues as non-fatal warnings
    return msg.startswith("Missing recommended key")


def main() -> int:
    root = Path(__file__).resolve().parents[1]  # repo root
    errors: List[str] = []
    warnings: List[str] = []

    # Index files presence
    required_paths = [
        root / "models" / "index.json",
        root / "models" / "microphones" / "index.json",
        root / "models" / "preamps" / "index.json",
        root / "CITATION.cff",
        root / "LICENSE",
        root / "README.md",
    ]
    for p in required_paths:
        if not p.exists():
            errors.append(f"Missing required file: {p.relative_to(root)}")

    # Validate metadata.json
    for meta in _collect_metadata(root):
        # category inferred from path
        parts = meta.parts
        category = "unknown"
        if "models" in parts:
            try:
                i = parts.index("models")
                category = parts[i + 1]  # microphones or preamps
            except Exception:
                category = "unknown"

        for iss in validate_metadata_json(meta, category):
            if _is_warning_message(iss.message):
                warnings.append(f"{iss.path}: {iss.message}")
            else:
                errors.append(f"{iss.path}: {iss.message}")

    # Validate CSV files (treat as errors by default)
    for csv_path in _collect_csvs(root):
        for iss in validate_frequency_response_csv(csv_path):
            errors.append(f"{iss.path}: {iss.message}")

    if warnings:
        print("WARNINGS\n")
        for msg in warnings:
            print(f"- {msg}")
        print()

    if errors:
        print("VALIDATION FAILED\n")
        for msg in errors:
            print(f"- {msg}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())