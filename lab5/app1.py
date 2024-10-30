import sympy
from sympy.abc import x
import numpy as np
f = 1 / (x ** 2 + 2)
integral = sympy.integrate(f, (x, 0, 1))
num_val = integral.evalf()
print(integral)
print(f"Приближенное значение: {num_val}")

# Интегральная сумма
def f(x):
    return 1/(x**2 + 2)  

import numpy as np

def f(x):
    return 1/(x**2 + 2)

a = 0
b = 1
n = 7

dx = (b - a) / n
x_points = [a + dx * (k + 0.5) for k in range(n)]

sigma = sum(f(x) * dx for x in x_points)
print(f"Интегральная сумма: {sigma}")

