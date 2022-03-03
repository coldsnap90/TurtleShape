
# Using the turtle function in python to draw a turtle
#1.Code will write a text saying "This Is Our Turtle!" above the turtle 
#2.Background will be filled as an aqua color
#3. We have created two functions to randomly return a value for
# color of the pen and for filling the shell.
#4. There is a decision structure for interpreting the value
# that is returned.
#5. Void functions with range loops will essentially draw all parts of
# the turtle.
#8.Code will fill color of arms and legs with green.
#9.Code will draw and fill eyes with color black. 
#10.Code will draw a spiral with random colors in the turtles shell.

import turtle
import random
t = turtle.Turtle()
def main():
    window=turtle.Screen()
    window.bgcolor("aqua")
    window.title("This is our turtle!")
    list = ['red','blue','black','green']
    t.penup()
    t.goto(-100,200)
    t.pendown()
    t.write("This is our turtle!", font=("cursive", 16, "normal"))
    turtleColor(list)
    colorOption = turtleColor(list)
    if(colorOption == 0):
        t.pencolor("red")
    elif(colorOption == 1):
        t.pencolor("blue")
    elif(colorOption==2):
        t.pencolor("black")
    else:
        t.pencolor("green")
    
    t.penup()
    t.goto(-50,70.71)

    turtleShellcolor(list)
    shellColour = turtleShellcolor(list)
    if(shellColour == 0):
        shellColourfill = t.fillcolor("red")
    elif(shellColour == 1):
        shellColourfill = t.fillcolor("blue")
    elif(shellColour == 2):
        shellColourfill = t.fillcolor("black")
    else:
        shellColourfill = t.fillcolor("green")

    turtleBody(shellColourfill)
    turtleHead()
    turtleLegs()
    turtleTail()
    turtleEyes()
    shellSpiral()
    
def turtleColor(list):
    list = ['red','blue','black','green']
    penColour = random.choice(range(len(list)))
    return penColour
def turtleShellcolor(list):
    list = ['red','blue','black','green']
    fillColour = random.choice(range(len(list)))
    return fillColour


def turtleBody(shellColourfill):
    t.pendown()
    shellColourfill
    t.begin_fill()
    for x in range(8):
        t.forward(100)
        t.right(45)
    t.end_fill()
    t.penup()

def turtleHead():
    t.goto(120.71,-50)
    t.pendown()
    t.left(45)
    t.fillcolor('#9ACD32')
    t.begin_fill()
    for x in range(4):
        t.forward(75)
        t.right(90)
    t.end_fill()
    t.penup()


def turtleLegs():
    t.goto(50,70.71)
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()
    t.fillcolor('#9ACD32')
    t.begin_fill()
    t.forward(50)
    t.circle(-25,180)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.penup()
    t.left(45)
    t.forward(135.36)
    
    t.fillcolor('#9ACD32')
    t.begin_fill()
    t.right(45)
    t.pendown()
    t.forward(50)
    t.circle(25,180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.penup()
    t.right(135)
    t.forward(206.064)

    t.right(45)
    t.pendown()
    t.fillcolor('#9ACD32')
    t.begin_fill()
    t.forward(50)
    t.circle(-25,180)
    t.forward(50)
    t.right(45)
    t.end_fill()
    t.penup()
    t.forward(206.064)

    t.right(45)
    t.pendown()
    t.fillcolor('#9ACD32')
    t.begin_fill()
    t.forward(50)
    t.circle(-25,180)
    t.forward(50)
    t.end_fill()
    t.penup()



def turtleTail():
    t.goto(-120.71,-25)
    t.left(90)
    t.pendown()
    t.fillcolor('#9ACD32')
    t.begin_fill()
    t.forward(35.355)
    t.left(90)
    t.forward(35.355)
    t.end_fill()
    t.penup()

def turtleEyes():
    t.speed(0)
    t.goto(120.71,-50)
    t.left(90)
    t.forward(75)
    t.right(90)
    t.forward(37.5)
    t.left(90)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(-10,180)
    t.end_fill()
    t.penup()
    t.goto(120.71,-50)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(37.5)
    t.right(90)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10,180)
    t.left(90)
    t.forward(20)
    t.end_fill()
    t.penup()
   
def shellSpiral():
     t.goto(0,-50)
     t.pendown()
     t.speed(5)
     for x in range(36):
         red=random.randint(0,1)
         blue=random.randint(0,1)
         green=random.randint(0,1)
         t.color(red,blue,green)
         t.circle(60)
         t.left(10)
     t.penup()
  

   
   

main()
