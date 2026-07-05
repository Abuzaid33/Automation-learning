import os
import json


class EmployeeDatabase:
    def __init__(self,employee_name,department,employee_id):
        self.employee_name = employee_name
        self.department = department
        self.employee_id = employee_id
    def create_employee():
        if os.path.exists("Day-11/data/employees.json"):
            with open("Day-11/data/employees.json","r") as file:
                employees = json.load(file) 
    def read_employees():
        pass
    def search_employee():
        pass
    def update_employee():
        pass
    def delete_employee():
        pass 


