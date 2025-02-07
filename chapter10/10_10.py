import chapter_10_module as c10m
import sympy as sp

print(f"********** 10.10题 **********")
a = 1.2
b = 0.7
t = sp.symbols("t", positive=True)
sigma_y = 240 * 1e6 # Pa
print(f"因为 a/b > 1，所以根据图10-30取 k = 4")
# 令 sigma_cr = sigma_y
eq = sp.Eq(4 * sp.pi**2 * c10m.cylindricalStiffness(t) / (b**2 * t), sigma_y)
sol = sp.solve(eq, t)
print(f"求解得到 t = {sol[0]*1e3:.2f} mm")
