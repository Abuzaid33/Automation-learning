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

    def employee_file_create(self):
        os.makedirs("Day-09/data", exist_ok=True)

        try:
            with open("Day-09/data/Employee_info.txt", "a") as file:
                file.write(f"Employee Name: {self.name}\n")
                file.write(f"Department: {self.department}\n")
                file.write(f"Employee ID: {self.employee_id}\n")
                file.write("-" * 30 + "\n")

        except Exception as e:
            print(e)

        finally:
            print("File creation process completed.")

    def employee_file_read(self):
        try:
            with open("Day-09/data/Employee_info.txt", "r") as file:
                content = file.read()
                print("Employee Information:")
                print(content)

        except FileNotFoundError:
            print("File not found. Please create the file first.")

        finally:
            print("File reading process completed.")