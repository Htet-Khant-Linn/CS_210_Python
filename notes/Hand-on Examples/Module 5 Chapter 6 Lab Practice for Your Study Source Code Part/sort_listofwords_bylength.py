# Write a function sort_by_length(words) that takes a list of words and returns them sorted by length.
# Sort List of Words by Length

def sort_by_length(words):
    return sorted(words, key=len)

#Example usage

word_list = ["apple", "kiwi", "banana", "fig", "cherry"]
sorted_words = sort_by_length(word_list)
print(sorted_words)

