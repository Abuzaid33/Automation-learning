import os


class FileManager:

    def __init__(self, file_path):
        self.file_path = file_path

    def create(self, content):

        try:
            with open(self.file_path, "w") as file:
                file.write(content)

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

        else:
            print(f"File created successfully: {self.file_path}")

    def read(self):

        try:
            with open(self.file_path, "r") as file:
                content = file.read()

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

        else:
            print(f"File read successfully: {self.file_path}")
            return content

    def delete(self):

        try:
            os.remove(self.file_path)

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

        else:
            print(f"File deleted successfully: {self.file_path}")