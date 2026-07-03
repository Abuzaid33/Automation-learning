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