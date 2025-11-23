#Calculate Power (Exponentiation)
#Write a Python program to compute the result of a number raised to a given power n

def power(a, b):
    return a ** b

# Input from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power {exponent} is {power(base, exponent)}")


