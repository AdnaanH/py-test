# todo.py
import sqlite3

class ToDoApp:
    def __init__(self, db_name='todos.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        ''')
        self.conn.commit()

    def view_tasks(self):
        self.cursor.execute('SELECT id, description, done FROM tasks')
        tasks = self.cursor.fetchall()

        if not tasks:
            print("No tasks yet!")
        else:
            print("\n==== Your Tasks ====")
            total = len(tasks)
            done_count = sum(1 for t in tasks if t[2] == 1)
            pending_count = total - done_count

            for task in tasks:
                status = '[X]' if task[2] == 1 else '[ ]'
                print(f"{task[0]}. {status} {task[1]}")

            print(f"\nTask Summary: Total = {total} | Done = {done_count} | Pending = {pending_count}")

    def add_task(self):
        desc = input("Enter new task: ").strip()
        if desc:
            self.cursor.execute('INSERT INTO tasks (description) VALUES (?)', (desc,))
            self.conn.commit()
            print("Task added!")
        else:
            print("Task cannot be empty.")

    def delete_task(self):
        task_id = input("Enter task number to delete: ").strip()
        if task_id.isdigit():
            self.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            self.conn.commit()
            print("Task deleted (if it existed).")
        else:
            print("Invalid task number.")

    def mark_task_done(self):
        task_id = input("Enter task number to mark as done: ").strip()
        if task_id.isdigit():
            self.cursor.execute('UPDATE tasks SET done = 1 WHERE id = ?', (task_id,))
            self.conn.commit()
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    def menu(self):
        while True:
            print("\n=== To-Do App (SQLite) ===")
            print("1. View tasks")
            print("2. Add task")
            print("3. Delete task")
            print("4. Mark task as done")
            print("5. Exit")

            choice = input("Choose an option (1-5): ").strip()
            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.mark_task_done()
            elif choice == '5':
                self.conn.close()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.menu()
