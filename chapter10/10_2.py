import chapter10module as c10m
 
print(f"********** 10.2题 **********")

l = 5
P = 300000
A = 42.4 * 1e-4
r = 5.32 * 1e-2
I = A * r**2
# 计算支柱截面惯性矩
print(f"支柱截面惯性矩：{I:.8f} m^4 = {I*1e8:.2f} cm^4")
# 计算欧拉力
T_E = c10m.eularForceSingleBeam(I, l)
print(f"欧拉力：{T_E:.2f} N")

# 计算安全系数
n = T_E / P
print(f"安全系数：{n:.2f}")