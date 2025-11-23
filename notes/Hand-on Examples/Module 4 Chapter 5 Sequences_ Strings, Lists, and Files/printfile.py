# printfile.py
#     Prints a file to the screen.

"""
def main():
    fname = input("Enter filename: ")
    infile = open(fname,'r')
    data = infile.read()
    print(data)

main()
"""

"""
infile = open(someFile.txt, "r")
for i in range(5):
	line = infile.readline()
	print(line[:-1])
"""

# Improved version with proper file handling and error checking

def print_first_five_lines(filename):
    try:
        with open(filename, "r") as infile:
            for i in range(5):
                line = infile.readline()
                if not line:  # Check if the line is empty, meaning end of file
                    break
                print(line[:-1])  # Remove the newline character
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")

# Example usage:
filename = input("Enter the filename: ")
print_first_five_lines(filename)

