import matplotlib.pyplot as plt
import numpy as np

years = [2006 + x for x in range(16)]
weigth = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
          82, 82, 83, 81, 80, 79]

plt.plot(years, weigth, c="green", lw=3, linestyle="-")
plt.show()

