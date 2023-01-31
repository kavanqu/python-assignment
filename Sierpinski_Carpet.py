# kavan qu zi jing, 224545C, BA2201

import turtle

def drawSquare(points,myTurtle,color):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[3][0],points[3][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()


def getSquareSize(points):
    return abs(points[1][1] - points[0][1]) + 1


def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'cyan', 'yellow',
                'violet', 'orange']

    drawSquare(points, myTurtle,colormap[degree])

    oneThirdSquare = getSquareSize(points) // 3
    twoThirdSquare = oneThirdSquare * 2
    wholeThirdSquare = oneThirdSquare * 3


    if degree > 0:
        # 1st square
        sierpinski([points[0],
                    [points[0][0], points[0][1] + oneThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1] + oneThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1]]],
                   degree - 1, myTurtle)
        # 2nd square
        sierpinski([[points[0][0], points[0][1] + oneThirdSquare],
                    [points[0][0], points[0][1] + twoThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1] + twoThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1] + oneThirdSquare]],
                   degree - 1, myTurtle)
        # 3rd square
        sierpinski([[points[0][0], points[0][1] + twoThirdSquare],
                    [points[0][0], points[0][1] + wholeThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1] + wholeThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1] + twoThirdSquare]],
                   degree - 1, myTurtle)
        # 4th square
        sierpinski([[points[0][0] + oneThirdSquare, points[0][1] + twoThirdSquare],
                    [points[0][0] + oneThirdSquare, points[0][1] + wholeThirdSquare],
                    [points[0][0] + twoThirdSquare, points[0][1] + wholeThirdSquare],
                    [points[0][0] + twoThirdSquare, points[0][1] + twoThirdSquare]],
                   degree - 1, myTurtle)
        # 5th square
        sierpinski([[points[0][0] + twoThirdSquare, points[0][1] + twoThirdSquare],
                    [points[0][0] + twoThirdSquare, points[0][1] + wholeThirdSquare],
                    [points[0][0] + wholeThirdSquare, points[0][1] + wholeThirdSquare],
                    [points[0][0] + wholeThirdSquare, points[0][1] + twoThirdSquare]],
                   degree - 1, myTurtle)
        # 6th square
        sierpinski([[points[0][0] + twoThirdSquare, points[0][1] + oneThirdSquare],
                    [points[0][0] + twoThirdSquare, points[0][1] + twoThirdSquare],
                    [points[0][0] + wholeThirdSquare, points[0][1] + twoThirdSquare],
                    [points[0][0] + wholeThirdSquare, points[0][1] + oneThirdSquare]],
                   degree - 1, myTurtle)
        # 7th square
        sierpinski([[points[0][0] + twoThirdSquare, points[0][1]],
                    [points[0][0] + twoThirdSquare, points[0][1] + oneThirdSquare],
                    [points[0][0] + wholeThirdSquare, points[0][1] + oneThirdSquare],
                    [points[0][0] + wholeThirdSquare, points[0][1]]],
                   degree - 1, myTurtle)
        # 8th square
        sierpinski([[points[0][0] + oneThirdSquare, points[0][1]],
                    [points[0][0] + oneThirdSquare, points[0][1] + oneThirdSquare],
                    [points[0][0] + twoThirdSquare, points[0][1] + oneThirdSquare],
                    [points[0][0] + twoThirdSquare, points[0][1]]],
                   degree - 1, myTurtle)



def main():
    turtle.tracer(0)
    myTurtle = turtle.Turtle()
    myTurtle.speed(10)  # adjust the drawing speed here
    myWin = turtle.Screen()
    # 4 points of the first square based on [x,y] coordinates
    myWin.tracer(False)
    myPoints = [[-150, -150], [-150, 150], [150, 150], [150, -150]]
    degree = 3 # Vary the degree of complexity here

    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle)
    myWin.tracer(True)
    myTurtle.hideturtle()  # hide the turtle cursor after drawing is completed
    myWin.exitonclick()  # Exit program when user click on window


main()
