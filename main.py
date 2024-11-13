from todo import TodoList

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter new task description (leave blank to keep current): ")
            completed = input("Is the task completed? (yes/no): ").lower() == "yes"
            todo_list.update_task(task_number, new_task if new_task else None, completed)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
    