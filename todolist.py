tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Mark Task as Done\n5. Pending Tasks\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({'task': task, 'done': False})
    elif choice == '2':
        if not tasks:
            print("No tasks added yet.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {'[X]' if task['done'] else '[ ]'} {task['task']}")
    elif choice == '3':
        if not tasks:
            print("No tasks to remove.")
        else:
            task_index = int(input("Enter task number to remove: "))
            if 1 <= task_index <= len(tasks):
                del tasks[task_index - 1]
                print("Task removed successfully.")
            else:
                print("Invalid task number.")
    elif choice == '4':
        if not tasks:
            print("No tasks to mark as done.")
        else:
            task_index = int(input("Enter task number to mark as done: "))
            if 1 <= task_index <= len(tasks):
                tasks[task_index - 1]['done'] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
    elif choice == '5':
        pending = [task for task in tasks if not task['done']]
        if not pending:
            print("No pending tasks.")
        else:
            print("Pending tasks:")
            for i, task in enumerate(pending, 1):
                print(f"{i}. {task['task']}")
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please choose again.")
