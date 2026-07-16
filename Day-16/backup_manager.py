import os
import zipfile
import logging
from datetime import datetime


logging.basicConfig(
    filename="Day-16/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class CompanyBackup:

    def __init__(self):

        self.report_folder = "Day-16/reports"
        self.backup_folder = "Day-16/backups"

        os.makedirs(self.report_folder, exist_ok=True)
        os.makedirs(self.backup_folder, exist_ok=True)

    def create_report(self):

        try:

            today = datetime.now()

            report_name = today.strftime("report_%d_%m_%Y.txt")

            report_path = os.path.join(
                self.report_folder,
                report_name
            )

            with open(report_path, "w") as file:

                file.write("Daily Employee Report\n")
                file.write("-" * 30 + "\n")
                file.write(f"Date : {today.strftime('%d/%m/%Y')}\n")
                file.write(f"Time : {today.strftime('%I:%M %p')}\n")
                file.write("Status : Completed\n")
                file.write("Generated Automatically\n")

            logging.info("Today's report created successfully.")

            print("Report Created:")
            print(report_name)

        except Exception as e:

            logging.error(e)

    def create_backup(self):

        try:

            today = datetime.now()

            backup_name = today.strftime(
                "employee_backup_%d_%m_%Y.zip"
            )

            backup_path = os.path.join(
                self.backup_folder,
                backup_name
            )
            counter = 1

            while os.path.exists(backup_path):

                backup_name = today.strftime(
                    f"employee_backup_%d_%m_%Y_{counter}.zip"
                )

                backup_path = os.path.join(
                    self.backup_folder,
                    backup_name
                )

                counter += 1

            with zipfile.ZipFile(
                backup_path,
                "w",
                zipfile.ZIP_DEFLATED
            ) as backup:

                for file in os.listdir(self.report_folder):

                    backup.write(
                        os.path.join(
                            self.report_folder,
                            file
                        ),
                        arcname=file
                    )

            logging.info("Backup created successfully.")

            print("Backup Created:")
            print(backup_name)

        except Exception as e:

            logging.error(e)
    def show_backup(self):

        try:

            backups = os.listdir(self.backup_folder)

            if not backups:

                print("No backups found.")
                return

            latest_backup = sorted(backups)[-1]

            backup_path = os.path.join(
                self.backup_folder,
                latest_backup
            )

            with zipfile.ZipFile(
                backup_path,
                "r"
            ) as backup:

                print("\nFiles Inside ZIP:\n")

                for file in backup.namelist():

                    print(file)

            logging.info("Displayed ZIP contents.")

        except Exception as e:

            logging.error(e)

    def extract_backup(self):

        try:

            backups = os.listdir(self.backup_folder)

            if not backups:

                print("No backups found.")
                return

            latest_backup = sorted(backups)[-1]

            backup_path = os.path.join(
                self.backup_folder,
                latest_backup
            )

            extract_folder = "Day-16/Extracted"

            os.makedirs(extract_folder, exist_ok=True)

            with zipfile.ZipFile(
                backup_path,
                "r"
            ) as backup:

                backup.extractall(extract_folder)

            logging.info("Backup extracted successfully.")

            print("\nBackup Extracted Successfully!")

        except Exception as e:

            logging.error(e)