import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

x = smp.symbols('x')

# Объявляем функцию
def f(x):
    return (1 + 7 * x) * (3 * smp.cot(x))

def plot_points():
    x_values = np.linspace(0.1, 10, 400)  # начинаем с 0.1, чтобы избежать деления на ноль
    y_values = [f(n) for n in x_values]

    # Строим график
    plt.plot(x_values, y_values, label='f(x)')
    
    # Вычисление предела
    lim = smp.limit(f(x), x, 0)
    
    # Изображаем предел точкой
    plt.plot(lim, 'o', color='orange', label='Limit')
    
    plt.xlabel('x')
    plt.ylabel('y')
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
