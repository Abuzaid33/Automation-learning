try:
    with open("students.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("Student file not found.")