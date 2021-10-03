# write a program to append to a file and display the text 

fobj = open("Batch2.txt", "a")
str_1 = "\nIt works on reading and writing of file"
fobj.write(str_1)
print("Text Written to the file")

fobj =  open("Batch2.txt", "r")
str_2 = fobj.read()
print("Concepts of File are:\n", str_2)
fobj.close()