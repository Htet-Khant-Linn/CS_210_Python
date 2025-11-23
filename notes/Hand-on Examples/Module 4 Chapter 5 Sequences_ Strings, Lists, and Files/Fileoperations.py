#Fileoperations.py

def copy_file_content(input_filename, output_filename):
    try:
        # Open the input file in read mode
        infile = open(input_filename, 'r')
        # Read the content of the input file
        content = infile.read()
        
        # Manually close the input file after reading
        infile.close()

        # Open the output file in write mode
        outfile = open(output_filename, 'w')
        # Write the content to the output file
        outfile.write(content)
        
        # Manually close the output file after writing
        outfile.close()
        
        print(f"Content copied successfully from {input_filename} to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")

# Example usage
input_filename = input("Enter the name of the input file: ")
output_filename = "output.txt"
copy_file_content(input_filename, output_filename)
