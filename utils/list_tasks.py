import json
from utils.get_tasks import get_tasks

def list_tasks(status=None):
    tasks = get_tasks()
    if status:
        if status not in ["to-do", "in-progress", "done"]:
            print("Invalid status. Please choose from 'to-do', 'in-progress', or 'done'.")
            return
        status = status.replace("-", " ").title()
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")