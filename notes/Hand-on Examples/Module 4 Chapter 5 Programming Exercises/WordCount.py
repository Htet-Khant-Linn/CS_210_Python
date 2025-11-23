def count_words(sentence):
    words = sentence.split()
    return len(words)

# Get user input
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"The number of words in the sentence is: {word_count}")
