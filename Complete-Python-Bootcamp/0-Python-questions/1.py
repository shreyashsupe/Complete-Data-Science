'''
Question:
Create a class Employee with attributes emp_id, name, salary. Write a method to display employee details. Create an object and display its details.
'''

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Method to display employee details
    def show_details(self):
        print(f"emp-id:{self.emp_id} Name: {self.name} Salary: {self.salary}")
    

# Create an object 
Obj1 = Employee(101, "Amol", 70000)

# Display employee details
Obj1.show_details()