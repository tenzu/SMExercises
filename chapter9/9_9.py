import chapter_9_module as c9m
import sympy as sp

print(f"********** 9.9题 **********")

a, b = sp.symbols("a b", positive=True)
t = sp.symbols("t", positive=True)
x, y = sp.symbols("x y")
E_beam, I_beam = sp.symbols("E_beam I_beam", positive=True)
# 挠曲面函数仅取第一项
A11 = sp.symbols("A11", real=True)
w = A11 * sp.sin(sp.pi * x / a) * sp.sin(sp.pi * y / (4 * b))

print(f"---- 写出边界条件 ----")
print(
    f"x = 0 时：w = {w.subs(x,0)}， w' = {w.diff(x).subs(x,0)}， w'' = {w.diff(x,2).subs(x,0)}"
)
print(
    f"x = a 时：w = {w.subs(x,a)}， w' = {w.diff(x).subs(x,a)}， w'' = {w.diff(x,2).subs(x,a)}"
)
print(
    f"y = 0 时：w = {w.subs(y,0)}， w' = {w.diff(y).subs(y,0)}， w'' = {w.diff(y,2).subs(y,0)}"
)
print(
    f"y = a 时：w = {w.subs(y,b)}， w' = {w.diff(y).subs(y,b)}， w'' = {w.diff(y,2).subs(y,b)}"
)

# 计算总位能
print(f"---- 计算应变能 ----")
V = c9m.plateStrainEnergy(w, t, 0, a, 0, b)
print(f"应变能 = {V}")  # 不满足格林公式使用条件，简化版应变能公式无法使用，死循环了
