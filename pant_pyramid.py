col = 7
i = 3
j = 1
print("* "*col)
while True:
    if i==0:
        break
    print("* "*i, end="")
    print("  "*j, end="")
    print("* "*i, end="\n")
    j = j+2
    i = i-1

