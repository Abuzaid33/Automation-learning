import json
import os

# creatig data folder
os.makedirs("Day-11/data",exist_ok=True)

# Reading operation

if os.path.exists("Day-11/data/employee.json"):
    with open("Day-11/data/employee.json","r") as file:
        employees = json.load(file) 
else:
    employees = []

# Adding operation 
new_employee = {
    "name" :"Abuzaid",
   "department" : "IT",
   "id" : 75 
}
employees.append(new_employee)

# saving operation
with open("Day-11/data/employee.json","w") as file:
    json.dump(employees,file,indent=4)
    
for employee in employees:
    if employee["id"] ==  75:
        print(employee)
        
for employee in employees:
    if employee["id"] == 75:
        employee["department"] = "AI"
    
with open("Day-11/data/employee.json","w") as file:
    json.dump(employees,file,indent=4)