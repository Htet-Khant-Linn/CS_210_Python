def average_word_length(sentence):
    words = sentence.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Get user input
sentence = input("Enter a sentence: ")
avg_length = average_word_length(sentence)
print(f"The average word length is: {avg_length:.2f}")


"""
Enter a sentence: The quick brown fox jumps over the lazy dog

Processing:

Words: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

Total character count: 3 + 5 + 5 + 3 + 5 + 4 + 3 + 4 + 3 = 35

Number of words: 9

Average word length: 35 / 9 = 3.89

The average word length is: 3.89  
"""
