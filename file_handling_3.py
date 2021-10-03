# write a program to read last n lines of file 

num_lines = int(input("Enter no. of last lines to read: "))
fobj = open("Batch2.txt", "r")
lines = fobj.readlines()
print(lines[-num_lines:])