# Day 16 - ZIP File Automation

## 📌 Objective

Learn how to automate file backups using Python's built-in `zipfile` module.

This project demonstrates how companies compress, archive, and restore files automatically.

---

## 📚 Concepts Covered

- zipfile Module
- File Compression
- File Extraction
- Backup Automation
- Logging
- Exception Handling
- OOP
- datetime Module

---

## 🏗 Project Structure

Day-16/

│── reports/

│ ├── report1.txt

│ ├── report2.txt

│ └── report3.txt

│

│── backups/

│ └── employee_backup.zip

│

│── extracted/

│

│── backup.py

│── automation.log

│── notes.md

│── README.md

---

## ⚙ Features

### Create Reports

Automatically creates report files if they do not exist.

### Create ZIP Backup

Compresses all reports into a ZIP archive.

Example:

employee_backup.zip

### View ZIP Contents

Displays all files stored inside the archive.

### Extract Backup

Extracts all files into a separate folder.

### Logging

Records all operations inside:

automation.log

### Error Handling

Handles file-related errors without crashing the program.

---

## 🔧 Modules Used

### os

Used for file and folder operations.

### zipfile

Used for:

- Creating ZIP files
- Reading ZIP files
- Extracting ZIP files

### logging

Used to store logs professionally.

### datetime

Used to generate date-based backup names.

---

## 🚀 How to Run

Open terminal and run:

```bash
python backup.py