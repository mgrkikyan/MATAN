import sympy
from sympy.abc import x
f = sympy.sin(x) * ((sympy.cos(x) + 2)**2)
print(f.integrate(x))
