import sys
import os

# Adds the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Interpolation.Methods as md
import numpy as np

def trap(data,x_axis):
    size=len(x_axis)-1
    start=0
    fb=data[size]
    fa=data[0]
    step=x_axis[size]-x_axis[start]

    value_1=0.5*step(fa-fb)

    error=10
    while error>1:

        spline,new_x_axis=md.spline(data,x_axis)

        midpoint=(x_axis[start]+x_axis[size])/2
        midpoint=np.argmin(new_x_axis-midpoint)
        Value_2=spline[midpoint]


        error=np.abs((value_2-value_1)/value_1)
    return fb

x_axis=np.linspace(0,10,10)
data=np.array([1,2,3,4,5,6,67,21,3,12])
print(trap(data,x_axis))

def find_midpoint(start_points):
    number=len(start_points)-1


    midpoint=(start_points[start]+start_points[size])/2
    midpoint=np.argmin(new_x_axis-midpoint)

