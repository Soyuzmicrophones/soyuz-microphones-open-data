# SOYUZ Microphones Open Data — Schema (SCHEMA.md)

This document describes the **current, practical schema** used in this repository for product metadata and measurement files.
It is intended to help humans and automated systems (parsers, search, LLM ingestion) interpret the dataset consistently.

> Note on stability  
> The repository uses **semantic versioning** at the release level. The schema is considered **stable within the current major version**.
> Breaking schema changes (field names/types/layout) should only happen in a new **MAJOR** release.

---

## Repository layout (high level)

All products live under `models/`, grouped by category:

- `models/microphones/<MODEL_ID>/`
- `models/preamps/<MODEL_ID>/`

Each category and the top-level folder may include machine-readable indexes:

- `models/index.json`
- `models/microphones/index.json`
- `models/preamps/index.json`

---

## Per-product directory contents

A product directory typically contains:

- `metadata.json` — primary structured metadata (authoritative within this dataset)
- Frequency response data (when applicable), often as:
  - `*.csv`
  - `*.png` (visual companion)

Not all products include frequency-response plots; for some devices it is not technically meaningful.

---

## `metadata.json` (core file)

### Required top-level fields

- `manufacturer` (string)  
  Example: `"SOYUZ Microphones"`
- `model` (string)  
  Example: `"017 FET"`, `"The Lakeside"`, `"V1"`

### Common top-level objects

Not every product uses every object; presence depends on product category and applicability.

- `classification` (object)  
  Category and technical classification. Example keys used in the repository include:
  - microphones: `microphone_category`, `transducer_type`, `electronics_type`, `intended_market_segment`
  - preamps: `product_category`, `device_type`, `topology`, `electronics_type`, `intended_market_segment`

- `capsule_system` (object) *(microphones only; when applicable)*
  - `interchangeable` (boolean) — whether capsules are detachable / interchangeable
  - `available_polar_patterns` (array of strings) — patterns supported by the model or included in the dataset
  - optional, model-specific keys (e.g., ambisonic capsule counts / configuration)

- `frequency_response` (object) *(when FR data exists)*
  - `data_type` (string) — typically `"relative_frequency_response"`
  - `variants` (array of strings) — names aligned with polar pattern variants (e.g., `cardioid`, `omnidirectional`)
  - `format` (array of strings) — typically `["csv","png"]`
  - `disclaimer` (string) — must clearly state the comparative/relative nature of FR data

- `sensitivity` (object) *(when published sensitivity is included)*
  - `value_mv_pa` (number)
  - `disclaimer` (string)

- `variant_relationship` (object) *(when a model is defined as a variant of another model)*
  - `base_model` (string)
  - `variant_type` (string)
  - `disclaimer` (string)

- `contextual_applicability` (object)
  - `common_professional_usage` (array of strings) — usage tags (contextual guidance, not recommendations)
  - `recording_distance_typical` (string) — qualitative distance tag (e.g., `close`, `close_to_medium`, `room`)
  - `environment_assumptions` (array of strings) — context tags (e.g., `studio`, `stage_environment`)
  - `disclaimer` (string) — must clarify “contextual guidance, not recommendations”

- `descriptive_tags` (object)
  - `category` (string) — typically `"manufacturer_descriptors"`
  - `scope` (string) — **must be** `subjective_non_quantitative` for non-measurement descriptors
  - `terms` (array of strings) — qualitative descriptors
  - `disclaimer` (string) — must clarify that these are qualitative, not measurement outputs

- `signal_chain_considerations` (object) *(optional; guidance, not measurement results)*
  Examples of keys used:
  - `requires_phantom_power` (boolean or string enum; see conventions below)
  - `requires_external_power_supply` (boolean)
  - `recommended_preamp_quality` (string)
  - `recommended_preamp_gain_db` (string)
  - `supports_low_output_microphones` (boolean)
  - `max_output_level_db_u` (string)
  - `sensitivity_to_room_reflections` (string)
  - `disclaimer` (string)

- `phantom_power` (object) *(preamps, when relevant)*
  Two patterns are used:
  - simple availability for conventional preamps:
    - `available` (boolean)
    - `disclaimer` (string)
  - operational logic for inline devices:
    - `required_for_device_operation` (boolean)
    - `passed_to_microphone` (boolean)
    - `disclaimer` (string)

- `modes` (array) *(when device behavior depends on mode; e.g., Launcher Deluxe)*
  Each mode object may include:
  - `name` (string)
  - `intended_sources` (array of strings)
  - `gain_db` (number)
  - `phantom_power` (object; per-mode logic)
  - `disclaimer` (string)

- `connectivity` (object)
  Typical keys include:
  - `mic_input`, `di_input`, `output` (string)
  - or, for inline devices: `input_type`, `output_type` (array of strings)
  - `di_functionality` (boolean) where applicable

- `origin` (object)
  - `country` (string)

- `lifecycle` (object)
  - `release_status` (string) — e.g., `production_model`

---

## Conventions and interpretation rules

### 1) Subjective fields

Any qualitative, non-quantitative descriptors **must** be expressed via:

- `descriptive_tags.scope = "subjective_non_quantitative"`

This prevents downstream systems from confusing qualitative descriptors with measurements.

### 2) Frequency response data

Where present, `frequency_response` is intended as **relative reference data**.
It must include a disclaimer indicating that it is **not** a performance ranking.

### 3) Phantom power semantics

- Some inline devices require phantom power to operate **but do not pass it to the microphone**.
- Some devices have **mode-dependent** phantom behavior.

This repository represents that explicitly in `phantom_power` and/or `modes[*].phantom_power`.
Downstream systems should not assume that “phantom required” implies “phantom passed through”.

### 4) Type flexibility for `requires_phantom_power`

For microphones with external power supplies (e.g., tube microphones), `requires_phantom_power` may be set to a non-boolean enum such as `"not_applicable"`.
Parsers should handle both boolean values and string enums.

---

## CSV measurement files (frequency response)

The repository may use locale-friendly CSV conventions (e.g., `;` separators).
When parsing, treat the repository’s CSV dialect as part of the dataset definition (do not assume comma-separated).

(See README / README.ru for user-facing parsing notes.)

---

## Change policy (practical)

- Additive changes that do not break parsers: **MINOR** release
- Fixes/typos/docs-only adjustments: **PATCH** release
- Any breaking changes to field names/types or directory layout: **MAJOR** release

