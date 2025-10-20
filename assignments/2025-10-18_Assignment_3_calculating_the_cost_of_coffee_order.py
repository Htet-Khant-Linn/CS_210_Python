'''
Htet Khant Linn
Assignment 3


2.	The Konditorei coffee shop sells coffee at $10.50 a pound plusthe cost of shipping. 
Each order ships for $0.86 per pound + $1.50 fixed cost for overhead. 
Write a program that calculates the cost of an order. 

'''

def total_coffee_cost(pounds_of_coffee):
    coffee_cost = 10.50 * pounds_of_coffee
    # coffee_price_per_pound = 10.50

    return coffee_cost

def shipping_cost(pounds_of_coffee):
    shipping_cost = 0.86 * pounds_of_coffee
    # shipping_cost_per_pound = 0.86

    return shipping_cost

def main():
    print("This program calculates a customer's total coffee cost at Konditorei coffee shop.\n")

    print("Developed by Htet Khant Linn.")
    print("------------------------------")

    pounds_of_coffee = float(input("Please enter the amount of coffee in pounds: "))
    
    total_cost = total_coffee_cost(pounds_of_coffee) + shipping_cost(pounds_of_coffee) + 1.50
    # the over head cost is fixed, which is $1.50

    print("\n-----Total order cost-----\n")

    print(f"{pounds_of_coffee} pounds of coffee cost ${total_cost:.2f} including the shipping cost.")
    # rounding to 2 decimal place using :.2f
    print('\n-----Thanks for your order-----')


main()


'''
Explanation:
My program calculates the total cost for a customer coffee order at the Konditorei coffee shop.
The main function handle the user input - ask for the amount of coffee in pounds.
This pound value is passed to two functions - total_coffee_cost() calculate the cost of the coffee beans (at $10.50/lb), 
and shipping_cost() calculates the variable part of the shipping (at $0.86/lb).
Then, in the main function, the program calculates the final total by adding the coffee cost, the shipping cost and 
the $1.50 fixed overhead cost.
Finally, the program prints the total formatted output to two decimal places using (:.2f). 
'''