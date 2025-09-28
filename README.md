# matplstudy
matplstudy

## code
**모든 값은 임의로 설정한 값들이므로, 실제 데이터와 무관하다. 말그대로 내가 학습할려고 만든 데이터다.**

### matplstudy.py
```python
import matplotlib.pyplot as plt
import numpy as np

Xdata = np.random.random(50) * 100
Ydata = np.random.random(50) * 100

plt.scatter(Xdata, Ydata, c= "green", marker = "*", s = 50)
plt.show()

```
<img width="640" height="480" alt="malp1" src="https://github.com/user-attachments/assets/5a3c6828-94a4-4319-8e3d-e2ace683babd" />


### matplstudy2.py
```python
import matplotlib.pyplot as plt
import numpy as np

years = [2006 + x for x in range(16)]
weigth = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
          82, 82, 83, 81, 80, 79]

plt.plot(years, weigth, c="green", lw=3, linestyle="-")
plt.show()
```
<img width="640" height="480" alt="malp2" src="https://github.com/user-attachments/assets/19b2e6f0-42dd-4fe7-bbf5-b0de17399612" />


### matplstudy3.py
```python
import matplotlib.pyplot as plt
import numpy as np

x = ["C++", "C#", "Python", "Jave", "Go"]

y = [20, 50, 140, 100, 45]

plt.bar(x, y, color='green', align='edge', width=0.5, edgecolor='red', lw=6)
plt.show()
```
<img width="640" height="480" alt="malp3" src="https://github.com/user-attachments/assets/10cfb05c-73cf-4b89-a8ed-ec69423afa5f" />


### matplstudy4.py
```python
import matplotlib.pyplot as plt
import numpy as np

age = np.random.normal(20, 1.5, 1000)

plt.hist(age, bins='auto', cumulative=True)
plt.show()
```
<img width="640" height="480" alt="malp4" src="https://github.com/user-attachments/assets/08183ee1-e741-45df-9b99-3726222bb547" />


### matplstudy5.py
```python
import matplotlib.pyplot as plt
import numpy as np

lang = ["C++", "C#", "Python", "Jave", "Go"]
votes = [50, 24, 14, 10, 17]
explode = [0, 0, 0, 0.2, 0]

plt.pie(votes, labels=lang, autopct='%.2f%%', explode=explode)
plt.show()
```
<img width="640" height="480" alt="malp5" src="https://github.com/user-attachments/assets/31e47b66-1c56-4a51-9980-8b53bc1f7a4c" />


### matplstudy6.py
```python
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
```
<img width="640" height="480" alt="malp6" src="https://github.com/user-attachments/assets/f58707b6-fb6d-4730-b256-f6ec5eaaa11e" />


### matplstudy7.py
```python
import matplotlib.pyplot as plt
import numpy as np

stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [98, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 95]

plt.plot(stock_a, label='A')
plt.plot(stock_b, label='B')
plt.plot(stock_c, label='C')

plt.legend(loc='lower right')
plt.show()
```
<img width="640" height="480" alt="malp7" src="https://github.com/user-attachments/assets/0f7876ef-6c62-42a5-933d-9f7d3703f783" />


### matplstudy8.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('dark_background')

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=None)
plt.legend(labels=people)

plt.show()

```
<img width="640" height="480" alt="malp8" src="https://github.com/user-attachments/assets/efccb270-fab9-4058-9183-83e33d9270e8" />


### matplstudy9.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.plot(x2, y2)

plt.show()
```
<img width="640" height="480" alt="malp9" src="https://github.com/user-attachments/assets/7739cb46-752e-4a1e-853c-1460776c7b99" />


### matplstudy10.py
```python
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
```
<img width="1920" height="1440" alt="malp10" src="https://github.com/user-attachments/assets/2e80d84f-60d9-4f29-a15b-55bac5170540" />


### matplstudy11.py
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

ax = plt.axes(projection='3d')

x = np.arange(0, 50, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.scatter(x,y,z)
ax.set_title("3D Plot")

plt.show()
```
<img width="640" height="480" alt="malp11" src="https://github.com/user-attachments/assets/7588aaf2-8161-4b56-8c5d-5f4ceb41a8aa" />


### matplstudy12.py
```python
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
```
<img width="640" height="480" alt="malp12" src="https://github.com/user-attachments/assets/2c6a7b57-d994-417d-90b1-19cdd80df49c" />

I studied with this YouTube video(NeuralNine - Matplotlib Full Python Course - Data Science Fundamentals)
