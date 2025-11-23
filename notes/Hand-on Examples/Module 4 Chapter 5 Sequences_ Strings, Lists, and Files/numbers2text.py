# numbers2text.py
#     A program to convert a sequence of Unicode numbers into
#         a string of text.

def main():
    print ("This program converts a sequence of Unicode numbers into")
    print ("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicde message
    message = ""
    for numStr in inString.split():
        # convert the (sub)string to a number
        codeNum = int(numStr)
        # append character to message
        message = message + chr(codeNum) 

    print("\nThe decoded message is:", message)
main()

# numbers2text.py
# A program to convert a sequence of Unicode numbers into
# a string of text.

"""
def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Initialize the message string
    message = ""

    # Loop through each substring and build the Unicode message
    for numStr in inString.split():
        try:
            # Convert the (sub)string to a number
            codeNum = int(numStr)
            # Append character to message
            message += chr(codeNum)
        except ValueError:
            print(f"Invalid number: '{numStr}' is not a valid Unicode number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

    # Output the decoded message
    print("\nThe decoded message is:", message)

main()
"""
