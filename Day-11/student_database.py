import os
import json


class StudentDatabase:

    def __init__(self, student_name, department, student_id):
        self.student_name = student_name
        self.department = department
        self.student_id = student_id

    def create_student(self):

        if os.path.exists("Day-11/data/students.json"):
            with open("Day-11/data/students.json", "r") as file:
                students = json.load(file)
        else:
            students = []

        student = {
            "student_name": self.student_name,
            "department": self.department,
            "student_id": self.student_id
        }

        students.append(student)

        with open("Day-11/data/students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Student Added Successfully!")

    def read_students(self):

        if os.path.exists("Day-11/data/students.json"):

            with open("Day-11/data/students.json", "r") as file:
                students = json.load(file)

            print("\nStudent Database\n")

            for student in students:
                print(student)

        else:
            print("Student database not found.")

    def search_student(self):

        if os.path.exists("Day-11/data/students.json"):

            with open("Day-11/data/students.json", "r") as file:
                students = json.load(file)

            for student in students:

                if student["student_id"] == self.student_id:

                    print("\nStudent Found\n")
                    print(student)
                    return student

        print("Student not found.")
        return None

    def update_student(self):

        if os.path.exists("Day-11/data/students.json"):

            with open("Day-11/data/students.json", "r") as file:
                students = json.load(file)

            for student in students:

                if student["student_id"] == self.student_id:

                    student["student_name"] = self.student_name
                    student["department"] = self.department

            with open("Day-11/data/students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student Updated Successfully!")

    def delete_student(self):

        if os.path.exists("Day-11/data/students.json"):

            with open("Day-11/data/students.json", "r") as file:
                students = json.load(file)

            students = [
                student
                for student in students
                if student["student_id"] != self.student_id
            ]

            with open("Day-11/data/students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student Deleted Successfully!")