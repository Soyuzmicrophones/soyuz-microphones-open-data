#!/usr/bin/env python3
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

@dataclass
class CsvIssue:
    path: str
    message: str

def _parse_float(s: str) -> float:
    # Support RU decimal comma and dot; strip spaces
    s = s.strip().replace("\u00a0", " ")
    s = s.replace(",", ".")
    return float(s)

def validate_frequency_response_csv(path: Path) -> List[CsvIssue]:
    issues: List[CsvIssue] = []
    try:
        text = path.read_text(encoding="utf-8", errors="strict")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="ignore")
        issues.append(CsvIssue(str(path), "Non-UTF8 characters detected; parsed with errors='ignore'."))

    # Expect semicolon-delimited to match repo convention (Excel RU).
    reader = csv.reader(text.splitlines(), delimiter=";")
    rows = list(reader)
    if not rows:
        return [CsvIssue(str(path), "Empty CSV file.")]
    header = [c.strip() for c in rows[0]]
    if header != ["frequency_hz", "response_db"]:
        issues.append(CsvIssue(str(path), f"Unexpected header: {header} (expected ['frequency_hz','response_db'])."))

    freqs: List[float] = []
    for i, r in enumerate(rows[1:], start=2):
        if not r or all(not c.strip() for c in r):
            continue
        if len(r) < 2:
            issues.append(CsvIssue(str(path), f"Line {i}: expected 2 columns, got {len(r)}."))
            continue
        try:
            f = _parse_float(r[0])
            _ = _parse_float(r[1])
        except Exception:
            issues.append(CsvIssue(str(path), f"Line {i}: non-numeric value(s): {r!r}."))
            continue
        freqs.append(f)

    if not freqs:
        issues.append(CsvIssue(str(path), "No numeric rows found."))
        return issues

    # Check monotonic increasing and duplicates
    for a, b in zip(freqs, freqs[1:]):
        if b <= a:
            issues.append(CsvIssue(str(path), f"Frequencies are not strictly increasing near {a} -> {b}."))
            break

    if len(freqs) != len(set(freqs)):
        issues.append(CsvIssue(str(path), "Duplicate frequency values detected."))

    return issues
