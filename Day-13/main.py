import csv
import os 
os.makedirs("Day-13/data" ,exist_ok=True)

students = [
    [101, "Abuzaid", "CS", 3.06],
    [102, "Ali", "HR", 3.4],
    [103, "Abuzaid", "IT", 3.9],
    [104, "Ali", "HR", 3.8],
    [105, "Ahmed", "Finance", 3.5],
    [106, "Sara", "CS", 3.75],
    [107, "Zain", "Finance", 3.2],
    [108, "Fatima", "HR", 3.95],
    [109, "Omar", "CS", 2.8],
    [110, "Aisha", "Finance", 3.6]
]
with open("Day-13/data/students.csv", "w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Department","CGPA"])

    for student in students:
        writer.writerow(student)
with open("Day-13/data/students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    count = 0

    for student in reader:

        if float(student[3]) >= 3.5:

            print(f"ID         : {student[0]}")
            print(f"Name       : {student[1]}")
            print(f"Department : {student[2]}")
            print(f"CGPA       : {student[3]}")
            print("-" * 30)

        if student[2] == "CS":
            count += 1

print(f"\nTotal CS Students: {count}")

        
# employees = [
#      [101,"Abuzaid","IT"],

#     [102,"Ali","HR"],

#       [103,"Abuzaid","IT"],

#     [104,"Ali","HR"],

#     [105,"Ahmed","Finance"],


# ]
# with open("Day-13/data/employees.csv", "w",newline="") as file:

#     writer = csv.writer(file)

#     writer.writerow(["ID", "Name", "Department"])

#     for employee in employees:
#         writer.writerow(employee)
# with open("Day-13/data/employees.csv", "r") as file:

#     reader = csv.reader(file)
#     next(reader)
#     for employee in reader:
#         print(employee)
#     print("-" * 30)
        
