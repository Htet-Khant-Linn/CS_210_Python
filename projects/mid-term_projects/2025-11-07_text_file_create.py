'''
This py file create the text file name called "greeting.txt".
'''

try:
    with open("projects\mid-term_projects\greeting.txt", "x") as infile:
        infile.write("Hello Everyone.\n")
        infile.write("My name is Htet Khant Linn.\n")
        infile.write("I am attending at Parami University, majoring in Statistics and Data Science.\n")
        infile.write("My favorite major is CS210.\n")
        infile.write("Nice to meet you all.")

except FileExistsError:
    print("Error: 'greeting.txt' already exists.")  