import turtle
turtle.speed(10)

def drawSquare(lengthOfSquare): #Draws a square taking a parameter of the square's sidelength.
    for x in range(4):
        turtle.forward(lengthOfSquare)
        turtle.left(90)

def drawTriangle(lengthOfTriangle): #Draws a triangle taking a parameter of the triangle's sidelength.
    for x in range(3):
        turtle.forward(lengthOfTriangle)
        turtle.left(120)

def cyclicalSquare(rotationCount): #Uses the square function to draw multimple rotating squares.
    for x in range(rotationCount):
        drawSquare(200)
        turtle.left(5)

def cyclicalTriangle(rotationCount): #Sses the triangle function to draw multiple rotating triangles.
    for x in range(rotationCount):
        drawTriangle(100)
        turtle.left(5)

cyclicalSquare(60)

input("Press any key and enter to exit: ")