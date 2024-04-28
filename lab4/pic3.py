import numpy as np
import math
import matplotlib.pyplot as plt

# Определение функций
def f(x):
    return np.sqrt(x / (x + 1))

def f1(x):
    y = np.sqrt(x) * np.sqrt(x + 1) - np.log(np.sqrt(x) + np.sqrt(x + 1))
    return y

def f2(x):
    y = np.sqrt(x) * np.sqrt(x + 1) - np.log(np.sqrt(x) + np.sqrt(x + 1)) + 2
    return y

def f3(x):
    y = np.sqrt(x) * np.sqrt(x + 1) - np.log(np.sqrt(x) + np.sqrt(x + 1)) - 2 
    return y

# Создание вектора значений x
x = np.linspace(-10, 10, 400)

# Построение графика
plt.plot(x, f(x), color='blue')
plt.plot(x, f1(x), color='green')
plt.plot(x, f2(x), color='green')
plt.plot(x, f3(x), color='green')

# Добавление сетки
plt.grid(True)

# Настройка масштаба по осям x и y
plt.xlim(0, 10)
plt.ylim(-2, 6)  # ограничение по оси y до ±6

# Настройка внешнего вида графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции и кривые')
plt.legend()

# Вывод графика на экран
plt.show()
