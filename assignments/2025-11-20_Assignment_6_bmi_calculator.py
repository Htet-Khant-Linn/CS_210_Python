'''
    4. The body mass index (BMI) is calculated as a person's weight (in pounds) times 720, 
    divided by the square of the person's height (in inches). 
    A BMI in the range 19-25, inclusive, is considered healthy. 
    Write a program that calculates a person's BMI and 
    prints a message telling whether they are above, within, 
    or below the healthy range. 
Hints:
    • Formula: (weight × 720) ÷ (height²)
    • Healthy BMI: Between 19 and 25 (inclusive)
    • Checks if the BMI is:
        ◦ Less than 19 → Below healthy range
        ◦ Between 19 and 25 → Within healthy range
        ◦ Greater than 25 → Above healthy range
'''

# create the bmi_calculator function
def bmi_calculator(weight, height):

    # use try-except to catch the ZeroDivisionError
    try:
        # apply the given formula to calculate the bmi
        bmi = (weight * 720) / height**2

        # check if whether the bmi is greater than 0
        if bmi > 0:
            # create decision structure for BMI value
            if bmi < 19:
                print("Below healthy range.")
            elif bmi >= 19 and bmi <= 25:
                print("Within healthy range.")
            else:
                print("Above healthy range.")
        # print error message for nonsensical BMI value
        elif bmi == 0:
            print("Input Error: BMI value can't be equal to zero.")
            print(f"Your input: weight -> {weight}, height -> {height}.")

        # print error message for negative BMI value
        else:
            print("Input Error: BMI value can't be negative.")
            print(f"Your input: weight -> {weight}, height -> {height}.")

    # print error message for ZeroDivisionError
    except ZeroDivisionError:
        print("Zero division error: Height value can't be equal to zero.")
        print(f"Your input: weight -> {weight}, height -> {height}.")
    
def main():

    print()
    print("This program calculate body mass index (BMI) based on user input weight (lbs) and height (in).")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    # use try-except to catch the user-input ValueError
    try:
        # accept the user input
        user_input = input("Please enter your weight (in pounds) and height (in inches) separated by comma: ")
        # split by comma
        user_input_wt, user_input_ht = user_input.split(",")
        # convert to float value
        wt = float(user_input_wt)
        ht = float(user_input_ht)

        # apply the function
        bmi_calculator(wt, ht)

    # print the ValueError
    except ValueError:
        print("Input Error: Please enter valid weight (in pounds) and height (in inches) separated by a comma.")
        print(f"Your input: {user_input}")

if __name__ == "__main__":
    main()