# Fibonacci (Recursive)
# Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

"""
Example usage:
fibonacci(3)
"""

"""
Note: eval() should be used with caution, especially if the input isn't trusted. For safer evaluation, consider using a parser like ast.literal_eval or third-party libraries like sympy or numexpr
"""
