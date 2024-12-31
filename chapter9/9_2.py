import chapter9module as c9m

l = 0.8
t = 0.02
q = 5 / (0.01**2)
sigma_0 = 80e6
T = sigma_0 * 1 * t

# 计算板条梁仅受横荷重时的最大挠度
print(f"计算板条梁仅受横荷重时的最大挠度：")
v_max = c9m.midSpanDeflection2(q, l, c9m.E1(2e11, 0.3), t)
print(f"v_max = {v_max :.4f} m = {v_max * 1000 :.3f} mm")
print(f"v_max/t = {v_max/t :.4f}，小于1/5")
print(f"固不需要考虑板条梁弯曲引起的中面力。\n")

print(f"计算u：")
u = c9m.u(l, T, c9m.cylindricalStiffness(t))
print(f"u = {u :.3f}")
print(f"计算复杂弯曲板条梁跨中挠度：")
v_max_complex = v_max * c9m.f0(u)
print(f"v_max_complex = {v_max_complex :.4f} m = {v_max_complex * 1000 :.3f} mm\n")

print(f"计算A点弯矩：")
M_A = c9m.bendingMomentMidSpan2(q, l) * c9m.phai0(u)
print(f"M_A = {M_A :.4f} N*m")
print(f"计算A点上表面正应力：")
sigma_A_up = sigma_0 - abs(c9m.bendingNormalStress(M_A, t))
print(f"sigma_A = {sigma_A_up :.4f} Pa = {sigma_A_up * 1e-6 :.3f} MPa (拉力)")
print(f"计算A点下表面正应力：")
sigma_A_down = sigma_0 + abs(c9m.bendingNormalStress(M_A, t))
print(f"sigma_A = {sigma_A_down :.4f} Pa = {sigma_A_down * 1e-6 :.3f} MPa (拉力)")
