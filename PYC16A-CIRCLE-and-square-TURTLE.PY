import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

for _ in range(360):
    board.forward(1)
    board.left(1)

board.penup()
board.goto(200, 0)
board.pendown()

for _ in range(4):
    board.forward(100)
    board.right(90)

turtle.done()
