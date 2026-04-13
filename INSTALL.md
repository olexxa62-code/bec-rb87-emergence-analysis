# Installation Guide

Complete installation instructions for the ⁸⁷Rb BEC Emergence Parameter Analysis project.

## System Requirements

### Minimum Requirements

- **OS:** Linux, macOS, or Windows 10/11
- **Python:** 3.8 or higher
- **RAM:** 2 GB
- **Storage:** 100 MB free space
- **Internet:** Required for initial setup

### Recommended Requirements

- **Python:** 3.10 or higher
- **RAM:** 4 GB or more
- **Storage:** 500 MB for dependencies and outputs

## Installation Methods

### Method 1: Clone from GitHub (Recommended)
```bash
# Clone repository
git clone https://github.com/[username]/A.1_bec_rb87_kappa_analysis.git
cd A.1_bec_rb87_kappa_analysis

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Method 2: Download ZIP
```bash
# Download and extract ZIP from GitHub
# Navigate to extracted folder
cd A.1_bec_rb87_kappa_analysis

# Create and activate virtual environment (as above)
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

## Dependencies

### Core Dependencies

All dependencies are listed in `requirements.txt`:
```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
scipy>=1.7.0
seaborn>=0.11.0
```

### Installation Verification

After installation, verify dependencies:
```bash
python3 << 'PYEOF'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"SciPy: {scipy.__version__}")
print(f"Seaborn: {sns.__version__}")
print("\nAll dependencies loaded successfully!")
PYEOF
```

Expected output:
```
NumPy: 1.21.x
Pandas: 1.3.x
Matplotlib: 3.4.x
SciPy: 1.7.x
Seaborn: 0.11.x

All dependencies loaded successfully!
```

## Platform-Specific Instructions

### Linux (Ubuntu/Debian)
```bash
# Install Python and pip (if not already installed)
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Install development tools (recommended)
sudo apt install build-essential python3-dev

# Follow standard installation from Method 1
```

### macOS
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.10

# Follow standard installation from Method 1
```

### Windows
```powershell
# Ensure Python is installed from python.org
# Open PowerShell or Command Prompt

# Navigate to project directory
cd A.1_bec_rb87_kappa_analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Testing Installation

### Quick Test
```bash
cd code/
python3 << 'PYEOF'
from emergence_analysis import BECParameters, BECAnalyzer

# Test with default parameters
params = BECParameters(
    N_condensate=2000,
    N_total_Tc=20000,
    T_c=170,
    omega_z=120,
    omega_r=42,
    a=5.3
)

analyzer = BECAnalyzer(params)
results = analyzer.full_analysis()

print(f"κ = {results['kappa']:.3f} ± {results['kappa_uncertainty']:.3f}")
print("\nInstallation test successful!")
PYEOF
```

Expected output:
```
κ = 0.806 ± 0.225

Installation test successful!
```

### Full Analysis Test
```bash
cd code/
python3 run_full_analysis.py
```

This will:
1. Load experimental data
2. Calculate all parameters
3. Generate figures
4. Create statistical report

Check for:
- `figures/bec_kappa_analysis_combined.png`
- `figures/bec_kappa_analysis_combined_highres.png`
- `docs/statistical_report.txt`

## Troubleshooting

### Common Issues

#### Issue: "No module named 'numpy'"

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: "Permission denied"

**Solution (Linux/macOS):**
```bash
# Don't use sudo with pip in virtual environment
# If necessary, fix permissions:
chmod +x code/*.py
```

#### Issue: matplotlib backend errors

**Solution:**
```bash
# Install tkinter (Linux)
sudo apt install python3-tk

# Or use non-interactive backend
export MPLBACKEND=Agg
```

#### Issue: "ModuleNotFoundError: No module named 'emergence_analysis'"

**Solution:**
```bash
# Ensure you're in the code/ directory
cd code/

# Or add parent directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Python Version Issues

If you have multiple Python versions:
```bash
# Use specific Python version
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Virtual Environment Issues

If virtual environment fails:
```bash
# Remove existing venv
rm -rf venv

# Recreate with different method
python3 -m venv --system-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
```

## Updating

### Update Code
```bash
# Pull latest changes (if using git)
git pull origin main

# Reinstall dependencies (in case requirements changed)
pip install --upgrade -r requirements.txt
```

### Update Dependencies
```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Or update specific package
pip install --upgrade numpy
```

## Uninstallation
```bash
# Deactivate virtual environment
deactivate

# Remove project directory
cd ..
rm -rf A.1_bec_rb87_kappa_analysis
```

## Docker Installation (Alternative)

For reproducible environment across platforms:
```dockerfile
# Dockerfile (create this file)
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "code/run_full_analysis.py"]
```

Build and run:
```bash
docker build -t bec-analysis .
docker run -v $(pwd)/figures:/app/figures bec-analysis
```

## Development Installation

For contributing to the project:
```bash
# Clone repository
git clone https://github.com/[username]/A.1_bec_rb87_kappa_analysis.git
cd A.1_bec_rb87_kappa_analysis

# Create development branch
git checkout -b dev

# Install in editable mode with dev dependencies
pip install -e .
pip install pytest black flake8 mypy

# Install pre-commit hooks (optional)
pip install pre-commit
pre-commit install
```

## Performance Optimization

### For faster computation:
```bash
# Install optimized NumPy (if available for your platform)
pip install numpy[mkl]  # Intel MKL
# or
pip install numpy[openblas]  # OpenBLAS
```

### For parallel processing:
```bash
# Install joblib for parallel uncertainty calculations
pip install joblib
```

## Getting Help

If installation problems persist:

1. Check GitHub Issues: [repository]/issues
2. Consult TROUBLESHOOTING section in README.md
3. Review system requirements
4. Create new issue with:
   - OS and Python version
   - Complete error message
   - Steps you've tried

## Next Steps

After successful installation:

1. Read `README.md` for project overview
2. Review `docs/METHODOLOGY.md` for scientific details
3. Run analysis: `cd code/ && python3 run_full_analysis.py`
4. Examine outputs in `figures/` and `docs/`

---

**Last Updated:** November 15, 2025  
**Tested Platforms:** Ubuntu 22.04, macOS 13, Windows 11  
**Python Versions:** 3.8, 3.9, 3.10, 3.11
