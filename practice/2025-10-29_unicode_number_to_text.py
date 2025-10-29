'''
This program converts a sequence of unicode number into the string of text that it represents.
'''


def main():

    print("This program converts a sequence of unicode number into \
the string of text that it represents.\n")
    
    # accept the user input
    input_str = input("Please enter the Unicode code message: ")

    # create a message string
    message = ""

    # for loop to loop through Unicode number splitted by space
    for num_str in input_str.split():
        try:
            # convert the sub-string to a number
            num_int = int(num_str)

            # append character to message
            message += chr(num_int)

        except ValueError:
            print(f"Invalid Input: [{num_str}] is not a valid Unicode code.")
            continue # this will continue the program while showing only the error character

        except Exception as e:
            print(f"An error occured: {e}")
            continue

    print(f"\n The decoded message is: {message}")

main()
