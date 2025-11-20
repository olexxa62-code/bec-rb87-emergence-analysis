"""
Statistical Analysis and Uncertainty Propagation for BEC κ Analysis

System Classification: A.1.1 bec_rb87_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

Statistical methods and uncertainty quantification.
Date: November 2025
"""

import numpy as np
from typing import Dict, Tuple
from scipy import stats


class BECStatisticalAnalysis:
    """Statistical analysis for BEC emergence parameter."""
    
    @staticmethod
    def uncertainty_propagation(A: float, A_c: float, tau: float,
                               Lambda: float, Lambda_c: float,
                               uncertainties: Dict[str, float]) -> Dict:
        """Propagate uncertainties through κ calculation."""
        kappa = (A / A_c) * tau * (Lambda / Lambda_c)
        
        delta_A_rel = uncertainties.get('A', 0)
        delta_Ac_rel = uncertainties.get('A_c', 0)
        delta_tau_rel = uncertainties.get('tau', 0)
        delta_Lambda_rel = uncertainties.get('Lambda', 0)
        delta_Lambdac_rel = uncertainties.get('Lambda_c', 0)
        
        delta_kappa_rel = np.sqrt(
            delta_A_rel**2 + delta_Ac_rel**2 + delta_tau_rel**2 + 
            delta_Lambda_rel**2 + delta_Lambdac_rel**2
        )
        
        delta_kappa = kappa * delta_kappa_rel
        
        return {
            'kappa': kappa,
            'kappa_uncertainty': delta_kappa,
            'relative_uncertainty': delta_kappa_rel
        }
    
    @staticmethod
    def confidence_interval(kappa: float, uncertainty: float,
                          confidence: float = 0.95) -> Tuple[float, float]:
        """Calculate confidence interval for κ."""
        z_score = stats.norm.ppf((1 + confidence) / 2)
        margin = z_score * uncertainty
        return (kappa - margin, kappa + margin)
    
    @staticmethod
    def kappa_interpretation(kappa: float, uncertainty: float) -> Dict:
        """Interpret κ value in context of phase transition."""
        # Use 95% confidence interval for hypothesis testing
        ci_lower, ci_upper = BECStatisticalAnalysis.confidence_interval(
            kappa, uncertainty, confidence=0.95
        )
        
        includes_one = (ci_lower <= 1.0 <= ci_upper)
        distance_from_one = abs(kappa - 1.0)
        
        if includes_one:
            regime = 'critical'
            interpretation = 'κ ≈ 1 within uncertainty (optimal emergence)'
        elif kappa < 0.7:
            regime = 'sub-critical'
            interpretation = 'κ < 1 (below critical point)'
        elif kappa > 1.3:
            regime = 'super-critical'
            interpretation = 'κ > 1 (above critical point)'
        else:
            regime = 'near-critical'
            interpretation = 'κ close to 1 (near critical point)'
        
        return {
            'kappa': kappa,
            'uncertainty': uncertainty,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'regime': regime,
            'interpretation': interpretation,
            'distance_from_critical': distance_from_one,
            'consistent_with_hypothesis': includes_one
        }


def generate_analysis_report(results: Dict, 
                            uncertainties: Dict[str, float],
                            output_file: str = 'statistical_report.txt'):
    """Generate comprehensive statistical report."""
    stats = BECStatisticalAnalysis()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("STATISTICAL ANALYSIS REPORT\n")
        f.write("Emergence Parameter (κ) Analysis for ⁸⁷Rb BEC\n")
        f.write("="*80 + "\n\n")
        
        f.write("1. MEASURED PARAMETERS\n")
        f.write("-"*80 + "\n")
        f.write(f"System: ⁸⁷Rb Bose-Einstein Condensate\n")
        f.write(f"Source: Anderson et al. (1995) Science 269:198-201\n\n")
        f.write(f"N_condensate (A): {results['A']:.0f} atoms\n")
        f.write(f"N_total at T_c (A_c): {results['A_c']:.0f} atoms\n")
        f.write(f"τ (order parameter): {results['tau']:.2f}\n\n")
        
        f.write("2. CALCULATED LENGTH SCALES\n")
        f.write("-"*80 + "\n")
        f.write(f"Thomas-Fermi radius (Λ):\n")
        f.write(f"  R_z (axial): {results['R_z_um']:.2f} μm\n")
        f.write(f"  R_r (radial): {results['R_r_um']:.2f} μm\n")
        f.write(f"  Geometric mean: {results['Lambda_um']:.2f} μm\n\n")
        f.write(f"Thermal de Broglie wavelength (Λ_c): {results['Lambda_c_um']:.3f} μm\n\n")
        
        f.write("3. EMERGENCE PARAMETER κ\n")
        f.write("-"*80 + "\n")
        f.write(f"Formula: κ = (A/A_c) × τ × (Λ/Λ_c)\n\n")
        f.write(f"Components:\n")
        f.write(f"  A/A_c = {results['A']/results['A_c']:.3f}\n")
        f.write(f"  τ = {results['tau']:.3f}\n")
        f.write(f"  Λ/Λ_c = {results['Lambda_um']/results['Lambda_c_um']:.3f}\n\n")
        f.write(f"Result: κ = {results['kappa']:.3f} ± {results['kappa_uncertainty']:.3f}\n\n")
        
        ci_lower, ci_upper = stats.confidence_interval(
            results['kappa'], 
            results['kappa_uncertainty']
        )
        f.write(f"95% Confidence Interval: [{ci_lower:.3f}, {ci_upper:.3f}]\n\n")
        
        f.write("4. INTERPRETATION\n")
        f.write("-"*80 + "\n")
        interp = stats.kappa_interpretation(
            results['kappa'],
            results['kappa_uncertainty']
        )
        f.write(f"Regime: {interp['regime']}\n")
        f.write(f"Distance from critical point (|κ-1|): {interp['distance_from_critical']:.3f}\n")
        f.write(f"Consistent with κ≈1 hypothesis: {interp['consistent_with_hypothesis']}\n")
        f.write(f"\n{interp['interpretation']}\n\n")
        
        f.write("="*80 + "\n")
        f.write("END OF REPORT\n")
        f.write("="*80 + "\n")
    
    print(f"Statistical report saved: {output_file}")


if __name__ == "__main__":
    from emergence_analysis import BECDataset, BECAnalyzer
    
    dataset = BECDataset()
    params = dataset.get_bec_parameters()
    analyzer = BECAnalyzer(params)
    results = analyzer.full_analysis()
    
    uncertainties = {
        'A': 0.05, 'A_c': 0.10, 'tau': 0.01,
        'Lambda': 0.25, 'Lambda_c': 0.05
    }
    
    generate_analysis_report(results, uncertainties,
                           output_file='../docs/statistical_report.txt')
    
    print("Statistical analysis completed!")
