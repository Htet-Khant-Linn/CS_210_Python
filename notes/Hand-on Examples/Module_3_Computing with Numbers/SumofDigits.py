# Exercise 1: Sum of Digits
#Write a Python program that calculates the sum of the digits of a given number.

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  # Add the last digit to the total
        number //= 10  # Remove the last digit
    return total

# Input from the user
num = int(input("Enter a number: "))
print(f"The sum of the digits of {num} is {sum_of_digits(num)}")
