import turtle
import random

turtle.register_shape('ship.gif')

player = turtle.Turtle()
player.left(90)
player.turtlesize(2)
player.penup()
player.shape('ship.gif')

bullet = turtle.Turtle()
bullet.turtlesize(2)
bullet.penup()
bullet.hideturtle()
bullet.left(90)



enemies = []

def spawn():
    while len(enemies) < 10:
        enemy = turtle.Turtle()
        enemy.penup()
        enemy.right(90)
        enemy.turtlesize(2)
        enemies.append(enemy)

def updateEnemy():
    for enemy in enemies:
        y = random.randint(0,300)
        x = random.randint(-300,300)
        enemy.goto(x,y)


def shoot():
    bullet.showturtle()

    x = player.xcor()
    y = player.ycor()

    bullet.speed(0)
    bullet.setx(x)
    bullet.sety(y)

    bullet.speed(3)
    bullet.forward(1000)
    
def moveRight():
    x = player.xcor()
    x = x + 10
    player.setx(x)

def moveLeft():
    x = player.xcor()
    x = x - 10
    player.setx(x)

def moveUp():
    y = player.ycor()
    y = y + 10
    player.sety(y)

def moveDown():
    y = player.ycor()
    y = y - 10
    player.sety(y)



window = turtle.Screen()

window.listen()

window.onkeypress(moveRight, 'd')
window.onkeypress(moveLeft, 'a')
window.onkeypress(moveUp, 'w')
window.onkeypress(moveDown, 's')
window.onkey(shoot, 'space')

spawn()
while True:
    updateEnemy()
    
turtle.done()
turtle.close()
