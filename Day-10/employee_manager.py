import json
from logger import log


class Employee:
    def __init__(self, name, department, employee_id, email):
        self.name = name
        self.department = department
        self.employee_id = employee_id
        self.email = email

    def save_employee(self):

        employee = {
            "Name": self.name,
            "Department": self.department,
            "Employee ID": self.employee_id,
            "Email": self.email
        }

        with open("Day-10/data/employees.json", "a") as file:
            json.dump(employee, file, indent=4)
            file.write("\n")

        log("Employee created successfully.")

    def read_employees(self):

        try:
            with open("Day-10/data/employees.json", "r") as file:
                data = file.read()

            print(data)

            log("Employee reading successfully.")

        except FileNotFoundError:
            print("File not found.")

    def add_employee(self):
        self.save_employee()