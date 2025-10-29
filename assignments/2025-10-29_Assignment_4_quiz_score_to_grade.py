'''
1.	A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as an input and prints out the corresponding grade.
Hints:
•  The program asks the user to input a quiz score. 
•  It checks the score using if-elif statements: 
If the score is 5, it prints "Grade: A".
If the score is 4, it prints "Grade: B".
If the score is 3, it prints "Grade: C".
If the score is 2, it prints "Grade: D".
If the score is 1 or 0, it prints "Grade: F".
•  If the score is outside the range of 0 to 5, the program prints an error message.


'''
# create the dict that match socre and grade
grades = {5 : "A", 
          4 : "B", 
          3 : "C", 
          2 : "D", 
          1 : "F", 
          0 : "F"}


def main():
    print("This program give the grade of the input score.\n")
    print("Developed by Htet Khant Linn.")
    print("------------------------------")
    # accept the user input
    input_text = input("Please enter the quize score (0-5): ")

    # include try-except to handle error such as user inputing invalid string
    try:
        # convert the input to int
        input_score  = int(input_text)
        
        # call the grade from dict using .get()
        grade = grades.get(input_score)

        # if not found in dict, it will return None
        # This handle the error if the socre not between 0 and 5
        if grade is not None:
            print(f"Your Grade is [{grade}]")

        # print the error message if the socre not between 0 and 5
        else:
            print("Error: The input socre must be between 0 and 5.")

    # except handle invalid input like string
    except ValueError:
        print(f"Error: The input '{input_text}' is not a valid integer. Please try again.\n")

        
main()

'''
Explanation:
In this program I try to create a program that gets a score from the user 
and uses a dictionary to find the matching grade. 
Although the hint mention about the 'if-else' method, 
I try to stick with the sample answer and modified 
to show the more details error using the combination of if-else and try-except, 
printing one message for invalid text (like "hkl") 
and another for valid numbers outside the 0-5 range.
'''