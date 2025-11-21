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

def bmi_calculator(weight, height):
    bmi = (weight * 720) / height**2
    if bmi > 0:
        if bmi < 19:
            print("Below healthy range.")
        elif bmi >= 19 and bmi <= 25:
            print("Within healthy range.")
        else:
            print("Above healthy range.")
    else:
        print("BMI value can't be negative.")
    
def main():
    user_input_wt, user_input_ht = input("Please enter your weight and height (in pounds) seperated by comma: ") 