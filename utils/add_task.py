import os
import json

def add_task(task):
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
    
    if tasks == []:
        id = 1
    else:
        id = max(task['id'] for task in tasks) + 1
    
    new_task = { "id": id, "task": task }
    
    tasks.append(new_task)

    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added successfully: (ID: {id})")