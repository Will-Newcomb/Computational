import numpy as np
import matplotlib.pyplot as plt
import Methods as md

import importlib
importlib.reload(md)

num_cycles = 4 
points_per_cycle = 12
total_points = num_cycles * points_per_cycle

x_axis = np.linspace(0, num_cycles, total_points, endpoint=False)
data = np.sin(2 * np.pi * x_axis)



#linear,new_x_axis=md.linear(data,x_axis)

poly,new_x_axis=md.Lagrange(data,x_axis)
#plt.plot(new_x_axis, linear)


plt.plot(new_x_axis, poly)
plt.scatter(x_axis, data)
plt.show()