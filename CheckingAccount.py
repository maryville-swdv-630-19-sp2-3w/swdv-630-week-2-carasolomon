# Tacara Solomon - Week 2 Assignment: Classes and Methods in Python
# March 24, 2019

class CheckingAccount:

    def __init__(self, name, address, accountNumber, _balance):
        self.name = name 
        self.address = address
        self.accountNumber = accountNumber
        # private variable
        self._balance = _balance 


    def __str__(self):
        return 'Name: ' + self.name + ' Address: '+ self.address + ' Account Number: '  + self.accountNumber  

    def debit(self, amount):
        # deducts tranactions from _balance
        newBalance = self._balance - amount 
        return newBalance
   
    def credit(self, amount):
        # adds transactions to _balance
        newBalance = self._balance + amount
        return newBalance       
    
    __repr__ = __str__
