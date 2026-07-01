"""
Day 04 - File Organization Automation

Purpose:
Automatically organize files into folders based on their extensions.
"""

import os
import shutil

# -------------------------------
# Create Required Folders
# -------------------------------

folders = ["JPG", "PDF", "TXT"]

for folder in folders:
    os.makedirs(f"incoming/{folder}", exist_ok=True)

# -------------------------------
# Create Sample Files
# -------------------------------

files = [
    "report1.pdf",
    "report2.pdf",
    "image1.jpg",
    "image2.jpg",
    "notes.txt"
]

for file in files:

    file_path = f"incoming/{file}"

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("Sample File")

# -------------------------------
# Organize Files
# -------------------------------

for file in files:

    source = f"incoming/{file}"

    if not os.path.exists(source):
        continue

    if file.endswith(".pdf"):

        destination = f"incoming/PDF/{file}"

    elif file.endswith(".jpg"):

        destination = f"incoming/JPG/{file}"

    elif file.endswith(".txt"):

        destination = f"incoming/TXT/{file}"

    else:

        continue

    shutil.move(source, destination)

print("\nAll files organized successfully!")