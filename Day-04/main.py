
import os
import shutil


folders = ["JPG", "PDF", "TXT"]
files = ["report1.pdf", "report2.pdf", "image1.jpg", "image2.jpg", "notes.txt"]

for folder in folders:
    os.makedirs(f"Day-04/incoming/{folder}", exist_ok=True)

for file in files:
    file_path = f"Day-04/incoming/{file}"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")
    else:
        print(f"{file} already exists in the incoming folder.")       
        
for file,folder in zip(files,folders):
    if file.endswith(".pdf"):
        shutil.move(f"Day-04/incoming/{file}",f"Day-04/incoming/PDF/{file}")
    elif file.endswith(".jpg"):
        shutil.move(f"Day-04/incoming/{file}",f"Day-04/incoming/JPG/{file}")
    elif file.endswith(".txt"):
        shutil.move(f"Day-04/incoming/{file}",f"Day-04/incoming/TXT/{file}")