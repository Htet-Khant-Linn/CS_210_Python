def read_from_file():
    with open("myfile.txt", "r") as file:
        content = file.read()
        print(content)

# Test
read_from_file()  # Output: "Hello, World!"
