

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
import zipfile


with zipfile.ZipFile("Day-16/reports/reports.zip","r") as backup:

    backup.extractall("Day-16/Extracted")