'''
5.	Modify the convert. py program with a loop so that it executes 5 times before quitting. 
Each time through the loop, the program should get another temperature from the user and print the converted value.
'''

# develop a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit


def main():
    print("This program will convert Celsius Temps to Fahrenheit.")
    print("Developer: Htet Khant Linn")

    for i in range(5):  # for loop for executing 5 times
        # accepting user input
        celsius = float(input("What is the Celsius temperature? Enter here: ")) # replace eval with float 
        fahrenheit = celsius_to_fahrenheit(celsius)

        print(f"The temperature is {fahrenheit} degrees Fahrenheit.") 

    print("\nThis is the end of the program. Have a nice day.")

main()


'''
This Python program converts temperatures from Celsius to Fahrenheit and run a total of five times before terminating the program. 
The main function controls the program flow by using a for loop to request the user for a Celsius temperature on each iteration. 
The user's input is then passed to celsius_to_fahrenheit() function which contains the mathematical formula to perform the conversion. 
The calculated Fahrenheit temperature is then returned to main and printed.
'''