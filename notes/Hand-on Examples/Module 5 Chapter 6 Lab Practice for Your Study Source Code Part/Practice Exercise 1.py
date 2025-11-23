# 1. Greet function
#Write a function greet(name) that takes a name as input and prints "Hello, [name]!".
def greet(name):
    print(f"Hello, {name}!")

# 2. Square function
#Write a function square(num) that returns the square of a number.
def square(num):
    return num * num

# 3. Is Even function
#Write a function is_even(n) that returns True if n is even, and False otherwise.
def is_even(n):
    return n % 2 == 0

# 4. Fahrenheit to Celsius function
#Write a function fahrenheit_to_celsius(f) that converts Fahrenheit to Celsius using the formula.
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# 5. Sum of List function
# Write a function sum_list(numbers) that takes a list of numbers and returns their sum.
def sum_list(numbers):
    return sum(numbers)

"""
Example usage:
greet("Alice")                        # Output: Hello, Alice!
print(square(4))                      # Output: 16
print(is_even(7))                     # Output: False
print(fahrenheit_to_celsius(98.6))   # Output: 37.0
print(sum_list([1, 2, 3, 4, 5]))      # Output: 15
"""
