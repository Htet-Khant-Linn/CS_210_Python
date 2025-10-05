'''
1.	Modify the avg2. py program to find the average of three exam scores. 
'''


# Modifying to calculate avarage three exam scores
def main(): 
    print("This program computes the average of three exam scores.")
    print("Developer: Htet Khant Linn")

    # create there variables to accept the three exam scores. 
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: ")) 
    
    # calculate the average of three exam scores by diving with 3
    average = (score1 + score2 + score3)/3

    # print out the result
    print(f"The avarage scores for {score1}, {score2}, {score3} is:")
    print(f">>> {average}")
    print("\nThanks. Have a nice day.")

main()


'''
Explanation:
I added another variable score 3 and changed the average, which is divided by 3. 
The updated version will calculate the average of three exam scores. 

'''