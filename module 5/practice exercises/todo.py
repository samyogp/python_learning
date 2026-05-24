# manage todo list 
todo_list = []
while True:
    print("\n1. Add task")
    print("2. VIew tasks")
    print("3. Remove task")
    print("4. exit")
    choice = input("choose: ")
    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")
        