tasks = []

while True:
    print("\n--- TASK MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(i, task)

        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
