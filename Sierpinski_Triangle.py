# kavan qu zi jing, 224545C, BA2201

import turtle

def drawTriangle(points,myTurtle,colours):
    myTurtle.fillcolor(colours)
    myTurtle.up() # Pen up
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down() # Pen down
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colours = ['blue', 'red', 'green', 'turquoise', 'yellow', 'purple']
    # Draw a triangle based on the 3 points given
    drawTriangle(points,myTurtle,colours[degree])
    if degree > 0:
        sierpinski([points[0],
        getMid(points[0], points[1]),
        getMid(points[0], points[2])],
        degree-1, myTurtle)
        sierpinski([points[1],
        getMid(points[0], points[1]),
        getMid(points[1], points[2])],
        degree-1, myTurtle)
        sierpinski([points[2],
        getMid(points[2], points[1]),
        getMid(points[0], points[2])],
        degree-1, myTurtle)

def main():
    turtle.tracer(0)
    myTurtle = turtle.Turtle()
    myTurtle.speed(10) # adjust the drawing speed here
    myWin = turtle.Screen()
    # 3 points of the first triangle based on [x,y] coordinates
    myWin.tracer(False)
    myPoints = [[-200,-50],[0,200],[200,-50]]
    degree = 4 # Vary the degree of complexity here
    # first call of the recursive function

    sierpinski(myPoints,degree,myTurtle)
    myWin.tracer(True)
    myTurtle.hideturtle()# hide the turtle cursor after drawing is
    # completed
    myWin.exitonclick() # Exit program when user click on window

main()


