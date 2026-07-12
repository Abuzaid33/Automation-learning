from datetime import datetime
import logging
import os


os.makedirs("Day-15/data", exist_ok=True)

logging.basicConfig(

    filename="Day-15/automation.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)


class Employee:

    def __init__(self, name, employee_id, department):

        self.name = name
        self.employee_id = employee_id
        self.department = department

    def mark_attendance(self):

        try:

            today = datetime.now()

            date = today.strftime("%d-%m-%Y")

            time = today.strftime("%I:%M %p")

            with open("Day-15/data/attendance.txt", "a") as file:

                file.write("-" * 40 + "\n")

                file.write(f"Employee : {self.name}\n")

                file.write(f"ID : {self.employee_id}\n")

                file.write(f"Department : {self.department}\n")

                file.write(f"Date : {date}\n")

                file.write(f"Time : {time}\n")

                file.write("-" * 40 + "\n\n")

            logging.info(f"{self.name} attendance marked.")

            print("Attendance Saved Successfully")

        except Exception as e:

            logging.error(e)

            print("Error occurred.")