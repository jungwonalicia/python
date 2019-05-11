# 텔레비전 => 클래스, 클래스이름 Tv
# 정적특징 - 채널, 색 => 멤버변수
# 동적특징 - 전원을켜다, 전원을끄다, 채널을바꾸다. => 멤버함수

class Tv:
    #멤버변수
    채널 = 0;
    색 = None;
    
    def __init__(self, 채널, 색): #객체생성시 자동으로 호출(생성자)
        print("부품을 복사할 때 자동을 실행되는 함수")
        self.채널 = 채널
        self.색 = 색
    
    def __str__(self): #출력할 때 멤버변수 편하게 출력
        return str(self.채널) + ", " + self.색
        
    #멤버함수
    def 전원을켜다(self):
        print("전원을 켜다.")
    def 전원을끄다(self):
        print("전원을 끄다.")
    def 채널을바꾸다(self):
        print("채널을 바꾸다.")

        
myTv = Tv(100, "검정색")
print(myTv)

yourTv = Tv(200, "빨간색")
print(yourTv)

    
    
    
    
    
    

