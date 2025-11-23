# Program: triangle2.py
#Using the distance function, we can augment the interactive triangle program from Chapter 4 to calculate the perimeter of the triangle. Here's the complete program:
import math 
from graphics import *

def square(x): 
    return x ** 2

def distance(p1, p2): 
    dist = math.sqrt(square(p2.getX() - p1.getX()) 
                    + square(p2.getY() - p1.getY())) 
    return dist

def main(): 
    win = GraphWin("Draw a Triangle") 
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points") 
    message.draw(win)

    # Get and draw three vertices of triangle 
    p1 = win.getMouse() 
    p1.draw(win) 
    p2 = win.getMouse() 
    p2.draw(win) 
    p3 = win.getMouse() 
    p3. draw(win)

    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1,p2,p3) 
    triangle.setFill("peachpuff") 
    triangle.setOutline("cyan") 
    triangle.draw(win)

    # Calculate the perimeter of the triangle 
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1) 
    message.setText("The perimeter is: {0:0.2f}".format(perim))

    # Wait for another click to exit 
    win.getMouse() 
    win. close()

main()

"""
Let's use the square function to write another function, one that finds the distance between two points. Given two points (x1, Yl) and (x2, Y2), the distance between them is calculated as below:
def distance(p1, p2): 
    dist = math.sqrt(square(p2.getX() - p1.getX()) 
                    + square(p2.getY() - p1.getY()) 
    return dist
"""
