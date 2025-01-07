import chapter10module as c10m
import sympy as sp

# 定义变量
x = sp.Symbol("x")
a1 = sp.Symbol("a1")
l = sp.Symbol("l", positive=True)
# v = a1 * sp.sin(sp.pi * x / l)
v = a1 * x * (l - x)
E = sp.Symbol("E", positive=True)
I0 = sp.Symbol("I0", positive=True)
# x = 0时I1=0.4*I0,x=0.2*l时I1=I0
I1 = (3 * I0 / l) * x + 0.4 * I0
I2 = I0
# x = 0.8*l 时 I3 = I0, x = 1.0*l 时 I3 减少到 0.4 * I0
I3 = (-3 * I0 / l) * x + 3.4 * I0

# 计算杆件弯曲应变能
V1 = c10m.beamBendingEnergy(v, I1, 0, 0.2 * l, E)
V2 = c10m.beamBendingEnergy(v, I2, 0.2 * l, 0.8 * l, E)
V3 = c10m.beamBendingEnergy(v, I3, 0.8 * l, 1.0 * l, E)
print(f"杆件弯曲应变能：{V1+V2+V3}")