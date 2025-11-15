"""
Visualization tools for BEC emergence parameter analysis.

This module provides publication-quality plotting for κ analysis of BEC.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional, Dict
import matplotlib.patches as mpatches


class BECVisualizer:
    """Publication-quality visualizations for BEC κ analysis."""
    
    # Color scheme
    COLORS = {
        'critical': '#70AD47',      # Green
        'sub-critical': '#4472C4',  # Blue
        'super-critical': '#E74C3C', # Red
        'measured': '#2E4057',       # Dark blue
        'calculated': '#FF6B35',     # Orange
        'uncertainty': '#95A3A4'     # Gray
    }
    
    def __init__(self, style: str = 'seaborn-v0_8-paper'):
        """Initialize visualizer."""
        plt.style.use(style)
    
    def plot_kappa_with_uncertainty(self,
                                    kappa: float,
                                    uncertainty: float,
                                    ax: Optional[plt.Axes] = None,
                                    title: str = 'κ for ⁸⁷Rb BEC') -> plt.Axes:
        """Plot κ value with uncertainty band."""
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 6))
        
        ax.errorbar([1], [kappa], yerr=[uncertainty],
                   fmt='o', markersize=15, capsize=10, capthick=2,
                   color=self.COLORS['measured'], 
                   ecolor=self.COLORS['uncertainty'],
                   label=f'κ = {kappa:.2f} ± {uncertainty:.2f}')
        
        ax.axhline(y=1.0, color='black', linestyle='--', 
                  linewidth=2.5, label='κ = 1 (critical point)')
        ax.axhspan(0.7, 1.3, alpha=0.15, color='gray',
                  label='κ ≈ 1.0 ± 0.3')
        
        ax.set_xlim(0.5, 1.5)
        ax.set_ylim(0, 1.5)
        ax.set_ylabel('κ (emergence parameter)', fontsize=14, fontweight='bold')
        ax.set_title(title, fontsize=16, fontweight='bold', pad=15)
        ax.set_xticks([1])
        ax.set_xticklabels(['⁸⁷Rb BEC\n(Anderson 1995)'])
        ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
        ax.grid(True, alpha=0.3, axis='y')
        
        return ax
    
    def plot_parameter_comparison(self,
                                 results: Dict,
                                 ax: Optional[plt.Axes] = None) -> plt.Axes:
        """Plot comparison of parameters (A/A_c, τ, Λ/Λ_c)."""
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        
        A_ratio = results['A'] / results['A_c']
        tau = results['tau']
        Lambda_ratio = results['Lambda_um'] / results['Lambda_c_um']
        
        parameters = ['A/A_c', 'τ', 'Λ/Λ_c']
        values = [A_ratio, tau, Lambda_ratio]
        
        bars = ax.bar(parameters, values, color=self.COLORS['calculated'],
                     edgecolor='black', linewidth=1.5, alpha=0.7)
        
        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{val:.3f}',
                   ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        ax.axhline(y=1.0, color='red', linestyle='--', 
                  linewidth=2, label='Reference value = 1')
        
        ax.set_ylabel('Parameter value', fontsize=13, fontweight='bold')
        ax.set_title('Components of κ = (A/A_c) × τ × (Λ/Λ_c)', 
                    fontsize=14, fontweight='bold', pad=15)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        ax.set_ylim(0, max(values) * 1.2)
        
        return ax
    
    def plot_thomas_fermi_radii(self,
                               R_z: float,
                               R_r: float,
                               Lambda_c: float,
                               ax: Optional[plt.Axes] = None) -> plt.Axes:
        """Plot Thomas-Fermi radii comparison."""
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, 6))
        
        radii = ['R_z\n(axial)', 'R_r\n(radial)', 'λ_dB\n(thermal)']
        values = [R_z, R_r, Lambda_c]
        colors = [self.COLORS['calculated'], 
                 self.COLORS['calculated'],
                 self.COLORS['critical']]
        
        bars = ax.bar(radii, values, color=colors, 
                     edgecolor='black', linewidth=1.5, alpha=0.7)
        
        for bar, val in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{val:.2f} μm',
                   ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        ax.set_ylabel('Length scale (μm)', fontsize=13, fontweight='bold')
        ax.set_title('Characteristic Length Scales in BEC', 
                    fontsize=14, fontweight='bold', pad=15)
        ax.grid(True, alpha=0.3, axis='y')
        
        return ax
    
    def plot_combined_analysis(self,
                              results: Dict,
                              save_path: Optional[str] = None,
                              dpi: int = 300) -> plt.Figure:
        """Create combined figure with multiple panels."""
        fig = plt.figure(figsize=(15, 5))
        
        ax1 = plt.subplot(1, 3, 1)
        self.plot_kappa_with_uncertainty(
            results['kappa'],
            results['kappa_uncertainty'],
            ax=ax1
        )
        
        ax2 = plt.subplot(1, 3, 2)
        self.plot_parameter_comparison(results, ax=ax2)
        
        ax3 = plt.subplot(1, 3, 3)
        self.plot_thomas_fermi_radii(
            results['R_z_um'],
            results['R_r_um'],
            results['Lambda_c_um'],
            ax=ax3
        )
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
            print(f"Figure saved: {save_path}")
        
        return fig


if __name__ == "__main__":
    from emergence_analysis import BECDataset, BECAnalyzer
    
    dataset = BECDataset()
    params = dataset.get_bec_parameters()
    analyzer = BECAnalyzer(params)
    results = analyzer.full_analysis()
    
    visualizer = BECVisualizer()
    fig = visualizer.plot_combined_analysis(
        results,
        save_path='../figures/bec_kappa_analysis_combined.png',
        dpi=300
    )
    
    print("Visualization created successfully!")
