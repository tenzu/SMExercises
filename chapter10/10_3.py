import chapter10module as c10m
import sympy as sp

# 定义变量
x = sp.Symbol("x")
a1 = sp.Symbol("a1")
l = sp.Symbol("l")
# v = sp.Function('v')(x)
v = a1 * sp.sin(sp.pi * x / l)
E = sp.Symbol("E")
I = sp.Symbol("I")

V = (
    1
    / 2
    * sp.integrate(E * I * a1 * sp.diff(sp.sin(sp.pi * x / l), x, 2), (x, 0, 0.2 * l))
)
print(f"应变能：{V}")

print(f"testing 3")