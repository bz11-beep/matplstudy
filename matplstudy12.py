
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

ax = plt.axes(projection='3d')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# ax.plot_surface(X,Y,Z)
ax.plot_surface(X,Y,Z, cmap="Spectral")
ax.set_title("3D Plot")

plt.show()