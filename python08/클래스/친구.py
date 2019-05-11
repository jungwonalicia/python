#친구
class Friend:
#정적특징-2개씩(멤버변수)
    name = None
    age = 0
    count = 0 #친구들 사이에 공유할 목적으로 사용되는 하나의 변수(클래스 변수)
    
#동적특징-2개씩(멤버함수)
    def play(self):
        print("놀다.")
    def tel(self):
        print("대화하다.")
        
#멤버변수 처음값 자동으로 넣어주는 함수
# __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Friend.count = Friend.count + 1
        
#멤버변수 값 쉽게 출력해주는 함수
# __str__
    def __str__(self):
        return self.name + ", " + str(self.age)

동네친구 = Friend("아이유", 20)
print(동네친구.count)
학교친구 = Friend("박보검", 25)
print(학교친구.count)
print(동네친구)
print(학교친구)


    
    
    
    
    
    
    
    
    


