'''
    1. A certain CS professor gives 100-point exams 
    that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. 
    Write a program that accepts an exam score as input and 
    uses a decision structure to calculate the corresponding grade. 
Hints:
        ◦ if elif else
        ◦ print()

'''

# create grade checking function
def grade_calculator(score):
    # check whether the socre range is between 0 and 100
    if 0 <= score <= 100:
        # proceed the decision structure using if-elif-else
        if score >= 90:
            print("Your Grade is: A. Congratulation!")
        elif score >= 80:
            print("Your Grade is: B. Keep it up!")
        elif score >= 70:
            print("Your Grade is: C. Need more work!")
        elif score >= 60:
            print("Your Grade is: D. Meet with your mentor!")
        else:
            print("Your Grade is: F. Meet with the Dean ASAP!")
    else:
        print("Please insert the valid score between 0 and 100.")

def main():

    print()
    print("This program give the Grade based on input score.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    # use try-except to catch invalid input
    try:
        # accept the user input
        user_input_score = input("Please insert the score (0-100): ")
        # chenge the float data type
        score = float(user_input_score)

        # apply the function
        grade_calculator(score)
    
    # except value will catch the invalid input
    except ValueError:
        print("Input Error: Please inset the score between 0 and 100.")
        print(f"Your Input is '{user_input_score}'.")


if __name__ == "__main__":
    main()