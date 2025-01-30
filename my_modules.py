from math import *
from math import pi
from math import sqrt
import sympy as sp

youngsModulus = 2.1e11
poissonsRatio = 0.3
x, y = sp.symbols("x y")


# E1
def E1(youngsModulus=2e11, poissonsRatio=0.3):
    return youngsModulus / (1 - poissonsRatio**2)


# 板条梁截面惯性矩
def I1(plateThickness):
    return 1 * plateThickness**3 / 12


# 筒形刚度
def cylindricalStiffness(plateThickness):
    return E1(youngsModulus, poissonsRatio) * I1(plateThickness)


# 形心计算公式
def centroidofAreas(A1, y1, A2, y2):
    y0 = (A1 * y1 + A2 * y2) / (A1 + A2)
    return y0


# 材料力学移轴公式
def shiftAxisFormula(I1, A1, d1, I2, A2, d2):
    I0 = I1 + I2 + A1 * d1**2 + A2 * d2**2
    return I0


# 两端固支梁跨中弯矩
def bendingMomentFixedEnd1(distributedLoad, span):
    return distributedLoad * span**2 / 24


# 两端固支梁固端弯矩
def bendingMomentFixedEnd2(distributedLoad, span):
    return distributedLoad * span**2 / 12


# 普通梁的弯曲正应力
def bendingNormalStress(moment, plateThickness):
    return 6 * moment / (plateThickness**2)


# 两端固支梁跨中挠度
def midSpanDeflection1(distributedLoad, span, E1, plateThickness):
    return distributedLoad * span**4 / (384 * E1 * I1(plateThickness))
    # return distributedLoad*span**4/(384*cylindricalStiffness(plateThickness))


# 两端简支梁跨中挠度
def midSpanDeflection2(distributedLoad, span, E1, plateThickness):
    return 5 * distributedLoad * span**4 / (384 * E1 * I1(plateThickness))


# 两端简支梁跨中弯矩
def bendingMomentMidSpan2(distributedLoad, span):
    return -distributedLoad * span**2 / 8


# 由 u 计算 T
def u2T(u, plateThickness, span):
    return 4 * u**2 * cylindricalStiffness(plateThickness) / span**2


"""以下为辅助函数相关"""


# 拉力下 u 的值
def u(span, inplaneForce, cylindricalStiffness):
    return span / 2 * sqrt(inplaneForce / cylindricalStiffness)


# 压力下 u* 的值
def uStar(span, inplaneForce, cylindricalStiffness):
    return span / 2 * sqrt(inplaneForce / cylindricalStiffness)


# 大挠度弯曲 U 的值
def U(
    plateThickness, distributedLoad, span, K=0.5, youngsModulus=2e11, poissonsRatio=0.3
):
    return (
        (youngsModulus / (1 - poissonsRatio**2) / distributedLoad) ** 2
        * (plateThickness / span) ** 8
        / K
    )


# 拉力弯矩辅助函数phai0
def phai0(u):
    return (2 / u**2) * (1 - 1 / cosh(u))


# 拉力弯矩辅助函数phai1
def phai1(u):
    return (6 / u**2) * (1 - u / sinh(u))


# 拉力弯矩辅助函数X
def X(u):
    return (3 / u**2) * (u / tanh(u) - 1)


# 拉力挠度辅助函数f1
def f1(u):
    return 24 / u**3 * (u / 2 - tanh(u / 2))


# 拉力挠度辅助函数f0
def f0(u):
    return (24 / 5 / u**4) * (u**2 / 2 + 1 / cosh(u) - 1)


# 压力挠度辅助函数f0*
def f0Star(uStar):
    return 24 / 5 / uStar**4 * (1 / cos(uStar) - uStar**2 / 2 - 1)


# 压力弯矩辅助函数phai0*
def phai0Star(uStar):
    return (2 / uStar**2) * (1 / cos(uStar) - 1)


""" 以下为能量法相关 """


# 板的弯曲应变能
# !!!diff(w,x,y)有错误!!!
def plateStrainEnergy(
    w,
    plateThickness,
    xLowerLimit,
    xUpperLimit,
    ylowerLimit,
    yUpperLimit,
):
    return (
        cylindricalStiffness(plateThickness)
        / 2
        * sp.integrate(
            (w.diff(x, 2) + w.diff(y, 2)) ** 2,
            (x, xLowerLimit, xUpperLimit),
            (y, ylowerLimit, yUpperLimit),
        )
    )


""" 以下为稳定性相关 """


# 单跨梁欧拉力公式
def eularForceSingleBeam(I, L, E=youngsModulus):
    return pi**2 * E * I / L**2


# 强度校验
def strengthCheck(stress, yieldStress=235):
    if stress > yieldStress:
        return "******** 应力超过材料屈服强度！*******"
    else:
        return "******** 材料未屈服。********"


# 单跨杆柔度系数lambda
def lamdaSingleBeam(L, I, A):
    return L / sqrt(I / A)


# lambda to sigma_cr
def lamda2Sigmacr(lamda, sigma_y=235, E=youngsModulus * 1e-6):
    return sigma_y - sigma_y**2 * lamda**2 / (4 * pi**2 * E)


# 杆件弯曲应变能
def beamBendingEnergy(v, I, lowerLimit, upperLimit, E=youngsModulus):
    return (
        1 / 2 * sp.integrate(E * I * sp.diff(v, x, 2) ** 2, (x, lowerLimit, upperLimit))
    )


# 悬臂梁刚度系数K
def cantileverStiffness(I, L, E=youngsModulus):
    return 3 * E * I / L**3


# Xj计算公式
def Xj(K, I, L, E=youngsModulus):
    return K / (sp.pi**4 * E * I / L**3)


# 横梁临界刚度
def K_cr(phai, Xj, I, L, E=youngsModulus):
    return phai * Xj * sp.pi**4 * E * I / L**3
