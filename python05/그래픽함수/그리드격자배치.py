from tkinter import *

w = Tk()

# 변수에 여러개를 넣어서 사용하는 자료 구조: 리스트
color = ['red', 'blue', 'yellow']

for imsi in color:
    label = Label(w, 
                  text = imsi, 
                  width=15, 
                  relief=RIDGE,
                  font=('굴림', 30))
    label.pack()
    
    
    button = Button(w, text='', 
                    width=10, 
                    bg= imsi,
                    font=('굴림', 30))
    button.pack()
w.mainloop()



