# Just creating a user-defined exception class to use later for any exception
class NobalanceException(Exception):
    pass

# Creating parent class Bankaccount and initiate object creation with attribute
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount {self.name} is created.\nBalance = ${self.balance:.2f}")
    
    # Creating object methods    
    def getBalance(self):
        print(f'\nAccount {self.name} balance = ${self.balance:.2f}')
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print('\nDeposit complete.')
        self.getBalance()
    
    # creating conditional method which implies on the balance availability    
    def viableTransaction(self, amount):
            if self.balance >= amount:
                return True
            else:
                raise NobalanceException(
                    f'\nSorry, Account {self.name} does not have sufficient balance. \nCurrent Balance is {self.balance:.2f}')
    
    # Using try and except block to raise exception to avoid errors if any occurs                
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print ('\nWithdraw complete. \n')
            self.getBalance()
        except NobalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    def transfer(self,amount,account):
        try:
            print ("\n********** \n\nBeginning Transfer.. 🤑🤑")
            self.viableTransaction(amount)
            self.withdraw(amount)  
            account.deposit(amount)
            print('\nTransfer complete.. ✅ \n*****')
        except NobalanceException as error:
            print(f'\nTransfer interrupted. ❌.. {error}')

# Using Inheritance concept and creating base class of parent class
class InterestrewardAcct(BankAccount):
    
    # Doing method overriding which is a form of polymorphism, adding bonus for deposit.
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit complete.')
        self.getBalance()
        
class SavingsAcct(InterestrewardAcct):
    def __init__(self, initialAmount, acctName):
        
        # inheriting initializing attribute from parent class and adding new attribute
        super().__init__(initialAmount, acctName)
        self.fee = 5
     
    # Method overriding as we are adding extra charge for withdrawal from this acct 
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraw complete. \n')
            self.getBalance()
        except NobalanceException as error:
            print(f'\nWithdraw interrupted: {error}')            
        
        
        
        
        
        