def squareArea(x):
    return(x*x)
def circleArea(x):
    return(3.14*(x,x))
def pointyShapeVolume(x, h, squarebase):
    if squarebase == True:
        return(squareArea(x)*(h/3))
    elif squarebase == False:
        return((3.14*x*x)*(h/3))

