tv프로그램 = []

def tv_print():
    for 프로그램 in tv프로그램:
        print(프로그램, end=" ")
        
tv프로그램.append("무한도전")
tv_print()
print("-----")

tv프로그램.append("런닝맨")
tv_print()
print("-----")

data = input("보고 싶은 tv프로그램을 입력")
tv프로그램.append(data)
tv_print()
print("-----")