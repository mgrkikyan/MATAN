import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(2*x) * np.cos(3*y - 1)

# Создание сетки
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Вычисление частных производных в заданных точках
A = (0.9, 0)
B = (1, 1)
C = (-1.1, 0)
D = (0, -1.3)

f_x_A = 2*np.cos(2*A[0])*np.cos(3*A[1] - 1)
f_y_A = -3*np.sin(2*A[0])*np.sin(3*A[1] - 1)

f_x_B = 2*np.cos(2*B[0])*np.cos(3*B[1] - 1)
f_y_B = -3*np.sin(2*B[0])*np.sin(3*B[1] - 1)

f_x_C = 2*np.cos(2*C[0])*np.cos(3*C[1] - 1)
f_y_C = -3*np.sin(2*C[0])*np.sin(3*C[1] - 1)

f_x_D = 2*np.cos(2*D[0])*np.cos(3*D[1] - 1)
f_y_D = -3*np.sin(2*D[0])*np.sin(3*D[1] - 1)

# Построение графика
plt.figure(figsize=(9, 9))
levels = sorted([f(A[0], A[1]), f(B[0], B[1]), f(C[0], C[1]), f(D[0], D[1])])
plt.contour(X, Y, f(X, Y), levels=levels, colors='k')
plt.quiver(A[0], A[1], f_x_A, f_y_A, color='r', scale=40)
plt.quiver(B[0], B[1], f_x_B, f_y_B, color='r', scale=40)
plt.quiver(C[0], C[1], f_x_C, f_y_C, color='r', scale=40)
plt.quiver(D[0], D[1], f_x_D, f_y_D, color='r', scale=5)
plt.plot(A[0], A[1], 'ro', markersize=1.5, linewidth=1)
plt.plot(B[0], B[1], 'ro', markersize=1.5, linewidth=1)
plt.plot(C[0], C[1], 'ro', markersize=1.5, linewidth=1)
plt.plot(D[0], D[1], 'ro', markersize=1.5, linewidth=1)
plt.text(A[0], A[1], 'A', fontsize=20)
plt.text(B[0], B[1], 'B', fontsize=20)
plt.text(C[0], C[1], 'C', fontsize=20)
plt.text(D[0], D[1], 'D', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

