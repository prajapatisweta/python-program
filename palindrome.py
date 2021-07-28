x = str(input("Enter a string: "))
y = ""
for i in x:
    y += i
if (x == y):
    print("Given string is Palindrome")
else:
    print("Given String is not Palindrome")