from sympy import symbols, diff, atan, expand

# Определение символьных переменных
x, y = symbols("x y")

# Определение функции
f = x * atan(x + y)

# Вычисление частных производных первого порядка
df_dx = diff(f, x)  # частная производная по x
df_dy = diff(f, y)  # частная производная по y

# Вычисление частных производных второго порядка
d2f_dx2 = diff(df_dx, x)  # вторая производная по x
d2f_dy2 = diff(df_dy, y)  # вторая производная по y
d2f_dxdy = diff(df_dx, y)  # смешанная производная

# Точка m=(0,0)
args = [(x, 0), (y, 0)]  # аргументы для подстановки, x = 0, y = 0

# Вычисление первого дифференциала
df = df_dx.subs(args)*x + df_dy.subs(args)*y

# Вычисление второго дифференциала
d2f = (1/2) * (d2f_dx2.subs(args)*x**2 + 2*d2f_dxdy.subs(args)*x*y + d2f_dy2.subs(args)*y**2)

# Вычисление многочлена Тейлора 2-й степени
Taylor_polynomial_2 = expand(f.subs(args) + df + d2f)

# Вывод результатов
print("Многочлен Тейлора 1-й степени:")
print("P1(x, y) = ", expand(f.subs(args) + df))
print("Многочлен Тейлора 2-й степени:")
print("P2(x, y) = ", Taylor_polynomial_2)

