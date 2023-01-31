# kavan qu zi jing, 224545C, BA2201

import turtle
import math

def drawCircle(x,y,radius,myTurtle,color):
    myTurtle.up()
    myTurtle.fillcolor(color)
    myTurtle.goto(x, y - radius)
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()


def getCircleSize(radius):
    return (radius/(1 + math.sqrt(2)))


def sierpinski(x,y,radius, degree, myTurtle,rotation):
    colormap = ['blue', 'red', 'green', 'cyan', 'yellow',
                'violet', 'pink']
    # print(colormap[degree])
    drawCircle(x,y,radius,myTurtle,colormap[degree])
    new_radius = getCircleSize(radius)
    if degree > 0:
        if rotation % 4 == 0:
            # 1st circle
            sierpinski(x-new_radius,y+new_radius,new_radius,degree - 1, myTurtle,rotation+1)
            # 2nd circle
            sierpinski(x+new_radius, y+new_radius, new_radius, degree - 1, myTurtle, rotation+1)
            # 3rd circle
            sierpinski(x+new_radius, y-new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
        elif rotation % 4 == 1:
            # 1st circle
            sierpinski(x + new_radius, y + new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
            # 2nd circle
            sierpinski(x + new_radius, y - new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
            # 3th circle
            sierpinski(x - new_radius, y - new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
        elif rotation % 4 == 2:
            # 1st circle
            sierpinski(x + new_radius, y - new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
            # 2nd circle
            sierpinski(x - new_radius, y - new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
            # 3th circle
            sierpinski(x - new_radius, y + new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
        elif rotation % 4 == 3:
            # 1st circle
            sierpinski(x - new_radius, y - new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
            # 2nd circle
            sierpinski(x - new_radius, y + new_radius, new_radius, degree - 1, myTurtle, rotation + 1)
            # 3th circle
            sierpinski(x + new_radius, y - new_radius, new_radius, degree - 1, myTurtle, rotation + 1)


def main():
    turtle.tracer(0)
    myTurtle = turtle.Turtle()
    # myTurtle.speed(10)  # adjust the drawing speed here
    myWin = turtle.Screen()
    # 3 points of the first triangle based on [x,y] coordinates
    x = 0
    y = 0
    radius = 200
    myWin.tracer(False)
    degree = 5 # Vary the degree of complexity here
    # first call of the recursive function
    rotation = 0
    sierpinski(x,y,radius,degree,myTurtle,rotation)
    myWin.tracer(True)
    myTurtle.hideturtle()  # hide the turtle cursor after drawing is
# completed
    myWin.exitonclick()  # Exit program when user click on window


main()




