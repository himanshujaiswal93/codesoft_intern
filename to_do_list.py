 # programe to make a to_do_list to add task and remove task , save, load, manage to_do_list
import os

# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    print()

# Function to add a task to the list
def add_task(todo_list):
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to your to-do list.\n")

# Function to remove a task from the list
def remove_task(todo_list):
    display_todo_list(todo_list)
    if not todo_list:
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from your list.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to save the to-do list to a file
def save_to_file(todo_list, filename):
    with open(filename, 'w') as f:
        for task in todo_list:
            f.write(task + '\n')
    print(f"Your to-do list has been saved to {filename}.\n")

# Function to load the to-do list from a file
def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [task.strip() for task in f.readlines()]
    return []

# Main function to manage the to-do list
def main():
    filename = "todo_list.txt"
    todo_list = load_from_file(filename)
    print("Welcome to the To-Do List Manager!")
    
    while True:
        print("Choose an option:")
        print("1. View to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Save to-do list")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            save_to_file(todo_list, filename)
        elif choice == '5':
            save_to_file(todo_list, filename)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
