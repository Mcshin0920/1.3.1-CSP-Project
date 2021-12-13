from turtle import Turtle, Screen
import random
import time

def start():
    wn = Screen()
    wn.setup(500, 500)
    wn.bgcolor("green")
    TURTLE_SIZE = 5
    yertle = Turtle(shape="turtle", visible=False)
    yertle.penup()
    yertle.goto(TURTLE_SIZE / 2 - wn.window_width() / 2, wn.window_height() / 2 - TURTLE_SIZE / 2)
    yertle.pendown()
    yertle.showturtle()
    yertle.penup()
    p = Turtle()

    yertle.color('blue')
    p.color('red')
    p.penup()

    speed = 5

    def travel():
        p.forward(speed)
        if p.ycor() >= 250:
            lambda: p.setheading(270)
        elif p.ycor() <= -250:
            lambda: p.setheading(90)
        elif p.xcor() >= 250:
            lambda: p.setheading(180)
        else:
            lambda: p.setheading(0)
        wn.ontimer(travel, 10)

    def enemy():
        yertle.goto(random.randint(-250, 250), random.randint(-250, 250))

    wn.onkey(lambda: p.setheading(90), 'Up')
    wn.onkey(lambda: p.setheading(180), 'Left')
    wn.onkey(lambda: p.setheading(0), 'Right')
    wn.onkey(lambda: p.setheading(270), 'Down')
    wn.listen()
    x = True
    travel()
    while x == True:
        enemy()

    if p.xcor() == yertle.xcor() or p.ycor() == yertle.ycor():
        x = False
        p.up()
        p.goto(-100, 0)
        p.down()
        p.write("YOU LOST")
        time.sleep(9999999999)



    wn.mainloop()