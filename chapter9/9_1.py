import chapter9module as c9m

a = 2
b = 0.6
t = 0.012
q = 6.5 / 0.01 / 0.01

print(f"计算A点弯矩：")
Ma = c9m.bendingMomentFixedEnd1(q, b)
print(Ma)
print(f"计算A点由弯曲引起的正应力：")
sigma_a = c9m.bendingNormalStress(Ma, t)
print(sigma_a)
print(f"计算A点挠度：")
v_a = c9m.midSpanDeflection1(q, b, c9m.E1(2e11, 0.3), t)
print(v_a)
print(f"计算B点弯矩：")
Mb = c9m.bendingMomentFixedEnd2(q, a)
print(Mb)