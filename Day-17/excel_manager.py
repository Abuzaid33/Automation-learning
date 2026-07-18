from openpyxl import Workbook
import os

os.makedirs("Day-17/data" , exist_ok=True)
workbook = Workbook()

sheet = workbook.active

sheet.title = "Employee Sheets"

sheet["A1"] = "Employee ID"
sheet["B1"] = "Name"

workbook.save("Day-17/data/employee.xlxs")