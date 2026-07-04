import json
from  logger import log
employee = {
    "name": "Abuzaid",
    "department": "IT",
    "employee_id": 101
}

with open("Day-10/data/employee.json","w") as file:
    json.dump(employee,file,indent=4)


log("File writing successfull")
with open("Day-10/data/employee.json","r") as file:
    data = json.load(file)
    
print(data)
log("File reading successfull")