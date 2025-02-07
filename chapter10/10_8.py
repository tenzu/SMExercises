import chapter_10_module as c10m
import sympy as sp

print(f"********** 10.8题 **********")
L = 12.5
B = 5
l = 2.5
b = 0.5
I = 5000 * 1e-8
i = 1250 * 1e-8
A = 64.05 * 1e-4
sigma_y = 240  # MPa
E = 2.1e11  # Pa
v1 = 0
print(f"自由支持端：v1 = {v1}")
alpha = 0.5 * B / (E * I)
v2 = 1 / (1 + (2 * alpha * E * I) / B)
print(f"弹性固定端：v2 = {v2}")
miu = 3.36
print(f"查图可知：miu = {miu}")

# 计算横梁刚度系数K
K = miu**4 * E * I * b / B**4
print(f"横梁刚度系数K为\t{K:.2f} N/m")
# 计算对应的单跨梁欧拉应力
sigma_0 = c10m.eularForceSingleBeam(i, l, E) / A * 1e-6
print(f"对应的单跨梁欧拉应力sigma_0为\t{sigma_0:.2f} MPa")

# 计算连续梁跨数
n = L / l
print(f"连续梁跨数 n 为\t{n}")
Xj_max = 0.364
print(f"n = 5时，临界刚度对应的 Xj_max 为\t{Xj_max:.3f}")
# 计算临界刚度
K_cr = c10m.K_cr(1.0, Xj_max, i, l, E)
print(f"临界刚度 K_cr 为\t{K_cr:.2f} N/m")
print(f"此处可知 K < K_cr")
# 计算Xj
Xj = I*(miu/sp.pi)**4*(l/B)**3*b/B*1/i
print(f"Xj = {Xj:.3f}")
lamda = 0.540
print(f"根据Xj查图可知 lamda = {lamda}")
sigma_E = lamda * sigma_0
print(f"根据lamda计算sigma_E = {sigma_E:.2f} MPa")
print(f"因为 sigma_E > sigma_y，所以需要进行非弹性修正")
phai_Xj = I*(miu/sp.pi)**4*(l/B)**3*b/B/i
print(f"phai*Xj = {phai_Xj:.3f}")
print(f"根据附录F的表格插值得到：sigma_cr = 212 MPa")