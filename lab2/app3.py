import matplotlib.pyplot as plt
import numpy as np
from math import * 
from sympy import *

# Определение символа x
x = Symbol ('x')

# Объявляем функцию
def f(x):
    return x * np.sin(1 / x)

# Создание массива значений x около точки разрыва
x0 = np.linspace(-0.125 * np.pi, 0.125 * np.pi, 100)
y0 = f(x0)

# Построение графика
plt.plot(x0, y0)
plt.axvline(x=0, color='red', linestyle='--', label='x=0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x) = x * sin(1/x)')
plt.legend()
plt.grid()
plt.show()


# определение символьного выражения, соответствующего функции x*sin(1/x)
f = x * sin(1 / x)

# вычисление предела слева в нуле
lim_left = limit(f, x, 0, dir='-')


# по умолчанию вычисляется предел справа
lim_right = limit(f, x, 0)

print(f'Предел слева в точке x=0: {lim_left}')
print(f'Предел справа в точке x=0: {lim_right}')