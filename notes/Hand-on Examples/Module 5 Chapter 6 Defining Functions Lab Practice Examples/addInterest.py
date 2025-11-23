"""
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance
def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)

test()
"""
"""
#How to Fix It?
#Option 1: Return the New Value and Assign It

def addInterest(balance, rate):
    return balance * (1 + rate)  # Return the new balance

def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)  # Update the amount
    print(amount)  # Now prints 1050

test()
"""
"""
#Option 2: Use a Mutable Data Type (List)

def addInterest(balanceList, rate):
    balanceList[0] *= (1 + rate)  # Modify the list in place

def test():
    amount = [1000]  # Use a list to hold the balance
    rate = 0.05
    addInterest(amount, rate)
    print(amount[0])  # Now prints 1050

test()
"""
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    return newBalance

def test():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount, rate)
    print(amount)

test()




