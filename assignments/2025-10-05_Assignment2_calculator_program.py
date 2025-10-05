'''
4.	Write an interactive Python calculator program. 
The program should allow the user to type a mathematical expression 
and then print the value of the expression. 
Include a loop so that the user can perform many calculations (say, up to 100).
'''



def main():
    print("This is an interactive calculator program developed by Htet Khant Linn.")

    for _ in range(100):    # create a for loop up to 100
        try:
            # accepting the user input
            math_expression = input("Please enter a valid math expression (or type 'quit' to exit the program): ")
            
            # checking for exit
            if math_expression.lower() == "quit":   # use lower() to avoid casing issue when quitting
                print("Thanks for using. Exiting the calculator... ")
                print("Have a nice day.")
                break

            # calculate the expression and show the result
            result = eval(math_expression)  # execute any valid Python code the user types

            print(f"Result for {math_expression}: {result}")



        except Exception as e:
            # To handle any erros in the expression.
            print(f"Error: Invalid expression. {e}")

main()


'''
Explanation:

This program is a basic interactive calculator that allows a user to perform up to 100 calculations in a single session. 
It works by taking mathematical expression as a string and using the built-in eval() function to compute the result. 
To ensure stability, a try...except block safely handles any invalid expressions which prevents program from crashing. 
The user can exit the loop at any time by typing 'quit' without considering about casing.
'''