import os

class Employee:
    def __init__(self, name, department, employee_id):
        self.name = name
        self.department = department
        self.employee_id = employee_id

    def displayinfo(self):
        print(f"Employee Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Employee ID: {self.employee_id}")


emp1 = Employee("Abuzaid", "IT", 101)
emp2 = Employee("Ali", "HR", 102)

emp1.displayinfo()
emp2.displayinfo()


def employee_file_create(employee):

    os.makedirs("Day-08/data", exist_ok=True)

    try:
        with open("Day-08/data/Employee_info.txt", "a") as file:
            file.write(f"Employee Name: {employee.name}\n")
            file.write(f"Department: {employee.department}\n")
            file.write(f"Employee ID: {employee.employee_id}\n")
            file.write("-" * 30 + "\n")

    except Exception as e:
        print(e)

    finally:
        print("File creation process completed.")


employee_file_create(emp1)
employee_file_create(emp2)


def employee_file_read():
    try:
        with open("Day-08/data/Employee_info.txt", "r") as file:
            content = file.read()
            print("Employee Information:")
            print(content)

    except FileNotFoundError:
        print("File not found. Please create the file first.")

    finally:
        print("File reading process completed.")


employee_file_read()