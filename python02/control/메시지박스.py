import tkinter.messagebox as box

box.showinfo("내가 제목", "나는 내용.")
print()

num = 100
data = "안녕히가세요."
person = "홍길동"
result = num + data + person + "님" #안됨(숫자+문자)
box.showinfo(person, data);



