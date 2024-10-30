# import numpy as np
# import matplotlib.pyplot as plt

# def f(x, y):
#     return x**2 + 2*y*np.sin(x)

# # Создание сетки
# x = np.linspace(-2, 2, 100)
# y = np.linspace(-2, 2, 100)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# # Вычисление частных производных в заданных точках
# A = (0.9, 0)
# B = (1, 1)
# C = (-1.1, 0)
# D = (0, -1.3)

# f_x_A = 2*A[0]+2*A[1]*np.cos(A[0])
# f_y_A = 2*np.sin(A[0])

# f_x_B = 2*B[0]+2*B[1]*np.cos(B[0])
# f_y_B = 2*np.sin(B[0])

# f_x_C = 2*C[0]+2*C[1]*np.cos(C[0])
# f_y_C = 2*np.sin(C[0])

# f_x_D = 2*D[0]+2*D[1]*np.cos(D[0])
# f_y_D = 2*np.sin(D[0])

# # Построение графика
# plt.figure(figsize=(9, 9))
# levels = sorted([f(A[0], A[1]), f(B[0], B[1]), f(C[0], C[1]), f(D[0], D[1])])
# plt.contour(X, Y, Z, 20, cmap='viridis')
# # plt.quiver(A[0], A[1], f_x_A, f_y_A, color='r', scale=25)
# # plt.quiver(B[0], B[1], f_x_B, f_y_B, color='r', scale=25)
# # plt.quiver(C[0], C[1], f_x_C, f_y_C, color='r', scale=25)
# # plt.quiver(D[0], D[1], f_x_D, f_y_D, color='r', scale=25)
# plt.plot(A[0], A[1], 'ro', markersize=1, linewidth=1)
# plt.plot(B[0], B[1], 'ro', markersize=1, linewidth=1)
# plt.plot(C[0], C[1], 'ro', markersize=1, linewidth=1)
# plt.plot(D[0], D[1], 'ro', markersize=1, linewidth=1)
# plt.text(A[0], A[1], 'A', fontsize=20)
# plt.text(B[0], B[1], 'B', fontsize=20)
# plt.text(C[0], C[1], 'C', fontsize=20)
# plt.text(D[0], D[1], 'D', fontsize=20)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + 2*y*np.sin(x)

# Создание сетки
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Вычисление частных производных в заданных точках
A = (0.9, 0)
B = (1, 1)
C = (-1.1, 0)
D = (0, -1.3)

f_x_A = 2*A[0]+2*A[1]*np.cos(A[0])
f_y_A = 2*np.sin(A[0])

f_x_B = 2*B[0]+2*B[1]*np.cos(B[0])
f_y_B = 2*np.sin(B[0])

f_x_C = 2*C[0]+2*C[1]*np.cos(C[0])
f_y_C = 2*np.sin(C[0])

f_x_D = 2*D[0]+2*D[1]*np.cos(D[0])
f_y_D = 2*np.sin(D[0])

# Построение графика
plt.figure(figsize=(9, 9))
levels = sorted([f(A[0], A[1]), f(B[0], B[1]), f(C[0], C[1]), f(D[0], D[1])])
plt.contour(X, Y, f(X, Y), levels=levels, colors='k')
plt.quiver(A[0], A[1], f_x_A, f_y_A, color='r', scale=25)
plt.quiver(B[0], B[1], f_x_B, f_y_B, color='r', scale=25)
plt.quiver(C[0], C[1], f_x_C, f_y_C, color='r', scale=25)
plt.quiver(D[0], D[1], f_x_D, f_y_D, color='r', scale=25)
plt.plot(A[0], A[1], 'ro', markersize=1, linewidth=1)
plt.plot(B[0], B[1], 'ro', markersize=1, linewidth=1)
plt.plot(C[0], C[1], 'ro', markersize=1, linewidth=1)
plt.plot(D[0], D[1], 'ro', markersize=1, linewidth=1)
plt.text(A[0], A[1], 'A', fontsize=20)
plt.text(B[0], B[1], 'B', fontsize=20)
plt.text(C[0], C[1], 'C', fontsize=20)
plt.text(D[0], D[1], 'D', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

