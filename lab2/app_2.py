#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

# Определение функции
def f(x):
    return np.log(np.sin(x))

# Создание массива значений x
x = np.linspace(0, np.pi, 300)

# Вычисление значений y для каждого значения x
y = f(x)

# Построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid()
plt.show()

