import sys
import os

# Adds the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Interpolation.Methods as md

from scipy.integrate import cumulative_trapezoid
import numpy as np

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

def Monte_min(f,strat_bounds, end_bounds):
    volume=np.prod(np.abs(end_bounds)+np.abs(strat_bounds))

def metropolis():
    return

