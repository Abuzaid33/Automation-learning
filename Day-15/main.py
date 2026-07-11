from datetime import datetime

today = datetime.now()

filename = today.strftime("report_%d_%m_%Y.txt")

print(filename)