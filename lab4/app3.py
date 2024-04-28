
import sympy
from sympy import sqrt
from sympy.abc import u, x

# Определение функции
f = (2 * u**2) / (sqrt(u**2 + 1))

# Вычисление интеграла
integral = sympy.integrate(f, u)

# Подстановка u = sqrt(x)
integral_x = integral.subs(u, sqrt(x))

print(integral_x)

