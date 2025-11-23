# convert.py 
# A program to convert Celsius temps to Fahrenheit 
# by: Susan Computewell 

def main():
    # Loop 5 times to get user input and print the converted temperature
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print(f"The temperature is {fahrenheit} degrees Fahrenheit.")

main()

#Explanation:
#Loop 5 times: The for i in range(5) loop makes the program run 5 times, prompting the user for input each time.
#Temperature Conversion: Each time through the loop, the program prompts the user for a Celsius temperature, converts it to Fahrenheit, and prints the result.
