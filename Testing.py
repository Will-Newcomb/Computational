import numpy as np
import matplotlib.pyplot as plt
import FFT as fft

num_cycles = 4          
points_per_cycle = 150
total_points = num_cycles * points_per_cycle

x_axis_time = np.linspace(0, num_cycles, total_points, endpoint=False)
data = np.sin(2 * np.pi * x_axis_time)


plt.figure(figsize=(8, 4))
plt.plot(x_axis_time, data)
plt.title(f"Sine Wave ({num_cycles} Cycles)")
plt.xlabel("Time (Units of 2π / Full Cycles)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()



fft_result = np.abs(np.fft.fft(data))
freq_axis = np.fft.fftfreq(total_points, d=1/points_per_cycle)
half_n = total_points // 2


my_fft,new_Length =fft.FFT(data, padding=True)
my_fft = np.abs(my_fft)


my_dft=np.abs(fft.DFT(data))

plt.figure(figsize=(8, 4))
plt.plot(freq_axis, my_dft)
plt.title("DFT of the Sine Wave")
plt.xlabel("Frequency (Cycles per unit time)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 4))
plt.plot(freq_axis, fft_result)
plt.title("FFT of the Sine Wave")
plt.xlabel("Frequency (Cycles per unit time)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()

if new_Length!=total_points:
    extra_points=new_Length-total_points
    extra_cyccles=extra_points/total_points
    freq_axis = np.fft.fftfreq(new_Length, d=1/points_per_cycle)
    
plt.figure(figsize=(8, 4))
plt.plot(freq_axis, my_fft)
plt.title("MINE")
plt.xlabel("Frequency (Cycles per unit time)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()