import os
import zipfile
import logging

logging.basicConfig(
    filename="Day-16/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

files = ["report1.txt", "report2.txt", "report3.txt"]


def creating_files():

    try:

        os.makedirs("Day-16/reports", exist_ok=True)

        for file in files:

            file_path = f"Day-16/reports/{file}"

            if not os.path.exists(file_path):

                with open(file_path, "w") as f:
                    f.write(f"{file} created successfully")

                logging.info(f"{file} created.")

            else:
                logging.info(f"{file} already exists.")

    except Exception as e:

        logging.error(e)


def compressing_files():

    try:

        os.makedirs("Day-16/backups", exist_ok=True)

        with zipfile.ZipFile(
            "Day-16/backups/employee_backup.zip",
            "w"
        ) as backup:

            for file in os.listdir("Day-16/reports"):

                backup.write(
                    os.path.join("Day-16/reports", file)
                )

        logging.info("Backup completed successfully.")

    except Exception as e:

        logging.error(e)


def displaying_zip_files():

    try:

        if os.path.exists("Day-16/backups/employee_backup.zip"):

            with zipfile.ZipFile(
                "Day-16/backups/employee_backup.zip",
                "r"
            ) as backup:

                print("\nFiles inside ZIP:\n")

                for file in backup.namelist():
                    print(file)


                backup.extractall("Day-16/Extracted")

            logging.info("ZIP extracted successfully.")

        else:

            logging.warning("Backup ZIP not found.")

    except Exception as e:

        logging.error(e)