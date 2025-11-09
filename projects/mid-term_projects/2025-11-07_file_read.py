'''
Create a text file called greetings.txt containing a few lines of text. 
Then write a Python program to: 
• Open and read the file 
• Print each line on the screen
'''

def print_each_line(filename):

    # use try-except to handle potential file errors
    try:
        print()
        print(f"Opening and reading the file [{filename}]...")
        print()

        # read the file using with open
        # use r mode for file reading
        with open(filename, "r") as infile:
            # .readlines() reads all the lines into a list
            lines = infile.readlines()

            # loop through each line in the list
            for line in lines:
                print(line.strip())     # .strip() remove the newline character
            print("--- End ---")


    # add except to catch the errors
    # this catch the error if the file doesn't exist
    except FileNotFoundError:
        print(f"Error: The file [{filename}] was not found. Please try again.")

    # this catch other issues like not haivng permission to read the file
    except IOError:
        print(f"Error: There was an issue with reading the file [{filename}].")

def main():
    # get the file path from the user
    filename = input("Enter the filename: ")
    # Can test with [projects\mid-term_projects\greeting.txt]
    
    print_each_line(filename)

main()