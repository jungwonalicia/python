# 강아지(클래스)- 클래스이름은 대문자로 시작!
# 정적특성- 색, 종류 (멤버변수)
# 동적특성- 짖다, 꼬리를흔들다(멤버함수)

class Dog:
    color = None
    field = None
    
    def 짖다(self):
        print("강아지가 짖다.")
    def 꼬리를흔들다(self):
        print("강아지가 꼬리를 흔들다.")

happy = Dog()
happy.color = "갈색"
happy.field = "포메리온"
happy.꼬리를흔들다()
happy.짖다() #함수를 사용하는 것을 "부른다(콜한다. call)"
print("내 강아지의 색은 ", happy.color)
print("내 강아지의  종류는 ", happy.field)

smile = Dog()











