import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def plot_curve():
    theta = np.linspace(np.pi/2, np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'b-')
    plt.plot([0, -1], [0, 0], 'ro')
    plt.text(0.1, 0.9, 'a(0,1)', fontsize=12)
    plt.text(-1.1, 0.1, 'b(-1,0)', fontsize=12)
    plt.axhline(y=0, color='k', linestyle='--')
    plt.axvline(x=0, color='k', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Дуга окружности x²+y²=1 от a(0,1) до b(-1,0)')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def calculate_integral():
    t = sp.Symbol('t')
    x = sp.cos(t)
    y = sp.sin(t)
    dx = sp.diff(x, t)
    dy = sp.diff(y, t)

    integrand = x * dy + (y + 1) * dx
    integral = sp.integrate(integrand, (t, sp.pi/2, sp.pi))

    print("Аналитическое решение:")
    print(integral)
    print(f"Численное значение: {float(integral)}")


if __name__ == "__main__":
    print("1. Построение кривой:")
    plot_curve()
    
    print("\n2. Параметрическое представление кривой:")
    print("x = cos(t)")
    print("y = sin(t)")
    print("где t изменяется от π/2 до π")
    
    print("\n3. Вычисление интеграла:")
    calculate_integral()
    