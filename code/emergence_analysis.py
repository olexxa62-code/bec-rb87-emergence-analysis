"""
Emergence Parameter (κ) Analysis for Bose-Einstein Condensate

System Classification: A.1.1 bec_rb87_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

Analysis of ⁸⁷Rb BEC in TOP magnetic trap based on Anderson et al. (1995).
Date: November 2025
"""
import numpy as np
import pandas as pd
from typing import Dict, Tuple, Optional
from dataclasses import dataclass
import json


@dataclass
class BECParameters:
    """Parameters for BEC system."""
    N_condensate: float  # Number of atoms in condensate
    N_total_Tc: float    # Total atoms at critical temperature
    T_c: float           # Critical temperature (nK)
    omega_z: float       # Axial trap frequency (Hz)
    omega_r: float       # Radial trap frequency (Hz)
    a: float             # Scattering length (nm)
    
    def __post_init__(self):
        """Validate parameters."""
        if self.N_condensate <= 0 or self.N_total_Tc <= 0:
            raise ValueError("Atom numbers must be positive")
        if self.T_c <= 0:
            raise ValueError("Temperature must be positive")
        if self.omega_z <= 0 or self.omega_r <= 0:
            raise ValueError("Trap frequencies must be positive")


class BECAnalyzer:
    """
    Analyzer for emergence parameter κ in BEC systems.
    
    κ = (A/A_c) · τ · (Λ/Λ_c)
    
    For BEC:
        A = N_condensate (atoms in condensate)
        A_c = N_total(T_c) (total atoms at critical temperature)
        τ = 1.00 (complete quantum coherence)
        Λ = Thomas-Fermi radius
        Λ_c = thermal de Broglie wavelength
    """
    
    # Physical constants
    HBAR = 1.055e-34  # J·s
    KB = 1.38e-23     # J/K
    H = 6.626e-34     # J·s
    M_RB87 = 87 * 1.66e-27  # kg (mass of 87Rb)
    A0 = 5.29e-11     # m (Bohr radius)
    
    def __init__(self, params: BECParameters):
        """Initialize analyzer with BEC parameters."""
        self.params = params
        
    def calculate_lambda_dB(self) -> float:
        """
        Calculate thermal de Broglie wavelength at T_c.
        
        λ_dB = h / √(2π m k_B T)
        
        Returns:
            Thermal de Broglie wavelength (μm)
        """
        T_kelvin = self.params.T_c * 1e-9  # Convert nK to K
        
        denominator = np.sqrt(2 * np.pi * self.M_RB87 * self.KB * T_kelvin)
        lambda_dB = self.H / denominator
        
        return lambda_dB * 1e6  # Convert to μm
    
    def calculate_thomas_fermi_radius(self) -> Tuple[float, float, float]:
        """
        Calculate Thomas-Fermi radii for anisotropic trap.
        
        Returns:
            Tuple of (R_z, R_r, R_mean) in μm
        """
        # Convert to SI units
        omega_z = 2 * np.pi * self.params.omega_z  # rad/s
        omega_r = 2 * np.pi * self.params.omega_r  # rad/s
        a_si = self.params.a * 1e-9  # m
        N0 = self.params.N_condensate
        
        # Geometric mean frequency
        omega_bar = (omega_z * omega_r**2)**(1/3)
        
        # Harmonic oscillator length
        a_ho = np.sqrt(self.HBAR / (self.M_RB87 * omega_bar))
        
        # Chemical potential
        factor = 15 * N0 * a_si / a_ho
        mu = (self.HBAR * omega_bar / 2) * factor**(2/5)
        
        # Thomas-Fermi radii
        R_z = np.sqrt(2 * mu / (self.M_RB87 * omega_z**2))
        R_r = np.sqrt(2 * mu / (self.M_RB87 * omega_r**2))
        
        # Geometric mean (characteristic size)
        R_mean = (R_z * R_r**2)**(1/3)
        
        return R_z * 1e6, R_r * 1e6, R_mean * 1e6  # Convert to μm
    
    def calculate_kappa(self, Lambda: float, Lambda_c: float, 
                       tau: float = 1.0) -> Dict:
        """
        Calculate emergence parameter κ.
        
        Args:
            Lambda: Interaction scale (μm)
            Lambda_c: Critical interaction scale (μm)
            tau: Order parameter (default 1.0 for BEC)
            
        Returns:
            Dictionary with analysis results
        """
        A = self.params.N_condensate
        A_c = self.params.N_total_Tc
        
        kappa = (A / A_c) * tau * (Lambda / Lambda_c)
        
        return {
            'kappa': kappa,
            'A': A,
            'A_c': A_c,
            'tau': tau,
            'Lambda': Lambda,
            'Lambda_c': Lambda_c,
            'A_ratio': A / A_c,
            'Lambda_ratio': Lambda / Lambda_c,
            'distance_from_critical': abs(kappa - 1)
        }
    
    def uncertainty_analysis(self, Lambda: float, Lambda_c: float,
                           uncertainties: Optional[Dict[str, float]] = None) -> Dict:
        """
        Propagate uncertainty through κ calculation using full error propagation.
        
        Args:
            Lambda: Interaction scale (μm)
            Lambda_c: Critical interaction scale (μm)
            uncertainties: Dictionary with relative uncertainties for all parameters
            
        Returns:
            Dictionary with uncertainty estimates
        """
        # Import here to avoid circular dependency
        from statistical_tests import BECStatisticalAnalysis
        
        # Default uncertainties if not provided
        if uncertainties is None:
            uncertainties = {
                'A': 0.05,
                'A_c': 0.10,
                'tau': 0.01,
                'Lambda': 0.25,
                'Lambda_c': 0.05
            }
        
        # Get parameters
        A = self.params.N_condensate
        A_c = self.params.N_total_Tc
        tau = 1.0
        
        # Use proper uncertainty propagation
        stats = BECStatisticalAnalysis()
        result = stats.uncertainty_propagation(
            A, A_c, tau, Lambda, Lambda_c, uncertainties
        )
        
        return result
    
    def full_analysis(self, uncertainties: Optional[Dict[str, float]] = None) -> Dict:
        """
        Perform complete analysis: calculate all parameters and κ.
        
        Args:
            uncertainties: Dictionary with relative uncertainties for all parameters
        
        Returns:
            Dictionary with complete analysis
        """
        # Calculate Lambda_c
        Lambda_c = self.calculate_lambda_dB()
        
        # Calculate Thomas-Fermi radii
        R_z, R_r, Lambda = self.calculate_thomas_fermi_radius()
        
        # Calculate kappa with proper uncertainty propagation
        uncertainty_result = self.uncertainty_analysis(Lambda, Lambda_c, uncertainties)
        
        return {
            'system': '87Rb BEC',
            'Lambda_c_um': Lambda_c,
            'R_z_um': R_z,
            'R_r_um': R_r,
            'Lambda_um': Lambda,
            'kappa': uncertainty_result['kappa'],
            'kappa_uncertainty': uncertainty_result['kappa_uncertainty'],
            'A': self.params.N_condensate,
            'A_c': self.params.N_total_Tc,
            'tau': 1.0,
            'interpretation': 'Critical' if abs(uncertainty_result['kappa'] - 1) < 0.3 
                            else 'Sub-critical' if uncertainty_result['kappa'] < 1 
                            else 'Super-critical'
        }


