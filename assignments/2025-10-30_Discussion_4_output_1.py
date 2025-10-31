s1 = "spam" 
s2 = "ni!" 

print()

# a) "The Knights who say, " + s2
print("a)", end=" ")
print("The Knights who say, " + s2)
# this join the first string with the value of s2
print("========\n")

# b) 3 * s1 + 2 * s2
print("b)", end=" ")
print(3 * s1 + 2 * s2)
# the * operator repeats the string. 
# 3 * s1 is "spamspamspam" and 2 * s2 is "ni!ni!". 
# The + then concatenates them.
print("========\n")

# c) s1 [1]
print("c)", end=" ")
print(s1[1])
# give the chaacter at index 1
print("========\n")


# d) s1[1:3]
print("d)", end=" ")
print(s1[1:3])
# string slice - gets character starting at index 1 and before index 3
print("========\n")

# e) s1 [2] + s2 [ : 2]
print("e)", end=" ")
print(s1[2] + s2[:2])
# this is the combination of indexig and slicing
# s1[2] is the character at index 2 of "spam", which is 'a'
# s2[:2] is a slice from the beginning of "ni!" up to index 2, which is "ni"
print("========\n")

# f) s1 + s2 [ -1]
print("f)", end=" ")
print(s1 + s2[-1])
# s2[-1] uses negative indexing to get the last character of s2, which is '!' 
# This is then concatenate with s1.
print("========\n")

# g) s1.upper()
print("g)", end=" ")
print(s1.upper())
# upper() method change the string into Uppercase
print("========\n")

# h) s2.upper() .l just(4) * 3
print("h)", end=" ")
print(s2.upper().ljust(4) * 3)
# .ljust(4) is "left justifies" and add white spaces on the right to make it 4 characters long
# then * 3 repeats the 4 character string three times
print("========\n")

