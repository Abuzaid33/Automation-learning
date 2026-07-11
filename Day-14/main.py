from employee_database import EmployeeDatabase
from csv_manager import export_to_csv, import_from_csv
from report_generator import generate_report
import os


while True:

    print("""
1 Add Employee
2 Search Employee
3 Update Employee
4 Delete Employee
5 View Employees
6 Export CSV
7 Import CSV
8 Create Folder
9 Generate Report
10 Exit
""")

    choice = input("Choice : ")

    if choice == "1":

        name = input("Name : ")
        department = input("Department : ")
        employee_id = int(input("ID : "))

        employee = EmployeeDatabase(name, employee_id, department)

        employee.create_employee()

    elif choice == "2":

        employee_id = int(input("Enter ID : "))

        employee = EmployeeDatabase("", employee_id, "")

        employee.search_employee()

    elif choice == "3":

        name = input("New Name : ")
        department = input("New Department : ")
        employee_id = int(input("ID : "))

        employee = EmployeeDatabase(name, employee_id, department)

        employee.update_employee()

    elif choice == "4":

        employee_id = int(input("ID : "))

        employee = EmployeeDatabase("", employee_id, "")

        employee.delete_employee()

    elif choice == "5":

        employee = EmployeeDatabase("", 0, "")

        employee.read_employees()

    elif choice == "6":

        export_to_csv()

    elif choice == "7":

        import_from_csv()

    elif choice == "8":

        name = input("Employee Name : ")

        os.makedirs(f"Day-14/data/{name}", exist_ok=True)

        print("Folder Created")

    elif choice == "9":

        generate_report()

    elif choice == "10":

        print("Good Bye")

        break