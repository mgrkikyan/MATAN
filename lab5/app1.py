import sympy
from sympy.abc import x
f = 1 / (x ** 2 + 2)
print(sympy.integrate(f, (x, 0, 1)))


# Интегральная сумма
import numpy as np

def f(x):
    return 1/(x**2 + 2)  # Пример функции, которую мы интегрируем

# Интегральная сумма 
def integral_sum(a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    sum = 0
    for i in range(n):
        sum += f(x[i]) * dx
    return sum

a = 0  # Нижний предел интегрирования
b = 1  # Верхний предел интегрирования
n = 7  # Количество отрезков разбиения

result = integral_sum(a, b, n)
print(result)