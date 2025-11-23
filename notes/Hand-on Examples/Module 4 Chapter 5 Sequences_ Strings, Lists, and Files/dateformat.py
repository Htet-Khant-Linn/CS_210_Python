#dateformat.py
#Input the date in mm/dd/yyyy format (dateStr)
#Create a new date string in the form “Month Day, Year”

def main():
    # Step 1: Input the date in mm/dd/yyyy format
    dateStr = input("Please enter the date (mm/dd/yyyy): ")

    # Step 2: Split dateStr into month, day, and year strings
    month_str, day_str, year_str = dateStr.split('/')

    # Step 3: Convert the month string into a month number
    month_num = int(month_str)

    # Step 4: Use the month number to look up the month name
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]

    # Get the month name from the list using the month number (adjusting for 0-based indexing)
    month_name = months[month_num - 1]

    # Step 5: Create a new date string in the form “Month Day, Year”
    new_date_str = f"{month_name} {int(day_str)}, {year_str}"

    # Step 6: Output the new date string
    print("The formatted date is:", new_date_str)

# Run the program
main()
