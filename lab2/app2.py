#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from math import * 
from sympy import *

# определение символа x
x = Symbol('x')

# Определение функции
f = (1 + 7 * x) ** (3 * cot(x))



# Вычисление предела
lim = limit(f, x, 0)
print("Значение предела = ", lim)