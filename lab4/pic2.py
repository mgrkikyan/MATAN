import numpy as np
import matplotlib.pyplot as plt

# Определение функций
def f(x):
    return np.sin(x) * (np.cos(x) + 2)**2

def f1(x):
    return (-np.cos(x)**3)/3 - 2*np.cos(x)**2 - 4*np.cos(x)

def f2(x):
    return (-np.cos(x)**3)/3 - 2*np.cos(x)**2 - 4*np.cos(x) + 2

def f3(x):
    return (-np.cos(x)**3)/3 - 2*np.cos(x)**2 - 4*np.cos(x) - 2

# Создание вектора значений x
x = np.linspace(-10, 10, 400)

# Построение графика
plt.plot(x, f(x), color='blue')
plt.plot(x, f1(x), color='green')
plt.plot(x, f2(x), color='green')
plt.plot(x, f3(x), color='green')

# Добавление сетки
plt.grid(True)

# Настройка масштаба по оси x
plt.xlim(-10, 10)

# Настройка внешнего вида графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции и кривые')
plt.legend()

# Вывод графика на экран
plt.show()

