import chapter10module as c10m
import sympy as sp

# 定义变量
x = sp.Symbol("x")
a1 = sp.Symbol("a1")
l = sp.Symbol("l", positive=True)
# v = sp.Function('v')(x)
v = a1 * sp.sin(sp.pi * x / l)
E = sp.Symbol("E", positive=True)
I = sp.Symbol("I", positive=True)

# 计算杆件弯曲应变能
V = c10m.beamBendingEnergy(v, I, 0, 0.2 * l, E)
print(f"应变能：{V}")
