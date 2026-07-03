# try:
#     file = open("notes.txt")
#     number = int(input())

# except FileNotFoundError:
#     print("File missing.")

# except ValueError:
#     print("Invalid number.")

try:
    number = int(input())

except ValueError:
    print("Invalid")

else:
    print("Everything worked.")
try:
    number = int(input())

except ValueError:
    print("Invalid")

finally:
    print("program ended successfully.")