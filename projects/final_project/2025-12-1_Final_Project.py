'''
2. ATM Simulation 
Project Description: Simulate a simple ATM system including the following menu: check balance, 
deposit money, withdraw money, and exit. 
Features: 
• Define functions for checking balance, depositing, and withdrawing. 
• Use a loop to allow users to perform multiple transactions until they choose to exit. 
• Use decision structures to handle incorrect PINs, insufficient funds, or invalid inputs. 
• Use Boolean flags for login success and session control. (100 marks)


Developed by Htet Khant Linn
'''
def password_check(password):
    print("\n======================")
    print("Welcome to KBZ Bank.")
    print("======================\n")

    # loop allows 3 attempts for the password
    for x in range(3):
        try:
            user_input_string = input("Enter your 4-digit PIN: ")

            # check if the PIN is exactly length of 4
            if len(user_input_string) == 4:
                user_input_pw = int(user_input_string)

                # check if password matches
                if user_input_pw == password:
                    return True
                else:
                    print("Wrong password.\n")
            else:
                print("The number of digit must be 4.\n")
        except:
            print("Invalid Input: The password must be digit.\n")
    
    print("Sorry. You have entered wrong password for 3 times. Please try again tomorrow.\n")
    return False # Login failed

# create check balance function
def check_balance(balance):
    print(f"Your balance is {balance}.\n")

# create deposit money function
def deposit_money(balance):
    try:
        dep_amount = float(input("Enter amount to deposit: "))

        # validate that deposit amount is positive
        if dep_amount > 0:
            balance += dep_amount
            print(f"Deposited: {dep_amount}.")
            print(f"New Balance: {balance}.\n")
        else:
            print("Invalid Amount.\n")
        return balance # return the updated balance
        
    except ValueError:
        print("Invalid Input. Please try again.\n")
        return balance  # return the original balance on error

# create withdraw money function
def withdraw_money(balance):

    try:
        wt_amount = float(input("Enter amount to withdraw: "))

        # check for sufficient funds
        if wt_amount > balance:
            print("Insufficient Balance.\n")
        elif wt_amount <= 0:
            print("Invalid Amount.\n")
        else:
            balance -= wt_amount

            print(f"Withdraw: {wt_amount}.")
            print(f"New Balance: {balance}.\n")
        return balance  # return updated balance
        
    except ValueError:
        print("Invalid Input. Please try again.\n")
        return balance
        # return the original balance on error

def main():

    password = 1234 # user password
    balance = 0     # initial balance

    # verify user before showing menu
    password_status = password_check(password)
    
    # continue the process if the verificatio pass
    if password_status == True:
        is_running = True   # use Boolean flag for session control

        # loop continues until use choose 4 "Exit"
        while is_running:
            print("\n======================")
            print("--- KBZ ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("======================\n")

            try:
                user_input = int(input("Select an option (1-4): "))
                
                if user_input == 1:
                    check_balance(balance)
                elif user_input == 2:
                    balance = deposit_money(balance)    # update balance variable
                elif user_input == 3:
                    balance = withdraw_money(balance)   # update balance variable
                elif user_input == 4:
                    print("Exiting. Thank you for choosing KBZ.\n")
                    is_running = False  # use Boolean flags to stop the loop
                else:
                    print("Please select a number between 1 and 4.\n")

            except ValueError:
                print("Invalid Input: Please enter a number.\n")


if __name__ == "__main__":
    main()

