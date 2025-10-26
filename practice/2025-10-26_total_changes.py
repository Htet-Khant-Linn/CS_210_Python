'''
This program counts the total values of different coin types (quarters, dimes, nickels, and pennies)
'''

def main():
    print("Welcome to Coin Counter!\n")
    print("How many of each coin do you have?")
    
    # accept the user input for each coin types
    quarters = int(input("Quarter: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    # calculating the total value
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    # printing the total value
    # {0>2} ensure 0 at the first digit if the value has only one digit e.g.  $9.05
    print("The total value of your changes is: ${0}.{1:0>2}.".format(total//100, total%100))

main()
