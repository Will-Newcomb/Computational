import sys
import os

# Adds the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Interpolation.Methods as md

from scipy.integrate import cumulative_trapezoid
import numpy as np
import matplotlib.pyplot as plt

def congruential_gen(a,c,m,N):
    #Using 4 seeds to speed up appraoch using leapfrogging and vectorization
    number_list=np.array([1561,21154,3315161,447984203])
    new_numbers=number_list
    for i in range(1,N):
        new_numbers= (a*new_numbers+c)%m
        number_list = np.append(number_list, new_numbers)
    return number_list

#rejection moethod that interpolates instead of taking the nearest data value for more accurate results
def Rejection(f,x_axis,N):
    bounds=[min(x_axis),max(x_axis)]
    accepted_samples=np.array([])
    max_func=np.max(f)+1e-5
    while N>0:
        random_x = np.random.uniform(bounds[0], bounds[1], N)
        random_y = np.random.uniform(0, max_func, N)

        random_x_prob=md.spline(f,x_axis,random_x)

        mask = random_x_prob>random_y

        accepted_x = random_x[mask]

        if len(accepted_x) > 0:
            accepted_samples = np.append(accepted_samples,accepted_x)
            N -= len(accepted_x)

    return accepted_samples


def Transformation(f,x_axis,N):

    random_p = np.random.uniform(0,1,N)

    step_size=x_axis[1]-x_axis[0]
    #to avoid any completly 0 CDF values that arent the start
    f_safe = f + 1e-5
    cdf=np.append(np.array([0]),(cumulative_trapezoid(f_safe)*step_size))
    #normalining 
    cdf=cdf/cdf[-1]
    values = md.spline(x_axis, cdf, random_p)

    return values
    #need to intergarte our PDF 
    #then need to solve algebratic equation

    #Might want to add other control functions after ive finished transformation method




x_axis = np.linspace(-5, 5, 200)

# Define a dictionary of different unnormalized shapes to test
shapes = {
    "Gaussian (Bell Curve)": np.exp(-0.5 * x_axis**2),
    "Bimodal (Two Peaks)": np.exp(-0.5 * (x_axis - 2.5)**2) + 0.8 * np.exp(-0.5 * (x_axis + 2)**2),
    "Oscillating Shape": np.sin(2 * x_axis)**2 * np.exp(-0.1 * x_axis**2),
    "Triangular Shape": np.maximum(0, 1 - np.abs(x_axis / 3))
}

# Set up the plot grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
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
    samples = Rejection(data_pdf, x_axis, N_samples)
    
    # Plot the histogram of the accepted samples
    ax.hist(samples, bins=50, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Sampled Data (Hist)')
    
    # Plot the theoretical PDF points over it
    ax.plot(x_axis, data_pdf, 'r--', lw=2, label='Target PDF (Normalized)')
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlim([min(x_axis), max(x_axis)])
    ax.legend()

plt.tight_layout()
plt.show()


def Monte_min(f,strat_bounds, end_bounds):
    volume=np.prod(np.abs(end_bounds)+np.abs(strat_bounds))

def metropolis():
    return




random = congruential_gen(123153,266231,1651156164,13215)
plt.hist(random)
plt.show()
