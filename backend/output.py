import numpy as np
import matplotlib.pyplot as plt

# Time in hours
time = np.linspace(0, 72, 200)

# Heat of hydration model for Alite (simplified exponential model)
ultimate_heat = 500  # J/g (typical for C3S)
rate_constant = 0.1

heat_release = ultimate_heat * (1 - np.exp(-rate_constant * time))

# Plot
plt.plot(time, heat_release)
plt.xlabel("Time (hours)")
plt.ylabel("Heat Release (J/g)")
plt.title("Heat of Hydration of Alite (C3S)")
plt.grid(True)
plt.show()
