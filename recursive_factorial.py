def factorial(n):
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1
n1=int(input("Enter a number: "))
print("Factorial of ",n1,"is ",factorial(n1))