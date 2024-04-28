import sympy
from sympy.abc import x
f = x**2 / (9-x**2)
print(f.integrate(x))
