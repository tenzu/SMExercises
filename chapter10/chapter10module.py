# This is a module for chapter 10 exercises.
from math import pi

youngsModulus = 2e11
poissonsRatio = 0.3


# 形心计算公式
def centroidofAreas(A1, y1, A2, y2):
    y0 = (A1 * y1 + A2 * y2) / (A1 + A2)
    return y0


# 材料力学移轴公式
def shiftAxisFormula(I1, A1, d1, I2, A2, d2):
    I0 = I1 + I2 + A1 * d1**2 + A2 * d2**2
    return I0


# 单跨梁欧拉力公式
def eularForceSingleBeam(I, L,E =youngsModulus):
    return pi**2*E*I/L**2

# 强度校验
def strengthCheck(stress, yieldStress=235):
    if stress > yieldStress:
        return "******** 应力超过材料屈服强度！********"
    else:
        return "********材料未屈服。********"