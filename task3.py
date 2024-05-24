todo_list = []

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice here(1/2/3/4/5): ")
    
    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added sucessfully!")
    elif choice == '2':
        print("\nTasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    elif choice == '3':
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(todo_list):
            todo_list[idx] = input("Enter updated task: ")
            print("Task updated successfully!")
        else:
            print("Invalid task number given.")
    elif choice == '4':
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(todo_list):
            todo_list.pop(idx)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please check the choice you have given.")
