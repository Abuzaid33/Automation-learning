# def greeting():
#     print("=" * 50)
#     print("\nwelcome to the Automation class")
#     print("\n"+"=" * 50)

# greeting()
# def greeting(name):
#     print("=" * 50)
#     print(f"\nwelcome {name} to the Automation class")
#     print("\n"+"=" * 50)

# greeting("Abuzaid khan khattak")
# greeting("Mahnoor khan khattak")
# greeting("Sanwal khan khattak")

# def add(a,b):
#     return a+b

# results = add(4,6)
# print(results)


import os
import shutil 
# student registration automation

# def studentf(name):
#     if not os.path.exists(name):
#         os.makedirs(f"Day-06/{name}" ,exist_ok=True)
        
# studentf("Abuzaid")
    
# def studentr(name):
#     if not os.path.exists(f"Day-06/{name}.txt"):
#         with open(f"Day-06/{name}.txt", "w") as f:
#             f.write(f"Student Name: {name}\n")
#             f.write("Registration Successful!\n")
            
# studentr("Abuzaid")   
    
# def studentm(name):
#     if os.path.exists(f"Day-06/{name}.txt"):
#         shutil.move(f"Day-06/{name}.txt", f"Day-06/{name}/{name}.txt")
        
# studentm("Abuzaid")   
       
# def studentd(name):
#     if os.path.exists(f"Day-06/{name}/{name}.txt"):
#         with open(f"Day-06/{name}/{name}.txt", "r") as f:
#             print(f.read())
 
# studentd("Abuzaid")
       
# 🏗 Mini Project
# Employee Folder Management System


def Employee(name):
    if not os.path.exists(name):
        os.makedirs(f"Day-06/{name}" ,exist_ok=True)
        
Employee("EMPLOYEE")
    
def EmployeeF(name):
    if not os.path.exists(f"Day-06/{name}.txt"):
        with open(f"Day-06/{name}.txt", "w") as f:
            f.write(f"Employee Name: {name}\n")
            f.write("Registration Successful!\n")
            
EmployeeF("sanwal")   
    
def EmployeeM(name):
    if os.path.exists(f"Day-06/{name}.txt"):
        shutil.move(f"Day-06/{name}.txt", f"Day-06/{name}/{name}.txt")
        
EmployeeM("Abuzaid")   
       
def EmployeeD(name):
    if os.path.exists(f"Day-06/{name}/{name}.txt"):
        with open(f"Day-06/{name}/{name}.txt", "r") as f:
            print(f.read())
 
EmployeeD("sanwal")

def EmployeeDEL(name):
    if os.path.exists(f"Day-06/{name}/{name}.txt"):
        os.remove(f"Day-06/{name}/{name}.txt")