# month2.py
#  A program to print the month name, given it's number.
#  This version uses a list as a lookup table.

def main():
    
    # months is a list used as a lookup table
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              #"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    """
    months = ["January", "February", "March", 
           "April", "May", "June", "July",
           "August", "September", "October",
           "November", "December"]

    
    n = int(input("Enter a month number (1-12): "))

    print ("The month abbreviation is", months[n-1] + ".")

main()
