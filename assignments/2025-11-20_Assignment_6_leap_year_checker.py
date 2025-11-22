'''
    3. A year is a leap year if it is divisible by 4, 
    unless it is a century year that is not divisible by 400. 
    (1800 and 1900 are not leap years while 1600 and 2000 are.) Write a program that calculates whether a year is a leap year. 
Hints: 
    • Example: 1800 and 1900 are divisible by 100 but not by 400 → Not leap years.
    • 1600 and 2000 are divisible by both 100 and 400 → Leap years.
'''

# create the function to check the leap year
def check_leap_year(year):
    # use if-else to check whether the input value is non-negative
    if year >= 0:
        # apply the leap-year calculation formula
        # use if-else to check the leap-year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
        # this will print error message if the input is negative value
    else:
        print(f"Invalid Input: Your input is '{year}'. The year value can't be negative.")

def main():

    print()
    print("This program checks whether the year is a leap year or not.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    # use try-except to catch the valueError
    try:
        # accept the user input
        user_input_year = input("Please enter a year: ")
        # change the input data to int
        year = int(user_input_year)
        # apply the function
        check_leap_year(year)

    except ValueError:
        print("Input Error: Please enter a valid year.")


if __name__ == "__main__":
    main()
