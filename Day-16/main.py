
import os
import zipfile

with zipfile.ZipFile("Day-16/reports/reports.zip", "w") as backup:
    for file in os.listdir("Day-16/reports"):
        backup.write(
            os.path.join("Day-16/reports", file)
        )
print("Backup completed")