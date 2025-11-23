# event_loop1.py -- keyboard-driven color changing window

"""
from graphics import *

def main():
    win = GraphWin("Color Window", 500, 500)

    # Event Loop: handle key presses until user 
    # presses the "q" key.
    while True:
        key = win.getKey()
        if key == "q": # loop exit
            break
        #process the key
        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")

    # exit program
    win.close()
main()
"""
from graphics import *

def main():
    win = GraphWin("Color Window", 500, 500)

    # Draw a circle in the center
    circle = Circle(Point(250, 250), 50)
    circle.setFill("red")
    circle.draw(win)

    # Draw a rectangle
    rect = Rectangle(Point(100, 400), Point(400, 450))
    rect.setFill("green")
    rect.draw(win)

    # Draw a label
    label = Text(Point(250, 480), "Press r/w/g/b to change color. Press q to quit.")
    label.setSize(12)
    label.draw(win)

    # Event Loop: handle key presses
    while True:
        key = win.getKey()
        if key == "q":
            break
        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")

    win.close()

main()

