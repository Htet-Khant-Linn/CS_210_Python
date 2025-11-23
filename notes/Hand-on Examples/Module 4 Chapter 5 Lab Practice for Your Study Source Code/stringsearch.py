def find_substring(s, sub):
    return sub in s

# Test
print(find_substring("Hello World", "World"))  # Output: True
print(find_substring("Hello World", "Python"))  # Output: False
