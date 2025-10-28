'''
This program will convert the content of input file to output file.

'''

def copy_file_content(input_filename, output_filename):
    try:
        # 'with' handles opening and automatically closing both files
        with open(input_filename, "r") as inputfile:
            content = inputfile.read()

        # inputfile.close()

        with open(output_filename, "w") as outputfile:
            outputfile.write(content)

        # outputfile.close()

        print(("The content form input file [{}] has been successfully copied to\
            the output file [{}].").format(input_filename, output_filename))
        
    except FileNotFoundError:
        print(("Error: The input file '{}' was not found.").format(input_filename))
    except IOError:
        print(("Error: There was an issue with writing or reading the file '{}'.").format(input_filename))

def main():
    input_filename = input("Enter the input file name (relative file path): ")
    output_filename = input("Enter the output filename (relative file path): ")

    copy_file_content(input_filename, output_filename)


main()

