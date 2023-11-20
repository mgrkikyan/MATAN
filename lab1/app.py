#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math
from sympy import *


n = Symbol("n")


def sequence(n):
    return (n ** 0.5 + 7) / (2 * n ** 0.5 + 1)


def plot_points(m):
    x = np.arange(1, m + 1)
    y = sequence(x)

    # (k, 0) - blue colour
    plt.plot(x, np.zeros_like(x), 'bo', label='$(k, 0)$')
    # (0, x_k) - green color
    plt.plot(np.zeros_like(x), y, 'go', label='$(0, x_k)$')
    # (k, x_k) - red color
    plt.plot(x, y, 'ro', label='$(k, x_k)$')

    lim_value = limit((n ** 0.5 + 7) / (2 * n ** 0.5 + 1), n, oo)
    plt.plot(0, lim_value, 'o', color='orange', label='$(lim)$')  # Точка предела

    plt.xlabel('$k$')
    plt.ylabel('$x_k$')
    plt.legend()
    plt.grid()
    plt.show()


m = 20  # number of points
plot_points(m)
a = limit((n ** 0.5 + 7) / (2 * n ** 0.5 + 1), n, oo)
print(a)