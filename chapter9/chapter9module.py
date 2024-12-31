# This is a module for chapter 9 exercises.
youngsModulus = 2e11
poissonsRatio = 0.3

# E1
def E1(youngsModulus=2e11, poissonsRatio=0.3):
    return youngsModulus/(2*(1-poissonsRatio**2))

# 板条梁截面惯性矩
def I1(plateThickness):
    return plateThickness**3/12

# 筒形刚度
# def cylindricalStiffness(plateThickness):
#     return youngsModulus*plateThickness**3/(12*(1-poissonsRatio**2))
def cylindricalStiffness(plateThickness):
    return E1(youngsModulus, poissonsRatio)*plateThickness**3/12

# 两端固支梁跨中弯矩
def bendingMomentFixedEnd1(distributedLoad, span):
    return distributedLoad*span**2/24

# 两端固支梁固端弯矩
def bendingMomentFixedEnd2(distributedLoad, span):
    return distributedLoad*span**2/12

# 普通梁的弯曲正应力
def bendingNormalStress(moment, plateThickness):
    return 6*moment/(plateThickness**2)

# 两端固支梁跨中挠度
def midSpanDeflection1(distributedLoad, span, E1, plateThickness):
    return distributedLoad*span**4/(384*E1*I1(plateThickness))