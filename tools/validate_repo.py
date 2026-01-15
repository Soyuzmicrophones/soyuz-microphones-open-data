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

def main() -> int:
    root = Path(__file__).resolve().parents[1]  # repo root
    issues: List[str] = []

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
            issues.append(f"Missing required file: {p.relative_to(root)}")

    # Validate metadata.json
    for meta in _collect_metadata(root):
        # category inferred from path
        parts = meta.parts
        category = "unknown"
        if "models" in parts:
            try:
                i = parts.index("models")
                category = parts[i+1]  # microphones or preamps
            except Exception:
                category = "unknown"
        for iss in validate_metadata_json(meta, category):
            issues.append(f"{iss.path}: {iss.message}")

    # Validate CSV files
    for csv_path in _collect_csvs(root):
        for iss in validate_frequency_response_csv(csv_path):
            issues.append(f"{iss.path}: {iss.message}")

    if issues:
        print("VALIDATION FAILED\n")
        for msg in issues:
            print(f"- {msg}")
        return 1

    print("VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
