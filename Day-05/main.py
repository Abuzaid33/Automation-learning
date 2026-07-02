# My first dictionary

# student ={
#     "name": "Abuzaid",
#     "age": 20,
#     "city": " Islamabad"
# }

# print(student)
# print(student["name"])
# print(student["age"])
# print(student["city"])


# employee = {
#     "Employee ID": 12345,
#     "Name": "John Doe",
#     "Department": "IT",
#     "Email": "john.doe@company.com"
# }

# print(employee["Employee ID"])
# print(employee["Name"])
# print(employee["Department"])
# print(employee["Email"])

# file_types = {
#     ".pdf": "PDF",
#     ".jpg": "Images",
#     ".txt": "Notes",
#     ".docx": "Documents"
# }

# print(file_types[".pdf"])
# print(file_types[".jpg"])
# print(file_types[".txt"])
# print(file_types[".docx"])

import os
import shutil


file_types = {
    ".pdf": "PDF",
    ".jpg": "Images",
    ".txt": "Notes",
    ".docx": "Documents"
}


for folder in file_types.values():
    os.makedirs(f"Day-05/incoming/{folder}", exist_ok=True)
    
files = [
    "report1.pdf",
    "report2.pdf",
    "image1.jpg",
    "image2.jpg",
    "notes.txt"
]

for file in files:
    if not os.path.exists(f"Day-05/incoming/{file}"):
        with open(f"Day-05/incoming/{file}", "w") as f:
            f.write("")
    
        

for file in files:
    source = f"Day-05/incoming/{file}"
    for keys in file_types:
        if file.endswith(keys):
            folder = file_types[keys]
            destination = f"Day-05/incoming/{folder}/{file}"
            shutil.move(source, destination)
            
