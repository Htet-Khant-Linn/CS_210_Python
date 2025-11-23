# numbers2text.py
# A program to convert a sequence of Unicode numbers into
# a string of text.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Initialize an empty string to build the message
    message = ""

    # Loop through each substring and build the Unicode message
    for numStr in inString.split():
        try:
            # Convert the (sub)string to a number
            codeNum = int(numStr)
            # Append character to message
            message += chr(codeNum)
        except ValueError:
            # Handle the case where the input is not a valid number
            print(f"Invalid input: '{numStr}' is not a valid number. Skipping.")
            continue
        except Exception as e:
            # Catch any other exceptions
            print(f"An error occurred: {e}")
            continue

    # Output the decoded message
    print("\nThe decoded message is:", message)

# Run the program
main()
