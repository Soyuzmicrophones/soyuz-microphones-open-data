#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

@dataclass
class JsonIssue:
    path: str
    message: str

# Minimal required keys by category; keep intentionally light to avoid breaking changes.
REQUIRED_COMMON = ["manufacturer", "model"]
REQUIRED_MIC = ["microphone_type", "transducer_type", "electronics"]
REQUIRED_PREAMP = ["type"]  # optional in your repo; validator treats as advisory

def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def validate_metadata_json(path: Path, category: str) -> List[JsonIssue]:
    issues: List[JsonIssue] = []
    try:
        data = _load_json(path)
    except Exception as e:
        return [JsonIssue(str(path), f"Invalid JSON: {e}")]
    if not isinstance(data, dict):
        return [JsonIssue(str(path), "Root JSON must be an object/dict.")]

    for k in REQUIRED_COMMON:
        if k not in data:
            issues.append(JsonIssue(str(path), f"Missing required key: {k}"))

    if category == "microphones":
        for k in REQUIRED_MIC:
            if k not in data:
                issues.append(JsonIssue(str(path), f"Missing recommended key for microphones: {k}"))
    elif category == "preamps":
        for k in REQUIRED_PREAMP:
            if k not in data:
                issues.append(JsonIssue(str(path), f"Missing recommended key for preamps: {k}"))

    # Basic sanity: if frequency_response exists, it should be object-like
    fr = data.get("frequency_response")
    if fr is not None and not isinstance(fr, dict):
        issues.append(JsonIssue(str(path), "frequency_response must be an object if present."))

    return issues
