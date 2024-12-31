import chapter9module as c9m

t = 0.006
l = 0.6
q = 10 / 0.01**2

print(f"计算板条梁仅受横荷重时的最大挠度：")
w_max = c9m.midSpanDeflection2(q, l, c9m.E1(), t)
print(f"板条梁的最大挠度为：{w_max:.4f} m = {w_max*1e3:.2f} mm")
print(f"w_max/t = {w_max/t :.4f}，远于1/5")
print(f"固需要考虑板条梁弯曲引起的中面力，且应采用大挠度弯曲理论。\n")

print(f"计算系数U：")
U = c9m.U(t, q, l, 0.5)
print(f"U = {U:.6f}")
print(f"查图前计算lg10^4*sqrt(U)")
UU = c9m.log10(10**4*c9m.sqrt(U))
print(f"lg10^4*sqrt(U) = {UU:.2f}")
print(f"查图得 u = 2.98\n")