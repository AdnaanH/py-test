# todo.py

todo_list = []

def show_menu():
    print("\n==== To-Do List ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter your task: ").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        print(f'"{task}" added!')
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, item in enumerate(todo_list, start=1):
            status = "[X]" if item["done"] else "[ ]"
            print(f"{i}. {status} {item['task']}")

def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f'"{removed["task"]}" deleted!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")
