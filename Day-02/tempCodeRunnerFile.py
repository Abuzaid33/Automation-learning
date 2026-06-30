"""
Day 02 - Python OS Module

Purpose:
Learn how Python communicates with the Operating System.
"""

import os

print("=" * 50)
print("Automation Engineering Bootcamp")
print("=" * 50)

print("Current Working Directory:")
print(os.getcwd())

print("\nfiles and folders present in the directory:")

for file in os.listdir():
    print(file)