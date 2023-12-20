import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

x = smp.Symbol('x')

# Объявляем функцию
def f(x):
    return (1 + 7 * x) ** (3 * smp.cot(x))


def plot_points():

    x_values1 = np.linspace(0.0000000000001, 0.1, 100)  
    y_values1 = [f(n) for n in x_values1]

    # Строим график
    # plt.plot(x_values, y_values, label='f(x)')
    plt.plot(x_values1, y_values1, label='f(x)')
    
    # Вычисление предела
    lim = smp.limit(f(x), x, 0)
    
    # Изображаем предел точкой
    plt.plot(lim, 'o', color='orange', label='Limit')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-0.1, 0.1)
    plt.title('График функции')
    plt.legend()
    plt.grid()
    plt.show()

plot_points()


# Определение функции
f = (1 + 7 * x) ** (3 * smp.cot(x))

# Вычисление предела
lim = smp.limit(f, x, 0)
print(f'Limit: {lim}')


# Определение функции
f = (1 + 7 * x) ** (3 * smp.cot(x))

# Вычисление предела
lim = smp.limit(f, x, 0)
print(f'Limit: {lim}')