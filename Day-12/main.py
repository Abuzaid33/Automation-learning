import logging
import os

from file_organizer import Employee_folders, Employee_reports, Move_files

# Create required folders
os.makedirs("Day-12/data", exist_ok=True)
os.makedirs("Day-12/data/incoming", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="Day-12/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation Started")

Employee_reports()
logging.info("Employee reports created successfully.")

Employee_folders()
logging.info("Employee folders created successfully.")

Move_files()
logging.info("Files moved successfully.")

logging.info("Automation Finished")
# logging.debug("Opening JSON")

# logging.info("Employee created")

# logging.warning("Email Missing")

# logging.error("Employee Not Found")

# logging.critical("Database Offline")

# import logging

# logging.basicConfig(
#     filename="Day-12/logs.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.info("Program Started")

# print("Automation Running")

# logging.info("Program Finished")

# import logging

# try:

#     number = int(input("Number: "))

# except ValueError:

#     logging.error("Invalid Number Entered")

#     print("Wrong Input")
