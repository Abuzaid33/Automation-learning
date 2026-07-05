import os
import json


class EmployeeDatabase:

    def __init__(self, employee_name, department, employee_id):
        self.employee_name = employee_name
        self.department = department
        self.employee_id = employee_id

    def create_employee(self):

        if os.path.exists("Day-11/data/employees.json"):
            with open("Day-11/data/employees.json", "r") as file:
                employees = json.load(file)
        else:
            employees = []

        employee = {
            "employee_name": self.employee_name,
            "department": self.department,
            "employee_id": self.employee_id
        }

        employees.append(employee)

        with open("Day-11/data/employees.json", "w") as file:
            json.dump(employees, file, indent=4)

        print("Employee Added Successfully!")

    def read_employees(self):

        if os.path.exists("Day-11/data/employees.json"):

            with open("Day-11/data/employees.json", "r") as file:
                employees = json.load(file)

            print("\nEmployee Database\n")

            for employee in employees:
                print(employee)

        else:
            print("Employee database not found.")

    def search_employee(self):

        if os.path.exists("Day-11/data/employees.json"):

            with open("Day-11/data/employees.json", "r") as file:
                employees = json.load(file)

            for employee in employees:

                if employee["employee_id"] == self.employee_id:

                    print("\nEmployee Found\n")
                    print(employee)
                    return employee

        print("Employee not found.")
        return None

    def update_employee(self):

        if os.path.exists("Day-11/data/employees.json"):

            with open("Day-11/data/employees.json", "r") as file:
                employees = json.load(file)

            for employee in employees:

                if employee["employee_id"] == self.employee_id:

                    employee["employee_name"] = self.employee_name
                    employee["department"] = self.department

            with open("Day-11/data/employees.json", "w") as file:
                json.dump(employees, file, indent=4)

            print("Employee Updated Successfully!")

    def delete_employee(self):

        if os.path.exists("Day-11/data/employees.json"):

            with open("Day-11/data/employees.json", "r") as file:
                employees = json.load(file)

            employees = [
                employee
                for employee in employees
                if employee["employee_id"] != self.employee_id
            ]

            with open("Day-11/data/employees.json", "w") as file:
                json.dump(employees, file, indent=4)

            print("Employee Deleted Successfully!")