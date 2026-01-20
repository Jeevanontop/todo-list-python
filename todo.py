# To-Do List Application

todo_list = []

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully!")

def view_tasks():
    if len(todo_list) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        i = 1
        for t in todo_list:
            if t["done"]:
                status = "Done"
            else:
                status = "Pending"
            print(i, ".", t["task"], "-", status)
            i = i + 1

def mark_done():
    view_tasks()
    if len(todo_list) > 0:
        num = int(input("Enter task number to mark as done: "))
        if num >= 1 and num <= len(todo_list):
            todo_list[num - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if len(todo_list) > 0:
        num = int(input("Enter task number to delete: "))
        if num >= 1 and num <= len(todo_list):
            todo_list.pop(num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
