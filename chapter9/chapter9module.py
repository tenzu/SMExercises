# This is a module for chapter 9 exercises.
from math import *

youngsModulus = 2e11
poissonsRatio = 0.3


# E1
def E1(youngsModulus=2e11, poissonsRatio=0.3):
    return youngsModulus / (1 - poissonsRatio**2)


# 板条梁截面惯性矩
def I1(plateThickness):
    return plateThickness**3 / 12


# 筒形刚度
# def cylindricalStiffness(plateThickness):
#     return youngsModulus*plateThickness**3/(12*(1-poissonsRatio**2))
def cylindricalStiffness(plateThickness):
    return E1(youngsModulus, poissonsRatio) * plateThickness**3 / 12


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

# u 的值
def u(span, inplaneForce, cylindricalStiffness):
    return span/2*sqrt(inplaneForce/cylindricalStiffness)

# 拉力弯矩辅助函数1
def phai1(u):
    return (6/u**2)*(1-u/sinh(u))

# 拉力弯矩辅助函数2
def X(u):
    return (3/u**2)*(u/tanh(u)-1)

# 拉力挠度辅助函数
def f1(u):
    return 24/u**3*(u/2-tanh(u/2))