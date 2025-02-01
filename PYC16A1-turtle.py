import turtle

turtle.Screen().bgcolor("Red")
turtle.Screen().setup(800,800)
pen = turtle.Turtle()

for i in range(4):
  pen.forward(100)
  pen.left(90)


pen.penup()
pen.goto(250,10)
pen.pendown()

for i in range(3):
  pen.forward(100)
  pen.left(120)

pen.penup()
pen.goto(-200,10)
pen.pendown()

for i in range(4):
  pen.forward(100)
  pen.left(90)
  pen.forward(50)
  pen.left(90)
  
pen.penup()
pen.goto(-200,-200)
pen.pendown()


for i in range(6):
  pen.forward(30)
  pen.left(60)
  





turtle.done() 