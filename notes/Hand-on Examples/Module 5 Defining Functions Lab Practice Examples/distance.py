"""
import math

def square(x):
    return x ** 2

def distance(p1, p2):
    return math.sqrt(square(p2[0] - p1[0]) + square(p2[1] - p1[1]))

# Example usage:
print(distance((1, 2), (4, 6)))  # Output: 5.0
"""

"""
import math

def square(x):
    return x ** 2  # Custom square function

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

# Example: Create a class with getX() and getY() methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

# Example usage:
p1 = Point(1, 2)
p2 = Point(4, 6)

print(distance(p1, p2))  # Output: 5.0
"""
"""
import math

def distance(p1, p2):
    dist = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    return dist
print(distance((1, 2), (4, 6)))
"""
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Example usage:
print(distance((1, 2), (4, 6)))  # Output: 5.0

