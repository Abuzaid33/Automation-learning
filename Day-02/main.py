# """
# Day 02 - Python OS Module

# Purpose:
# Learn how Python communicates with the Operating System.
# """

import os

# print("=" * 50)
# print("Automation Engineering Bootcamp")
# print("=" * 50)

# print("Current Working Directory:")
# print(os.getcwd())

# print("\nfiles and folders present in the directory:")

# for file in os.listdir():
# 0#     else:
#         print(f"{file} is a folder")
# for file in os.listdir():
#     print(os.path.relpath(file))
# for file in os.listdir():
#     print(os.path.abspath(file))

print("="*50)

print("\nDirectory Inspector")

print("\n="*50)

print("\nCurrent Working Directory:")

print("\n" + os.getcwd())

print("\nItems found:")


for file in os.listdir():
    if os.path.isfile(file):
        print(f"\n {"="*50}\n{file}\nType : File\nAbsolute Path : {os.path.abspath(file)}\n {"="*50}")
    else:
        print(f"\n {"="*50}\n{file}\nType : Folder\nAbsolute Path : {os.path.abspath(file)}\n {"="*50}")