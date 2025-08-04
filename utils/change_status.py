from utils.get_tasks import get_tasks
import json

def change_task_status(id, new_status):
    tasks = get_tasks()
    task_founded = False
    for task in tasks:
        if task['id'] == id:
            task['status'] = new_status
            task_founded = True
            break
    if not task_founded:
        print(f"Task with ID {id} not found.")
        return
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error updating task: {e}")