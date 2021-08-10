#predifined input
def histogram(h1):
    for element in h1:
        for i in range(element):
            print("* ",end='')
        print()
histogram([1,2,3,4,5,4,3,2,1])


#user input
# def histogram(h1):
#     for element in h1:
#         for i in range(int(element)):
#             print("* ",end='')
#         print()
# str_1=input("Enter elements separated by space: ")
# list_1=str_1.split()
# histogram(list_1)