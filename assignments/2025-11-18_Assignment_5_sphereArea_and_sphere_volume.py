'''
2.	Write definitions for these functions: 
sphereArea(radius) Returns the surface area of a sphere having the given radius.
sphere Volume (radius) Returns the volume of a sphere having the given radius.
Hints: 
•	Surface Area of a Sphere: A=4πr2
•	Volume of a Sphere: V=4/3πr3
Where:
•	r is the radius of the sphere.
•	π is approximately 3.14159 (or you can use math.pi in Python for precision).

'''
import math
# use math library

def sphereArea(radius):
    # use Surface Area of a Sphere: A=4πr2 and return the surface area of a sphere
    return 4 * math.pi * (radius**2)

def sphereVolume(radius):
    # use Volume of a Sphere: V=4/3πr3 and return the volume of a sphere
    return (4/3) * math.pi * (radius**3)


# testing
r = 5

# printing the test result
print(f"Radius: {r}")
print(f"Surface Area: {sphereArea(r):.2f}")
print(f"Volume: {sphereVolume(r):.2f}")

