from employee_database import EmployeeDatabase


employee1 = EmployeeDatabase(101, "Abuzaid", "IT", 50000)
employee2 = EmployeeDatabase(102, "Ali", "HR", 45000)
employee3 = EmployeeDatabase(103, "Ahmed", "Finance", 65000)

# Create Workbook
employee1.create_workbook()

# Add Employees
employee1.add_employee()
employee2.add_employee()
employee3.add_employee()

print("=" * 40)

# Read Employees
employee1.read_employees()

print("=" * 40)

# Search Employee
employee2.search_employee()

print("=" * 40)

# Update Department
employee3.update_department("Artificial Intelligence")

employee2.delete_employee()

