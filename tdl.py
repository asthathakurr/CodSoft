import sys

tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def update_task():
    display_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to update: ").strip())
        if 1 <= task_number <= len(tasks):
            new_description = input("Enter the new task description: ").strip()
            if new_description:
                tasks[task_number - 1] = new_description
                print("Task updated successfully.")
            else:
                print("Task description cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
