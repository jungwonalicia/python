from tkinter import *

import random
import time
import threading #동시에 여러개를 실행.

class ThreadBar():
    thread = None
    progress = None
    label = None
    
    def __init__(self, parent, x1, y1):
        self.label = Label(parent, text="자동차")
        self.thread = threading.Thread(target=self.runProgress, args = (self.label, x1, y1,))
        self.thread.start()
    def runProgress(self, label, x1, y1):
        hop = 0
        while True:
            hop = random.randrange(0, 10)
            if x1 == 200:
                break
            x1 = x1 + hop
            label.place(x=x1, y=y1)
            time.sleep(0.5)
def run():
    car1 = ThreadBar(w, 30, 100)       
    car2 = ThreadBar(w, 30, 150)       
    car3 = ThreadBar(w, 30, 200)       
    
w = Tk()
w.geometry("400x250")
w.title("스레드 프로그래밍")
button = Button(w, text ="멀티 스레드 시작", command=run)
button.pack(side=TOP, fill=X)  
w.mainloop()  
        
        
        
        
        
    
