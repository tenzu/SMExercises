import chapter_9_module as c9m

print(f"********** 9.4题 **********\n")

t = 0.6 * 1e-2
l = 60 * 1e-2
q = 10 / (1e-2) ** 2
K = 0.5

w_max = c9m.midSpanDeflection2(q, l, c9m.E1(), t)
print(f"板条梁仅受横荷重时的最大挠度 w_max 为\t{w_max*1e3:.2f} mm")
print(f"w_max/t = {w_max/t :.4f}，远大于1/5")
print(f"固需要考虑板条梁弯曲引起的中面力，且应采用大挠度弯曲理论。\n")

U = c9m.U(t, q, l, K)
print(f"U = {U:.6f}")
print(f"查图前需先计算lg10^4*sqrt(U)")
UU = c9m.log10(10**4 * c9m.sqrt(U))
print(f"lg10^4*sqrt(U) = {UU:.2f}")
u = 3.01
print(f"查图得 u = {u:.2f}\n")

T = 4 * u**2 * c9m.cylindricalStiffness(t) / l**2
print(f"根据 u 计算板条梁中面力 T 为\t{T:.4f} N")
sigma_0 = T / 1 / t
print(f"对应的单跨梁欧拉应力 sigma 为\t{T/1/t*1e-6:.2f} MPa\n")

w_max_complex = c9m.midSpanDeflection2(q, l, c9m.E1(), t) * c9m.f0(u)
print(f"板条梁最大挠度 w_max_complex 为\t{w_max_complex*1e3:.2f} mm\n")

M_max = c9m.bendingMomentMidSpan2(q, l) * c9m.phai0(u)
print(f"板条梁最大弯矩 M_max 为\t{M_max:.3f} N*m\n")
sigma_b_max = abs(c9m.bendingNormalStress(M_max, t))
print(f"板条梁最大弯曲正应力 sigma_b_max 为\t{sigma_b_max*1e-6:.2f} MPa (拉应力)\n")
sigma_max = sigma_0 + sigma_b_max
print(f"板条梁最大应力 sigma_max 为\t{sigma_max*1e-6:.2f} MPa (拉应力)\n")

print(f"求解完毕！")
