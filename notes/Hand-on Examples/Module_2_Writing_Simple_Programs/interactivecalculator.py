# Interactive Python calculator program

# Start a loop to perform up to 100 calculations
for _ in range(100):
    try:
        # Prompt the user to enter a mathematical expression
        expression = input("Enter a mathematical expression (or 'quit' to exit): ")

        # Check if the user wants to quit
        if expression.lower() == 'quit':
            print("Exiting the calculator.")
            break
        
        # Evaluate the expression and print the result
        result = eval(expression)
        print(f"Result: {result}")
    
    except Exception as e:
        # Handle any errors in the expression
        print(f"Error: Invalid expression. {e}")
        

#Explanation:
#Loop up to 100 times: The for _ in range(100) ensures the program will run for up to 100 iterations.
#User Input: The input() function takes a mathematical expression as input from the user.
#Check for 'quit': If the user types 'quit', the program exits early using break.
#eval() function: This function evaluates the mathematical expression entered by the user. It can handle basic arithmetic and other Python expressions like +, -, *, /, **, etc.
#Error handling with try-except: If an invalid expression is entered (like 2 + or 5 / 0), the program will catch the exception and display an error message.
