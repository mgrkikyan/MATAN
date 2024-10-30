import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (x * (np.log(x) ** 2 + 2))

# Границы интегрирования и количество разбиений
a = 0.1
b = 1
n = 7

x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

# Шаг разбиения
dx = (b - a) / n

plt.plot(x_vals, y_vals)  # Добавляем график функции
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

for k in range(1, n+1):
    x_k = a + (k - 0.5) * dx
    f_x_k = f(x_k)
    color = 'blue' if f_x_k < 0 else '#F39C12'
    rect = plt.Rectangle((x_k - dx/2, 0), dx, f_x_k, color=color, alpha=0.5)
    plt.gca().add_patch(rect)

plt.show()  # Отображаем график с прямоугольниками