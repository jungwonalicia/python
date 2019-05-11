from tkinter import *

w = Tk()

# 변수에 여러개를 넣어서 사용하는 자료 구조: 리스트
color = ['red', 'blue', 'yellow']

count = 0 #row의 시작값.
for imsi in color:
    label = Label(w, 
                  text = imsi, 
                  width=15, 
                  relief=RIDGE,
                  font=('굴림', 30))
    label.grid(row=count, column=0)
    # row: 행(가로줄)
    # column: 열(세로줄)
    # 위치값(index)은 0부터 시작
    
    
    button = Button(w, text='', 
                    width=10, 
                    bg= imsi,
                    font=('굴림', 30))
    button.grid(row=count, column=1)
    count = count + 1
w.mainloop()



