import os
import json
import logging

os.makedirs("Day-12/data", exist_ok=True)


class EmployeeDatabase:

    def __init__(self, employee_name, employee_id, employee_department):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_department = employee_department

    def create_employee(self):

        try:

            if os.path.exists("Day-12/data/employees.json"):

                with open("Day-12/data/employees.json", "r") as file:
                    employees = json.load(file)

            else:
                employees = []

            employee = {
                "employee_name": self.employee_name,
                "department": self.employee_department,
                "employee_id": self.employee_id
            }

            employees.append(employee)

            with open("Day-12/data/employees.json", "w") as file:
                json.dump(employees, file, indent=4)

            logging.info("Employee created successfully!")

        except Exception as e:
            logging.error(e)

    def search_employee(self):

        try:

            if os.path.exists("Day-12/data/employees.json"):

                with open("Day-12/data/employees.json", "r") as file:
                    employees = json.load(file)

                for employee in employees:

                    if employee["employee_id"] == self.employee_id:

                        logging.info("Employee found")
                        print(employee)
                        return employee

                logging.warning("Employee not found")
                return None

        except Exception as e:
            logging.error(e)

    def update_employee(self):

        try:

            if os.path.exists("Day-12/data/employees.json"):

                with open("Day-12/data/employees.json", "r") as file:
                    employees = json.load(file)

                found = False

                for employee in employees:

                    if employee["employee_id"] == self.employee_id:

                        employee["employee_name"] = self.employee_name
                        employee["department"] = self.employee_department

                        found = True

                with open("Day-12/data/employees.json", "w") as file:
                    json.dump(employees, file, indent=4)

                if found:
                    logging.info("Employee updated successfully")
                else:
                    logging.warning("Employee not found")

        except Exception as e:
            logging.error(e)

    def delete_employee(self):

        try:

            if os.path.exists("Day-12/data/employees.json"):

                with open("Day-12/data/employees.json", "r") as file:
                    employees = json.load(file)

                original_length = len(employees)

                employees = [
                    employee
                    for employee in employees
                    if employee["employee_id"] != self.employee_id
                ]

                with open("Day-12/data/employees.json", "w") as file:
                    json.dump(employees, file, indent=4)

                if len(employees) < original_length:
                    logging.info("Employee deleted successfully")
                else:
                    logging.warning("Employee not found")

        except Exception as e:
            logging.error(e)

    def read_employees(self):

        try:

            if os.path.exists("Day-12/data/employees.json"):

                with open("Day-12/data/employees.json", "r") as file:
                    employees = json.load(file)

                print("\nEmployee Database\n")

                for employee in employees:
                    print(employee)

                logging.info("Employees loaded successfully")

            else:
                logging.warning("employees.json not found")

        except Exception as e:
            logging.error(e)