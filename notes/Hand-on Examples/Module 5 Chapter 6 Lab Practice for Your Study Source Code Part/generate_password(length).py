# Write a function generate_password(length) that generates a random password of a given length using letters, numbers, and special characters.
# generate_password(length)

import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

"""
Example usage:
print(generate_password(12))
"""
