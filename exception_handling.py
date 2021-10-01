import sys

try:
    x = int(input("Enter a number : "))
except ValueError:
    print("Err... Enter number only")
    sys.exit()
else:
    print("Number you entered is :", x )
