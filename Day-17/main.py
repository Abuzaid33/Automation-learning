from employee_database import EmployeeDatabase

employee1 = EmployeeDatabase(101, "Abuzaid", "IT", 50000)
employee2 = EmployeeDatabase(102, "Ali", "HR", 45000)
employee3 = EmployeeDatabase(103, "Ahmed", "Finance", 65000)

employee1.create_workbook()

employee1.add_employee()
employee2.add_employee()
employee3.add_employee()

employee1.read_employees()

employee2.search_employee()

employee3.update_department("AI")

employee2.delete_employee()