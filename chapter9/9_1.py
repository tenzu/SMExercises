import chapter9module as c9m

a = 2
b = 0.6
t = 0.012
q = 6.5 / 0.01 / 0.01
sigma_0 = 18.8e6

print(f'求解（a)')
print(f"计算A点弯矩：")
M_A = c9m.bendingMomentFixedEnd1(q, b)
print(f'M_A = {M_A :.2f} N*m\n')
print(f"计算A点由弯曲引起的正应力：")
sigma_A = c9m.bendingNormalStress(M_A, t)
print(f'sigma_A = {sigma_A :.2f} Pa = {sigma_A*1e-6 :.2f} MPa\n')

print(f"计算B点弯矩：")
M_B = c9m.bendingMomentFixedEnd2(q, b)
print(f'M_B = {M_B :.2f} N*m\n')
print(f'计算B点由弯曲引起的正应力：')
sigma_B = c9m.bendingNormalStress(M_B, t)
print(f'sigma_B = {sigma_B :.2f} Pa = {sigma_B*1e-6 :.2f} MPa\n')

print(f'计算A点挠度：')
v_A = c9m.midSpanDeflection1(q,b,c9m.E1(2e11,0.3),t)
print(f'v_A = {v_A :.4f} m = {v_A*1e3 :.3f} mm\n')

print(f'求解（b)')
print(f'计算板条梁的中面拉力：')
T = 18.8e6*1*t
print(f'T = {T :.2f} N\n')
print(f'计算 u 的值：')
u = c9m.u(b, T, c9m.cylindricalStiffness(t))
print(f'u = {u :.3f}\n')
print(f'计算A点复杂弯曲弯矩：')
M_A_complex = M_A*c9m.phai1(u)
print(f'M_A_complex = {M_A_complex :.2f} N*m\n')
print(f'计算A点由复杂弯曲引起的正应力：')
sigma_A_complex = c9m.bendingNormalStress(M_A_complex, t)
print(f'sigma_A_complex = {sigma_0+sigma_A_complex :.2f} Pa = {(sigma_0+sigma_A_complex)*1e-6 :.2f} MPa\n')

print(f'计算A点复杂弯曲挠度：')
v_A_complex = v_A*c9m.f1(u)
print(f'v_A_complex = {v_A_complex :.4f} m = {v_A_complex*1e3 :.3f} mm\n')

print(f'计算B点复杂弯曲弯矩：')
M_B_complex = c9m.bendingMomentFixedEnd2(q, b)*c9m.X(u)
print(f'M_B_complex = {M_B_complex :.2f} N*m\n')
print(f'计算B点由复杂弯曲引起的正应力：')
sigma_B_complex = c9m.bendingNormalStress(M_B_complex, t)
print(f'sigma_B_complex = {sigma_0+sigma_B_complex :.2f} Pa = {(sigma_0+sigma_B_complex)*1e-6 :.2f} MPa\n')

print(f'恭喜，求解完毕！')