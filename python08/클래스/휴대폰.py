# 휴대폰의 특징
# 정적특성-색, 회사명(변수)
# 동적특성-전화하다, 게임하다(함수)

class Phone:
    color = "";
    name = None;
    
    def 전화하다(self):
        print("전화하다.")
    
    def 게임하다(self):
        print("게임하다.")
    
apple = Phone() #w = Tk()
banana = Phone()

apple.color = "빨강"
apple.name = "사과전화기"
apple.게임하다()
apple.전화하다() #w.mainloop()
print(apple.name, "는 색이 ", apple.color)
print()
  
    