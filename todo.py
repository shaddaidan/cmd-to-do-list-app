# import required libraries.

import argparse
import os

# set up argumetn parser
# -a or --add to add tasks
# -l or --list to list all tasks
# -r or --remove to remove tasks using index

def create_parser():
    parser = argparse.ArgumentParser(description="Command_line Todo List App")
    parser.add_argument("-a", "--add"_, metavar="", help="List all tasks")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="remove a task by index")
    parser.add_argument("-f",)
    return parser
                        