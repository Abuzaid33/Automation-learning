import json
from logger import log


class Student:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def save_student(self):

        student = {
            "Name": self.name,
            "Department": self.department
        }

        with open("Day-10/data/student.json", "a") as file:
            json.dump(student, file, indent=4)
            file.write("\n")

        log("Student created successfully.")

    def read_student(self):

        try:
            with open("Day-10/data/student.json", "r") as file:
                data = file.read()

            print(data)

            log("Student reading successfully.")

        except FileNotFoundError:
            print("File not found.")

    def add_student(self):
        self.save_student()