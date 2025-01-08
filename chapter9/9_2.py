import chapter9module as c9m

print(f"********** 9.2题 **********")

l = 0.8
t = 0.02
q = 5 / (0.01**2)
sigma_0 = 80e6
T = sigma_0 * 1 * t

print(f"计算板条梁仅受横荷重时的最大挠度：")
w_max = c9m.midSpanDeflection2(q, l, c9m.E1(), t)
print(f"w_max = {w_max :.4f} m = {w_max * 1e3 :.2f} mm")
print(f"w_max/t = {w_max/t :.4f}，小于1/5")
print(f"固不需要考虑板条梁弯曲引起的中面力。\n")

print(f"计算系数u：")
u = c9m.u(l, T, c9m.cylindricalStiffness(t))
print(f"u = {u :.3f}")
print(f"计算复杂弯曲板条梁跨中挠度：")
w_max_complex = w_max * c9m.f0(u)
print(f"v_max_complex = {w_max_complex :.4f} m = {w_max_complex * 1e3 :.3f} mm\n")

print(f"计算A点弯矩：")
M_A = c9m.bendingMomentMidSpan2(q, l) * c9m.phai0(u)
print(f"M_A = {M_A :.4f} N*m")
print(f"计算A点上表面正应力：")
sigma_A_top = sigma_0 - abs(c9m.bendingNormalStress(M_A, t))
print(f"sigma_A = {sigma_A_top :.4f} Pa = {sigma_A_top * 1e-6 :.3f} MPa (拉应力)")
print(f"计算A点下表面正应力：")
sigma_A_bottom = sigma_0 + abs(c9m.bendingNormalStress(M_A, t))
print(f"sigma_A = {sigma_A_bottom :.4f} Pa = {sigma_A_bottom * 1e-6 :.3f} MPa (拉应力)")

print(f"恭喜，求解完毕！")
