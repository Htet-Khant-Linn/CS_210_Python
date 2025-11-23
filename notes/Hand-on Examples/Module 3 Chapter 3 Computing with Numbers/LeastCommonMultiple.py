#Find the LCM (Least Common Multiple)
#Write a Python program to find the least common multiple (LCM) of two numbers.

import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
