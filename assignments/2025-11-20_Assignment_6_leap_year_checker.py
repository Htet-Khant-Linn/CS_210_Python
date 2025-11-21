'''
    3. A year is a leap year if it is divisible by 4, 
    unless it is a century year that is not divisible by 400. 
    (1800 and 1900 are not leap years while 1600 and 2000 are.) Write a program that calculates whether a year is a leap year. 
Hints: 
    • Example: 1800 and 1900 are divisible by 100 but not by 400 → Not leap years.
    • 1600 and 2000 are divisible by both 100 and 400 → Leap years.
'''

def check_leap_year(year):
    if year > 0:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"Invalid Input: Your input is '{year}'. The year value can't be a negative.")

def main():

    print()
    print("This program give check whether the year is a leap year or not.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")


    try:
        user_input_year = input("Please enter a year: ")
        year = int(user_input_year)

        check_leap_year(year)

    except ValueError:
        print("Input Error: Please enter the valid year.")


if __name__ == "__main__":
    main()
