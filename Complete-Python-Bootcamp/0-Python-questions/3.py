'''
Create an abstract class Employee with an abstract method work(). Implement this method in Developer and Manager.
Concepts: Abstraction with abstract base class
'''

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name 
        self. salary =  salary 

    @abstractmethod
    def  work(self):
        pass

class Developer(Employee):
    def work(self):
        print(f"{self.name} is wirting the code")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team")


# Create objects 
developer = Developer("Alex", 80000)
manager =  Manager("Peter", 50000)

developer.work()
manager.work()
