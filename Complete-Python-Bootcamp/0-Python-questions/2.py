'''
Question:
Create a base class Employee and child classes Developer and Manager. Add a method in each child class to display role-specific work.
Concepts: Inheritance and method overriding 
'''

# Base class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


# Child class
class Developer(Employee):
    def work(self):
        print(f'{self.name} is writing the code')


class Manager(Employee):
    def work(self):
        print(f'{self.name} is managing the team')

    
# Create objects
developer = Developer(101, "Amol", 70000)
manager = Manager(102,"Ritik", 60000)

developer.work()
manager.work()