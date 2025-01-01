import sympy as sp

# 定义变量
x, y = sp.symbols("x y")
# 定义 w 为 x,y 的函数
w = sp.Function("w")(x, y)
D = sp.symbols("D")
q = sp.Function("q")(x, y)
A = sp.symbols("A")
m, n = sp.symbols("m n")
a, b = sp.symbols("a b")

# 边界条件
print(f"边界条件:")
print(f"x = 0 和 a 时: w=0, {w.diff(x, 2)}=0")
print(f"y = 0 和 b 时: w=0, {w.diff(y, 2)}=0")

# 矩形板弯曲微分方程
eq1 = D * (w.diff(x, 4) + 2 * w.diff(x, 2, y, 2) + w.diff(y, 4)) - q
print(f"矩形板弯曲微分方程: \n{eq1}")

# 定义挠曲面函数
w = sp.series(A * sp.sin(m * sp.pi * x / a) * sp.sin(n * sp.pi * y / b), x, y).removeO()
print(f"挠曲面函数: \n{w}")
