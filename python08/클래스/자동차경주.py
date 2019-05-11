from tkinter import *

from tkinter.ttk import *
import random
import time
import threading

## 클래스 선언 부분 ##
class ThreadProgressBar():
    thread = None
    progress = None
    label = None
    labels = []
    img = None
    count = 0
    def __init__(self, parent, icon, x1, y1):
        global label
        self.label = Label(parent, text=icon + ' : 자동차')
        self.thread = threading.Thread(target=self.runProgress, args = (self.label, x1, y1,))
        self.thread.start()

    def runProgress(self,  label, x1, y1):
        hop = 0
        while True :
            hop = random.randrange(0, 10)
            if  x1 == 200 :   # 프로그레스가 100이면 멈춤
                break
            x1 = x1 + hop
            label.place(x=x1, y=y1)
            time.sleep(0.5)

## 함수 선언 부분 ##
def runThreadProgress() :
    thBar1 = ThreadProgressBar(window, 'car1.gif', 30, 100)
    thBar2 = ThreadProgressBar(window, 'car2.gif', 30, 150)
    thBar3 = ThreadProgressBar(window, 'car3.gif', 30, 200)

## 메인 코드 부분 ##
if __name__ == "__main__" :
    window = Tk()
    window.geometry("600x250")
    window.title('멀티 스레드')
    icon = PhotoImage('car1.gif')
    threadtButton = Button(window, text = '멀티 스레드 시작', command = runThreadProgress)
    threadtButton.pack(side = TOP, fill = X, ipadx  = 10, ipady = 10, padx = 10, pady = 10)
    
    window.mainloop()

