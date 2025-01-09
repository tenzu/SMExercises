import chapter10module as c10m
import sympy as sp

print(f"********** 10.5题 **********")
print(f"********** 使用能量法求解 **********")
# 定义变量
x = sp.Symbol("x")
a1 = sp.Symbol("a1")
l0 = sp.Symbol("l0", positive=True)  # 令l2的长度为l0
v = a1 * x * (l0 - x)
E = sp.Symbol("E", positive=True)
I0 = sp.Symbol("I0", positive=True)
T = sp.Symbol("T", positive=True)  # 本章默认杆件轴向压力为正
I1 = 8 * I0
I2 = I0
l1 = 2 * l0
l2 = l0

# 计算杆件应变能
V1 = c10m.beamBendingEnergy(v, I1, 0, l1, E)
V2 = c10m.beamBendingEnergy(v, I2, l1, l1 + l2, E)
V = V1 + V2
print(f"应变能：{V}")

# 计算杆件力函数
U = 1 / 2 * sp.integrate(T * sp.diff(v, x) ** 2, (x, 0, l1 + l2))
print(f"杆件力函数：{U}")

# 另总位能对系数求偏导等于零
PI = V - U
equation = sp.Eq(sp.diff(PI, a1), 0)
T = sp.solve(equation, T)
print(f"杆件欧拉力：{T} N") # 68/21*E*I/l0**2
