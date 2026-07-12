
from datetime import datetime
import os


# os.makedirs("Day-15/reports" , exist_ok=True)

# today = datetime.now()

# filename = today.strftime("report_%d_%m_%Y.txt")
# with open(f"Day-15/reports/{filename}" , "w") as file:
#     file.write("\nDaily Employee Report")
#     file.write(f"\nDate : {today.strftime("%d/%m/%Y")}")
#     file.write("\nStatus : Completed")
#     file.write("\nGenerated Automatically")
# print("Report Generated Successfully")


from attendance import Employee


employee1 = Employee("Abuzaid",101,"IT")

employee2 = Employee("Ali",102,"HR")

employee3 = Employee("Ahmed",103,"Finance")


employee1.mark_attendance()

employee2.mark_attendance()

employee3.mark_attendance()