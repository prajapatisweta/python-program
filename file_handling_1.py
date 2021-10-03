# write a program to read an entire text file 

fobj = open("Batch2.txt", "w")
str_1 = "Welcome Batch 2! \nWe are working on Practical 6\nIt is based on File Handling concepts"
fobj.write(str_1)
print("Text Written to the file")

fobj =  open("Batch2.txt", "r")
str_2 = fobj.read()
print("Concepts of File are:\n", str_2)
fobj.close()