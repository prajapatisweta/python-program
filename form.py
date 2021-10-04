from tkinter import *
root = Tk()
root.geometry("500x500")
root.title('Form')

label_0 =Label(root,text="Form", width=20,font=("bold",20))
label_0.place(x=90,y=20)

label_1 =Label(root,text="UserName :", width=20,font=("times",10))
label_1.place(x=80,y=70)
entry_1=Entry(root)
entry_1.place(x=240,y=70)

label_3 =Label(root,text="Email :", width=20,font=("times",10))
label_3.place(x=68,y=120)
entry_3=Entry(root)
entry_3.place(x=240,y=120)


label_4 =Label(root,text="Gender :", width=20,font=("times",10))
label_4.place(x=70,y=170)
var=IntVar()
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=170)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=170)

label_5=Label(root,text="Hobbies :",width=20,font=("times",10))
label_5.place(x=70,y=220)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(root, text = "Painting", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(root, text = "Dancing", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(root, text = "Sketching", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.place(x=180,y=190)
C2.place(x=180,y=240)
C3.place(x=180,y=290)


lable_6 = Label(root, text="Select Age : ")
age_1 = Scale(root, from_=15, to = 55, orient= HORIZONTAL)
lable_6.place(x=105,y=360)
age_1.place(x=220,y=345)

Button(root, text='Submit' , width=20,bg="black",fg='white').place(x=180,y=400)
root.mainloop()