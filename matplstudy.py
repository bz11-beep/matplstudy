import matplotlib.pyplot as plt
import numpy as np

Xdata = np.random.random(50) * 100
Ydata = np.random.random(50) * 100

plt.scatter(Xdata, Ydata, c= "green", marker = "*", s = 50)
plt.show()

