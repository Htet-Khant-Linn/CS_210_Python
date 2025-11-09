'''
Write a program that takes two numbers as input and displays their: 
• Sum 
• Difference 
• Product 
• Quotient 
• Remainder
'''
# create add function
def add(num_1, num_2):
    return num_1 + num_2

# create difference function
def difference(num_1, num_2):
    return num_1 - num_2

# create product function
def product(num_1, num_2):
    return num_1 * num_2

# create quotient function
def quotient(num_1, num_2):
    return num_1 // num_2

# create remainder function
def remainder(num_1, num_2):
    return num_1 % num_2

def main():
    print("This program give the sum, difference, product, quotient, and remainder of two whole numbers.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    try:
        # accept the user input - two numbers
        num_1_str, num_2_str = input("Please enter two numbers seperated by comma (e.g; 10, 14): ").split(",")

        # change the input into float data types
        num_1 = float(num_1_str)
        num_2 = float(num_2_str)
        

        print("The calculation results are: ")
        print()
        print(f"Sum of [{num_1}] and [{num_2}]: {add(num_1, num_2):.2f}")
        print(f"Difference of [{num_1}] and [{num_2}]: {difference(num_1, num_2):.2f}")
        print(f"Product of [{num_1}] and [{num_2}]: {product(num_1, num_2):.2f}")

        # checking for zero division error
        if num_2 == 0:
            print(f"Quotient of [{num_1}] and [{num_2}]: Error! Cannot be divided by zero.")
            print(f"Remainder of [{num_1}] and [{num_2}]: Error! Cannot be divided by zero.")
        else:
            print(f"Quotient of [{num_1}] and [{num_2}]: {quotient(num_1, num_2):.2f}")
            print(f"Remainder of [{num_1}] and [{num_2}]: {remainder(num_1, num_2):.2f}")
        
        print()

    # Handles errors if the input isn't a number or if the input is less than or more than 2 values
    except ValueError:
        print("Input Error: Please enter two valid whole numbers separated by a comma.")


main()