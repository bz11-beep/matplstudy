
import matplotlib.pyplot as plt
import numpy as np

lang = ["C++", "C#", "Python", "Jave", "Go"]
votes = [50, 24, 14, 10, 17]
explode = [0, 0, 0, 0.2, 0]

plt.pie(votes, labels=lang, autopct='%.2f%%', explode=explode)
plt.show()

