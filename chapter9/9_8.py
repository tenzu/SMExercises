import chapter9module as c9m

t = 1 * 1e-2
q = 5 * 1e4
a = 150 * 1e-2
b = 40 * 1e-2  # 板条梁跨长
# 查表得以下系数
k1 = 0.1356
k2 = 0.0397
k3 = 0.1203
k4 = 0.1249
# 按公式计算板的重点挠度
w_eq = k1 * q * b**4 / (c9m.youngsModulus * t**3)
print(f"根据公式计算出板的最大挠度为{w_eq:.3f} m = {w_eq*1000:.4f} mm")