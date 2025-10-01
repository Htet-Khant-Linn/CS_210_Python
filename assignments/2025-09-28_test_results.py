# test_results.py
# Htet Khant Linn
# ======================================
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Test the functions with some sample values
a = 10
b = 5

print(f"Testing with a = {a}, b = {b}:")

# Testing addition
result_add = add(a, b)
print(f"Addition: {a} + {b} = {result_add}")

# Testing subtraction
result_sub = subtract(a, b)
print(f"Subtraction: {a} - {b} = {result_sub}")

# Testing multiplication
result_mul = multiply(a, b)
print(f"Multiplication: {a} * {b} = {result_mul}")

# Testing division
result_div = divide(a, b)
print(f"Division: {a} / {b} = {result_div}")

# Test division by zero
result_div_zero = divide(a, 0)
print(f"Division by zero: {a} / 0 = {result_div_zero}")
