import numpy as np
import matplotlib.pyplot as plt

# Функция под интегралом
def f(x):
    return 1 / (x ** 2 + 2)

# Границы интегрирования и количество разбиений
a = 0
b = 1
n = 7

# Шаг разбиения
dx = (b - a) / n

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Генерируем точки для графика функции
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)
ax.plot(x_vals, y_vals, label='f(x)', linewidth=2.5)

# Добавляем прямоугольники
for k in range(1, n+1):
    # Середина каждого отрезка
    x_k = a + (k - 0.5) * dx
    # Значение функции в середине отрезка
    f_x_k = f(x_k)
    # Цвет прямоугольника в зависимости от знака f(x_k)
    color = 'blue' if f_x_k < 0 else '#F39C12'
    # Добавляем прямоугольник
    ax.add_patch(plt.Rectangle((x_k - dx/2, 0), dx, f_x_k, color=color, alpha=0.5))

# Настройки графика
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('График')
ax.legend()

# Показываем график
plt.show()