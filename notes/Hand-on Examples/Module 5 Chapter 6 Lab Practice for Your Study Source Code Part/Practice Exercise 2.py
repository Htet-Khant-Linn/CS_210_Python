# 1. Reverse a string
# Write a function reverse_string(s) that returns the reverse of a string.
def reverse_string(s):
    return s[::-1]

# 2. Recursive factorial
# Write a function factorial(n) that calculates the factorial of a given number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 3. Check if a string is a palindrome
# Write a function is_palindrome(s) that checks if a given string is a palindrome (reads the same forward and backward).
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # optional: ignore spaces and case
    return s == s[::-1]

# 4. Count vowels in a string
# Write a function count_vowels(s) that returns the number of vowels (a, e, i, o, u) in a string.
def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

# 5. Find the maximum in a list
# Write a function find_maximum(numbers) that takes a list of numbers and returns the largest number.
def find_maximum(numbers):
    if not numbers:
        return None  # or raise an error
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

"""
Example usage:
print(reverse_string("hello"))        # "olleh"
print(factorial(5))                   # 120
print(is_palindrome("Racecar"))       # True
print(count_vowels("Hello World"))    # 3
print(find_maximum([3, 7, 2, 9, 5]))  # 9
"""
