
     


  #def calculate_interest(self):
  # return self.__balance*(5/100)
  # referring clas defined on another class
from BankAccount import BankAccount

class SavingAccount(BankAccount):

    def display_balance(self):
        pass

    def calculate_intrests(self,rate):
        intrest=self.balance*(rate/100)
        self.balance+=intrest
        print(f'intrest of {rate} added to your account')
        print('your account balance is' ,self.balance)