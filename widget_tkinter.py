# 9 a 

from tkinter import *

page= Tk()
page.title("Hello All")
page.geometry("300x300")
my_lable = Label(page, text="Hello", bg="red", fg="white", font=('times', 18))
my_lable.place(x = 120, y = 55)
page.mainloop()