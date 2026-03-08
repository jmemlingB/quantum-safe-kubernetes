"""
Quantum-Safe Kubernetes: A Framework for Vacuum-Entropy Integration
Script B: Performance Visualizer (MTTE vs. Entropy Quality)
Authors: Hyemin Yoo (Georgia Tech), Johannes Memling (Marymount)
Date: January 2026
"""

import matplotlib.pyplot as plt

def generate_mtte_plot():
    """
    Generates Figure 1 from the study, illustrating the relationship between 
    Min-Entropy degradation and the Mean Time to Eviction (MTTE).
    """
    # Benchmarked data points from the simulation (Table 1 calibration)
    entropy_x = [1.0, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70]
    mtte_y = [0, 0, 0, 850, 420, 180, 142.5] # MTTE latency in ms

    plt.figure(figsize=(10, 6))
    plt.plot(entropy_x, mtte_y, marker='s', markersize=8, linewidth=2, color='#2c3e50')
    
    # Highlight the NIST SP 800-90B Critical Threshold
    plt.axvline(x=0.85, color='red', linestyle='--', label='NIST Threshold (0.85)')

    plt.title('Figure 1: Eviction Latency (MTTE) vs. Entropy Quality', fontsize=14)
    plt.xlabel('Min-Entropy ($H_\infty$)', fontsize=12)
    plt.ylabel('Mean Time to Eviction (ms)', fontsize=12)
    
    # Invert x-axis to show degradation from left to right
    plt.gca().invert_xaxis()
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save a high-res version for the paper/GitHub repository
    print("Generating Figure_1_MTTE.png...")
    plt.savefig("Figure_1_MTTE.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    print("Initializing MTTE Performance Visualizer...")
    generate_mtte_plot()
