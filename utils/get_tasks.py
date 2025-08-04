import json

def get_tasks():
    try:
        with open("tasks.json", 'r') as file:
            content = file.read().strip()
            if not content:
                tasks = []
            else:
                file.seek(0)
                tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
        
    return tasks