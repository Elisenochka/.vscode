import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100) # Create a list of evenly-spased numbers over
plt.plot(x, np.sin(x))
plt.show