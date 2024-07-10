class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
        else:
            print("Invalid task index. Please choose a valid index.")

    def display_tasks(self):
        print("Your To-Do List:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task index to update: "))
            new_task = input("Enter the updated task: ")
            todo_list.update_task(index - 1, new_task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")