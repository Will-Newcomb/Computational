import numpy as np
import matplotlib.pyplot as plt
import Methods as md
import time


start_time = time.time()

num_cycles = 1
points_per_cycle = 5
total_points = num_cycles * points_per_cycle

x_axis = np.linspace(0, num_cycles, total_points, endpoint=False)
data = np.sin(2 * np.pi * x_axis)



linear,new_x_axis=md.linear_vector(data,x_axis)

#poly,new_x_axis=md.Lagrange(data,x_axis)
plt.plot(new_x_axis, linear)


#plt.plot(new_x_axis, poly)
plt.scatter(x_axis, data)

print("--- %s seconds ---" % (time.time() - start_time))
