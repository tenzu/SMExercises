import chapter9module as c9m

print(f"********** 9.8题 **********\n")

print(f"---- 套公式求解 ----")
t = 1 * 1e-2
q = 5 * 1e4
a = 40 * 1e-2  # 板条梁跨长
b = 150 * 1e-2
# 查表得以下系数
k1 = 0.1356
k2 = 0.0397
k3 = 0.1203
k4 = 0.1249
# 按公式计算板的重点挠度
w_eq = k1 * q * a**4 / (c9m.youngsModulus * t**3)
print(f"根据公式计算出板的最大挠度为{w_eq:.3f} m = {w_eq*1000:.4f} mm\n")
# 按公式计算板的最大弯矩
M_eq = -k4 * q * a**2
print(f"根据公式计算出板的最大弯矩为{M_eq:.3f} N*m\n")
# 根据弯矩计算应力
sigma_eq = c9m.bendingNormalStress(M_eq, t)
print(f"根据弯矩计算出板的应力为{abs(sigma_eq * 1e-6):.3f} MPa\n")

print(f"---- 使用板条梁模型求解 ----")
# 校验是否需要考虑弯曲引起的中面力
w_bending = c9m.midSpanDeflection2(q, a, c9m.E1(), t)
print(f"普通弯曲时板条梁的最大挠度为{w_bending*1e3:.2f} mm")
print(f"0.2倍的板厚为：{0.2 * t*1e3:.2f} mm")
print(f"普通弯曲挠度小于0.2倍板厚，因此不计弯曲引起的中面力\n")
M_bending = -1 / 8 * q * a**2
print(f"板条梁弯矩为{M_bending:.3f} N*m\n")
sigma_bending = c9m.bendingNormalStress(M_bending, t)
print(f"板条梁应力为{abs(sigma_bending * 1e-6):.3f} MPa\n")

print(f"---- 总结 ----")
print(f"板条梁模型计算结果偏大，偏安全。")