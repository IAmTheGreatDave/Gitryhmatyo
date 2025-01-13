tasks = []  # List to store tasks

def remove_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f"Removed task: {removed_task}")
    except IndexError:
        print("Invalid task index")
    except:
        print("Failed to remove task")
