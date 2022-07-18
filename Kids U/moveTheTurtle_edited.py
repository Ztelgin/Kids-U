import turtle
import random
import time

#setup player
player = turtle.Turtle()



player.left(90)

player.penup()
player.turtlesize(2)

#setup turtle
bullet = turtle.Turtle()
bullet.turtlesize(2)
bullet.penup()
bullet.speed(0)
bullet.left(90)
bullet.hideturtle()

enemies = []

# spawn enemy
def spawn():
    while len(enemies) < 10:
        enemy = turtle.Turtle()
        enemy.penup()
        enemy.speed(0)
        enemy.turtlesize(2)
        x = random.randint(-290, 290)
        y = random.randint(0, 290)
        enemy.goto(x,y)
        enemies.append(enemy)

def changeColor():
    colors = ["blue","purple","green","brown","yellow","pink"]
    i = random.randint(0, len(colors) - 1)
    player.pencolor(colors[i])

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

def shoot():
    bullet.showturtle()

    # Move bullet to player Postion
    bullet.speed(0)
    x = player.xcor()
    y = player.ycor()
    bullet.setx(x)
    bullet.sety(y)

def updateEnemies():
    for enemy in enemies:

        y = bullet.ycor()
        y = y + 25
        bullet.sety(y)

        for unit in enemies:
            if bullet.distance(unit) <20:
                unit.hideturtle()


        x = random.randint(-290, 290)
        y = random.randint(0, 290)
        enemy.setx(x)
        enemy.sety(y)






window = turtle.Screen()

window.listen()

window.onkey(shoot, 'space')
window.onkeypress(moveRight, 'd')
window.onkeypress(moveLeft, 'a')
window.onkeypress(moveUp, 'w')
window.onkeypress(moveDown, 's')
window.onkeypress(changeColor, 'q')

spawn()
while True:
    updateEnemy()




turtle.done()
turtle.close()
