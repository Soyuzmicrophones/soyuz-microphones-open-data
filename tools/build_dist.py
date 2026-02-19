#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Iterable


def iter_metadata_files(root: Path) -> Iterable[Path]:
    return (p for p in root.rglob("metadata.json") if p.is_file() and "models" in p.parts)


def infer_category(meta_path: Path) -> str:
    parts = meta_path.parts
    try:
        i = parts.index("models")
        return parts[i + 1]  # microphones / preamps
    except Exception:
        return "unknown"


def load_json(p: Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def collect_assets(model_dir: Path) -> Dict[str, List[str]]:
    # We keep it intentionally simple & robust:
    # collect common measurement assets if present; otherwise empty lists.
    assets: Dict[str, List[str]] = {
        "frequency_response": [],
        "polar_patterns": [],
        "other": [],
    }

    for p in model_dir.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(model_dir).as_posix()
        ext = p.suffix.lower()

        if ext == ".csv":
            # Heuristic: FR csv often contains 'fr' or 'frequency' or 'response'
            name = p.name.lower()
            if "fr" in name or "frequency" in name or "response" in name:
                assets["frequency_response"].append(rel)
            elif "polar" in name or "pattern" in name:
                assets["polar_patterns"].append(rel)
            else:
                assets["other"].append(rel)

        elif ext in [".png", ".jpg", ".jpeg", ".webp"]:
            name = p.name.lower()
            if "polar" in name or "pattern" in name:
                assets["polar_patterns"].append(rel)
            else:
                assets["other"].append(rel)

        elif ext in [".pdf", ".txt", ".md", ".wav"]:
            assets["other"].append(rel)

    # stable ordering for diffs
    for k in assets:
        assets[k] = sorted(set(assets[k]))
    return assets


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    dist_dir = repo_root / "dist"
    dist_dir.mkdir(parents=True, exist_ok=True)
    out_path = dist_dir / "models_flat.ndjson"

    rows: List[Dict[str, Any]] = []

    for meta_path in sorted(iter_metadata_files(repo_root)):
        category = infer_category(meta_path)
        model_dir = meta_path.parent
        meta = load_json(meta_path)

        # best-effort id/slug/name extraction without enforcing schema
        model_id = meta.get("id") or meta.get("model_id") or meta.get("sku") or model_dir.name
        name = meta.get("name") or meta.get("model_name") or model_dir.name
        slug = meta.get("slug") or meta.get("model_slug") or model_dir.name

        model_path = model_dir.relative_to(repo_root).as_posix()
        metadata_rel = meta_path.relative_to(repo_root).as_posix()

        rows.append({
            "id": model_id,
            "category": category,
            "slug": slug,
            "name": name,
            "brand": meta.get("brand", "SOYUZ"),
            "model_path": model_path,
            "metadata_path": metadata_rel,
            "assets": collect_assets(model_dir),
            "metadata": meta,
        })

    # sort for stability
    rows.sort(key=lambda r: (r.get("category", ""), str(r.get("id", "")), r.get("model_path", "")))

    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False))
            f.write("\n")

    print(f"Wrote {len(rows)} rows to {out_path.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())