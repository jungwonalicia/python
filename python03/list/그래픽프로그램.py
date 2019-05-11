from tkinter import *

def b처리():
    print('나를 눌렀군요...')
def b2처리():
    print('나도 눌렀군요...')

w = Tk()
w.geometry('300x300')

b = Button(w, 
            text = '나를 눌러요.', 
            bg = 'yellow', 
            width = 15,
            font = ('궁서', 20),
            command=b처리
            )
b.pack()

b2 = Button(w, 
            text = '나도 눌러요.', 
            bg = 'green', 
            width = 15,
            font = ('궁서', 20),
            command=b2처리
            )
b2.pack()


w.mainloop()