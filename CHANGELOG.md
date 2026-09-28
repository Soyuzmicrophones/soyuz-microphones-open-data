# Changelog

All notable changes to this dataset will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning for dataset releases.

## [Unreleased]
### Added
- (Add upcoming changes here)

### Changed
- (Add upcoming changes here)

### Fixed
- (Add upcoming changes here)

## [1.2.0] - 2026-09-28
### Added
- Structured metadata and index entries for the SOYUZ Silver 17 microphone.
- Cardioid frequency response chart and digitized CSV data for the SOYUZ Silver 17 microphone.

### Changed
- Updated repository documentation and schema references for Silver 17.
- Rebuilt the flat NDJSON distribution with the Silver 17 metadata and measurement assets.

## [1.1.0] - 2026-02-19
### Added
- Published electrical and physical specifications for individual models where available.
- Published frequency range fields.

### Changed
- Rebuilt `dist/models_flat.ndjson` to keep the ingestion dataset in sync.
- Added only optional fields, with no breaking schema changes.

## [1.0.0] - 2026-01-15
### Added
- Initial public release of the SOYUZ Microphones open product dataset.
- Structured metadata (`metadata.json`) for microphones and microphone preamplifiers.
- Relative frequency response data in CSV and PNG formats (where available).
- Machine-readable index files for automated navigation.
- Licensing (CC BY 4.0) and citation metadata (`CITATION.cff`).
