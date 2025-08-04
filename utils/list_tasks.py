import json
from utils.get_tasks import get_tasks

def list_tasks():
    tasks = get_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}")