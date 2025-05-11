# todo.py
# A simple command-line To-Do List application
import json
import os

FILENAME = "todos.json"

todo_list = []

def save_tasks():
    with open(FILENAME, 'w') as f:
        json.dump(todo_list, f)

def load_tasks():
    global todo_list
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            todo_list = json.load(f)
    else:
        todo_list = []

def show_menu():
    print("\n==== To-Do List ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("5. Mark Task as Done")

def add_task():
    task = input("Enter your task: ").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        save_tasks() 
        print(f'"{task}" added!')
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        print("\n==== Your Tasks ====")
        for idx, task in enumerate(todo_list, start=1):
            status = "[X]" if task.get("done") else "[ ]"
            print(f"{idx}. {status} {task.get('task')}")
        show_task_summary()   

def show_task_summary():
    total = len(todo_list)
    done = sum(1 for task in todo_list if task.get("done"))
    pending = total - done
    print(f"\nTask Summary: Total = {total} | Done = {done} | Pending = {pending}\n")

def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            save_tasks() 
            print(f'"{removed["task"]}" deleted!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_done():
    if not todo_list:
        print("No tasks to mark as done.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            save_tasks() 
            print(f'"{todo_list[task_num - 1]["task"]}" marked as done!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

load_tasks()
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    elif choice == '5':
        mark_task_done()  
    else:
        print("Invalid choice. Please select 1-5.")
