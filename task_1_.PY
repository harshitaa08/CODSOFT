# To-Do List Application
# Internship Task 1 - CODSOFT
# Created by: Harshita Shukla

# This is a simple command-line To-Do List App
# where the user can add, view, update and delete tasks.

tasks = []  # List to store tasks

def show_menu():
    print("\n====== TO-DO LIST APPLICATION ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("====================================")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available. Please add some!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Empty task cannot be added.")

def update_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        task_no = int(input("Enter the task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter the updated task: ").strip()
            if new_task:
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Thank you for using the To-Do List Application!")
        break
    else:
        print("Invalid choice! Please select a number between 1 and 5.")
