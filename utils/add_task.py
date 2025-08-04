import json
from utils.get_tasks import get_tasks
from datetime import datetime

def add_task(task):
    tasks = get_tasks()
    
    if tasks == []:
        id = 1
    else:
        id = max(task['id'] for task in tasks) + 1
    
    new_task = { "id": id, "task": task, "status": "To Do", "created_at": datetime.now().isoformat(), "updated_at": None }
    
    tasks.append(new_task)

    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added successfully: (ID: {id})")