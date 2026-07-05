from employee_database import EmployeeDatabase
from student_database import StudentDatabase


# ---------------- EMPLOYEES ---------------- #

employee1 = EmployeeDatabase("Abuzaid", "IT", 75)
employee2 = EmployeeDatabase("Ali", "HR", 76)
employee3 = EmployeeDatabase("Ahmed", "Finance", 77)

# Create Employees
employee1.create_employee()
employee2.create_employee()
employee3.create_employee()

print("\n========== Employee Database ==========\n")

employee1.read_employees()

print("\n========== Search Employee ==========\n")

employee1.search_employee()

print("\n========== Update Employee ==========\n")

employee1.department = "Artificial Intelligence"

employee1.update_employee()

employee1.read_employees()

print("\n========== Delete Employee ==========\n")

employee2.delete_employee()

employee1.read_employees()


# ---------------- STUDENTS ---------------- #

student1 = StudentDatabase("John", "Computer Science", 1)
student2 = StudentDatabase("Sara", "Artificial Intelligence", 2)
student3 = StudentDatabase("Ahmed", "Cyber Security", 3)

# Create Students
student1.create_student()
student2.create_student()
student3.create_student()

print("\n========== Student Database ==========\n")

student1.read_students()

print("\n========== Search Student ==========\n")

student2.search_student()

print("\n========== Update Student ==========\n")

student2.department = "Data Science"

student2.update_student()

student1.read_students()

print("\n========== Delete Student ==========\n")

student3.delete_student()

student1.read_students()