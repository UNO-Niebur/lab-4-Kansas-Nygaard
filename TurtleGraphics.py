#TurtleGraphics.py
#Name: Kansas Nygaard
#Date: 02/15/25
#Assignment: Lab 4 

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
#drawing for polygons
def drawPolygon(myTurtle, sides):
    for s in range(sides):
        myTurtle.forward(80)
        myTurtle.right(360/sides)
        
#filling corners
def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    myTurtle.penup()
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 2:
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 3:
        myTurtle.goto(0,-50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    else:
        myTurtle.goto(50,-50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
#Drawing Squares in squares
def squaresInSquares(myTurtle, num):
    start_size = 40
    step = 20
    for i in range(num):
        size = start_size + i * step
        myTurtle.penup()
        myTurtle.goto(-size/2,size/2)
        myTurtle.pendown()
        drawSquare(myTurtle, size)
    


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

