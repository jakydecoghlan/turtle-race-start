from turtle import Turtle, Screen
import random


leonardo = Turtle(shape="turtle")
leonardo.fillcolor("DodgerBlue")
rafael = Turtle(shape="turtle")
rafael.fillcolor("red")
donatello = Turtle(shape="turtle")
donatello.fillcolor("purple4")
miguel_angel = Turtle(shape="turtle")
miguel_angel.fillcolor("orange")

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="APUESTA", prompt="¿Qué tortuga ganará la carrera: Leonardo, Miguel Angel, Rafael o"
                                                    " Donatello?")

leonardo.penup()
leonardo.setposition(-230, -100)
donatello.penup()
donatello.setposition(-230, -50)
miguel_angel.penup()
miguel_angel.setposition(-230, 0)
rafael.penup()
rafael.setposition(-230, +50)

def random_forward (turtle):
    turtle.forward(random.randint(0,10))

def check_llegada(turtle):
    if turtle.xcor() > 230:
        turtle.write(f"EL GANADOR ES: {turtle}")
        return False



race = True

while race:
    random_forward(leonardo)
    check_llegada(leonardo)
    random_forward(donatello)
    random_forward(miguel_angel)
    random_forward(rafael)



screen.exitonclick()