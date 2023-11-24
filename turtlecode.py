#Basic snippets of turtle programming

import turtle
turtle.speed(10)

def drawSquare(lengthOfSquare): #Function that creates a square. Uses a parameter for the sidelength of the square.
    for x in range(4):
        turtle.forward(lengthOfSquare)
        turtle.left(90)

def drawTriangle(lengthOfTriangle): #Function that creates a triangle. Uses a parameter for the sidelength of the triangle.
    for x in range(3):
        turtle.forward(lengthOfTriangle)
        turtle.left(120)

def cyclicalSquare(rotationCount): #Utilizes the square function to draw N rotating squares.
    for x in range(rotationCount):
        drawSquare(200)
        turtle.left(5)

def cyclicalTriangle(rotationCount): #Utilizes the triangle function to draw N rotating triangles.
    for x in range(rotationCount):
        drawTriangle(100)
        turtle.left(5)

def polygonCreator(sides): #The exterior angle sum of a convex polygon is always 360. Dividing 360 by the sides yields each angle. Creates a polygon.
    for x in range(sides):
        turtle.forward(100)
        turtle.left(360 / sides)

input("Press any key and enter to exit!: ")
