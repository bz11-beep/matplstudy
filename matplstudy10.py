
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

x = np.arange(100)

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(x, np.sin(x))
ax[0, 0].set_title('Sine Wave')

ax[0, 1].plot(x, np.cos(x))
ax[0, 1].set_title('Cosine Wave')

ax[1, 0].plot(x, np.random.random(100))
ax[1, 0].set_title('Random Function')

ax[1, 1].plot(x, np.log(x + 1))
ax[1, 1].set_title('Log Function')
ax[1, 1].set_xlabel('x')

fig.suptitle('Four Plots')

plt.tight_layout()
plt.savefig('plot.png', dpi = 300)
