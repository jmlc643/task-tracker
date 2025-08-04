import os
def verify_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return
    except (FileNotFoundError):
        with open(file_path, 'w') as file:
            file.write("")
        return