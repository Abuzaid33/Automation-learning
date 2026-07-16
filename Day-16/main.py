import os






from backup_manager import CompanyBackup


company = CompanyBackup()

company.create_report()

company.create_backup()

company.show_backup()

company.extract_backup()
from backup import (
    creating_files,
    compressing_files,
    displaying_zip_files
)


os.makedirs("Day-16/reports", exist_ok=True)
os.makedirs("Day-16/backups", exist_ok=True)
os.makedirs("Day-16/Extracted", exist_ok=True)

creating_files()

compressing_files()

displaying_zip_files()







# import zipfile

# with zipfile.ZipFile("Day-16/reports/reports.zip", "w") as zip_file:
#     zip_file.write("Day-16/reports/report1.txt")
#     zip_file.write("Day-16/reports/report2.txt")

# with zipfile.ZipFile("Day-16/reports/reports.zip", "w") as backup:
#     for file in os.listdir("Day-16/reports"):
#         backup.write(
#             os.path.join("Day-16/reports", file)
#         )
# print("Backup completed")

# import os
# import zipfile


# with zipfile.ZipFile("Day-16/reports/reports.zip","r") as backup:

#     backup.extractall("Day-16/Extracted")