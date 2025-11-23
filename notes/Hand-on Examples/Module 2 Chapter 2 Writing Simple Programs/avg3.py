# avg3.py 
# A simple program to average three exam scores  
# Illustrates use of multiple input

def main(): 
    print("This program computes the average of three exam scores.") 
    score1, score2, score3 = eval(input("Enter three scores separated by commas: ")) 
    average = (score1 + score2 + score3) / 3  # Adjusted for three scores

    print("The average of the scores is:", average) 

main()


#Changes:
#Input for Three Scores: The eval(input(...)) line now expects the user to input three scores, separated by commas. For example, you would enter 85, 90, 78 to input three exam scores.
#Average Calculation: The formula for calculating the average is updated to include three scores: (score1 + score2 + score3) / 3.
