from tkinter import *
from tkinter import messagebox

def test():
    data1 = text.get()
    messagebox.showinfo("입력받은 값>> ", data1)
    print("입력받은 값>> ", data1)
    
root = Tk()

name = Label(root, text = "이름입력하세요..")
name.pack()

text = Entry(root)
text.pack()

btn = Button(root, text = "입력버튼", command=test)
btn.pack()


root.mainloop() 
