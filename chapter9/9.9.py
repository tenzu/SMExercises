import chapter9module as c9m
import sympy as sp

print(f"********** 9.9题 **********")

a,b = sp.symbols('a b', positive=True)
x, y = sp.symbols('x y')
E_beam, I_beam = sp.symbols('E_beam I_beam', positive=True)
# 挠曲面函数仅取第一项
A11 = sp.symbols('A11', real=True)
w = A11* sp.sin(sp.pi*x/a)*sp.sin(sp.pi*y/(4*b))

print(f"---- 写出边界条件 ----")
