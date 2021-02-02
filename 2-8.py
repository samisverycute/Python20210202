def draw(cm):
    for i in range(4):
        kouki.forward(cm)
        kouki.left(90)
import turtle
kouki = turtle.Turtle()
draw(10)
draw(20)
draw(30)
turtle.done()