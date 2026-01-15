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

---

### Preamps

Preamplifier products are located under:

models/preamps/

Preamp directories include:
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

---

## Data usage and licensing

Unless otherwise stated, all data in this repository is licensed under the
Creative Commons Attribution 4.0 International (CC BY 4.0) license.

You are free to share and adapt the data for any purpose, provided that
appropriate credit is given to SOYUZ Microphones.

Use of the SOYUZ Microphones name, trademarks, or logos is not granted by this license.

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
