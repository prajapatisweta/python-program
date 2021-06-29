a,b,c=0,1,0
n=int(input("Enter No. of terms for fibonacci series :"))
print(a)
print(b)
for i in range (n-2):
    c=a+b
    print(c)
    a=b
    b=c