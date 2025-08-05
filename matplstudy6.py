
import matplotlib.pyplot as plt
import numpy as np

year = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
income = [55, 56, 62, 61, 72, 72, 73, 75]

income_ticks = list(range(50, 81, 2))

plt.plot(year, income, color='blue')
plt.title('Income of John')

plt.xlabel('Year')
plt.ylabel('Income In USD')

plt.show()

