# Factorial of a Number
#Write a Python program to compute the factorial of a number n using a function.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input from the user
n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")
