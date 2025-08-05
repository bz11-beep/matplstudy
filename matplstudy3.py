
import matplotlib.pyplot as plt
import numpy as np

x = ["C++", "C#", "Python", "Jave", "Go"]

y = [20, 50, 140, 100, 45]

plt.bar(x, y, color='green', align='edge', width=0.5, edgecolor='red', lw=6)
plt.show()

