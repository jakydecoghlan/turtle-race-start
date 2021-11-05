from turtle import Turtle, Screen

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

is_race_on = True





screen.exitonclick()