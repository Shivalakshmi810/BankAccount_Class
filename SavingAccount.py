 from BankAccount import BankAccount
#vere oru filinu eduthondvarunu values

class SavingsAccount(BankAccount):
 def __init__(self, balance):
  super().__init__(balance)


  #def calculate_interest(self):
  # return self.__balance*(5/100)