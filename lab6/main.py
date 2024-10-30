import numpy as np
import matplotlib.pyplot as plt

# Определение функции
def f(x, y):
    return np.sin(2*x) * np.cos(3*y - 1)

# Производные функции
def df_dx(x, y):
    return 2 * np.cos(2*x) * np.cos(3*y - 1)

def df_dy(x, y):
    return -3 * np.sin(2*x) * np.sin(3*y - 1)

# Создание сетки для построения линий уровня
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Отображение заданных точек
A = (0.9, 0)
B = (1, 1)
C = (-1.1, 0)
D = (0, -1.3)

# Значения функции в заданных точках
f_A = float(f(A[0], A[1]))
f_B = f(B[0], B[1])
f_C = f(C[0], C[1])
f_D = f(D[0], D[1])

levels = sorted([f_A, f_B, f_C, f_D])

# Построение линий уровня
plt.contour(X, Y, Z, levels=levels)
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')

plt.plot(A[0], A[1], 'ro')
plt.plot(B[0], B[1], 'go')
plt.plot(C[0], C[1], 'bo')
plt.plot(D[0], D[1], 'yo')

# Векторы градиентов в точках
grad_A = np.array([df_dx(A[0], A[1]), df_dy(A[0], A[1])])
grad_B = np.array([df_dx(B[0], B[1]), df_dy(B[0], B[1])])
grad_C = np.array([df_dx(C[0], C[1]), df_dy(C[0], C[1])])
grad_D = np.array([df_dx(D[0], D[1]), df_dy(D[0], D[1])])

scale = 2.0

# Увеличение длины стрелок векторов градиентов
plt.quiver(A[0], A[1], grad_A[0]*scale, grad_A[1]*scale, scale_units='xy', angles='xy', color='r')
plt.quiver(B[0], B[1], grad_B[0]*scale, grad_B[1]*scale, scale_units='xy', angles='xy', color='g')
plt.quiver(C[0], C[1], grad_C[0]*scale, grad_C[1]*scale, scale_units='xy', angles='xy', color='b')
plt.quiver(D[0], D[1], grad_D[0]*scale, grad_D[1]*scale, scale_units='xy', angles='xy', color='y')

# Добавление подписей к точкам на графике
plt.text(A[0], A[1], 'A', color='r', fontsize=20)
plt.text(B[0], B[1], 'B', color='g', fontsize=20)
plt.text(C[0], C[1], 'C', color='b', fontsize=20)
plt.text(D[0], D[1], 'D', color='y', fontsize=20)

plt.show()


