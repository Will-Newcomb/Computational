import sys
import os

# Adds the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Interpolation.Methods as md

from scipy.integrate import cumulative_trapezoid
import numpy as np
import matplotlib.pyplot as plt
import Random as ra

x_axis = np.linspace(-5, 5, 200)

# Define a dictionary of different unnormalized shapes to test
shapes = {
    "Gaussian (Bell Curve)": np.exp(-0.5 * x_axis**2),
    "Bimodal (Two Peaks)": np.exp(-0.5 * (x_axis - 2.5)**2) + 0.8 * np.exp(-0.5 * (x_axis + 2)**2),
    "Oscillating Shape": np.sin(2 * x_axis)**2 * np.exp(-0.1 * x_axis**2),
    "Triangular Shape": np.maximum(0, 1 - np.abs(x_axis / 3)),
    "sine shape": np.sin(2 * x_axis)+1

}

# Set up the plot grid
fig, axes = plt.subplots(3, 2, figsize=(14, 15))
axes = axes.flatten()

# Loop through each shape, calculate area, normalize, and sample
for idx, (title, data) in enumerate(shapes.items()):
    ax = axes[idx]
    
    # Calculate the area under the curve using the trapezoidal rule
    area = np.trapezoid(data, x_axis)
    
    # Normalize the data to make it a true PDF
    data_pdf = data / area
    
    # Run Rejection Sampling
    N_samples = 100000
    samples = ra.Transformation(data_pdf, x_axis, N_samples)
    
    # Plot the histogram of the accepted samples
    ax.hist(samples, bins=50, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Sampled Data (Hist)')
    
    # Plot the theoretical PDF points over it
    ax.plot(x_axis, data_pdf, 'r--', lw=2, label='Target PDF (Normalized)')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlim([min(x_axis), max(x_axis)])
    ax.legend()

plt.tight_layout()
plt.show()


random = ra.congruential_gen(123153,266231,1651156164,13215)
plt.hist(random)
plt.show()
