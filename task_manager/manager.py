tasks = []

def add_task(name):
    id = len(tasks) + 1
    
    task = {"id": id,  "name": name, "completed": False}
    tasks.append(task)
    print("Task added successfully")
    
    return

def view_task():
    if (len(tasks) == 0):
        print("No task available")
        return
    
    for task in tasks:
        print(f"{task['id']}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")
    return

def update_task(id, name):
    if (len(tasks) == 0):
        print("No task available")
        return
    
    task = tasks[id - 1]
    
    if task is None:
        print("Task not found")
        return
    
    task['name'] = name
    print("Task updated successfully")

def complete_task(id):
    if (len(tasks) == 0):
        print("No task available")
        return
    
    task = tasks[id - 1]
    
    if task is None:
        print("Task not found")
        return
    
    task['completed'] = True
    
    print("Task completed successfully")

def delete_completed_task():
    tasks = [task for task in tasks if not task['completed']]
    
    print("Completed task deleted successfully")
    
def close_application():
    print("Thank you for using our application")
    return

while True:
    print("\n Menu: Todo List")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Completed Task")
    print("6. Exit")
    
    chose = input("Enter your choice: ")
    
    match chose:
        case "1":
            name = input("Enter task name: ")
            add_task(name)
            pass
        case "2":
            view_task()
            pass
        case "3":
            view_task()
            id = int(input("Enter task id: "))
            name = input("Enter new task name: ")
            update_task(id, name)
            pass
        case "4":
            view_task()
            id = int(input("Enter task id: "))
            complete_task(id)
            pass
        case "5":
            delete_completed_task()
        case "6":
            close_application()
            pass
        case _:
            print("Invalid choice")
    
    
print("Thank you for using our application")