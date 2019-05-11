from tkinter import *

w = Tk()
b = Button(w, 
           text="나를 눌러요.", 
           bg="yellow", 
           fg="blue")
b.pack()

b2 = Button(w, text="나도 버튼이예요.")
b2.pack()

img = PhotoImage(file="img1.PNG")
b3 = Button(w, image = img)
b3.pack()

w.mainloop()