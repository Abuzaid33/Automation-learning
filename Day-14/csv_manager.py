import os
import json
import csv
import logging


JSON_FILE = "Day-14/data/employees.json"
CSV_FILE = "Day-14/data/employees.csv"


def export_to_csv():

    try:

        if not os.path.exists(JSON_FILE):
            logging.warning("employees.json not found")
            return

        with open(JSON_FILE, "r") as file:
            employees = json.load(file)

        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(
                ["Employee Name", "Department", "Employee ID"]
            )

            for employee in employees:

                writer.writerow([
                    employee["employee_name"],
                    employee["department"],
                    employee["employee_id"]
                ])

        logging.info("Employees exported to CSV")

    except Exception as e:
        logging.error(e)


def import_from_csv():

    try:

        employees = []

        with open(CSV_FILE, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                employees.append({

                    "employee_name": row[0],
                    "department": row[1],
                    "employee_id": int(row[2])

                })

        with open(JSON_FILE, "w") as file:
            json.dump(employees, file, indent=4)

        logging.info("Employees imported from CSV")

    except Exception as e:
        logging.error(e)