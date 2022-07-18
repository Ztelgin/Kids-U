# 🐢🐢🐢
import turtle

player = turtle.Turtle()
player.penup()

def moveRight():
    x = player.xcor()
    x += 10
    player.setx(x)
    
def moveLeft():
    x = player.xcor()
    x -= 10
    player.setx(x)

def moveForward():
    y = player.ycor()
    y += 10
    player.sety(y)

def moveBackward():
    y = player.ycor()
    y -= 10
    player.sety(y)

wn = turtle.Screen()
wn.listen()

wn.onkey(moveRight, 'd')
wn.onkey(moveLeft, 'a')
wn.onkey(moveForward, 'w')
wn.onkey(moveBackward, 's')

turtle.done() #this just keeps the window open until we close it.
turtle.close() #this just fixes issues related to closing the window
