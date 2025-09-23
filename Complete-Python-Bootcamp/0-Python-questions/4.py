'''
Question:
Create a class Employee with a private attribute __salary. Write getter and setter to access and update salary.
Concepts: Encapsulation
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.__salary = salary  

    # Getter 
    def get_salary(self):
        return self.__salary
    
    #setter
    def set_salary(self, amount):
        if amount > 0:
            self.__salary  = amount 
        else:
            print("invalid salary")

# Create an object 
emp = Employee("Peter",  70000)

# get the salary 
print(emp.get_salary())

# set salary
emp.set_salary(40000)
print(emp.get_salary())