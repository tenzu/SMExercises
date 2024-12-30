# This is a module for chapter 9 exercises.
youngsModulus = 2e11
poissonsRatio = 0.3

def cylindricalStiffness(plateThickness):
    return youngsModulus*plateThickness**3/(12*(1-poissonsRatio**2))