class BECDataset:
    """Handler for BEC data."""
    
    def __init__(self, csv_path: Optional[str] = None):
        """
        Initialize dataset.
        
        Args:
            csv_path: Path to CSV file with BEC data
        """
        if csv_path:
            self.data = pd.read_csv(csv_path)
        else:
            # Load from default location
            import os
            default_path = os.path.join(
                os.path.dirname(__file__), 
                '..', 'data', 'anderson_1995_bec_data.csv'
            )
            self.data = pd.read_csv(default_path)
    
    def get_bec_parameters(self) -> BECParameters:
        """Extract BEC parameters from dataset."""
        row = self.data.iloc[0]
        
        return BECParameters(
            N_condensate=row['N_condensate'],
            N_total_Tc=row['N_total_Tc'],
            T_c=row['T_c_nK'],
            omega_z=row['omega_z_Hz'],
            omega_r=row['omega_r_Hz'],
            a=row['a_nm']
        )
    
    def analyze_system(self, uncertainties: Optional[Dict[str, float]] = None) -> pd.DataFrame:
        """
        Analyze BEC system and return results as DataFrame.
        
        Args:
            uncertainties: Dictionary with relative uncertainties for all parameters
        
        Returns:
            DataFrame with analysis results
        """
        params = self.get_bec_parameters()
        analyzer = BECAnalyzer(params)
        result = analyzer.full_analysis(uncertainties)
        
        # Add to original data
        df = self.data.copy()
        df['kappa_calculated'] = result['kappa']
        df['kappa_uncertainty'] = result['kappa_uncertainty']
        df['R_z_um'] = result['R_z_um']
        df['R_r_um'] = result['R_r_um']
        df['Lambda_calculated'] = result['Lambda_um']
        df['Lambda_c_calculated'] = result['Lambda_c_um']
        df['interpretation'] = result['interpretation']
        
        return df


def save_analysis_summary(results: Dict, filepath: str = "analysis_summary.json"):
    """
    Save analysis summary to JSON.
    
    Args:
        results: Analysis results dictionary
        filepath: Path to save JSON file
    """
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2)


# Example usage
if __name__ == "__main__":
    # Load data
    dataset = BECDataset()
    
    # Get parameters
    params = dataset.get_bec_parameters()
    print("BEC Parameters:")
    print(f"  N_condensate: {params.N_condensate}")
    print(f"  N_total(T_c): {params.N_total_Tc}")
    print(f"  T_c: {params.T_c} nK")
    print()
    
    # Full analysis
    analyzer = BECAnalyzer(params)
    results = analyzer.full_analysis()
    
    print("Analysis Results:")
    print(f"  κ = {results['kappa']:.3f} ± {results['kappa_uncertainty']:.3f}")
    print(f"  Λ = {results['Lambda_um']:.2f} μm (TF radius)")
    print(f"  Λ_c = {results['Lambda_c_um']:.3f} μm (de Broglie)")
    print(f"  Interpretation: {results['interpretation']}")
