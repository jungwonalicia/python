import calendar
from tkinter import *
import time

w= Tk()

time = time.asctime();
print(time)

label2 = Label(w, text=time,
              bg = 'yellow',
              fg = 'lime',
              font = ('굴림', 20)
              )
label2.pack()

cal = calendar.month(2019, 5)
print(cal)

# label은 그래픽 화면에 글씨를 쓰고 싶을 때
label = Label(w, text=cal,
              bg = 'blue',
              fg = 'yellow',
              font = ('굴림', 20)
              )
label.pack()

w.mainloop()









