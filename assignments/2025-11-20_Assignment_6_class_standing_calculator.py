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

def class_standing_calculator(credits):
    if credits > 0:
        if credits >= 26:
            print("Senior")
        elif credits >= 16:
            print("Junior")
        elif credits >= 7:
            print("Sophomore")
        else:
            print("Freshman")
    else:
        print("Input Error: Credit Score can't be negative value.")

def main():

    print()
    print("This program classifies students according to credits earned.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")


    try:
        user_input_credit = input("Please enter the number of credit earned: ")
        credits = float(user_input_credit)

        print("Student's year is: ")
        class_standing_calculator(credits)

    except ValueError:
        print("Value Error: Please enter the valid credit score.")

    
if __name__ == "__main__":
    main()
    
        