from tkinter import *
from tkinter.messagebox import *

def login():
    #입력한 id, pw를 가지고 옴.
    id = id_text.get()
    pw = pw_text.get()
    
    #입력한 id에 맞는 파일을 open.(읽기 모드)
    file = open(id + ".txt", "r")
    print("내가 입력한 id: " + id)
    print("내가 입력한 pw: " + pw)
    
    #id,pw에 해당하는 2줄만 읽어옴.
    id_file = file.readline()
    pw_file = file.readline()
    
    id_file2 = id_file.strip() #string앞뒤의 공백 제거   
    pw_file2 = pw_file.strip()  
      
    print("파일에 저장된 id " , id_file2)
    print("파일에 저장된 pw " , pw_file2)
    #내가 입력한 id, pw와 파일에서 읽어온 id, pw가 동일한지 체크
    #동일하다면 login처리, 동일하지 않다면 login처리 하면 안됨.
    if(id == id_file2 and pw == pw_file2) :
        print('로그인 OK.....!!!')
        showinfo("로그인처리", "로그인이 완료되었습니다.")
    else:
        print('로그인 NOT.....!!!')
        showinfo("로그인처리", "로그인이 완료되지 않았습니다. 재로그인해주세요.")
    
w = Tk()
w.geometry('500x400')
w.configure(bg='lime')
id_label = Label(w, 
                 text='사용자 ID입력',
                 font=('맑은 고딕', 30),
                 bg='lime',
                 fg='blue')
id_label.pack()

id_text = Entry(w, 
                font=('맑은 고딕', 30),
                bg='yellow',
                fg='red')
id_text.pack()
pw_label = Label(w, 
                 text='사용자 PW입력',
                 font=('맑은 고딕', 30),
                 bg='lime',
                 fg='blue')
pw_label.pack()

pw_text = Entry(w, 
                font=('맑은 고딕', 30),
                bg='yellow',
                fg='red')
pw_text.pack()

icon = PhotoImage(file='035.png')
button = Button(w, image=icon, command=login)
button.pack()                
w.mainloop()

