# 7 c 28/9 

class Numbers:
    MULTIPLIER= 15.2    #class variable
    def __init__(self, x, y):       #constructor
        self.x=x
        self.y=y
    def add(self):      #instance method       
        return(self.x+self.y)
    def multiply(cls, a):       #class method
        return(a*cls.MULTIPLIER)
    def subtract(b,c):      #static method
        return(b-c)

x = int(input("Enter 1st number for addition: "))
y = int(input("Enter 2nd number for addition: "))        
n= Numbers(x,y)
print("Addition is : ", n.add())
a = int(input("Enter number for multiplication: "))
print("Multiplication is : ", n.multiply(a))
p = int(input("Enter 1st number for subtraction: "))
q = int(input("Enter 2nd number for subtraction: "))
print("Subtraction is : ", Numbers.subtract(p,q))


