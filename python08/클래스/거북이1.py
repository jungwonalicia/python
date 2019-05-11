import turtle

def leftClick(x, y):
    print("x축: " , x , ", " + "y축: ", y)
    
    while True:
        myTurtle.penup() #내가 정해준 위치로 이동!
        x2 = int(input("이동하고 싶은 X축 위치: "))
        y2 = int(input("이동하고 싶은 Y축 위치: "))
        myTurtle.goto(x2, y2)
        myTurtle.pendown() #그림을 그리는 것이 기본값.
        myTurtle.goto(0,0)
    

myTurtle = turtle.Turtle('turtle')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.title('거북이로 사각형 그리기')
turtle.onscreenclick(leftClick, 1)
turtle.done()



