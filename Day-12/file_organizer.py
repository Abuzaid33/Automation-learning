import os
import shutil
import logging


def Employee_reports():

    try:

        incoming_folder = "Day-12/data/incoming"

        # Create report.pdf
        if not os.path.exists(f"{incoming_folder}/reports.pdf"):
            with open(f"{incoming_folder}/reports.pdf", "w") as file:
                file.write("PDF File")
            logging.info("reports.pdf created")

        # Create image.jpg
        if not os.path.exists(f"{incoming_folder}/image.jpg"):
            with open(f"{incoming_folder}/image.jpg", "w") as file:
                file.write("JPG File")
            logging.info("image.jpg created")

        # Create notes.txt
        if not os.path.exists(f"{incoming_folder}/notes.txt"):
            with open(f"{incoming_folder}/notes.txt", "w") as file:
                file.write("TXT File")
            logging.info("notes.txt created")

    except Exception as e:
        logging.error(e)


def Employee_folders():

    try:

        os.makedirs("Day-12/data/PDF", exist_ok=True)
        os.makedirs("Day-12/data/JPG", exist_ok=True)
        os.makedirs("Day-12/data/TXT", exist_ok=True)

        logging.info("Folders created successfully.")

    except Exception as e:

        logging.error(e)


def Move_files():

    source = "Day-12/data/incoming"

    try:

        for file in os.listdir(source):

            source_path = os.path.join(source, file)

            if file.lower().endswith(".pdf"):

                destination = "Day-12/data/PDF"

                shutil.move(source_path, os.path.join(destination, file))

                logging.info(f"{file} moved to PDF")

            elif file.lower().endswith(".jpg"):

                destination = "Day-12/data/JPG"

                shutil.move(source_path, os.path.join(destination, file))

                logging.info(f"{file} moved to JPG")

            elif file.lower().endswith(".txt"):

                destination = "Day-12/data/TXT"

                shutil.move(source_path, os.path.join(destination, file))

                logging.info(f"{file} moved to TXT")

    except Exception as e:

        logging.error(e)