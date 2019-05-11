#콘솔에서 입력(키보드)
#데이타의 종류: 숫자(정수,실수), 문자(String), 
           #논리(TRUE,FALSE)
data = 100
data2 = 11.22
data3 = '02-844-1234'
data4 = input("당신의 개발 언어는 ")
data5 = int(input("오늘 수업시간은 "))

#콘솔에 출력
print("나의 주요 언어는 ", data4)

#box에 출력
import tkinter.messagebox as box
box.showinfo("오늘 남은 수업 시간은 ", data5-1)






