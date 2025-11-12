# futval_graph2.py
# This program makes use of the graphics library to draw a bar chart showing the growth of an investment. 
from graphics import *

def main(): 
        # Introduction 
        print("This program plots the growth of a 10-year investment.")
        
        # Get principal and interest rate 
        principal = float(input("Enter the initial principal: ")) 
        apr = float(input("Enter the annualized interest rate: "))
        
        # Create a graphics window with labels on left edge 
        win = GraphWin("Investment Growth Chart", 320, 240) 
        win.setBackground("white") 
        win.setCoords(-1.75,-200, 11.5, 10400) 
        Text(Point(-1, 0), ' 0.0K').draw(win) 
        Text(Point(-1, 2500), ' 2.5K').draw(win) 
        Text(Point(-1, 5000), ' 5.0K').draw(win) 
        Text(Point(-1, 7500), ' 7.5k').draw(win) 
        Text(Point(-1, 10000), '10.0K').draw(win)
        
        # Draw bar for initial principal 
        bar = Rectangle(Point(0, 0), Point(1, principal)) 
        bar.setFill("green") 
        bar.setWidth(2) 
        bar.draw(win)
        
        # Draw a bar for each subsequent year 
        for year in range(1, 11): 
            principal = principal * (1 + apr) 
            bar = Rectangle(Point(year, 0), Point(year+1, principal)) 
            bar. setFill ("green") 
            bar.setWidth(2) 
            bar.draw(win)
            
        input("Press <Enter> to quit.") 
        win. close()
        
main()

"""
This is certainly a workable program, but there is a nagging issue of program style that really should be addressed. Notice that this program draws bars in two different places.
The initial bar is drawn just before the loop, and the subsequent bars are drawn inside the loop. 
Having similar code like this in two places has some drawbacks.
Obviously, one issue is having to write the code twice.
A more subtle problem is that the code has to be maintained in two different places.
Should we decide to change the color or other facets of the bars, we would have to make sure these changes occur in both places.
Failing to keep related parts of the code in sync is a common problem in program maintenance. 
Functions can be used to reduce code duplication and to make programs more understandable and easier to maintain.
"""
