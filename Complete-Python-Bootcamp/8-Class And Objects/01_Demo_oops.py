# The code below is the example where all the oops concepts are used together

'''
A company has employees of different types: Developers, Managers, and Interns.
Each employee has personal data (Encapsulation).
Developers and Managers inherit common features from Employee.
Each role has its own work behavior (Polymorphism).
Some functions are abstract—every employee must implement them, but details vary.
'''

from abc import ABC, abstractmethod

# Abstract base class
class Employee(ABC):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary           # private variable / encapsulation 

    # encapsulation: getter and setter for salary 
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount 
        else:
            print("Invalid salary amount")

    # Abstract Method 
    def work(self):
        pass 

    def show_details(self):
        return f"Employee-id: {self.emp_id}, Name: {self.name}, Salary: {self.__salary}"
    

# Child classes 
class developer(Employee):
    def __init__(self, emp_id, name, salary, skills):
        super().__init__(emp_id, name, salary)
        self.skills = skills 
    
    # Polymorphism: same method name different work 
    def work(self):
        return f"{self.name} is writing code in {', '.join(self.skills)}"
    
class manager(Employee):
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    def work(self):
        return f"{self.name} is handling a team of {self.team_size} employees."
    
class intern(Employee):
    def work(self):
        return f"{self.name} is learning and asssisting in task"
    

# Create the objects for the classes 
# (Polymorphism: same method called on different objects)

# employees = [
#     developer(101, "Atharv", 70000, ["Python", "SQL"]),
#     manager(102, "Shreyash", 90000, 5),
#     intern(103, "Vaibhav", 20000)
# ]

# for emp in employees:
#     print(emp.show_details())
#     print(emp.work())
#     print("----------------")


# create objects 
Developer = developer(101, "Atharv", 70000, ["Python", "SQL"])
Manager  = manager(102, "Shreyash", 90000, 5)
Intern = intern(103, "Vaibhav", 20000)

print(Developer.work())
print(Manager.work())
print(Intern.work())

print("-----------------------")
print(Developer.show_details())
print(Manager.show_details())
print(Intern.show_details())

print("-----------")
print(Developer.name)
print(Manager.name)
print(Intern.name)

print("-----------")
print(Developer.emp_id)
print(Manager.emp_id)
print(Intern.emp_id)

print("-----------------")
print(Developer.get_salary())
print(Manager.get_salary())
print(Intern.get_salary())

print("----------------")
print(Developer.skills)
print(Manager.team_size)

print("----------")
Developer.set_salary(1200)
print(Developer.get_salary())