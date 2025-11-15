# Security Policy

## Overview

This repository contains scientific computational code for analyzing emergence parameters in ⁸⁷Rb Bose-Einstein condensate. While this is primarily a research project, we take security seriously to ensure data integrity and reproducibility.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |
| < 1.0   | :x:                |

## Scope

This security policy covers:

- Code vulnerabilities that could affect data integrity
- Dependency vulnerabilities in Python packages
- Documentation accuracy and correctness
- Computational reproducibility issues

This policy does NOT cover:

- General scientific disagreements (use GitHub Issues)
- Feature requests (use GitHub Discussions)
- Performance optimization suggestions (use Pull Requests)

## Data Integrity

### Primary Data Sources

All experimental data is sourced from published, peer-reviewed literature:
- Anderson M.H., et al. (1995). Science 269:198-201

Any modifications to source data parameters must:
1. Be clearly documented
2. Include justification
3. Update all dependent calculations
4. Maintain traceability to original publication

### Computational Integrity

The code must:
- Use validated physical constants (CODATA 2018)
- Implement standard formulas from peer-reviewed literature
- Propagate uncertainties correctly
- Maintain numerical stability
- Be reproducible across platforms

## Reporting a Vulnerability

### What to Report

Report issues related to:

**Critical (respond within 24 hours):**
- Data corruption or loss
- Incorrect physical constants
- Mathematical errors in core calculations
- Incorrect uncertainty propagation
- Non-reproducible results

**High (respond within 1 week):**
- Dependency vulnerabilities (critical severity)
- Code that produces incorrect physics
- Documentation errors affecting interpretation
- Missing citations or attribution

**Medium (respond within 2 weeks):**
- Dependency vulnerabilities (moderate severity)
- Code style or maintainability issues
- Documentation improvements
- Performance issues

**Low (respond as time permits):**
- Minor typos
- Cosmetic improvements
- Feature suggestions

### How to Report

**For security-sensitive issues:**
1. Do NOT open a public GitHub issue
2. Email directly to: [maintainer email]
3. Include:
   - Description of the issue
   - Steps to reproduce
   - Expected vs actual behavior
   - Potential impact on results
   - Suggested fix (if available)

**For non-sensitive issues:**
1. Open a GitHub issue
2. Use appropriate labels
3. Provide detailed description
4. Include code snippets if applicable

### What to Expect

After reporting:

1. **Acknowledgment** (within 48 hours)
   - Confirmation that report was received
   - Initial assessment of severity

2. **Investigation** (timeline depends on severity)
   - Review of reported issue
   - Verification and testing
   - Impact assessment

3. **Resolution** (timeline depends on severity)
   - Fix development
   - Testing and validation
   - Documentation update
   - Release of patched version

4. **Disclosure** (after fix is deployed)
   - Public acknowledgment
   - Credit to reporter (if desired)
   - Update to CHANGELOG.md
   - Security advisory if applicable

## Vulnerability Handling

### Critical Issues

Issues affecting data integrity or computational correctness:

1. Immediate investigation begins
2. Public repository may be temporarily restricted
3. All dependent results reviewed
4. Fix tested thoroughly before release
5. Full disclosure with corrected results
6. Update to all documentation

### Dependency Vulnerabilities

For Python package vulnerabilities:

1. Review vulnerability details
2. Assess impact on our code
3. Update to patched version
4. Test all functionality
5. Update requirements.txt
6. Release new version

### False Positives

If a reported issue is not a vulnerability:

1. Explain why it's not an issue
2. Provide documentation or references
3. Close report with clear explanation
4. Thank reporter for their diligence

## Security Best Practices

### For Users

- Use virtual environments
- Install from official PyPI packages
- Verify checksums when available
- Keep dependencies updated
- Review code before running

### For Contributors

- Never commit sensitive data
- Use standard libraries when possible
- Validate all inputs
- Document assumptions
- Write tests for critical functions
- Follow secure coding practices

### For Maintainers

- Review all pull requests carefully
- Test thoroughly before merging
- Keep dependencies updated
- Monitor security advisories
- Maintain version control discipline
- Document all changes

## Computational Validation

### Self-Consistency Checks

All releases must pass:
- Mathematical verification tests
- Physical validity checks
- Reproducibility tests
- Uncertainty propagation validation

### Independent Verification

Calculations verified against:
- Published literature
- Independent implementations
- Standard reference values
- Peer review

## Disclosure Policy

### Public Disclosure

After a security fix is released:
- Update CHANGELOG.md
- Create GitHub security advisory (if applicable)
- Credit reporter (unless anonymity requested)
- Document impact on previous results

### Retroactive Corrections

If a vulnerability affected previous results:
- Full disclosure of impact
- Corrected calculations provided
- Updated documentation
- Clear communication to users

## Contact

**Security Contact:** Oleksii Onasenko  
**Organization:** SubstanceNet  
**Project:** System A.1 - ⁸⁷Rb BEC Emergence Analysis

**Reporting Methods:**
- Private: [Email for sensitive issues]
- Public: GitHub Issues (non-sensitive)
- Discussion: GitHub Discussions (general questions)

## Acknowledgments

We thank all researchers who help maintain the integrity and security of this scientific code.

---

**Version:** 1.0  
**Last Updated:** November 15, 2025  
**Review Cycle:** Annually or after critical issues
