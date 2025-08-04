import argparse

from utils.add_task import add_task

parser = argparse.ArgumentParser()
parser.add_argument("-add", help="Add a new task to the task list", type=str)
args = parser.parse_args()

if args.add:
    add_task(args.add)