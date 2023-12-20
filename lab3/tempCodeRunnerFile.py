import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) * np.log(x)

def tangent_line(x, x0):
    return f(x0) + (np.cos(x0) * np.log(x0) + np.sin(x0) / x0) * (x - x0)

def normal_line(x, x0):
    return f(x0) - (1 / (np.cos(x0) * np.log(x0) + np.sin(x0) / x0)) * (x - x0)

x = np.linspace(0, 22, 1000)
y = f(x)
x0 = 1
y_tangent = tangent_line(x, x0)
y_normal = normal_line(x, x0)

plt.plot(x, y, label='Функция')
plt.plot(x, y_tangent, label='Касательная')
plt.plot(x, y_normal, label='Нормаль', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 22)
plt.ylim(-15, 7)
plt.title('График функции')
plt.legend()
plt.show()
