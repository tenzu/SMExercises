import chapter9module as c9m

print(f"********** 9.3题 **********\n")

a = 0.6
b = 2
t = 0.014
q = 13 / 0.01**2
TStar = 4750 / 0.01
# 板条梁压应力
sigma_0Star = TStar / (1 * t)

print(f"求解（a）：")
print(f"计算系数u*：")
uStar = c9m.uStar(a, TStar, c9m.cylindricalStiffness(t))
print(f"u* = {uStar:.4f}\n")
print(f"计算B点挠度：")
w_B = c9m.midSpanDeflection2(q / 2, a, c9m.E1(2e11, 0.3), t) * c9m.f0Star(uStar)
print(f"w_B = {w_B*1e3:.2f} mm\n")

print(f"求解（b）：")
print(f"计算B点弯矩：")
M_B_complex = c9m.bendingMomentMidSpan2(q / 2, a) * c9m.phai0Star(uStar)
print(f"M_B = {M_B_complex:.4f} N*m\n")
print(f"计算B点弯曲正应力大小：")
sigma_B = c9m.bendingNormalStress(M_B_complex, t)
print(f"sigma_B = {sigma_B*1e-6:.3f} MPa (拉为正)\n")

print(f"计算B点上表面应力：")
sigma_B_top = -sigma_0Star + sigma_B
print(f"sigma_B_top = {sigma_B_top*1e-6:.3f} MPa (压应力)\n")
print(f"计算B点下表面应力：")
sigma_B_bottom = -sigma_0Star - sigma_B
print(f"sigma_B_bottom = {sigma_B_bottom*1e-6:.3f} MPa (拉应力)\n")

print(f"求解完毕！")
