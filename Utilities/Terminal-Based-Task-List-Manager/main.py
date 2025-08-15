# modules
import os
import json
import sys

# functions
def hold_screen():
    input("Press Enter to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def error(err, newline=False):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(f"{RED}error: {err}{RESET}{'\n' if newline else ''}")

def initialization(filename):
    if os.path.isfile(filename):
        with open(filename) as f:
            data = json.load(f)

            if not isinstance(data, list):
                overwrite = input(f"Already there exists a file name '{filename}'. "
                                "Would you like to overwrite it (y/n)? ").strip()
                
                if overwrite.lower() == 'y':
                    with open(filename, 'w') as f:
                        json.dump([], f)
                else:
                    print("Operation cancelled. Good Bye!")
                    sys.exit()
    else:
        with open(filename, 'w') as f:
            json.dump([], f)
        
    print()

def get_tasks(filename):
    with open(filename) as f:
        return json.load(f)

def get_int(prompt, start=None, end=None):
    while True:
        try:
            val = int(input(prompt))
            if start is not None and end is not None:
                if not start <= val <= end:
                    error(f"enter a value between {start} and {end}", True)
                    continue
            return val
        except ValueError:
            error("enter a valid integer value")

def add_task(task_list):
    while True:
        task = input("\nEnter a task: ")

        if not task:
            error("enter a valid task")
            continue

        task_list.append({"title": task, "done": False})

        break
    
    print(f"\nTask created successfully!\n")

def view_tasks(task_list):
    if not task_list:
        print("\nThere doesn't exist any task to show!\n")

        return False

    print("\n--- TASKS --- ")
    for sr_no, task_info in enumerate(task_list, 1):
        title = task_info["title"]
        status = "Done" if task_info["done"] else "Not Done"
        print(f"{sr_no}. {title} -> {status}")

    print()

    return True

def mark_task_as_completed(task_list):
    if not view_tasks(task_list):
        return
    
    start, end = 1, len(task_list)

    choice = get_int(f"Select task to mark as complete ({start}-{end}): ", start, end)

    task_in_list = task_list[choice-1]

    if task_in_list["done"]:
        error("selected task is already marked as complete, try again", True)
        return
    
    task_in_list["done"] = True

    print("\nSelected task has been marked as done successfully!\n")

def delete_task(task_list):
    if not view_tasks(task_list):
        return

    start, end = 1, len(task_list)

    choice = get_int(f"Select task to delete ({start}-{end}): ", start, end)

    task_idx = choice-1

    task_list.pop(task_idx)

    print("\nSelected task has been successfully deleted!\n")

def save_tasks(filename, task_list):
    with open(filename, 'w') as f:
        json.dump(task_list, f, indent=2)

# main code
TASKS_FILE_NAME = "tasks.json"

initialization(TASKS_FILE_NAME)

task_list = get_tasks(TASKS_FILE_NAME)

while True:

    clear_screen()

    menu_list = [
        "Add Task",
        "View Tasks",
        "Mark Task as Completed",
        "Delete Task",
        "Exit"
    ]

    print("--- MENU ---")
    for sr_no, menu_item in enumerate(menu_list, 1):
        print(f"{sr_no}. {menu_item}")
    
    choice = get_int("Enter your choice (1-5): ", 1, 5)

    clear_screen()

    match choice:
        case 1:
            add_task(task_list)
            save_tasks(TASKS_FILE_NAME, task_list)
        case 2:
            view_tasks(task_list)
        case 3:
            mark_task_as_completed(task_list)
            save_tasks(TASKS_FILE_NAME, task_list)
        case 4:
            delete_task(task_list)
            save_tasks(TASKS_FILE_NAME, task_list)
        case 5:
            print("\nGood Bye!")
            sys.exit()
    
    hold_screen()