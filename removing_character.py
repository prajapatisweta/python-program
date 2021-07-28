string = str(input("Enter any string: "))
remove = str(input("Enter a character to be removed: "))
print ("Original String : " + string)
for i in remove :
    string = string.replace(i, '')
print ("Resultant string : " + str(string))