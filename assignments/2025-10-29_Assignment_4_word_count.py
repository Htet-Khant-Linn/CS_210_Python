'''
2.	Write a program that counts the number of words in a sentence entered by the user.
Hints: 
•	The program asks the user to enter a sentence. 
•	The split() method is called on the sentence, which splits the sentence into words based on spaces. 
•	The len() function is used to count the number of words in the resulting list. 
•	Finally, the program prints the word count.

'''
# print("htet khant linn".split())

def word_counter(sentence):

    # this will store the split word in list
    words = sentence.split()
    word_count = len(words)
    return word_count

def main():

    print("This program give the total number of words in your sentence.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    input_text = input("Please enter a sentence: ")

    word_count = word_counter(input_text)

    print(f"There are a total of {word_count} word/s in your sentence.")

main()

'''
Explanation:

This program asks for a sentence and uses the .split() method 
to break it into a list of words,
and then uses len() to count how many words are in that list.
'''