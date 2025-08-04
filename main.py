import argparse

from utils.add_task import add_task
from utils.list_tasks import list_tasks
from utils.delete_task import delete_task
from utils.update_task import update_task
from utils.change_status import change_task_status

parser = argparse.ArgumentParser(prog="Task Tracker", description="Task Tracker CLI", epilog="Use this tool to manage your tasks.")
parser.add_argument("-add", help="Add a new task to the task list", type=str)
parser.add_argument("-list", help="List all tasks (optionally filter by status)", nargs='?', const='all', type=str)
parser.add_argument("-update", help="Update a task by ID", nargs=2, type=str)
parser.add_argument("-delete", help="Delete a task by ID", type=int)
parser.add_argument("-mark-in-progress", help="Mark a task as In Progress by ID", type=int)
parser.add_argument("-mark-done", help="Mark a task as Done by ID", type=int)
parser.add_argument("-v", "-version", action="version", version="%(prog)s 1.0", help="Show the version of the Task Tracker CLI")
args = parser.parse_args()

if args.add:
    add_task(args.add)
if args.list is not None:
    if args.list == 'all':
        list_tasks()
    else:
        list_tasks(args.list)
if args.update:
    if len(args.update) != 2:
        print("Please provide an ID and the updated task description.")
    else:
        update_task(args.update[0], args.update[1])
if args.delete:
    delete_task(args.delete)
if args.mark_in_progress:
    change_task_status(args.mark_in_progress, "In Progress")
if args.mark_done:
    change_task_status(args.mark_done, "Done")