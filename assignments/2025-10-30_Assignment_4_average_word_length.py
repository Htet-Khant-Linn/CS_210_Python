'''
3.	Write a program that calculates the average word length in a sentence entered by the user.
Hints: 
•	split() is used to break the sentence into individual words. 
•	sum(len(word) for word in words) calculates the total number of characters in all words. 
•	The average is calculated by dividing the total length by the number of words. 
•	The program handles edge cases, such as if the sentence is empty or contains no words.

'''


def avg_word_length_counter(sentence):
    # split the sentence into words
    words = sentence.split()

    # return 0 if the input is null
    if not words:
        return 0
    
    else:
        # count the total no. of words in the sentence.
        words_count = len(words)

        # create a var to store the total length
        total_length = 0
        # create for looping to count and add the words length
        for word in words:
            total_length += len(word)

        # calcualte the avarage length
        avg_word_length = total_length/words_count

        return avg_word_length
    
def main():

    print("This program give the avarage word length in your sentence.")
    print("Developed by Htet Khant Linn.")
    print("------------------------------\n")

    # accept the user input
    user_input = input("Please enter a sentence: ")

    # use the avg_word_length_counter function
    avg_word_length = avg_word_length_counter(user_input)

    # format the output to 2 decimal places
    print(f"The average word length is {avg_word_length:.2f}.")

main()
