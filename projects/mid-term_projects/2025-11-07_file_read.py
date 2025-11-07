'''
Create a text file called greetings.txt containing a few lines of text. 
Then write a Python program to: 
• Open and read the file 
• Print each line on the screen
'''

def print_each_line(filename):
    try:
        # read the file using with open
        print()
        print(f"Opening and reading the file [{filename}]...")
        print()
        with open(filename, "r") as infile:
            # loop through the first five line
            lines = infile.readlines()
            for line in lines:
                print(line.strip())
            print("--- End ---")


    # add except to catch the errors
    except FileNotFoundError:
        print(f"Error: The file [{filename}] was not found. Please try again.")
    except IOError:
        print(f"Error: There was an issue with reading the file [{filename}].")

def main():
    filename = input("Enter the filename: ")
    # Can test with [projects\mid-term_projects\greeting.txt]
    print_each_line(filename)

main()