import os

"""
Day 03 - File Handling

Purpose:
Learn how to create and write files using Python.
"""
# creating a file 
# with open("note.txt", "w") as file:
#     file.write("This is my first time creating a file using Python.\n")
#     file.write("File creation\n")
#     file.write("Day-03\n")
# print("File created successfully!")


# adding new data to file 
# with open("note.txt", "a") as file:
#     file.write("\nThis is my first time appending data to a file.\n")


# reading th econtent of the file
# with open("note.txt", "r") as file:
#     content = file.read()
#     print(content)


# 💻 Mini Project – Student Registration Logger

if not os.path.exists("students.txt"):
    with open("students.txt","w") as file:
        file.write("Student 1: Abuzaid\n")
        file.write("Student 2: khan\n")
        file.write("Student 3: khattak\n")
else:
    print("File already exists!")


if os.path.exists("students.txt"):
    with open("students.txt","r") as file:
        content =file.read()
        print(content)
        
if os.path.exists("students.txt"):
    with open("students.txt","a") as file:
        file.write("Student 4: Ali\n")

if os.path.exists("students.txt"):
    with open("students.txt","r") as file:
        content =file.read()
        print(content)
        