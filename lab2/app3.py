#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from math import * 
from sympy import *

# определение символа x
x = Symbol ('x')

# определение символьного выражения, соответствующего функции x*sin(1/x)

f = x * sin(1 / x)

# вычисление предела слева в нуле
lim_left = limit(f, x, 0, dir='-')


# по умолчанию вычисляется предел справа
lim_right = limit(f, x, 0)


print(f'Предел слева в точке x=0: {lim_left}')
print(f'Предел справа в точке x=0: {lim_right}')