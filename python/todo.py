""" A simple command-line to-do list manager"""
import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n") #write task into the opened file - tasks.txt

def list_tasks():
    """ Function: list_tasks
    
    Input: a task to add to the list
    Resturn: a string of the tasks in the list 
    """
    output_string =""
    if os.path.exists(TASK_FILE):  
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines() # stores all the lines in the opened files as strings in tasks
            for index, task in enumerate(tasks, start=1): #add a counter
                output_string += (f"{index}. {task.strip()}\n")
    return output_string.strip()

def remove_task(index):
    """Function: remove_task
    
    Input:a task to remove from the list (index)
    Returen:nothing
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            for i, task in enumerate(tasks, start=1):
                if i != index: 
                    file.write(task)
        print("task removed.")
    else:
        print("no task found")
        
def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
