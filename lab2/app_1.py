#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *

# Определение функции
def f(x):
    return sqrt(5 + 4 * x - x ** 2)

# Создание массива значений x
x = np.linspace(-1, 5, 200)

# Вычисление значений y для каждого значения x
y = []
for i in x:
    y.append(f(i))

# Построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid()
plt.show()

