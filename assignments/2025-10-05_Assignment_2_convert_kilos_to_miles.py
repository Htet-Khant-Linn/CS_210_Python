'''
2.	Write a program that converts distances measured in kilometers to miles. 
One kilometer is approximately 0.62 miles.
'''

def kilometers_to_miles(km):
    miles = km * 0.62
    return miles

def main():
    print("This program will convert distances measured in Kilometers to Miles")
    print("Developer: Htet Khant Linn")

    # accepting user input in float data type
    km = float(input("Please enter distance in kilometers: "))

    # calling kilometers_to_miles function and inputting user input
    miles = kilometers_to_miles(km)

    # print the result
    print(f"{km} kilometers is approximately {miles} miles.")
    print("\nThanks. Have a nice day.")

main()


'''
Explanation:
I have created the kilometers_to_miles function, which taks a distance in km and multiplies it by 0.62 to convert it to miles.
Then, in the main funciton, I created the float(input()) which accept the user input km and converts to float data type.
Then, I recall the kilometers_to_miles() to calculate the miles based on user input km. 
Finally, the result is printed out. 

'''