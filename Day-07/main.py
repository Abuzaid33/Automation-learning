# try:
#     file = open("notes.txt")
#     number = int(input())

# except FileNotFoundError:
#     print("File missing.")

# except ValueError:
#     print("Invalid number.")

# try:
#     number = int(input())

# except ValueError:
#     print("Invalid")

# else:
#     print("Everything worked.")
# try:
#     number = int(input())

# except ValueError:
#     print("Invalid")

# finally:
#     print("program ended successfully.")


import os


try:
    print("Creating Employee:")
    def create_employee(name):
        if not os.path.exists(name):
            os.makedirs(f"Day-07/{name}" ,exist_ok=True)    
    create_employee("Abuzaid")
    print("Employee created successfully.")
except Exception as e:
    print(f"Error creating employee: {e}")
finally:
    print("Create operation completed.")    

try:   
    print("Reading Employee:") 
    def read_employee(name):
        if os.path.exists(f"Day-07/{name}/{name}.txt"):
            with open(f"Day-07/{name}/{name}.txt", "r") as f:
                print(f.read())
    read_employee("Abuzaid")
    print("Employee created successfully.")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Read operation completed.")


try:
    print("Deleting Employee:")
    def delete_employee(name):
        if os.path.exists(f"Day-07/{name}/{name}.txt"):
            os.remove(f"Day-07/{name}/{name}.txt")
    delete_employee("Abuzaid")
    print("Employee deleted successfully.")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Delete operation completed.")