# 아빠지갑에서는 1000씩 줄거예요.
# 딸들이 아빠용돈주세요.
class Money:
# 딸들이 이름과 나이는 다 다르다.
# 딸들의 이름과 나이는 일반변수로 만든다.
    name = None
    age = 0
# 아빠 지갑은 하나만 있어야 함.
# 아빠 지갑은 클래스 변수로 만든다.
    wallet = 10000
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Money.wallet = Money.wallet - 1000

girl1 = Money('김연아', 15)
print("현재 아빠 지갑에 남은 돈 ", Money.wallet)
girl2 = Money('김세리', 10)
print("현재 아빠 지갑에 남은 돈 ", Money.wallet)
    
    
    
    
    
    
    
    



