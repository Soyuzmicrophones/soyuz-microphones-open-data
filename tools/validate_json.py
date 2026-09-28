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


REQUIRED_COMMON = ["manufacturer", "model"]
REQUIRED_MIC_CLASSIFICATION = [
    "microphone_category",
    "transducer_type",
    "electronics_type",
]


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

    for key in REQUIRED_COMMON:
        if key not in data:
            issues.append(JsonIssue(str(path), f"Missing required key: {key}"))

    classification = data.get("classification")
    if not isinstance(classification, dict):
        issues.append(JsonIssue(str(path), "classification must be an object."))
    elif category == "microphones":
        for key in REQUIRED_MIC_CLASSIFICATION:
            if key not in classification:
                issues.append(
                    JsonIssue(
                        str(path),
                        f"Missing required microphone classification key: {key}",
                    )
                )

    fr = data.get("frequency_response")
    if fr is not None:
        if not isinstance(fr, dict):
            issues.append(JsonIssue(str(path), "frequency_response must be an object if present."))
        else:
            formats = fr.get("format", [])
            if not isinstance(formats, list) or not all(isinstance(v, str) for v in formats):
                issues.append(JsonIssue(str(path), "frequency_response.format must be an array of strings."))
            elif fr.get("measurement_data_included", True):
                for extension in formats:
                    if extension not in {"csv", "png"}:
                        continue
                    if not any(path.parent.rglob(f"*.{extension}")):
                        issues.append(
                            JsonIssue(
                                str(path),
                                f"frequency_response declares {extension!r}, but no .{extension} file exists.",
                            )
                        )

    return issues
