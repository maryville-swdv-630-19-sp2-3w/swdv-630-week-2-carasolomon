# Tacara Solomon - Week 2: Classes and Methods in Python

# import class and random 
from CheckingAccount import CheckingAccount
from random import random

# function to generate random floats
def randomFee():
    number = random()
    return number * 15


# main class
def main():
    # Get user input
    name = input('Enter name: ')
    address = input('Enter Address: ')
    accountNumber = input('Enter Account Number: ')
    balance = int(input('Enter Account Balance: '))

    # Create instance of CheckingAccount class
    newAccount = CheckingAccount(name, address, accountNumber, balance)
    print(newAccount)
    # Perform debits/credits
    counter = 0
    while counter < 10:
        # Create random debit amount
        amount = randomFee()

        # Generate a debit and print end balance
        debitTransaction = newAccount.debit(amount)
        print('The new balance after the debit is' + ' ' +  '{:.2f}'.format(debitTransaction))

        # Generate a credit and print end balance
        creditTransaction = newAccount.credit(amount)
        print('The new balance after the credit is' + ' ' + '{:.2f}'.format(creditTransaction))
        
        counter += 1

# main function call
main() 


