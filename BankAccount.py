from abc import ABC,abstractmethod





class BankAccount(ABC) :
    #creating an astract method :
    # this method must be inherited by the  child classes
    @abstractmethod

    def __init__(self,balance):
        self.__balance = balance 




        def display_balance(self):
        # we are displaying a private information
        print ("The account  balance is (self.balance)")


        @property
        def balance(self):
            return self.__balance

        @balance.setter 

        def balance(Self,amount):
            if amount<0:
                raise ValueError("updated balance cannot be a negative value ")
            self.__balance=amount
            print(f' Salary :(self.__balance)')

            def deposit(self,amount):
                if amount>0:
                    self.__balance=self.__balance+amount
                    # print (f'Deposit amount is successful :{self.__balance}')
                    
                    else
                    print("The deposit amount must be a positive value")

                    def withdraw(self,amount):
                        if(amount>0) and(self.__balance>=amount)
                        
                