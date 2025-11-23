# Write a function calculate(expression) that takes a mathematical expression as a string (e.g., "3 + 5 * 2") and evaluates it.
# calculate expression - evaluates a mathematical expression

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"
    
"""
Example usage:
print(calculate("3 + 5 * 2"))
"""
