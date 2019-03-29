from tkinter import *
from tkinter import messagebox

def onClick():
   data1 = text.get()
   print("입력받은 값: " , data1)
   messagebox.showinfo("입력받은 값: ", data1)


root = Tk()

name = Label(root, text= "이름")
name.pack()

text = Entry(root)
text.pack()

btn = Button(root, text="입력완료.", command=onClick)
btn.pack()










root.mainloop()