# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-04-13
### Fixed
- Scattering length: a = 5.3 → 5.77 nm (Boesten et al. 1997 via Dalfovo et al. 1999)
- Λ formula in docs: √(Rz×Rr) → (Rz×Rr²)^(1/3) to match code
- Condensate fraction formula: (1-T/Tc)^(3/2) → 1-(T/Tc)³ (harmonic trap)
- ω̄ = 53.7 → 59.6 Hz in PARAMETER_JUSTIFICATION.md
- T/Tc = 0.79 → 0.965 (correct for N₀/N = 0.10)
### Changed
- N_condensate source clarified as estimate (~10% of N_total)
- All documentation updated to reflect new values
### Key Result
- κ = 0.806 ± 0.225
- 95% CI: [0.366, 1.247]
- Confirms critical emergence at κ ≈ 1

## [2.0.0] - 2025-11-15

### Added
- Complete academic documentation in English
- Comprehensive peer review validation
- Apache 2.0 license
- GitHub publication preparation files
- Professional README with detailed methodology
- CONTRIBUTING guidelines
- CITATION.cff for academic citations
- .gitignore for repository management

### Changed
- Full rewrite of METHODOLOGY.md with academic rigor
- Enhanced uncertainty analysis with detailed propagation
- Improved physical validation section
- Updated documentation structure for publication
- Removed informal language and emojis
- Standardized all equations and notation

### Verified
- All experimental data verified against Anderson et al. (1995), page 200
- Mathematical calculations independently validated
- Physical consistency checks confirmed
- Thomas-Fermi approximation validity assessed
- Uncertainty budget comprehensively analyzed

### Key Result
- κ = 0.806 ± 0.225 (updated from 0.793)
- 95% CI: [0.366, 1.247]
- Confirms critical emergence at κ ≈ 1

## [1.0.0] - 2025-11-04

### Added
- Initial implementation of emergence parameter calculation
- Basic data processing pipeline
- Visualization module
- Statistical analysis tools
- Documentation framework

### Calculated
- Thermal de Broglie wavelength: λ_dB = 0.454 μm
- Thomas-Fermi radii: Rz = 1.82 μm, Rr = 5.20 μm
- Emergence parameter: κ = 0.806

### Implemented
- Object-oriented code structure
- Type hints and docstrings
- CODATA 2018 physical constants
- Uncertainty propagation
- Publication-quality figures (300/600 DPI)

## [0.1.0] - 2025-10-29

### Added
- Project structure initialization
- Data extraction from Anderson et al. (1995)
- Basic calculation framework
- Figure generation system

### Established
- Theoretical framework based on κ ≈ 1
- Parameter definitions for BEC systems
- Data validation procedures

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):
- MAJOR version: incompatible API changes or major methodology revisions
- MINOR version: backwards-compatible functionality additions
- PATCH version: backwards-compatible bug fixes

## Notes

### Data Sources
All experimental parameters extracted from:
- Anderson M.H., et al. (1995). Science 269:198-201
- Verified against original publication, page 200

### Theoretical Framework
Based on:
- The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems
- Author: Oleksii Onasenko
- Developer: SubstanceNet

### System Classification
- System Code: A.1.1
- System Type: Bose-Einstein Condensate
- Species: ⁸⁷Rb (Rubidium-87)
- Experiment: JILA (1995)

---

**Maintained by:** Oleksii Onasenko  
**Repository:** SubstanceNet  
**Last Updated:** November 15, 2025
