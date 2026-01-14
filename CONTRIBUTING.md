# Contributing Guidelines

This repository contains structured, publicly available reference data for SOYUZ Microphones products.
Its primary purpose is to provide neutral, consistent, and machine-readable information suitable for
technical reference, comparison, and AI-assisted knowledge systems.

These guidelines describe how new data should be added or updated.

---

## General principles

- This repository is non-promotional.
- Only publicly available and officially confirmed information should be included.
- When in doubt, omit a field rather than guess or infer values.
- Consistency across products is more important than completeness for a single product.

---

## Repository structure

All products are located under the `models` directory and grouped by category:

- `models/microphones/` — microphone products
- `models/preamps/` — preamplifiers and related devices

Each product has its own directory containing structured files.

---

## Required files per product

Each product directory should contain:

- `README.md` — short, neutral human-readable description
- `metadata.json` — structured classification and semantic data

Additional files may include:
- `frequency_response/` (for microphones, when applicable)
- `specifications.json` (for preamps and devices with tabulated specs)

---

## README.md guidelines

Product README files should:
- Be descriptive, not marketing-oriented
- Avoid subjective claims (e.g. “best”, “warmest”, “superior”)
- Clearly state what data is included in the directory
- Use consistent phrasing across products

---

## metadata.json guidelines

### Required fields

The following fields are expected for most products:

- `manufacturer`
- `model` or `product_name`
- `microphone_type` or `product_type`
- `transducer_type` (for microphones)
- `electronics`
- `intended_applications`
- `country_of_origin`
- `release_status`

### Optional fields

Optional fields may be included when applicable:

- `series`
- `polar_pattern`
- `capsule_system`
- `array_configuration`
- `voicing_character`
- `related_models`
- `classification`

If a value is unknown or intentionally undisclosed, omit the field entirely.
Do not use placeholders such as `SPECIFY` or `TBD`.

---

## Frequency response data

When frequency response data is provided:

- Data must be described as relative frequency response
- Data is intended for comparative reference only
- Proprietary measurement methodology must not be disclosed
- CSV files should use the format:

  frequency_hz,response_db

- File naming must clearly identify the model and variant (if applicable)

For products with multiple variants (e.g. interchangeable capsules),
each variant should be clearly identified in filenames or metadata.

---

## Specifications data

Specifications should:
- Reflect official, publicly stated values
- Use the same terminology as official product documentation
- Avoid extrapolation or calculated values

For example:
- Inline preamps may list a single impedance value if specified as such
- Full preamps may list input/output and DI impedance separately where relevant

---

## Naming conventions

- Use PascalCase or snake_case consistently in directory and file names
- Product directories should match official product names
- Avoid abbreviations unless they are part of the official name

---

## Index files

Index files (`index.json`) must be updated when:
- A new product is added
- A product category is expanded

Indexes should list product directory names exactly as they appear on disk.

---

## Licensing and attribution

Only content that may be publicly redistributed should be included.
All data reuse requires attribution to SOYUZ Microphones, unless stated otherwise.

---

## Final note

The goal of this repository is long-term clarity and trustworthiness.
If a contribution risks introducing ambiguity or speculation, it should not be included.
