'''
This program will change the input date format (mm-dd-yyyy) to
a new desire data format "Month Day, Year"
'''

def main():
    # accept the user input in mm-dd-yyyy date fornat
    input_date_str = input("Please enter the date in the following format (mm-dd-yyyy): ")

    # extract month, day, year from user input
    month_str, day_str, year_str = input_date_str.split('-')

    # change month_num from str to int
    month_num = int(month_str)

    months = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]
    # adjust the month index
    month_name = months[month_num - 1]

    # create a new date format to print out
    new_date_str = f"{month_name} {int(day_str)}, {year_str}"

    print(f"The new date format is: {new_date_str}")


main()
