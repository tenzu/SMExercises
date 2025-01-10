import chapter10module as c10m

print(f"********** 10.1题 **********")
print(f"********** 非弹性稳定性的解 **********\n")
print(f"求解（1)：")
l = 350 * 1e-2
t = 20 * 1e-2
A1 = 11.15 * 1e-4  # 球扁钢截面积，题目中原为16.7
# A2 = 0.22 * 2 * 75 * 20 * 1e-4  # 带板截面积，带板宽度按0.22*2倍扶强材间距计算
A2 = 75 * t * 1e2 * 1e-4  # 带板截面积，带板宽度按1.0倍扶强材间距计算
I1 = 158 * 1e-8  # 球扁钢截面惯性矩
# I2 = 0.22 * 2 * 75 * 20**3 / 12 * 1e-8  # 带板截面惯性矩，带板宽度按0.22*2倍扶强材间距计算
I2 = 75 * 20**3 / 12 * 1e-8  # 带板截面惯性矩，带板宽度按1.0倍扶强材间距计算

# 计算球扁钢和带板的形心高度和截面惯性矩
y1 = t + 75.5 * 1e-3  # 查表得到球扁钢形心高度
y2 = t / 2  # 带板高度为板厚的一半
y0 = c10m.centroidofAreas(A1, y1, A2, y2)
print(f"组合体形心高度为\t{y0:.3f} m = {y0*1e2:.2f} cm")

d1 = y1 - y0
d2 = y0 - t / 2
I0 = c10m.shiftAxisFormula(I1, A1, d1, I2, A2, d2)
print(f"组合体截面惯性矩为\t{I0:.8f} m^4 = {I0*1e8:.2f} cm^4")

# 计算单跨梁柔度系数
lamda = c10m.lamdaSingleBeam(l, I0, (A1 + A2))
print(f"单跨梁柔度系数为\t{lamda:.1f}")
print(f"柔度系数小于100，在非弹性范围内。")

# 计算单跨梁临界应力
sigma_cr = c10m.lamda2Sigmacr(lamda, 235)
print(f"单跨梁临界应力为\t{sigma_cr:.2f} MP")
text = c10m.strengthCheck(sigma_cr)
print(f"{text}\n")

print(f"求解（2）：")
l = 2
t = 6 * 1e-3
A1 = 8.63 * 1e-4  # 球扁钢截面积
A2 = 50 * 1e-2 * t  # 带板截面积，带板宽度按1.0倍扶强材间距计算
# A2 = 0.22 * 2 * 50 * 1e-2 * t # 带板截面积，带板宽度按0.22*2倍扶强材间距计算
I1 = 85.22 * 1e-8  # 球扁钢截面惯性矩
I2 = 50 * 0.6**3 / 12 * 1e-8  # 带板截面惯性矩，带板宽度按1.0倍扶强材间距计算
# I2 = 0.22 * 2 * 50 * 0.6**3 / 12 * 1e-8  # 带板截面惯性矩，带板宽度按0.22*2倍扶强材间距计算
y1 = t + 6.29 * 1e-2  # 查表得到球扁钢形心高度
y2 = t / 2  # 带板高度为板厚的一半
y0 = c10m.centroidofAreas(A1, y1, A2, y2)
print(f"组合体形心高度为\t{y0:.3f} m = {y0*1e2:.2f} cm")

d1 = y1 - y0
d2 = y0 - t / 2
I0 = c10m.shiftAxisFormula(I1, A1, d1, I2, A2, d2)
print(f"组合体截面惯性矩为\t{I0:.8f} m^4 = {I0*1e8:.2f} cm^4")

# 计算单跨梁柔度系数
lamda = c10m.lamdaSingleBeam(l, I0, (A1 + A2))
print(f"单跨梁柔度系数为\t{lamda:.1f}")
print(f"柔度系数大于100，在非弹性范围外。")

# 计算单跨梁临界应力
sigma_cr = c10m.lamda2Sigmacr(lamda, 235)
print(f"单跨梁临界应力为\t{sigma_cr:.2f} MP")
text = c10m.strengthCheck(sigma_cr)
print(f"{text}\n")