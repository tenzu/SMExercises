import chapter9module as c9m

print(f"********** 9.1题 **********\n")

a = 2
b = 0.6
t = 0.012
q = 6.5 / 0.01 / 0.01
sigma_0 = 18.8e6

print(f"求解（a)")
M_A = c9m.bendingMomentFixedEnd1(q, b)
print(f"A点弯矩 M_A 为\t{M_A :.2f} N*m\n")
sigma_A = c9m.bendingNormalStress(M_A, t)
print(f"A点由弯曲引起的正应力 sigma_A 为\t{sigma_A*1e-6 :.2f} MPa\n")
M_B = c9m.bendingMomentFixedEnd2(q, b)
print(f"B点弯矩 M_B 为\t{M_B :.2f} N*m\n")
sigma_B = c9m.bendingNormalStress(M_B, t)
print(f"B点由弯曲引起的正应力 sigma_B 为\t{sigma_B*1e-6 :.2f} MPa\n")
w_A = c9m.midSpanDeflection1(q, b, c9m.E1(), t)
print(f"A点挠度 w_A 为\t{w_A*1e3 :.3f} mm\n")
print(f"求解（b)")
T = 18.8e6 * 1 * t
print(f"板条梁中面拉力 T 为\t{T :.2f} N\n")
u = c9m.u(b, T, c9m.cylindricalStiffness(t))
print(f"u = {u :.3f}\n")
print(f"phai1(u) = {c9m.phai1(u) :.3f}")
M_A_complex = M_A * c9m.phai1(u)
print(f"A点由复杂弯曲引起的弯矩 M_A_complex 为\t{M_A_complex :.2f} N*m\n")
sigma_A_complex = c9m.bendingNormalStress(M_A_complex, t)
print(f"A点由复杂弯曲引起的正应力 sigma_A_complex 为\t{(sigma_0+sigma_A_complex)*1e-6 :.2f} MPa\n")
print(f"f1(u) = {c9m.f1(u) :.3f}")
w_A_complex = w_A * c9m.f1(u)
print(f"A点复杂弯曲挠度 w_A_complex 为\t{w_A_complex*1e3 :.3f} mm\n")
print(f"X(u) = {c9m.X(u) :.3f}")
M_B_complex = c9m.bendingMomentFixedEnd2(q, b) * c9m.X(u)
print(f"B点由复杂弯曲引起的弯矩 M_B_complex 为\t{M_B_complex :.2f} N*m\n")
sigma_B_complex = c9m.bendingNormalStress(M_B_complex, t)
print(f"B点由复杂弯曲引起的正应力 sigma_B_complex 为\t{(sigma_0+sigma_B_complex)*1e-6 :.2f} MPa\n")
print(f"求解完毕！")
