

import zipfile

with zipfile.ZipFile("Day-16/reports/reports.zip", "w") as zip_file:
    zip_file.write("Day-16/reports/report1.txt")
    zip_file.write("Day-16/reports/report2.txt")