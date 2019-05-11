# --------------
# id:       kg
# pw:       1234
# 로그인    리셋
# -------------

from tkinter import *
def login처리():
    id = id_entry.get() 
    pw = pw_entry.get() 
    
    if(id == 'root' and pw == '1234'):
        print('로그인 ok')
        result['text'] = '로그인OK'
    else:
        print('로그인 not')
        result['text'] = '로그인NOT'
    
    
    
w = Tk()
id_label = Label(w, text="id", font=('굴림', 50),
                 width=5)
id_label.grid(row = 0, column = 0)

id_entry = Entry(w, font=('굴림', 50), 
                 width=10,
                 bg='yellow'
                 )
id_entry.grid(row = 0, column = 1)

pw_label = Label(w, text="pw", font=('굴림', 50),
                 width=5)
pw_label.grid(row = 1, column = 0)

pw_entry = Entry(w, font=('굴림', 50), 
                 width=10,
                 bg='yellow'
                 )
pw_entry.grid(row = 1, column = 1)

login_button = Button(w, text="로그인", font=('굴림', 50),
                bg='lime',
                width=5,
                command=login처리)
login_button.grid(row = 2, column = 1)

result = Label(w, text="", font=('굴림', 50),
                 width=10, bg = 'pink',
                 )
result.grid(row = 3, column = 1)






w.mainloop()
