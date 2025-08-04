import argparse

from utils.add_task import add_task
from utils.list_tasks import list_tasks
from utils.delete_task import delete_task

parser = argparse.ArgumentParser()
parser.add_argument("-add", help="Add a new task to the task list", type=str)
parser.add_argument("-list", help="List all tasks", action="store_true")
parser.add_argument("-delete", help="Delete a task by ID", type=int)
args = parser.parse_args()

if args.add:
    add_task(args.add)
if args.list:
    list_tasks()
if args.delete:
    delete_task(args.delete)