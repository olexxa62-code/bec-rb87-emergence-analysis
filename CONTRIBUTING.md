# Contributing to BEC Emergence Parameter Analysis

Thank you for your interest in contributing to this project. This document provides guidelines for contributing to the ⁸⁷Rb Bose-Einstein Condensate emergence parameter analysis.

## Project Scope

This repository contains a rigorous computational analysis of the emergence parameter κ for ⁸⁷Rb BEC based on experimental data from Anderson et al. (1995). The project is part of a larger theoretical framework studying criticality in physical and biological systems.

## Types of Contributions

### 1. Bug Reports

If you find a bug in the code or documentation:

- Check if the issue already exists in the issue tracker
- Provide a clear description of the problem
- Include steps to reproduce the issue
- Specify your environment (Python version, OS, dependencies)
- Include relevant error messages or output

### 2. Code Improvements

We welcome contributions that:

- Improve computational efficiency
- Enhance numerical stability
- Add validation tests
- Improve code documentation
- Fix bugs or errors

### 3. Documentation

Documentation improvements are valuable:

- Clarify existing explanations
- Add examples or use cases
- Correct typos or formatting
- Improve mathematical notation
- Add references to relevant literature

### 4. Extension to Other Systems

This project analyzes System A.1 (⁸⁷Rb BEC). If you wish to extend the framework to other BEC systems or quantum phase transitions, please:

- Create a separate analysis following the same methodology
- Maintain independence between system analyses
- Use the same theoretical framework (κ ≈ 1)
- Ensure rigorous data validation

## Contribution Process

### 1. Fork and Clone
```bash
git clone https://github.com/[username]/A.1_bec_rb87_kappa_analysis.git
cd A.1_bec_rb87_kappa_analysis
```

### 2. Create Branch
```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `fix/bug-description` for bug fixes
- `feature/feature-name` for new features
- `docs/description` for documentation

### 3. Make Changes

- Follow existing code style (PEP 8 for Python)
- Add docstrings to new functions
- Include type hints
- Update documentation as needed
- Add tests if applicable

### 4. Test Your Changes
```bash
# Run the analysis
cd code/
python3 run_full_analysis.py

# Verify outputs
ls -la ../figures/
cat ../docs/statistical_report.txt
```

### 5. Commit
```bash
git add .
git commit -m "Brief description of changes"
```

Commit message format:
- Use imperative mood ("Add feature" not "Added feature")
- First line: brief summary (50 chars or less)
- Blank line
- Detailed description if needed

### 6. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Code Standards

### Python Style

- Follow PEP 8
- Use meaningful variable names
- Add type hints
- Maximum line length: 88 characters (Black formatter)
- Use docstrings (Google style)

Example:
```python
def calculate_parameter(value: float, uncertainty: float) -> Tuple[float, float]:
    """Calculate parameter with uncertainty propagation.
    
    Args:
        value: Measured value
        uncertainty: Measurement uncertainty
        
    Returns:
        Tuple of (result, result_uncertainty)
    """
    result = complex_calculation(value)
    result_uncertainty = propagate_uncertainty(uncertainty)
    return result, result_uncertainty
```

### Documentation Style

- Use clear, concise language
- Include equations in LaTeX format
- Provide physical interpretation
- Cite sources properly
- Avoid informal language

### Physical Constants

Use CODATA 2018 values:
```python
from scipy.constants import h, hbar, k, m_u

# Planck constant
H = h  # 6.62607015e-34 J⋅s

# Boltzmann constant
KB = k  # 1.380649e-23 J/K
```

## Review Process

All contributions undergo review:

1. **Automated checks**: Code style, tests
2. **Technical review**: Correctness of calculations
3. **Documentation review**: Clarity and completeness
4. **Scientific review**: Physical validity

Reviews may take several days. Be patient and responsive to feedback.

## Academic Integrity

### Data Sources

- Only use published, peer-reviewed experimental data
- Cite all sources properly
- Do not fabricate or modify experimental results
- Clearly distinguish experimental data from calculations

### Methodology

- Document all assumptions
- Justify approximations
- Report uncertainties
- Maintain reproducibility

### Authorship

Contributions to this repository do not automatically grant authorship on related publications. Authorship decisions follow standard academic criteria.

## Questions and Discussion

- Open an issue for questions about methodology
- Use discussions for general questions
- Email maintainer for private inquiries

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

## Code of Conduct

### Expected Behavior

- Be respectful and professional
- Focus on scientific merit
- Provide constructive feedback
- Acknowledge others' contributions

### Unacceptable Behavior

- Personal attacks or harassment
- Plagiarism or data fabrication
- Disrespectful or discriminatory language
- Sharing confidential information

## Contact

**Author:** Oleksii Onasenko  
**Developer:** SubstanceNet  
**Project:** System A.1 - ⁸⁷Rb BEC Emergence Analysis

For questions about the theoretical framework or methodology, refer to:
- `docs/METHODOLOGY.md` - Complete methodology
- `README.md` - Project overview
- GitHub Issues - Technical questions

---

**Last Updated:** November 15, 2025
