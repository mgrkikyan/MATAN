import numpy as np
import matplotlib.pyplot as plt

# Определение функци1
def f(x):
    return x**2 / (9 - x**2)

def f1(x):
    return -x - 3 * np.log(x - 3) / 2 + 3 * np.log(x + 3) / 2 - 2

def f2(x):
    return -x - 3 * np.log(x - 3) / 2 + 3 * np.log(x + 3) / 2 + 2

def f3(x):
    return -x - 3 * np.log(x - 3) / 2 + 3 * np.log(x + 3) / 2

# Создание вектора значений x
x = np.linspace(-10, 10, 400)

# Построение графика и кривых
plt.plot(x, f(x), color='blue')
plt.plot(x, f1(x), color='green')
plt.plot(x, f2(x), color='green')
plt.plot(x, f3(x), color='green')

# Добавление сетки
plt.grid(True)

# Настройка масштаба графика
plt.ylim(-10, 10)
plt.xlim(3.1, 10)

# Настройка внешнего вида графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции f(x) и кривые')
plt.legend()

# Вывод графика на экран
plt.show()
