'''
Write a program that takes two numbers as input and displays their: 
• Sum 
• Difference 
• Product 
• Quotient 
• Remainder
'''

def add(num_1, num_2):
    return num_1 + num_2

def difference(num_1, num_2):
    return num_1 - num_2

def product(num_1, num_2):
    return num_1 * num_2

def quotient(num_1, num_2):
    return num_1 // num_2

def remainder(num_1, num_2):
    return num_1 % num_2

def main():
    print("This program give the sum, difference, product, quotient, and remainder of two whole numbers.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    try:
        num_1_str, num_2_str = input("Please enter two numbers seperated by comma (e.g; 10, 14): ").split(",")

        num_1 = int(num_1_str)
        num_2 = int(num_2_str)
        
        print("The calculation results are: ")
        print()
        print(f"Sum of [{num_1}] and [{num_2}]: {add(num_1, num_2)}")
        print(f"Difference of [{num_1}] and [{num_2}]: {difference(num_1, num_2)}")
        print(f"Product of [{num_1}] and [{num_2}]: {product(num_1, num_2)}")

        # checking for zero division error
        if num_2 == 0:
            print(f"Quotient of [{num_1}] and [{num_2}]: Error! Cannot be divided by zero.")
            print(f"Remainder of [{num_1}] and [{num_2}]: Error! Cannot be divided by zero.")
        else:
            print(f"Quotient of [{num_1}] and [{num_2}]: {quotient(num_1, num_2)}")
            print(f"Remainder of [{num_1}] and [{num_2}]: {remainder(num_1, num_2)}")
        
        print()

    except ValueError:
        print("Input Error: Please enter two valid whole numbers separated by a comma.")


main()