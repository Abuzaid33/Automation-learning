import json
import os
import logging


JSON_FILE = "Day-14/data/employees.json"
REPORT_FILE = "Day-14/reports/report.txt"


def generate_report():

    try:

        if not os.path.exists(JSON_FILE):

            logging.warning("employees.json not found")
            return

        with open(JSON_FILE, "r") as file:

            employees = json.load(file)

        total = len(employees)

        departments = []

        ids = []

        for employee in employees:

            departments.append(employee["department"])

            ids.append(employee["employee_id"])

        report = f"""
Employee Report

============================

Total Employees : {total}

Departments :

{set(departments)}

Highest ID : {max(ids)}

Lowest ID : {min(ids)}
"""

        os.makedirs("Day-14/reports", exist_ok=True)

        with open(REPORT_FILE, "w") as file:

            file.write(report)

        logging.info("Report Generated Successfully")

        print(report)

    except Exception as e:

        logging.error(e)