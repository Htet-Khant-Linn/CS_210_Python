# Basic Maths Calculation

import math

# 1. Basic Arithmetic Operations
# Addition
num1 = 10
num2 = 5
sum_result = num1 + num2
print(f"Addition: {num1} + {num2} = {sum_result}")

# Subtraction
difference_result = num1 - num2
print(f"Subtraction: {num1} - {num2} = {difference_result}")

# Multiplication
product_result = num1 * num2
print(f"Multiplication: {num1} * {num2} = {product_result}")

# Division (Handling division by zero)
try:
    quotient_result = num1 / num2
    print(f"Division: {num1} / {num2} = {quotient_result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2. Square Root Calculation
square_root_result = math.sqrt(49)
print(f"Square Root: The square root of 49 is {square_root_result}")

# 3. Exponentiation (Power operation)
exponent_result = num1 ** num2
print(f"Exponentiation: {num1} raised to the power of {num2} is {exponent_result}")

# 4. Percentage Calculation
total_amount = 200
percentage = 15
percentage_value = (percentage / 100) * total_amount
print(f"Percentage: {percentage}% of {total_amount} is {percentage_value}")

# 5. Computing with Lists of Numbers
numbers = [10, 20, 30, 40, 50]
# Sum of numbers in the list
total_sum = sum(numbers)
print(f"Sum of the list {numbers} is {total_sum}")

# Multiplying all elements in the list
product_of_list = 1
for num in numbers:
    product_of_list *= num
print(f"Product of the list {numbers} is {product_of_list}")

# 6. Working with Fractions
from fractions import Fraction
frac1 = Fraction(3, 4)
frac2 = Fraction(2, 5)
fraction_result = frac1 + frac2
print(f"Adding fractions: {frac1} + {frac2} = {fraction_result}")

# 7. Solving a simple algebraic equation: ax + b = c
a = 2
b = 3
c = 11
# Solving for x
x = (c - b) / a
print(f"Solving equation {a}x + {b} = {c}, we get x = {x}")

# 8. Using the math module for advanced operations
# Factorial of a number
factorial_result = math.factorial(5)
print(f"Factorial: 5! = {factorial_result}")

# 9. Converting a Decimal to Binary
decimal_number = 10
binary_result = bin(decimal_number)
print(f"Decimal {decimal_number} in binary is {binary_result}")

