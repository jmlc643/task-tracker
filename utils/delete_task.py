from utils.get_tasks import get_tasks
import json

def delete_task(id):
    tasks = get_tasks()
    tasks = [task for task in tasks if task['id'] != id]
    with open("tasks.json", 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Task deleted successfully: (ID: {id})")