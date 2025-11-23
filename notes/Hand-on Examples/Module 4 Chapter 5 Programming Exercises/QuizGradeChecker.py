def get_grade(score):
    grades = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'F', 0: 'F'}
    return grades.get(score, 'Invalid score')

# Get user input
try:
    score = int(input("Enter the quiz score (0-5): "))
    print(f"The corresponding grade is: {get_grade(score)}")
except ValueError:
    print("Please enter a valid integer between 0 and 5.")
