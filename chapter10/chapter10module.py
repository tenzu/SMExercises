# This is a module for chapter 10 exercises.
from math import pi
from math import sqrt
import sympy as sp

youngsModulus = 2e11
poissonsRatio = 0.3
x = sp.Symbol("x")


# 形心计算公式
def centroidofAreas(A1, y1, A2, y2):
    y0 = (A1 * y1 + A2 * y2) / (A1 + A2)
    return y0


# 材料力学移轴公式
def shiftAxisFormula(I1, A1, d1, I2, A2, d2):
    I0 = I1 + I2 + A1 * d1**2 + A2 * d2**2
    return I0


# 单跨梁欧拉力公式
def eularForceSingleBeam(I, L, E=youngsModulus):
    return pi**2 * E * I / L**2


# 强度校验
def strengthCheck(stress, yieldStress=235):
    if stress > yieldStress:
        return "******** 应力超过材料屈服强度！*******"
    else:
        return "******** 材料未屈服。********"


# 单跨杆柔度系数
def lamdaSingleBeam(L, I, A):
    return L / sqrt(I / A)


# lamda to sigma_cr
def lamda2Sigmacr(lamda, sigma_y=235, E=youngsModulus * 1e-6):
    return sigma_y - sigma_y**2 * lamda**2 / (4 * pi**2 * E)


# 杆件弯曲应变能
def beamBendingEnergy(v, I, lowerLimit, upperLimit, E=youngsModulus):
    return (
        1 / 2 * sp.integrate(E * I * sp.diff(v, x, 2) ** 2, (x, lowerLimit, upperLimit))
    )


# 悬臂梁刚度系数
def cantileverStiffness(I, L, E=youngsModulus):
    return 3 * E * I / L**3


# Xj计算公式
def Xj(K, I, L, E=youngsModulus):
    return K / (sp.pi**4 * E * I / L**3)
