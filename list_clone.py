# date 17/09/21
# Write a Python program to clone or copy a list
size = int(input("Enter size for list : "))
list_1 = []
for i in range(0, size):
    list_1.append(int(input(f"Enter element {i+1} : ")))
clone = []
for num in list_1:
    clone.append(num)

print(f"Cloned list : {clone}")