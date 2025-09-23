'''
Question:
Create a banking system with an abstract class Account. It should have:
Attributes: account_no, balance.
Methods: deposit(), withdraw(), and abstract calculate_interest().
Subclasses: SavingsAccount (4% interest) and CurrentAccount (no interest).

Concepts: Abstraction + Inheritance + Method Overriding + Real-world Simulation
'''

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    #Methods
    def deposite(self, amount):
        self.balance += amount 
        print(f"{amount} is deposted. The new balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount 
            print(f"{amount} is withdraw. The new balance is {self.balance}")
        else:
            print('Insufficent balance')

    @abstractmethod
    def calculate_interest(self):
        pass


# Create subclass
class SavingAccount(Account):
    def calculate_interest(self):
        interest = self.balance * 0.04
        print(f"interest earned: {interest}")
        return interest
    
class CurrentAccount(Account):
    def calculate_interest(self):
        print(f"Current Account do not earn interest")
        return 0
    
# Create Objects

s = SavingAccount(101, 1000)
s.deposite(1000)
s.calculate_interest()


c = CurrentAccount(102, 1000)
c. withdraw(200)
c.calculate_interest()
