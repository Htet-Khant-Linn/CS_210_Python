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

    width_str, height_str = input("Please input the width and height of the rectangle seperated by comma (e.g; 10, 14): ").split(",")
    try:
        width = float(width_str)
        height = float(height_str)
        if width and height < 0:
            if width < 0:
                print("Your width [{width_str}] can't be a negative value.")
            elif height < 0:
                print("Your height [{height_str}] can't be a negative value.")
            else:
                print("Your width [{width_str}] & height [{height_str} can't be a negative value.]")
        reac_area = cal_rec_area(width, height)

        print(f"The area of the rectagle with width [{width}] & height [{height}] is {reac_area}.")

    except ValueError:
        print("Invalid Input: Your input width:{width_str} & height:{height_str} is not a valid numeric input.")

main()