import turtle
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.shapesize(stretch_wid=5, stretch_len=1)
a.penup()
a.goto(-350, 0)

# Paddle B
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.shapesize(stretch_wid=5, stretch_len=1)
b.penup()
b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

# Functions
def a_up():
    y = a.ycor()
    y += 20
    a.sety(y)


def a_down():
    y = a.ycor()
    y -= 20
    a.sety(y)


def b_up():
    y = b.ycor()
    y += 20
    b.sety(y)


def b_down():
    y = b.ycor()
    y -= 20
    b.sety(y)

# KeyBinds
wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        print("hei")
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        print("hei")
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    # Paddle and Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < b.ycor() + 40 and ball.ycor() > b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < a.ycor() + 40 and ball.ycor() > a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1

    # Game End
    if score_b or score_a == 10:
        break
    else:
        pass

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 0)
pen2.write("GAME OVER", align="center", font=("courier", 40, "normal"))

time.sleep(5)
