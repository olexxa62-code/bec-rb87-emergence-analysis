"""
Sensitivity Analysis for Emergence Parameter κ

System Classification: A.1.1 bec_rb87_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

Explores robustness of κ ≈ 1 result to parameter choices.
Date: November 2025
"""
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple, List
from emergence_analysis import BECParameters, BECAnalyzer

class SensitivityAnalyzer:
    """Analyze sensitivity of κ to parameter choices."""
    
    def __init__(self, base_params: BECParameters):
        """Initialize with baseline parameters."""
        self.base_params = base_params
        self.base_analyzer = BECAnalyzer(base_params)
        self.base_results = self.base_analyzer.full_analysis()
        
    def vary_Ac_choice(self) -> Dict:
        """Compare κ using different Ac definitions."""
        # Current: N_total(Tc) = 20,000
        # Ideal gas: N_c = 247,000
        
        Ac_values = {
            'Measured N_total(Tc)': 20000,
            'Ideal gas N_c': 247000,
            'Intermediate (50k)': 50000,
            'Intermediate (100k)': 100000
        }
        
        results = {}
        for label, Ac in Ac_values.items():
            params = BECParameters(
                N_condensate=self.base_params.N_condensate,
                N_total_Tc=Ac,
                T_c=self.base_params.T_c,
                omega_z=self.base_params.omega_z,
                omega_r=self.base_params.omega_r,
                a=self.base_params.a
            )
            analyzer = BECAnalyzer(params)
            result = analyzer.full_analysis()
            results[label] = result['kappa']
            
        return results
    
    def vary_tau_definition(self) -> Dict:
        """Explore different τ definitions."""
        # Current: τ = 1.00 (perfect coherence)
        # Alternative: τ = sqrt(N0/N)
        # Alternative: τ = N0/N
        
        N0 = self.base_params.N_condensate
        N_total = self.base_params.N_total_Tc
        
        tau_definitions = {
            'Perfect coherence (τ=1)': 1.00,
            'sqrt(N0/N)': np.sqrt(N0 / N_total),
            'N0/N (linear)': N0 / N_total,
            'Conservative (τ=0.9)': 0.90
        }
        
        results = {}
        base_kappa = self.base_results['kappa']
        
        for label, tau in tau_definitions.items():
            # Scale κ by tau ratio (since κ ∝ τ)
            kappa_scaled = base_kappa * (tau / 1.00)
            results[label] = kappa_scaled
            
        return results
    
    def vary_length_scale(self) -> Dict:
        """Compare different length scale choices."""
        # Get from base results
        R_z = self.base_results['R_z_um']
        R_r = self.base_results['R_r_um']
        Lambda_c = self.base_results['Lambda_c_um']
        
        length_definitions = {
            'Geometric mean (current)': (R_z * R_r**2)**(1/3),
            'Radial R_r only': R_r,
            'Axial R_z only': R_z,
            'Arithmetic mean': (R_z + R_r) / 2,
            'Harmonic mean': 2 * R_z * R_r / (R_z + R_r)
        }
        
        results = {}
        base_Lambda = (R_z * R_r**2)**(1/3)
        base_kappa = self.base_results['kappa']
        
        for label, Lambda in length_definitions.items():
            # Scale κ by (Λ/Λc) ratio
            kappa_scaled = base_kappa * (Lambda / base_Lambda)
            results[label] = kappa_scaled
            
        return results
    
    def temperature_dependence(self, T_ratios: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Calculate κ(T/Tc) for various temperatures.
        
        Assumes:
        - N0(T) ∝ (1 - T/Tc)^(3/2) for T < Tc
        - Λ(T) changes with temperature
        """
        kappa_values = []
        
        for ratio in T_ratios:
            if ratio >= 1.0:
                kappa_values.append(0.0)  # No condensate above Tc
            else:
                # Condensate fraction
                N0_T = self.base_params.N_total_Tc * (1 - ratio**3)
                
                # Temperature scaling
                T = ratio * self.base_params.T_c
                
                # Create temperature-dependent parameters
                params = BECParameters(
                    N_condensate=N0_T,
                    N_total_Tc=self.base_params.N_total_Tc,
                    T_c=T,
                    omega_z=self.base_params.omega_z,
                    omega_r=self.base_params.omega_r,
                    a=self.base_params.a
                )
                
                analyzer = BECAnalyzer(params)
                result = analyzer.full_analysis()
                kappa_values.append(result['kappa'])
        
        return T_ratios, np.array(kappa_values)

def plot_sensitivity_analysis(save_path: str = '../figures/'):
    """Generate comprehensive sensitivity analysis plots."""
    # Load baseline parameters
    from emergence_analysis import BECParameters
    
    params = BECParameters(
        N_condensate=2000,
        N_total_Tc=20000,
        T_c=170,
        omega_z=120,
        omega_r=42,
        a=5.77
    )
    
    analyzer = SensitivityAnalyzer(params)
    
    # Create figure with 4 subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Sensitivity Analysis: Emergence Parameter κ', 
                 fontsize=16, fontweight='bold')
    
    # 1. Ac variation
    ax1 = axes[0, 0]
    ac_results = analyzer.vary_Ac_choice()
    labels = list(ac_results.keys())
    values = list(ac_results.values())
    
    colors = ['#2E4057' if 'Measured' in l else '#95A3A4' for l in labels]
    ax1.barh(labels, values, color=colors)
    ax1.axvline(1.0, color='black', linestyle='--', linewidth=2, label='κ = 1')
    ax1.set_xlabel('κ (emergence parameter)', fontsize=12, fontweight='bold')
    ax1.set_title('A) Critical Number Choice (Ac)', fontsize=13, fontweight='bold')
    ax1.legend()
    ax1.grid(axis='x', alpha=0.3)
    
    # 2. τ variation
    ax2 = axes[0, 1]
    tau_results = analyzer.vary_tau_definition()
    labels = list(tau_results.keys())
    values = list(tau_results.values())
    
    colors = ['#2E4057' if 'Perfect' in l else '#95A3A4' for l in labels]
    ax2.barh(labels, values, color=colors)
    ax2.axvline(1.0, color='black', linestyle='--', linewidth=2, label='κ = 1')
    ax2.set_xlabel('κ (emergence parameter)', fontsize=12, fontweight='bold')
    ax2.set_title('B) Order Parameter Definition (τ)', fontsize=13, fontweight='bold')
    ax2.legend()
    ax2.grid(axis='x', alpha=0.3)
    
    # 3. Length scale variation
    ax3 = axes[1, 0]
    length_results = analyzer.vary_length_scale()
    labels = list(length_results.keys())
    values = list(length_results.values())
    
    colors = ['#2E4057' if 'Geometric' in l else '#95A3A4' for l in labels]
    ax3.barh(labels, values, color=colors)
    ax3.axvline(1.0, color='black', linestyle='--', linewidth=2, label='κ = 1')
    ax3.set_xlabel('κ (emergence parameter)', fontsize=12, fontweight='bold')
    ax3.set_title('C) Length Scale Choice (Λ)', fontsize=13, fontweight='bold')
    ax3.legend()
    ax3.grid(axis='x', alpha=0.3)
    
    # 4. Temperature dependence
    ax4 = axes[1, 1]
    T_ratios = np.linspace(0.6, 1.0, 50)
    T_vals, kappa_vals = analyzer.temperature_dependence(T_ratios)
    
    ax4.plot(T_vals, kappa_vals, linewidth=2.5, color='#2E4057')
    ax4.axhline(1.0, color='black', linestyle='--', linewidth=2, label='κ = 1')
    ax4.axvline(0.965, color='gray', linestyle=':', linewidth=1.5, 
                label='T/Tc = 0.965 (experimental)')
    ax4.fill_between(T_vals, 0.7, 1.3, alpha=0.15, color='gray', 
                      label='Critical region')
    ax4.set_xlabel('T/Tc', fontsize=12, fontweight='bold')
    ax4.set_ylabel('κ (emergence parameter)', fontsize=12, fontweight='bold')
    ax4.set_title('D) Temperature Dependence κ(T)', fontsize=13, fontweight='bold')
    ax4.legend()
    ax4.grid(alpha=0.3)
    ax4.set_ylim([0, 2.5])
    
    plt.tight_layout()
    
    # Save both resolutions
    plt.savefig(f'{save_path}sensitivity_analysis.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{save_path}sensitivity_analysis_highres.png', dpi=600, bbox_inches='tight')
    
    print(f"Sensitivity analysis saved to {save_path}")
    plt.close()
    
    return fig

if __name__ == '__main__':
    print("Running sensitivity analysis...")
    plot_sensitivity_analysis()
    print("Complete!")
