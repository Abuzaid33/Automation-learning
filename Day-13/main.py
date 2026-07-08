import csv
import os 
os.makedirs("Day-13/data" ,exist_ok=True)
with open("Day-13/data/employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Department"])

    writer.writerow([101, "Abuzaid", "IT"])

    writer.writerow([102, "Ali", "HR"])

    writer.writerow([103, "Ahmed", "Finance"])