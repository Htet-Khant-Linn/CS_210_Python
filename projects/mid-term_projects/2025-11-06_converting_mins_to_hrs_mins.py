'''
Write a program that converts minutes into hours and remaining minutes. 
Example: 135 minutes is 2 hours and 15 minutes.
'''

def hours_mins_convert(input_mins):
    hours, mins = input_mins // 60, input_mins % 60
    print(f"{input_mins} minutes is {hours} hours and {mins} minutes.")

def main():
    print("This program converts minutes into hours and remaining minutes.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    try:
        input_mins = input("Please enter the minutes: ")
        mins = int(input_mins)
        if mins < 0:
            print("Input Errors: Time values cannot be negative.")
            print(f"Your input is [{input_mins}].")
        else:
            hours_mins = hours_mins_convert(mins)
            return hours_mins
    except ValueError:
        print("Input Error: Please enter valid integer values.")
        print(f"Your input is [{input_mins}].")

main()
