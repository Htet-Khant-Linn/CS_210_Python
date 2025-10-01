# Program to count the number of vowels in a string

def count_vowels(string):
    # Define the vowels
    vowels = "aeiouAEIOU"
    # Initialize a variable to count vowels
    count = 0
    
    # Loop through each character in the string
    for char in string:
        if char in vowels:
            count += 1
    
    return count

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to count vowels and display the result
vowel_count = count_vowels(user_input)
print(f"The number of vowels in the string is: {vowel_count}")


#Explanation:
#Function count_vowels(string): This function takes a string and counts how many vowels are present. It iterates over each character in the string and checks if the character is a vowel (both lowercase and uppercase vowels are considered).
#Input from User: The program asks the user to enter a string using the input() function.
#Counting Vowels: The program calls count_vowels() to count how many vowels are in the entered string and stores the result in vowel_count.
#Output: The program prints the number of vowels in the input string.
