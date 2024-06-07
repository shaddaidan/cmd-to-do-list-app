# import required libraries.

import argparse
import os
import schedule
import time
import threading

# set up argumetn parser
# -a or --add to add tasks
# -l or --list to list all tasks
# -r or --remove to remove tasks using index

def create_parser():
    parser = argparse.ArgumentParser(description="Command_line Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="remove a task by index")
    parser.add_argument("-f", "--find", metavar="", help="Find a word in tasks and return indexes")
    parser.add_argument("-e", "--emphasize", metavar="", help="Emphasize a task by index or add a new emphasized task")
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
        print("bra you got no tasks left congrats bro. : )")

# def remove_task(index):
#     if os.path.exists("tasks.txt"):
#         with open("tasks.txt", "r") as file:
#             tasks = file.readlines()
#         with open("tasks.txt", "w") as file:
#             for i, task in enumerate(tasks, start=1):
#                 if i != index:
#                     file.write(task)
#         print(f"we have crushed task: ")
#     else:
#         print("No tasks found.")

def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if 0 < index <= len(tasks):
            removed_task = tasks[index - 1].strip()  # Store the task being removed
            with open("tasks.txt", "w") as file:
                for i, task in enumerate(tasks, start=1):
                    if i != index:
                        file.write(task)
            print(f"We have crushed task: {removed_task}")
        else:
            print("Invalid index.")
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

def emphasize_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 0 < index <= len(tasks):
            task_to_emphasize = tasks.pop(index - 1).strip().upper()
            tasks.insert(0, task_to_emphasize + '\n') 
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Emphasized task: {task_to_emphasize}")
            
        else:
            print("invalid index,")
    else:
        print("no tasks found.")

# def clear_tasks():
#     if os.path.exists("tasks.txt"):
#         open("tasks.txt", "w").close()
#         print("All tasks have been cleared.")

# def schedule_clearing():
#     schedule.every().day.at("03:00").do(clear_tasks)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# parse command line arguments.

# def start_schedule_thread():
#     clear_thread = threading.Thread(target=schedule_clearing)
#     clear_thread.daemin = True
#     clear_thread.start()

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
    elif args.emphasize:
        emphasize_task(int(args.emphasize))
    else:
        parser.print_help()

    # start the schedule clearing in a seperate thread or process
    # if args.add or args.remove or args.emphasize:
    #     start_schedule_thread()


if __name__ == "__main__":
    main()

# now the app is ready to be run.
