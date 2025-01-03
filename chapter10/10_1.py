import chapter10module as c10m

print(f"求解（1)：")
l = 350 * 1e-2
t = 20 * 1e-2
A1 = 11.15 *1e-4  # 扶强材截面积，题目中原为16.7
# A2 = 0.22 * 2 * 75 * 20 * 1e-4  # 坞墙截面积，带板宽度按0.22*2倍扶强材间距计算
A2 = 75 * 20 * 1e-4 # 坞墙截面积，带板宽度按0.22*2倍扶强材间距计算
I1 = 158 * 1e-8 # 扶强材截面惯性矩
# I2 = 0.22 * 2 * 75 * 20**3 / 12 * 1e-8  # 坞墙截面惯性矩
I2 = 75 * 20**3 / 12  * 1e-8# 坞墙截面惯性矩

# 计算扶强材和坞墙的形心坐标
y1 = t + 75.5 * 1e-3  # 查表得到扶强材形心高度
y2 = t / 2  # 坞墙高度为板厚的一半
y0 = c10m.centroidofAreas(A1, y1, A2, y2)
print(f"组合体形心坐标：{y0:.2f} m = {y0*1e2:.2f} cm")

d1 = 75.5 * 1e-3 + 20 * 1e-2 - y0
d2 = y0 - t/2
I0 = c10m.shiftAxisFormula(I1, A1, d1, I2, A2, d2)
print(f"组合体截面惯性矩：{I0:.8f} m^4 = {I0*1e8:.2f} cm^4\n")

# 计算单跨梁欧拉力
T_E = c10m.eularForceSingleBeam(I0, l)
print(f"单跨梁欧拉力：{T_E:.2f} N = {T_E*1e-6:.2f} MN")
sigma_E = T_E / (A1 + A2)
print(f"单跨梁欧拉应力：{sigma_E:.2f} Pa = {sigma_E*1e-6:.2f} MPa")

print(f"求解（2）：")
