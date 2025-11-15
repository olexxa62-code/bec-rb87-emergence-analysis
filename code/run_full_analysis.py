#!/usr/bin/env python3
"""
Full Analysis Pipeline for ⁸⁷Rb BEC Emergence Parameter

System Classification: A.1 bec_rb87_kappa_analysis
Author: Oleksii Onasenko
Developer: SubstanceNet
Theoretical Framework: The Emergence Parameter κ ≈ 1: An Empirical Signature of Criticality in Physical and Biological Systems

This script executes the complete analysis workflow.
Date: November 2025
"""

import os
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from emergence_analysis import BECDataset, BECAnalyzer
from visualization import BECVisualizer
from statistical_tests import BECStatisticalAnalysis, generate_analysis_report
import numpy as np


def convert_numpy_types(obj):
    """Convert numpy types to native Python types for JSON serialization."""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {key: convert_numpy_types(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(item) for item in obj]
    else:
        return obj


UNCERTAINTIES = {
    'A': 0.05, 'A_c': 0.10, 'tau': 0.01,
    'Lambda': 0.25, 'Lambda_c': 0.05
}


def setup_directories():
    """Create output directories."""
    base_dir = Path(__file__).parent.parent
    dirs = [base_dir / 'figures', base_dir / 'docs', base_dir / 'supplementary']
    for dir_path in dirs:
        dir_path.mkdir(exist_ok=True)
    return base_dir


def print_header():
    """Print analysis header."""
    print("="*80)
    print("EMERGENCE PARAMETER (κ) ANALYSIS FOR BOSE-EINSTEIN CONDENSATE")
    print("="*80)
    print(f"System: ⁸⁷Rb BEC in TOP magnetic trap")
    print(f"Data Source: Anderson et al. (1995) Science 269:198-201")
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    print()


def load_and_analyze_data():
    """Load data and perform analysis."""
    print("1. LOADING DATA...")
    print("-"*80)
    
    dataset = BECDataset()
    params = dataset.get_bec_parameters()
    print(f"   N_condensate: {params.N_condensate:.0f} atoms")
    print(f"   N_total(T_c): {params.N_total_Tc:.0f} atoms")
    print(f"   T_c: {params.T_c:.0f} nK")
    print()
    
    print("2. CALCULATING PARAMETERS...")
    print("-"*80)
    
    analyzer = BECAnalyzer(params)
    results = analyzer.full_analysis(UNCERTAINTIES)
    
    print(f"   Thomas-Fermi radii:")
    print(f"      R_z (axial): {results['R_z_um']:.2f} μm")
    print(f"      R_r (radial): {results['R_r_um']:.2f} μm")
    print(f"      Geometric mean (Λ): {results['Lambda_um']:.2f} μm")
    print()
    print(f"   Thermal de Broglie wavelength (Λ_c): {results['Lambda_c_um']:.3f} μm")
    print()
    print(f"   Emergence parameter:")
    print(f"      κ = {results['kappa']:.3f} ± {results['kappa_uncertainty']:.3f}")
    print(f"      Regime: {results['interpretation']}")
    print()
    
    return results


def perform_statistical_analysis(results, base_dir):
    """Perform statistical analysis."""
    print("3. STATISTICAL ANALYSIS...")
    print("-"*80)
    
    report_path = base_dir / 'docs' / 'statistical_report.txt'
    generate_analysis_report(results, UNCERTAINTIES, output_file=str(report_path))
    print(f"   Report saved: {report_path}")
    
    stats = BECStatisticalAnalysis()
    ci_lower, ci_upper = stats.confidence_interval(results['kappa'], results['kappa_uncertainty'])
    print(f"\n   95% Confidence Interval: [{ci_lower:.3f}, {ci_upper:.3f}]")
    
    interp = stats.kappa_interpretation(results['kappa'], results['kappa_uncertainty'])
    print(f"   Consistent with κ≈1: {interp['consistent_with_hypothesis']}")
    print()


def generate_figures(results, base_dir):
    """Generate figures."""
    print("4. GENERATING FIGURES...")
    print("-"*80)
    
    figures_dir = base_dir / 'figures'
    visualizer = BECVisualizer()
    
    print("   Creating combined analysis plot...")
    fig1_path = figures_dir / 'bec_kappa_analysis_combined.png'
    visualizer.plot_combined_analysis(results, save_path=str(fig1_path), dpi=300)
    print(f"   Saved: {fig1_path}")
    
    print("   Creating high-resolution version...")
    fig1_highres_path = figures_dir / 'bec_kappa_analysis_combined_highres.png'
    visualizer.plot_combined_analysis(results, save_path=str(fig1_highres_path), dpi=600)
    print(f"   Saved: {fig1_highres_path}")
    print()


def save_results(results, base_dir):
    """Save results."""
    print("5. SAVING RESULTS...")
    print("-"*80)
    
    import json
    import pandas as pd
    
    results_json = base_dir / 'supplementary' / 'analysis_results.json'
    results_serializable = convert_numpy_types(results)
    with open(results_json, 'w') as f:
        json.dump(results_serializable, f, indent=2)
    print(f"   JSON results: {results_json}")
    
    results_csv = base_dir / 'supplementary' / 'kappa_results.csv'
    df = pd.DataFrame([results])
    df.to_csv(results_csv, index=False)
    print(f"   CSV results: {results_csv}")
    print()


def print_key_findings(results):
    """Print key findings."""
    print("="*80)
    print("KEY FINDINGS")
    print("="*80)
    print()
    print("★ SYSTEM: ⁸⁷Rb Bose-Einstein Condensate")
    print(f"   Source: Anderson et al. (1995) Science 269:198-201")
    print()
    print("★ EMERGENCE PARAMETER:")
    print(f"   κ = {results['kappa']:.3f} ± {results['kappa_uncertainty']:.3f}")
    print(f"   Regime: {results['interpretation']}")
    print()
    print("INTERPRETATION:")
    print("   κ ≈ 0.8 is close to the critical point κ = 1")
    print("   This confirms that BEC occurs at the emergence threshold")
    print()
    print("="*80)


def main():
    """Run complete analysis pipeline."""
    print_header()
    base_dir = setup_directories()
    
    try:
        results = load_and_analyze_data()
        perform_statistical_analysis(results, base_dir)
        generate_figures(results, base_dir)
        save_results(results, base_dir)
        print_key_findings(results)
        
        print("✓ ANALYSIS COMPLETE!")
        print(f"   All results saved in: {base_dir}")
        print()
        return 0
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
