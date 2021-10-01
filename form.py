from tkinter import *
root = Tk()
root.geometry("500x500")
root.title('Form')

label_0 =Label(root,text="Form", width=20,font=("bold",20))
label_0.place(x=90,y=60)

label_1 =Label(root,text="Full Name", width=20,font=("times",10))
label_1.place(x=80,y=130)
entry_1=Entry(root)
entry_1.place(x=240,y=130)

label_3 =Label(root,text="Email", width=20,font=("times",10))
label_3.place(x=68,y=180)
entry_3=Entry(root)
entry_3.place(x=240,y=180)

label_4 =Label(root,text="Gender", width=20,font=("times",10))
label_4.place(x=70,y=230)
var=IntVar()
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)

label_5=Label(root,text="Hobbies",width=20,font=("times",10))
label_5.place(x=70,y=280)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(root, text = "Singing", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(root, text = "Dancing", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(root, text = "Gaming", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.place(x=180,y=250)
C2.place(x=180,y=300)
C3.place(x=180,y=350)

Button(root, text='Submit' , width=20,bg="black",fg='white').place(x=180,y=420)
root.mainloop()