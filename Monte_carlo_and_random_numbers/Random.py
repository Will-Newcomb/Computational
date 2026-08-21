import sys
import os

# Adds the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Interpolation.Methods as md


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


def Transformation():
    return
    #need to intergarte our PDF 
    #then need to solve algebratic equation

    #Might want to add other control functions after ive finished transformation method

def Rejection(f,x_axis,bounds,N):
    accepted_samples=np.array([])
    max_func=np.max(f)+0.01

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

num_cycles = 2
points_per_cycle = 10
total_points = num_cycles * points_per_cycle
x_axis_fine=np.linspace(0, num_cycles, 5000, endpoint=False)

x_axis = np.linspace(0, num_cycles, total_points, endpoint=False)
data = 10 * np.exp(-2 * np.pi * x_axis)

hist=Rejection(data,x_axis, bounds=[min(x_axis),max(x_axis)], N= 100000)
plt.hist(hist,x_axis_fine)
plt.show()
plt.scatter(x_axis,data)
plt.show()




def Monte_min(f,strat_bounds, end_bounds):
    volume=np.prod(np.abs(end_bounds)+np.abs(strat_bounds))

def metropolis():
    return




random = congruential_gen(123153,266231,1651156164,13215)
plt.hist(random)
plt.show()
