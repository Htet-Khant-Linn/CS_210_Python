# Count Words in a Sentence
# Write a function count_words(sentence) that takes a sentence and returns a dictionary where keys are words and values are their occurrences.

def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word = word.strip(".,!?;:")  # Remove punctuation
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

"""
Example usage:
count_words ("Today is a blessed day!")
"""
