import turtle
import random

colors = ['red', 'green', 'blue', 'pink']

def leftClick(x, y):
    print("x축: " , x , ", " + "y축: ", y)
    
    color = random.randint(0,3) #0, 1, 2, 3, if color=0
    myTurtle.pencolor(colors[color]) #colors[color]=colors[0]
    width = 50
    height = 50
    
    x2 = x - width
    y2 = y - height
    
    #클릭한 위치까지 그림을 그려줘!
    myTurtle.goto(x, y)

myTurtle = turtle.Turtle('turtle')
myTurtle.pensize(20)
myTurtle.pencolor('red')
turtle.title('거북이로 사각형 그리기')
turtle.onscreenclick(leftClick, 1)
turtle.done()



