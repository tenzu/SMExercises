import chapter10module as c10m
import sympy as sp

print(f"********** 10.7题 **********")
longitudinal_A = 20 * 1e-4
longitudinal_I = 1000 * 1e-8
longitudinal_L = 5
beam_I = 15000 * 1e-8
beam_L = 6

print(f"求解（a)：")
# 使用单位力法计算悬臂梁刚度系数
K = c10m.cantileverStiffness(beam_I, beam_L)
print(f"悬臂梁刚度系数K = {K:.2f} N/m = {K * 1e-3:.2f} kN/m")

print(f"求解（b）：")
