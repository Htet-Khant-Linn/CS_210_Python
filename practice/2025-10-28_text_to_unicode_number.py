'''
This is a program to convert a textual message into a sequence of numbers, 
utlilizing the underlying Unicode encoding.
'''


def main():
    print("This program will convert a textual message \
into a sequence of numbers that represents.\n")
    
    inputtxt = input("Please enter the message to encode: ")

    print("\nHere is the Unicode code: ")
    for ch in inputtxt:
        print(ord(ch), end = " ")

    # print a blank line before the prompt
    print()

main()