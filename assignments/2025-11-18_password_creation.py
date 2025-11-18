'''
4.	Write a function is_strong_password(pwd) that returns True if a password:
•	Is at least 8 characters long
•	Contains at least one uppercase letter
•	Contains at least one lowercase letter
•	Contains at least one digit
Hints:
•	isupper()
•	islower()
•	isdigit()


'''
# create function
def is_strong_password(pwd):
    # check if the length is at least 8
    if len(pwd) < 8:
        return False
    
    # create has_upper, has_lower, and has_digit to store False
    has_upper = False
    has_lower = False
    has_digit = False

    # loop through each characters in the pwd to check whether it meets with the requirements
    for char in pwd:
        # check for upper char and if there is at least one upper then it will change has_upper to True
        if char.isupper():
            has_upper = True
        # check for lower char
        elif char.islower():
            has_lower = True
        # check for digit
        elif char.isdigit():
            has_digit = True

    # check process will return True only if all the three variables has_upper, has_lower and has_digit are true
    check_process = has_upper and has_lower and has_digit

    return check_process


# test

print(f"Test1: {is_strong_password("htetkhantlinn")}")
print(f"Test2: {is_strong_password("Htet Khant Linn")}")
print(f"Test3: {is_strong_password("Htet Khant Linn 123")}")
print(f"Test4: {is_strong_password("123")}")