# This is a module for chapter 9 exercises.
from math import *
from math import log10

youngsModulus = 2e11
poissonsRatio = 0.3


# E1
def E1(youngsModulus=2e11, poissonsRatio=0.3):
    return youngsModulus / (1 - poissonsRatio**2)


# 板条梁截面惯性矩
def I1(plateThickness):
    return 1 * plateThickness**3 / 12


# 筒形刚度
def cylindricalStiffness(plateThickness):
    return E1(youngsModulus, poissonsRatio) * I1(plateThickness)


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
def U(plateThickness, distributedLoad, span, K=0.5, youngsModulus=2e11, poissonsRatio=0.3):
    return (
        (youngsModulus / (1 - poissonsRatio**2) / distributedLoad) ** 2
        * (plateThickness / span) ** 8
        / K
    )


# 拉力弯矩辅助函数0
def phai0(u):
    return (2 / u**2) * (1 - 1 / cosh(u))


# 拉力弯矩辅助函数1
def phai1(u):
    return (6 / u**2) * (1 - u / sinh(u))


# 拉力弯矩辅助函数2
def X(u):
    return (3 / u**2) * (u / tanh(u) - 1)


# 拉力挠度辅助函数
def f1(u):
    return 24 / u**3 * (u / 2 - tanh(u / 2))


# 拉力挠度辅助函数
def f0(u):
    return (24 / 5 / u**4) * (u**2 / 2 + 1 / cosh(u) - 1)


# 压力挠度辅助函数
def f0Star(uStar):
    return 24 / 5 / uStar**4 * (1 / cos(uStar) - uStar**2 / 2 - 1)


# 压力弯矩辅助函数
def phai0Star(uStar):
    return (2 / uStar**2) * (1 / cos(uStar) - 1)

''' 以下为能量法相关 '''
# 板的弯曲应变能
def plateStrainEnergy(w, plateThickness, possionsRatio = 0.3):
    pass