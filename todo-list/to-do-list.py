tasks = []

def show_tasks():
    if not tasks:
        print("Your list is empty.\n")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"Added: {task}\n")

def remove_task():
    show_tasks()
    if not tasks:
        return
    choice = int(input("Enter the number of the task to remove: "))
    if 1 <= choice <= len(tasks):
        removed = tasks.pop(choice - 1)
        print(f"Removed: {removed}\n")
    else:
        print("That's not a valid task number.\n")

print("To-Do List Manager")
print("Commands: add, remove, view, quit\n")

while True:
    command = input("What do you want to do? ").lower()

    if command == "add":
        add_task()
    elif command == "remove":
        remove_task()
    elif command == "view":
        show_tasks()
    elif command == "quit":
        print("See you next time")
        break
    else:
        print("Not a valid command, try add, remove, view, or quit\n")