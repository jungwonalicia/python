import turtle
import random

colors = ['red', 'green', 'blue', 'pink']

def leftClick(x, y):
    color = random.randint(0,3) #0, 1, 2, 3, if color=0
    myTurtle.pencolor(colors[color]) #colors[color]=colors[0]
    width = random.randint(10, 70)
    height = random.randint(10, 70)
    myTurtle.pensize(random.randint(5, 20))
    x1 = x - width
    y1 = y - height
    x2 = x + width
    y2 = y + height
    
    result = input("1) 별 그리기 , 2) 사각형 그리기")
    if result == '1':
        myTurtle.penup()
        myTurtle.goto(x, y)
        myTurtle.pendown()
        for x in range(0, 10):
            myTurtle.left(130)
            myTurtle.forward(100)
    
    if result == '2':
        myTurtle.penup() #이동 설정
        myTurtle.goto(x1, y1)
        myTurtle.pendown() #그리기 설정
        myTurtle.goto(x1, y2)
        myTurtle.goto(x2, y2)
        myTurtle.goto(x2, y1)
        myTurtle.goto(x1, y1)
        
        #클릭한 위치까지 그림을 그려줘!

myTurtle = turtle.Turtle('turtle')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.title('거북이로 사각형 그리기')
turtle.onscreenclick(leftClick, 1)
turtle.done()



