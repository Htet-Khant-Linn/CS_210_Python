'''
Write a program that calculates the area of a rectangle. The program should: 
• Ask the user to enter the width and height 
• Compute the area 
• Display the result 
'''

def cal_rec_area(width, height):
    rec_area = width * height
    return rec_area

def main():
    print("This program give the area of a rectangle.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    try:
        # accept the user's width and height inputs
        width_str, height_str = input("Please input the width and height of the rectangle seperated by comma (e.g; 10, 14): ").split(",")
        # change the input values to float
        width = float(width_str)
        height = float(height_str)

        # use if-else to check if width or height is negative
        if width < 0 or height < 0:
            print(f"Input Error: Dimension values cannot be negative. You entered width: {width_str} & height: {height_str}.")
        
        else:
            # calculate if the numbers are valid (zero or positive values)
            rec_area = cal_rec_area(width, height)
            print(f"The area of the rectangle with width [{width}] & height [{height}] is {rec_area}.")

    except ValueError:
        # Handles input errors such as not two number inputs or not two numerics
        print(f"Invalid Input: Please enter two numeric values separated by a comma.")
        print()

main()