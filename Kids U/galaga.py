import turtle
import random
import time

player = turtle.Turtle()
player.left(90)
player.penup()

bullet = turtle.Turtle()
bullet.penup()
bullet.hideturtle()

enemies = []

def changeColor():
    colors = ["blue","purple","green","brown","yellow","pink"]
    i = random.randint(0, len(colors) - 1)
    player.pencolor(color[i])

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

def moveEnemies():
    for unit in enemies:





window = turtle.Screen()

window.listen()

window.onkeypress(moveRight, 'd')
window.onkeypress(moveLeft, 'a')
window.onkeypress(moveUp, 'w')
window.onkeypress(moveDown, 's')
window.onkeypress(changeColor, 'q')

delay = .05
while True:
    time.sleep(delay)
    moveEnemies()
    checkCollisions()
    if len(enemies) < 10:
        spawnEnemy()

turtle.done()
turtle.close()
