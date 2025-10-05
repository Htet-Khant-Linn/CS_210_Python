'''
3.	Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string.
'''

def count_vowels(string):
    # define the vowels
    vowels = "aeiouAEIOU"
    # create a variable to store the vowels count 
    count = 0
    
    # Loop through each character in the string
    for char in string:
        if char in vowels: # checking if char is in vowels
            count += 1 # increse the count by one if founded
    
    return count



def main():
    print("This program will count the number of vowels in your given string.")
    print("Developer: Htet Khant Linn")

    # get the user input
    user_input = input("Please type a sencence to count the vowels in it: ")

    # recall the count_vowels function
    vowel_count = count_vowels(user_input)


    print(f"\nThere are {vowel_count} vowel/s in your sentence.")
    print("\nThanks. Have a nice day.")

main()



'''
Explanation:

This program counts the total number of vowels (a, e, i, o, u) in a string provided by the user.
The main() function prompts the user to enter a string.
The input string is passed to the count_vowels() function. 
This function iterates through each character, check if it exists within the predefined vowel string "aeiouAEIOU". 
A counter increases for every match.

The final count is returned to main() and print the result.
'''