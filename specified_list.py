# date 17/09/21
# Write a Python program to print a specified list after removing the 0th, 2nd, 4th
# and 5th elements.
list_1 = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92]
for i in range(len(list_1)):
    if i not in [0, 2, 4, 5]:
        print(list_1[i], end=" ")