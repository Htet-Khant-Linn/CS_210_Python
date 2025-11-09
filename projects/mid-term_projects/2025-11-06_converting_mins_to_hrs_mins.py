'''
Write a program that converts minutes into hours and remaining minutes. 
Example: 135 minutes is 2 hours and 15 minutes.
'''

# create a function to convert mins to hours and remaining minutes
def hours_mins_convert(input_mins):
    # use integer division and remainder operator
    hours, mins = input_mins // 60, input_mins % 60
    print(f"{input_mins} minutes is {hours} hours and {mins} minutes.")


def main():
    print("This program converts minutes into hours and remaining minutes.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    try:
        # accept the user input
        input_mins = input("Please enter the minutes: ")

        # change the user input into int data type
        mins = int(input_mins)

        # check for invalid negative input values
        if mins < 0:
            print("Input Errors: Time values cannot be negative.")
            print(f"Your input is [{input_mins}].")

        # if not negative carry out the conversion
        else:
            hours_mins_convert(mins)
    
    # check invalid input like floats, and strings
    except ValueError:
        print("Input Error: Please enter valid integer values.")
        print(f"Your input is [{input_mins}].")

main()
