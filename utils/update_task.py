from utils.get_tasks import get_tasks
import json

def update_task(id, task_updated):
    try:
        id = int(id)
    except ValueError:
        print("Invalid ID. Please provide a valid integer ID.")
        return
    tasks = get_tasks()
    task_founded = False
    for task in tasks:
        if task['id'] == id:
            task['task'] = task_updated
            task_founded = True
            break
    if not task_founded:
        print(f"Task with ID {id} not found.")
        return
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
    except Exception as e:
        print(f"Error updating task: {e}")