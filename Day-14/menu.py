print("=" * 30)
print("\nEmployee Automation System\n")
print("=" * 30)

while True:

    print("\nChoose from the following options:")

    print("\n1. Add Employee")
    print("\n2. Read Employees")
    print("\n3. Search Employee")
    print("\n4. Update Employee")
    print("\n5. Delete Employee")
    print("\n6. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Employee added successfully")

    elif choice == 2:
        print("Employees displayed successfully")

    elif choice == 3:
        print("Employee found successfully")

    elif choice == 4:
        print("Employee updated successfully")

    elif choice == 5:
        print("Employee deleted successfully")

    elif choice == 6:
        print("Thank you for using Employee Automation System.")
        break

    else:
        print("Invalid choice. Please try again.")