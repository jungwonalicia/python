from tkinter import *

def call1():
    print("생일을 선택하셨군요.")
    w2 = Tk()
    b4 = Button(w2, text='나는 생일', font=('굴림', 30))
    b4.pack()
    w2.mainloop
def call2():
    print("헬보이를 선택하셨군요.")
    w3 = Tk()
    b5 = Button(w3, text='나는 헬보이', font=('굴림', 30))
    b5.pack()
    w3.mainloop
    
def call3():
    print("돈을 선택하셨군요.")
    w4 = Tk()
    b6 = Button(w4, text='나는 돈', font=('굴림', 30))
    b6.pack()
    w4.mainloop
    
w = Tk()

icon1 = PhotoImage(file='m1.PNG')
b1 = Button(w, image=icon1, command=call1)
b1.pack()

icon2 = PhotoImage(file='m2.PNG')
b2 = Button(w, image=icon2, command=call2)
b2.pack()

icon3 = PhotoImage(file='m3.PNG')
b3 = Button(w, image=icon3, command=call3)
b3.pack()

w.mainloop()