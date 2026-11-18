from BankAccount import BankAccount  
from SavingAccount import SavingsAccount
from CurrentAccount import CurrentAccount






#creating an object of class 'SimpleAccount'
# sAccount1=SimpleAccount()
# sAccount1.method()


# # creating an object of class 'BankAccount'
# #  not  possible  because, we cannot cerate an project of astract class
# bank




# create an object of current account 
cal = CurrentAccount()
cal.dummymethod()          #method is defined in the child class
cal.deposit_amount(1000)    #method is defined in the parent class
# # cannot bedone because varible is protected  frombeing accessd from outside
# print(f'balance amount is :{cal.__account_balance}')

# to display the balance  use the function from the parent class.
cal.display_balance()

cal.deposit_amount(1700)
cal.display_balance()

cal.calculate_interest()

# testing

