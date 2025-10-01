# Function to convert kilometers to miles
def kilometers_to_miles(km):
    miles = km * 0.62
    return miles

# Get user input for distance in kilometers
km = float(input("Enter distance in kilometers: "))

# Convert the kilometers to miles
miles = kilometers_to_miles(km)

# Display the result
print(f"{km} kilometers is approximately {miles} miles.")


#Explanation:
#kilometers_to_miles(km): A function that takes a distance in kilometers and multiplies it by 0.62 to convert it to miles.
#input(): Prompts the user to input the distance in kilometers.
#float(): Converts the input into a floating-point number for precision.
#The result is then printed out in a formatted string.
