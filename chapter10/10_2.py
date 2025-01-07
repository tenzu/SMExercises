import chapter10module as c10m

A = 42.4 * 1e-4
r = 5.32 * 1e-2
I = A * r**2
print(f"支柱截面惯性矩：{I:.8f} m^4 = {I*1e8:.2f} cm^4")
