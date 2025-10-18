'''
3. Write a program to find the sum of the first n natural numbers, where the value of n is provided by the user.

Formula: sum = n(n+1)/2
'''

def sum_of_natural_numbers(n):
    total_sum = n * (n+1)//2 # use // to avoid decimal result
    return total_sum

def is_natural_number(n):
    # natural number start from 1, so checking whether it is greater than 1.
    return n >= 1

def main():
    print("This program find the sum of the first n natural numbers.\n")
    print("Developed by Htet Khant Linn.")
    print("------------------------------")

    try:
        user_input_str = input("Please enter a natural number (n): ")
        user_input_num = int(user_input_str)

        if is_natural_number(user_input_num):
            total_sum = sum_of_natural_numbers(user_input_num)
            
            print(f"The sum of the first {user_input_num} natural numbers is {total_sum}.")

        else:
            # handle integers that are not natural numbers (0 or negatives)
            print(f"Your input {user_input_num} is not a natural number (1 or greater). Please try again.")
    
    except ValueError:
        # to hanlde non-integer value
        print(f"Invalid input. Your input [{user_input_str}] is not a natural number (1 or greater). Please try again.")


main()
