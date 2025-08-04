import argparse

from utils.add_task import add_task
from utils.list_tasks import list_tasks

parser = argparse.ArgumentParser()
parser.add_argument("-add", help="Add a new task to the task list", type=str)
parser.add_argument("-list", help="List all tasks", action="store_true")
args = parser.parse_args()

if args.add:
    add_task(args.add)
if args.list:
    list_tasks()