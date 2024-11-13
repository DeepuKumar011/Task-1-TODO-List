class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index}. {task['task']} - {status}")

    def update_task(self, task_number, new_task=None, completed=None):
        if 0 < task_number <= len(self.tasks):
            if new_task is not None:
                self.tasks[task_number - 1]["task"] = new_task
            if completed is not None:
                self.tasks[task_number - 1]["completed"] = completed
            print(f"Updated task {task_number}.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")