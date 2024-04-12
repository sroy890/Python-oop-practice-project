from bank_account import *

Roy = BankAccount(1000, 'Roy')
Nikhil = BankAccount(2000, 'Nikhil')

Roy.getBalance()
Nikhil.getBalance()

Nikhil.deposit(500)

Nikhil.transfer(5000, Roy)

Anuj = InterestrewardAcct(1000, 'Anuj')

Anuj.getBalance()

Anuj.deposit(100)

Anuj.transfer(100, Roy)

Pratap = SavingsAcct(1000, 'Pratap')

Pratap.getBalance()

Pratap.deposit(100)

Pratap.transfer(1000, Nikhil)