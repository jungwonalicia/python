import turtle
t = turtle.Pen()

while True:
    방향 = input("왼쪽:left, 오른쪽:right>> ")
    각도 = int(input("각도 입력>> "))
    if 방향 == 'left':
        t.left(각도)
        t.forward(150)
    if 방향 == 'right':
        t.right(각도)
        t.forward(150)


# for count in range(10):
# t.right(90)
# t.forward(300)
