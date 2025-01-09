import chapter10module as c10m
import sympy as sp

print(f"********** 10.3题 **********")
# 定义变量
x = sp.Symbol("x")
a1 = sp.Symbol("a1")
l = sp.Symbol("l", positive=True)
# v = a1 * sp.sin(sp.pi * x / l)
v = a1 * x * (l - x)
E = sp.Symbol("E", positive=True)
I0 = sp.Symbol("I0", positive=True)
T = sp.Symbol("T", positive=True) # 本章默认杆件轴向压力为正
# x = 0时I1=0.4*I0,x=0.2*l时I1=I0
I1 = (3 * I0 / l) * x + 0.4 * I0
I2 = I0
# x = 0.8*l 时 I3 = I0, x = 1.0*l 时 I3 减少到 0.4 * I0
I3 = (-3 * I0 / l) * x + 3.4 * I0

# 计算杆件弯曲应变能
V1 = c10m.beamBendingEnergy(v, I1, 0, 0.2 * l, E)
V2 = c10m.beamBendingEnergy(v, I2, 0.2 * l, 0.8 * l, E)
V3 = c10m.beamBendingEnergy(v, I3, 0.8 * l, 1.0 * l, E)
V = V1 + V2 + V3
print(f"杆件弯曲应变能：{V}")

# 计算杆件力函数
U = 1/2 * sp.integrate(T*sp.diff(v,x)**2, (x, 0, l))
print(f"杆件力函数：{U}")

# 另总位能对系数求偏导等于零
PI = V - U
equation = sp.Eq(sp.diff(PI,a1),0)
T = sp.solve(equation,T)
print(f"杆件欧拉力：{T} N")