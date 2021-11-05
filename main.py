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
leonardo.setposition(210, -150)
leonardo.pendown()
leonardo.setposition(210, 150)
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
    if turtle.xcor() >= 200:
        return False
    else:
        return True



race = True

while race:
    random_forward(leonardo)
    if check_llegada(leonardo) == False:
        print("El Ganador es Leonardo. ")
        if user_bet.lower() == leonardo:
            print("Ganaste!")
        else:
            print("Perdiste!")
        break
    random_forward(donatello)
    if check_llegada(donatello) == False:
        print("El Ganador es Donatello. ")
        if user_bet.lower() == donatello:
            print("Ganaste!")
        else:
            print("Perdiste!")
        break
    random_forward(miguel_angel)
    if check_llegada(miguel_angel) == False:
        print("El Ganador es Miguel Angel. ")
        if user_bet.lower() == "miguel angel":
            print("Ganaste!")
        else:
            print("Perdiste!")
        break
    random_forward(rafael)
    if check_llegada(rafael) == False:
        print("El Ganador es Rafael ")
        if user_bet.lower() == "rafael":
            print("Ganaste!")
        else:
            print("Perdiste!")
        break



screen.exitonclick()