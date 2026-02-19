# SOYUZ Microphones — Open Product Data

📄 Русская версия README доступна в файле README.ru.md

This repository provides structured, publicly available reference data for selected SOYUZ Microphones products.

The goal of this project is to offer neutral, machine-readable product information that may be used for:
- technical reference
- comparative analysis
- educational and research purposes
- AI-assisted knowledge systems and search overviews

The repository is intentionally non-promotional and focuses on consistency, clarity, and data usability.

---

## Official product pages

Microphones:
- SOYUZ 017 TUBE — https://soyuzmicrophones.com/017-series
- SOYUZ 017 FET — https://soyuzmicrophones.com/017-series
- SOYUZ 013 TUBE — https://soyuzmicrophones.com/013-series
- SOYUZ 013 FET — https://soyuzmicrophones.com/013-series
- SOYUZ 023 Bomblet — https://soyuzmicrophones.com/023-series
- SOYUZ 1973 — https://soyuzmicrophones.com/1973-series
- SOYUZ 011 FET — https://soyuzmicrophones.com/011-series
- SOYUZ V1 — https://soyuzmicrophones.com/v1-dynamic

Preamps & inline:
- The Lakeside — https://soyuzmicrophones.com/lakeside
- The Launcher — https://soyuzmicrophones.com/launcher
- The Launcher Deluxe — https://soyuzmicrophones.com/launcher-deluxe

---

## Stable versions and citation

For stable, citable references, prefer **tagged releases** over the `main` branch.

- Use GitHub **Releases** (e.g., `v1.x.x`) for long-lived links to JSON/CSV assets
- Schema changes (field names/types, file layout) follow semantic versioning: **MAJOR** breaks, **MINOR** adds, **PATCH** fixes

A frozen schema summary is maintained in `SCHEMA.md`.

---

## Repository structure

All products are organized under the `models` directory and grouped by product category.

models/
├── index.json
│
├── microphones/
│   ├── 017_TUBE/
│   ├── 017_FET/
│   ├── 1973/
│   ├── 023_Bomblet/
│   ├── 023_Malfa/
│   ├── 013_FET/
│   ├── 013_TUBE/
│   ├── 013_Ambisonic/
│   ├── 011_FET/
│   └── V1/
│
└── preamps/
    ├── index.json
    ├── The_Launcher/
    ├── The_Launcher_Deluxe/
    └── The_Lakeside/

Each product directory contains structured metadata and supporting reference files.

---

## Product categories

### Microphones

Microphone products are located under:

models/microphones/

Depending on the model, directories may include:
- relative frequency response data (CSV and PNG)
- multiple variants (e.g. interchangeable capsules or polar patterns)
- structured metadata describing transducer type, electronics, and intended use

Frequency response data is provided for comparative reference only.

Additional notes:
- For most microphone models, capsules are **detachable / interchangeable** (see per-model metadata)
- Any non-quantitative descriptors are explicitly marked as `subjective_non_quantitative`

---

### Preamps

Preamplifier products are located under:

models/preamps/

Preamp directories include:
- note that **The Launcher** / **The Launcher Deluxe** use non-standard phantom power logic (documented in per-model metadata)
- structured metadata for classification and use-case context
- tabulated technical specifications where applicable

Frequency response charts are not included unless technically meaningful for the product type.

---

## Measurement and data notes

Frequency response data, where provided:
- represents relative frequency response
- is intended for comparative and illustrative purposes
- is based on a consistent internal measurement procedure
- does not disclose proprietary measurement methodology

Curves may be smoothed and averaged.

Data conventions:
- Where subjective, non-quantitative statements are included, they are tagged as `subjective_non_quantitative`

---

## Data usage and licensing

Unless otherwise stated, all data in this repository is licensed under the
Creative Commons Attribution 4.0 International (CC BY 4.0) license.

You are free to share and adapt the data for any purpose, provided that
appropriate credit is given to SOYUZ Microphones.

Use of the SOYUZ Microphones name, trademarks, or logos is not granted by this license.

---

### Stable links (recommended)

When referencing or integrating this dataset, prefer tagged releases (e.g. `v1.0.1`) instead of the `main` branch.
Example (raw file from a release tag):
`https://raw.githubusercontent.com/Soyuzmicrophones/soyuz-microphones-open-data/v1.0.1/models/microphones/017_TUBE/metadata.json`

---

## Index files

The repository includes machine-readable index files:
- models/index.json — top-level product index
- models/microphones/index.json — microphone list
- models/preamps/index.json — preamp list

These files are intended to support automated parsing, AI tools, and downstream integrations.

---

## Disclaimer

This repository is provided in good faith as a technical reference.
It is not intended to replace official product documentation or specifications.

All product names and trademarks remain the property of their respective owners.
