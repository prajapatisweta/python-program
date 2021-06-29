# reverse

def reverseNo(num):
    rem=p=0
    while(num>0):
        rem=num%10
        p=p*10+rem
        num=num//10
    print("Reverse of given number is : ",p)

num1=int(input("Enter any number :"))
reverseNo(num1)

