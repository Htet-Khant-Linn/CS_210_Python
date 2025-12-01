'''
2. ATM Simulation 
Project Description: Simulate a simple ATM system including the following menu: check balance, 
deposit money, withdraw money, and exit. 
Features: 
• Define functions for checking balance, depositing, and withdrawing. 
• Use a loop to allow users to perform multiple transactions until they choose to exit. 
• Use decision structures to handle incorrect PINs, insufficient funds, or invalid inputs. 
• Use Boolean flags for login success and session control. (100 marks) 
'''
def password_check(password):
    print("Welcome to KBZ Bank.")
    for x in range(3):
        try:
            user_input_string = input("Enter your 4-digit PIN: ")
            if len(user_input_string) == 4:
                user_input_pw = int(user_input_string)
                if user_input_pw == password:
                    return True
                else:
                    print("Wrong password.")
            else:
                print("The number of digit must be 4.")
        except:
            print("Invalid Input: The password must be digit.")
    print("Sorry. You have entered wrong password for 3 times. Please try again tomorrow.")
    return False

def check_balance():
    print("hi")

def deposit_money():
    print("hi")

def withdraw_money():
    print("hi")



def main():


    password = 1234
    password_status = password_check(password)
    
    if password_status == True:
        while True:
            print("--- KBZ ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            try:
                user_input = int(input("Select an option (1-4): "))
                
                if user_input == 1:
                    check_balance()
                elif user_input == 2:
                    deposit_money()
                elif user_input == 3:
                    withdraw_money()
                elif user_input == 4:
                    print("Exiting. Thank you for choosing KBZ.")
                    break
                else:
                    print("Please select a number between 1 and 4.")

            except ValueError:
                print("Invalid Input: Please enter a number.")


if __name__ == "__main__":
    main()