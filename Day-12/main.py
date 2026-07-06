# import logging

# logging.basicConfig(
#     filename="Day-12/automation.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
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

import logging

try:

    number = int(input("Number: "))

except ValueError:

    logging.error("Invalid Number Entered")

    print("Wrong Input")