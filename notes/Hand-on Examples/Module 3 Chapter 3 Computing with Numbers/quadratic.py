# quadratic.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library.
#    Note: This program crashes if the equation has no real roots.

import math  # Makes the math library available.

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    # Calculate the discriminant
    discriminant = b * b - 4 * a * c

    # Check if the discriminant is negative
    if discriminant < 0:
        print("This equation has no real solutions.")
    else:
        # Calculate the real roots
        discRoot = math.sqrt(discriminant)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        # Output the solutions
        print()
        print("The solutions are:", root1, root2)

# Call the main function to run the program
main()


"""
discRoot = math.sqrt(b * b - 4 * a * c)
root1 = (-b + discRoot) / (2 * a)
root2 = (-b - discRoot) / (2 * a)

print()
print("The solutions are:", root1, root2 )

main()

# Calculate the discriminant
    discriminant = b * b - 4 * a * c

    # Check if the discriminant is negative
    if discriminant < 0:
        print("This equation has no real solutions.")
    else:
        # Calculate the real roots
        discRoot = math.sqrt(discriminant)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        # Output the solutions
        print()
        print("The solutions are:", root1, root2)

# Call the main function to run the program
main()
"""
