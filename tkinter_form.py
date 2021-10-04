from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x400")
root.title('Form')

r1= IntVar()
name1=StringVar()
email1=StringVar()
age1=DoubleVar()
c1=IntVar()
c2=IntVar()
c3=IntVar()

def getDetails():
    str1 = "Name: "+str(name1.get())+"\n"
    str1 += "Email: "+str(email1.get())+"\n"
    str1 += "Age: "+str(int(age1.get()))+"\n"
    str1 +="Hobbies: "
    if c1.get()==1:
        str1 += "Singing"
    if c2.get()==1:
        str1 += "Dancing"
    if c3.get()==1:
        str1 += " Painting"
    if r1.get()==1:
        str1+="\nGender : Female"
    else:
        str1+="\nGender : Male"
    m1= messagebox.showinfo("Details are: ", str1)

lable_1 = Label(root, text="UserName : ").grid(row= 1 , column= 0)
entry_1 = Entry(root, textvariable = name1).grid(row=1, column=1)

lable_2 = Label(root, text="E-mail : ").grid(row= 2 , column= 0)
entry_2 = Entry(root, textvariable = email1).grid(row=2, column=1)

lable_3 = Label(root, text="Select Age : ").grid(row= 3 , column= 0)
age_1 = Scale(root, from_=15, to = 55, orient= HORIZONTAL, variable=age1).grid(row=3, column=1)

lable_4 = Label(root, text="Select Hobbies : ").grid(row= 4 , column= 0)
h1 = Checkbutton(root, text="Singing", variable=c1).grid(row=4, column=1, sticky="w")
h2 = Checkbutton(root, text="Dancing", variable=c2).grid(row=5, column=1, sticky="w")
h3 = Checkbutton(root, text="Painting", variable=c3).grid(row=6, column=1, sticky="w")

lable_5 = Label(root, text="Select Gender : ").grid(row= 7 , column= 0)
g1 = Radiobutton(root, text="Female",variable=r1, value=1).grid(row=7, column=1, sticky="w")
g2 = Radiobutton(root, text="Male",variable=r1, value=2).grid(row=8, column=1, sticky="w")

btn = Button(root, text="SUBMIT",bg="black",fg='white' , command=getDetails ).grid(row=9, columnspan=2)

root.mainloop()