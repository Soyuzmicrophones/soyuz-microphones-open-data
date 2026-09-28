#!/usr/bin/env python3
from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class CsvIssue:
    path: str
    message: str


def _parse_float(s: str) -> float:
    # Support RU decimal comma and dot; strip spaces.
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

    reader = csv.reader(text.splitlines(), delimiter=";")
    rows = list(reader)
    if not rows:
        return [CsvIssue(str(path), "Empty CSV file.")]

    header = [c.strip() for c in rows[0]]
    if header != ["frequency_hz", "response_db"]:
        issues.append(CsvIssue(str(path), f"Unexpected header: {header} (expected ['frequency_hz','response_db'])."))

    freqs: List[float] = []
    for i, row in enumerate(rows[1:], start=2):
        if not row or all(not cell.strip() for cell in row):
            continue
        if len(row) != 2:
            issues.append(CsvIssue(str(path), f"Line {i}: expected 2 columns, got {len(row)}."))
            continue
        try:
            frequency = _parse_float(row[0])
            response = _parse_float(row[1])
        except Exception:
            issues.append(CsvIssue(str(path), f"Line {i}: non-numeric value(s): {row!r}."))
            continue
        if not math.isfinite(frequency) or not math.isfinite(response):
            issues.append(CsvIssue(str(path), f"Line {i}: values must be finite: {row!r}."))
            continue
        if frequency <= 0:
            issues.append(CsvIssue(str(path), f"Line {i}: frequency must be greater than zero."))
            continue
        freqs.append(frequency)

    if not freqs:
        issues.append(CsvIssue(str(path), "No valid numeric rows found."))
        return issues

    for previous, current in zip(freqs, freqs[1:]):
        if current <= previous:
            issues.append(CsvIssue(str(path), f"Frequencies are not strictly increasing near {previous} -> {current}."))
            break

    if len(freqs) != len(set(freqs)):
        issues.append(CsvIssue(str(path), "Duplicate frequency values detected."))

    return issues
