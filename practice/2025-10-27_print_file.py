'''
This program prints the first five line of a txt file.
'''

def print_first_five_line(filename):
    try:
        # read the file using with open
        with open(filename, "r") as infile:
            # loop through the first five line
            for i in range(5):
                line = infile.readline()
                if not line:    # break if found an empty line
                    break
                print(line.strip()) 
                # strip remove the invisible character from beginning and end of the line

    # add except to catch the errors
    except FileNotFoundError:
        print(f"Error: The file [{filename}] was not found. Please try again.")
    except IOError:
        print(f"Error: There was an issue with reading the file [{filename}].")

def main():
    filename = input("Enter the filename: ")
    # Can test with [resources\hello.txt]
    print_first_five_line(filename)

main()