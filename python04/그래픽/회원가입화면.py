from tkinter import *

#복사: 컨트롤+알트+화살표아래
#이동: 알트+화살표아래
def file_write():
    #입력한 데이터를 가지고 옴: get()
    id_text = id.get()
    pw_text = pw.get()
    name_text = name.get()
    tel_text = tel.get()
    file = open(id_text + ".txt", "w")
    file.write(id_text + "\n")
    file.write(pw_text + "\n")
    file.write(name_text + "\n")
    file.write(tel_text + "\n")
    #file.close() #연결통로인 stream을 제거

#그래픽 화면에서 입력한 데이터를 가지고 온 후, 출력하는 함수
def insert():
    print("당신이 넣은 데이터 확인======")
    id_text = id.get()
    print("당신이 입력한  id: ", id_text)
    pw_text = pw.get()
    print("당신이 입력한  pw: ", pw_text)
    name_text = name.get()
    print("당신이 입력한  name: ", name_text)
    tel_text = tel.get()
    print("당신이 입력한  tel: ", tel_text)

   
w = Tk()
w.geometry('500x550')
w.title('나의 회원가입 화면')
w.configure(bg = 'white')

#이미지는 혼자 w라는 프레임에 올리지 못함.
#라벨이나 버튼을 먼저 만들어서 그곳에 끼워넣어야 함.
icon = PhotoImage(file='naver.png')
img = Label(w, image=icon)
img.pack()

l1 = Label(w, text='아이디 입력', font = ('궁서', 30), bg='white', fg='blue')
l1.pack()
id = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
id.pack()
l2 = Label(w, text='패스워드 입력', font = ('궁서', 30), bg='white', fg='blue')
l2.pack()
pw = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
pw.pack()
l3 = Label(w, text='이름 입력', font = ('궁서', 30), bg='white', fg='blue')
l3.pack()
name = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
name.pack()
l4 = Label(w, text='전화번호 입력', 
           font = ('궁서', 30), bg='white', fg='blue')
l4.pack()

tel = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
tel.pack()

button = Button(w, text='회원가입처리', 
           font = ('궁서', 30), bg='pink', fg='blue',
           command = file_write)
button.pack()

w.mainloop()






