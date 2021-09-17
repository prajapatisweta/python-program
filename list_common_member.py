# date 17/09/21
# Write a program that takes two lists and returns True if they have at least one
# common member.
list_1 = [4, 14, 24, 34, 44, 54, 64, 74]
list_2 = [8, 18, 28, 38, 44, 58, 64, 74]
for i in list_1:
    if i in list_2:
        print("True")
        break
else:
    print("Flase")