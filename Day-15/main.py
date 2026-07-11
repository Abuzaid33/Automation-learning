
from datetime import datetime
import os


os.makedirs("Day-15/reports" , exist_ok=True)

today = datetime.now()

filename = today.strftime("report_%d_%m_%Y.txt")
with open(f"Day-15/reports/{filename}" , "w") as file:
    file.write("\nDaily Employee Report")
    file.write(f"\nDate : {today.strftime("%d/%m/%Y")}")
    file.write("\nStatus : Completed")
    file.write("\nGenerated Automatically")
print("Report Generated Successfully")