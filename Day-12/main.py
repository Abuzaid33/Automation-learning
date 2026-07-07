import logging
import os

from file_organizer import Employee_folders, Employee_reports, Move_files
from employee_database import EmployeeDatabase
from logger import log
os.makedirs("Day-12/data", exist_ok=True)
os.makedirs("Day-12/data/incoming", exist_ok=True)
# Create Employees

employee1 = EmployeeDatabase("Abuzaid", 75, "IT")
employee2 = EmployeeDatabase("Ali", 76, "HR")
employee3 = EmployeeDatabase("Ahmed", 77, "Finance")

employee1.create_employee()
employee2.create_employee()
employee3.create_employee()

print("=" * 50)
print("Employee Database")
print("=" * 50)

employee1.read_employees()

print("\n" + "=" * 50)
print("Search Employee")
print("=" * 50)

employee1.search_employee()

print("\n" + "=" * 50)
print("Update Employee")
print("=" * 50)

employee1.employee_department = "Artificial Intelligence"
employee1.update_employee()

employee1.read_employees()

print("\n" + "=" * 50)
print("Delete Employee")
print("=" * 50)

employee2.delete_employee()

employee1.read_employees()

log("Program Finished Successfully")
# Create required folders


# Configure logging
logging.basicConfig(
    filename="Day-12/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation Started")

Employee_reports()
logging.info("Employee reports created successfully.")

Employee_folders()
logging.info("Employee folders created successfully.")

Move_files()
logging.info("Files moved successfully.")

logging.info("Automation Finished")
# logging.debug("Opening JSON")

# logging.info("Employee created")

# logging.warning("Email Missing")

# logging.error("Employee Not Found")

# logging.critical("Database Offline")

# import logging

# logging.basicConfig(
#     filename="Day-12/logs.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("Program Started")

# print("Automation Running")

# logging.info("Program Finished")

# import logging

# try:

#     number = int(input("Number: "))

# except ValueError:

#     logging.error("Invalid Number Entered")

#     print("Wrong Input")
