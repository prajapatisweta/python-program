def armstrong(num):
    rem=p=0
    while(num>0):
        rem=num%10
        p=p+rem**3
        num=num//10
    return p

def palindrome(num):
    copy_num=num
    rem=p=0
    while(num>0):
        rem=num%10
        p=p*10+rem
        num=num//10
    if copy_num==p:
        print("Number is palindrome")
    else:
        print("Number is not a palindrome")

num1=int(input("Enter any number :"))
arm1=armstrong(num1)
if(num1==arm1):
    print("Number is Armstrong")
else:
    print("Number is not an Armstrong")

palindrome(num1)
