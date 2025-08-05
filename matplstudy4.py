
import matplotlib.pyplot as plt
import numpy as np

age = np.random.normal(20, 1.5, 1000)

plt.hist(age, bins='auto', cumulative=True)
plt.show()

