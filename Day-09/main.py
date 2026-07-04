from employee import Employee
from file_manager import FileManager
from logger import log


employee1 = Employee("Abuzaid", "IT", 101)
employee2 = Employee("Khan", "NETWORKING", 102)
employee3 = Employee("Khattak", "CSE", 103)


log("Employees Created Successfully.")

employee1.displayinfo()
employee2.displayinfo()
employee3.displayinfo()


employee1.employee_file_create()
employee2.employee_file_create()
employee3.employee_file_create()

log("Employee information saved successfully.")

employee1.employee_file_read()




manager = FileManager("Day-09/data/sample.txt")

manager.create("This file was created using FileManager.")

print(manager.read())