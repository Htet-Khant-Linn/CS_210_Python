#Check if a Number is Prime
#Write a Python program that checks if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

"""Checks if a number is prime, tracing the logic for n = 97.

1. Initial Check: The function first checks `if n <= 1`.
- For n = 97, this is false, so the function continues.

2. Loop Setup: The code sets up the loop `for i in range(2, int(n ** 0.5) + 1)`.
- The square root of 97 is ~9.85.
- `int(9.85)` becomes 9.
- `9 + 1` is 10.
- The loop will iterate through `range(2, 10)`, meaning it will check the numbers
2, 3, 4, 5, 6, 7, 8, and 9.

3. Loop Iterations: The function checks if `97 % i == 0` for each number `i`.
- 97 is not divisible by 2, 3, 4, 5, 6, 7, 8, or 9.
- In every case, the remainder is not 0, so the `if` condition is never met.

4. Final Return: Since the loop completes without finding any divisors,
the function exits the loop and executes the final line, `return True`.
This correctly identifies 97 as a prime number.
"""