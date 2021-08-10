#user input
# print("Enter 10 values: ")
# list_1=[0,0,0,0,0,0,0,0,0,0]
# for i in range(10): 
#     list_1[i]=int(input())
# for element in list_1:
#     if element<5:
#         print(element,end=' ')


#end function is used to specify that whether the print statement should go in next line after printing one output
#default value of end in print is \n

#predefined input
# list_1=[1,2,45,34,3,43,4,66,5]
# for element in list_1:
#     if element<5:
#         print(element,end=' ')

#separated by space
str_1=input("Enter list values separated by space: ")
list_1=str_1.split()
for element in list_1:
    if int(element)<5:
         print(element,end=' ')