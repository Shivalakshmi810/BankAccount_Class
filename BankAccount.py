
from abc import ABC,abstractmethod

# create a class as an abstract class
# we cannot create an object of an abstract class - Abstraction

class BankAccount(ABC):
    #constructor of the class
 def __init__(self,balance):
        #encapsulation
        self.__balance =balance   #private
    #creating an abstract method
    #this method must be inheritted by the child classes
 @abstractmethod
 def calculate_intrests(self):
        pass

@property
def balance(self):
          return self.__balance

@balance.setter
def balance(self,value):
          self.__balance=value

def display_balance(self):
        print(f"{self.__balance}")
def deposite_money(self,inp_amt):
        if  (inp_amt>0):
            print('your money has been successfully credited to you account xxxxxxx345 ')
            self.__balance+= inp_amt
            print(f'your current balance :{self.__balance}')
        else:
            print('please provide a +ve number as deposite amt')

def withdraw_amt(self,inp_amt):
        if  ((inp_amt > 0 )and( inp_amt<self.__balance)):
                    self.__balance-= inp_amt
                    print(f'your current balance :{balance}')
        elif(inp_amt<self.__balance):
                    print('insufficent money')
        else:
                    print('please provide a +ve number ')
                