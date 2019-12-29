import turtle
import getch

gift = turtle.Turtle()
turtle.speed(1)

def sap():
    gift.right(45)
    gift.forward(50)

def pentagon():
    for i in range(8):
        sap()

def draw():
    for j in range(8):
        pentagon()
        gift.right(135)
        turtle.color("red","blue")

draw()

a = getch.getch()
