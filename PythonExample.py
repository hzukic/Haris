import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_csv('data.txt')

print(data)

data.plot()

x = np.linspace(-2,4,20)
y = x**3 - 2*x**2 - 3*x


plt.plot(x,y, marker='o', linestyle= '--', color='green')
plt.grid()
plt.show()
