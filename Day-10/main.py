from employee_manager import Employee


employee1 = Employee(
    "Abuzaid",
    "IT",
    101,
    "abuzaid333@gmail.com"
)

employee2 = Employee(
    "Khan",
    "Networking",
    102,
    "khan333@gmail.com"
)

employee3 = Employee(
    "Khattak",
    "CSE",
    103,
    "khattak333@gmail.com"
)


employee1.save_employee()
employee2.save_employee()
employee3.save_employee()

employee1.read_employees()