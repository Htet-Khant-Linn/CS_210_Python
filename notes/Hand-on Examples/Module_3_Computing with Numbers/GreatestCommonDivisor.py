#Find the Greatest Common Divisor (GCD)
#Write a Python program that computes the greatest common divisor (GCD) of two numbers.

import math

def gcd(a, b):
    return math.gcd(a, b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
