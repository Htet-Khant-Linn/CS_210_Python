'''
Htet Khant Linn
Assignment 3

1.	Write a program that determines the distance to a lightning strike based on 
the time elapsed between the flash and the sound of thunder. 
The speed of sound is approximately 1100 ft/ sec, and 1 mile is 5280 ft.
'''

def dist_lighting_strike_in_mile(time):
    distance_in_ft = time * 1100 
    # The speed of sound = 1100ft/sec (approx.)

    distance_in_mile = distance_in_ft /5280
    # 1 mile = 5280 ft

    return distance_in_mile

def main():
    print("This program will give the distance (in miles) to a " \
    "lighting strike based on the time elapsed between the flash "\
    "and the sound of the thunder.\n")
    print("Developed by Htet Khant Linn.")
    print("------------------------------")

    time_elapsed = float(input("Please enter the time elapsed (in seconds) between the flash and the sound of thunder: "))
    distance_in_mile = dist_lighting_strike_in_mile(time_elapsed)

    print(f"The lighting strike is {distance_in_mile:.2f} mile/s away from you. Be safe!")
    # priting the output by rounding to two decimal places
main()

'''
Explanation:
My program calculates the distance to a lighting strike in miles.
I use the main function that handles user input (the time elapsed (in seconds) between the flash and the sound of thunder)
and passed the input time value (time_elapsed) into the dist_lighting_strike_in_mile function. 
This function first calculates the total distance in feet by multiplying the time by the speed of the sound (1100 ft/sec).
It then converts this distance to miles by dividing the result by 5280.
Finally, this function returns the distance in miles to the main function,
which further prints the formatted answers by rounding to two decimal places. 
'''