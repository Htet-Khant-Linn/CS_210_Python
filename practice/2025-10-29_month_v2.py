'''
This program print the month name, given its number. 
'''
months = ["January", "February", "March",
          "April", "May", "June", "July",
          "August", "September", "October",
          "November", "December"]

def main():
    try:
        input_month_num = input("Enter a month number (1-12): ")

        n = int(input_month_num)
        if 1 <= n <= 12:
            pos = n - 1
            print(f"The month name is {months[pos]}.")
        else:
            print(f"Invalid input: Your input [{n}] is not a number between 1 and 12.")

    except ValueError:
        print(f"Invalid input: Your input [{input_month_num}] is invalid.")

main()
