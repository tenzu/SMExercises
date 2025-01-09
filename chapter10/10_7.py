import chapter10module as c10m
import sympy as sp

print(f"********** 10.7题 **********")
longitudinal_A = 20 * 1e-4
longitudinal_I = 1000 * 1e-8
longitudinal_L = 5
beam_I = 15000 * 1e-8
beam_L = 6

print(f"求解（a)：")
# 使用单位力法计算悬臂梁刚度系数
K = c10m.cantileverStiffness(beam_I, beam_L)
print(f"悬臂梁刚度系数K = {K:.2f} N/m = {K * 1e-3:.2f} kN/m")  # 1250000/3

print(f"求解（b）：")
# 查附录G
print(f"查附录G得3跨梁弹性制作达到临界刚度时lamda = 1.0")
lamda = 1.0
print(f"此时Xj_max = 0.302")
Xj_max = 0.302
# 对应的单跨梁欧拉应力
sigma_0 = c10m.eularForceSingleBeam(longitudinal_I, longitudinal_L) / longitudinal_A
print(f"对应的单跨梁欧拉应力sigma_0 = {sigma_0:.2f} Pa = {sigma_0 * 1e-6:.3f} MPa")

# 定义变量
sigma_cr = sp.Symbol("sigma_cr")
phai = sp.Symbol("phai")
sigma_y = 400  # MPa
# 计算lamda
# 列出方程
eq1 = sp.Eq(lamda, sigma_cr / (phai * sigma_0))
eq2 = sp.Eq(phai, (4 * (sigma_y - sigma_cr) * sigma_cr) / sigma_y**2)
# 解方程
solution = sp.solve([eq1, eq2], [sigma_cr, phai])
sigma_cr = solution[0][0]
phai = solution[0][1]
print(f"sigma_cr = {sigma_cr:.2f} MPa")
