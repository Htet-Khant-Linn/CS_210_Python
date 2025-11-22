'''
    2. A certain college classifies students according to credits earned. 
    A student with less than 7 credits is a Freshman. 
    At least 7 credits are required to be a Sophomore, 
    16 to be a Junior and 26 to be classified as a Senior. 
    Write a program that calculates class standing from the number of credits earned.  
Hints: 
        ◦ if elif else
        ◦ print()

'''

# create a function to check class standing based on the student's credits
def class_standing_calculator(credits):
    # check for negative credits
    if credits >= 0:
        # create the decision structure using if-elif-else
        if credits >= 26:
            print("Senior")
        elif credits >= 16:
            print("Junior")
        elif credits >= 7:
            print("Sophomore")
        else:
            print("Freshman")
    else:
        # will print an error message if the input is negative credit value
        print("Input Error: Credit Score can't be negative value.")

def main():

    print()
    print("This program classifies students according to credits earned.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    # use try-except to catch invalid inputs
    try:
        # accept the user input
        user_input_credit = input("Please enter the number of credit earned: ")
        # change the data type for float
        credits = float(user_input_credit)

        # print out the result
        print("Student's year is: ")
        class_standing_calculator(credits)  # call the function

    # use except to catch valueError
    except ValueError:
        print("Value Error: Please enter the valid credit score.")

    
if __name__ == "__main__":
    main()
    
        