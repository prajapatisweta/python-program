import geometry

x=int(input("Enter side/radius for a pointyShape: "))
h=float(input("Enter height for a pointyShape: "))
print("Directory of Geometry module is : ", dir(geometry))
print("Volume of a square pyramid is : ", geometry.pointyShapeVolume(x,h,True))
print("Volume of a circular cone is : ", geometry.pointyShapeVolume(x,h,False))
print("Base area of square pyramid is : ", geometry.squareArea(x))
print("Base area of circular cone is : ", geometry.squareArea(x))
