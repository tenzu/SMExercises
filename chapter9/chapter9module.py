# This is a module for chapter 9 exercises.
youngsModulus = 2e11
poissonsRatio = 0.3

# cylindrical stiffness
def cylindricalStiffness(plateThickness):
    return youngsModulus*plateThickness**3/(12*(1-poissonsRatio**2))

# bending moment at fixed end
def bendingMomentFixedEnd(distributedLoad, beamWidth):
    return distributedLoad*beamWidth**2/12