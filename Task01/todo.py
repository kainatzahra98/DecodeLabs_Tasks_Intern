# ==========================================
# --- STORAGE & MODEL (Data Logic) ---
# ==========================================

# Volatile In-Memory Database (List of Dictionaries)
# List -> Full Database Table
# Dictionary -> Table Row
my_tasks = []

# Autoincrement ID counter (Primary Key Generator)
next_task_id = 1

def add_task(task_text):
    """
    Appends a new task dictionary to the tasks list.
    Equivalent to 'INSERT INTO Table (id, task, completed) VALUES (id, task_text, False)'.
    """
    global next_task_id
    
    # Dictionary represents a single row in the database
    # "id" -> Primary Key
    task_row = {
        "id": next_task_id,
        "task": task_text,
        "completed": False
    }
    
    # list.append(row) -> INSERT INTO
    my_tasks.append(task_row)
    next_task_id += 1
    return task_row

def complete_task(task_id):
    """
    Marks a task as completed by finding its ID in the database.
    Equivalent to 'UPDATE Table SET completed = True WHERE id = task_id'.
    """
    for task_row in my_tasks:
        if task_row["id"] == task_id:
            task_row["completed"] = True
            return True
    return False


# ==========================================
# --- VIEW & CONTROLLER (User Interface) ---
# ==========================================

def display_add_task():
    """Handles user input for adding a task."""
    task_text = input("Enter the task description: ").strip()
    if task_text:
        new_row = add_task(task_text)
        print(f"Task added: '{new_row['task']}' (assigned ID: {new_row['id']})")
    else:
        print("Error: Task description cannot be empty!")

def display_complete_task():
    """Handles user input to mark a task as completed."""
    if len(my_tasks) == 0:
        print("\nNo tasks to mark as completed.")
        return
    
    try:
        task_id = int(input("Enter the ID of the task to mark completed: "))
        if complete_task(task_id):
            print(f"Task with ID {task_id} successfully marked as completed!")
        else:
            print(f"Error: Task with ID {task_id} not found.")
    except ValueError:
        print("Error: Please enter a valid integer for the Task ID.")

def view_tasks():
    """
    Reads all items from memory and displays them.
    Using enumerate() is the professional way to print index + value together.
    """
    if len(my_tasks) == 0:
        print("\nNo tasks in your list yet.")
    else:
        print("\n--- Your To-Do List ---")
        # enumerate() provides simultaneous access to the loop index and the dictionary value
        for index, task_row in enumerate(my_tasks, 1):
            status = "[✓]" if task_row["completed"] else "[ ]"
            print(f"{index}. {status} [ID: {task_row['id']}] {task_row['task']}")

def main():
    print("=" * 45)
    print("Welcome to the DecodeLabs In-Memory To-Do App!")
    print("=" * 45)
    
    while True:
        print("\nMenu Options:")
        print("1. Add a task (INSERT)")
        print("2. View all tasks (SELECT)")
        print("3. Mark task completed (UPDATE)")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            display_add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            display_complete_task()
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid input! Please choose option 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
