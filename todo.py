# import required libraries.

import argparse
import os

# set up argumetn parser
# -a or --add to add tasks
# -l or --list to list all tasks
# -r or --remove to remove tasks using index

def create_parser():
    parser = argparse.ArgumentParser(description="Command_line Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="List all tasks")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="remove a task by index")
    parser.add_argument("-f", "--find", metavar="", help="Find a word in tasks and return indexes")
    return parser
                        
# add task management functions

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write( task + '\n')

def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    else:
        print("No takss found.")

def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index:
                    file.write(task)
        print("Task removed succesfully.")
    else:
        print("No tasks found.")

def find_word(word):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        indexes = [index + 1 for index, task in enumerate(tasks) if word in task]
        if indexes:
            print(f"Word '{word}' found in tasks at indexes: {indexes}")
        else:
            print(f"Word '{word}' not found in any tasks.")
    else:
        print("No tasks found.")

# parse command line arguments.

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(int(args.remove))
    elif args.find:
        find_word(args.find)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# now the app is ready to be run.
