'''
3.	Write a function that computes the area of a triangle given the length of its three sides as parameters.
Hints: 
•	Area=0.5×base×height 

'''


def triangle_area(base, height):
    # Area=0.5×base×height 
    return 0.5 * base * height

# test
b = 10
h = 5

print("This code computes the area of a triangle given the length of its two sides.")
print("Developed by Htet Khant Linn.")
print("------------------------------\n")

print(f"Base: {b}, Height: {h}")
print(f"Area: {triangle_area(b, h)}")
