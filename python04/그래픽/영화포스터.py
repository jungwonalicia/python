from tkinter import *

def call():
    print("버튼이 눌러졌어요...")
    
w = Tk()

icon = PhotoImage(file='m1.PNG')
label = Label(w, image=icon)
label.pack()

button = Button(w, text="나를 눌러요.",
                font=('궁서', 30),
                fg='red', bg='yellow',
                command=call
                )
button.pack()
w.mainloop()




