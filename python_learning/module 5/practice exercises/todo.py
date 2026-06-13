# todo.py
todo_list = []
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        task_num = int(input("Task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")
    elif choice == "4":
        break
    else:
        print("Invalid choice")