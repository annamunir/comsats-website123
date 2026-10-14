tasks = []

def show_menu():
    print("TO-DO LIST")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    print("Your tasks:")
    for i in range(len(tasks)):
        print(tasks[i])

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    view_tasks()
    num = int(input("Enter task number to remove: "))
    tasks.pop(num - 1)
    print("Task removed!")

while True:
    show_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        view_tasks()
    elif choice == 2:
        add_task()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("Exit.")
        break