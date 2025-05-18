# Lamar Logan
# 5/14/2025
# INST326
# Prof. Patrick

import json
import re
from datetime import datetime

# Task class defines the structure and behavior of a to-do task
class Task:
    """Represents only one to-do task."""
    def __init__(self, title, description, due_date, priority, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        # Right here, it will show that the task as completed
        self.completed = True

    def edit(self, title=None, description=None, due_date=None, priority=None):
        # This step right here will allow the user to edit the task. 
        # The user will be able to edit the title, description, due date, and priority of the task.
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority
    
    def to_dict(self):
    # Right here, convert the task to dictionary for saving to JSON
        return self.__dict__

    @staticmethod
    def from_dict(data):
        # Create a task object from a dictionary here
        return Task(**data)
    
    def __str__(self):
        # String representation of a task
        status = 'Completed' if self.completed else 'Not yet completed'
        return f"{self.title} | Due: {self.due_data} | Priority: {self.priority} | Status: {status}"
    
# TaskManager class manages a list of tasks
class TaskManager:
    """Manages a list of tasks."""
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def validate_date(self, date_str):
        # Validate date format as YYYY-MM-DD
        return re.match(r"^\d{4}-\d{2}-\d{2}$", date_str) is not None
    
    def load_tasks(self):
        # Load tasks from a JSON file
        try:
            with open(self.filename, 'r') as f:
                return [Task.from_dict(task) for task in json.load(f)]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON. Starting with an empty task list.")
            return []
        
    def save_tasks(self):
        # Save tasks to a JSON file
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        print("Tasks saved successfully.")

    def add_task(self, title, description, due_date, priority):
        # Add a new task to the list
        try:
            title = imput("Title: ").strip()
            description = input("Description: ").strip()
            due_date = input("Due date (YYYY-MM-DD): ").strip()
            while not self.validate_date(due_date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                due_date = input("Due date (YYYY-MM-DD): ").strip().lower()
            priority = input("Priority (low, medium, high): ").strip().lower()
            if priority not in ['high', 'medium', 'low']:
                raise ValueError("Priority must be 'high', 'medium', or 'low'.")
            task = Task(title, description, due_date, priority)
            self.tasks.append(task)
            print("Task added.")
        except Exception as e:
            print(f"Error adding task: {e}")

    def view_tasks(self):
        # Display all of the tasks
        if not self.tasks:
            print("No tasks available.")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def edit_task(self):
        # Edit an existing task
        self.view_tasks()
        try:
            index = int(input("Enter the task number to edit: ")) - 1
            task = self.tasks[index]
            title = input(f"New title (or press enter to keep '{task.title}'): ") or task.title
            description = input(f"New description (or press enter to keep current): ") or task.description
            due_date = input(f"New due date (or press enter to keep '{task.due_date}'): ") or task.due_date
            if not self.vaildate_date(due_date):
                print("Invalid date format. Keeping original date.")
                due_date = task.due_date
            priority = input(f"New priority (or press enter to keep '{task.priority}'): ") or task.priority
            task.edit(title, description, due_date, priority)
            print("Task updated.")
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")

    def delete_task(self):
        # Delete a task
        self.view_tasks()
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            del self.tasks[index]
            print("Task deleted.")
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")

    def mark_completed(self):
        # Mark a task as completed
        self.view_tasks()
        try:
            index = int(input("Enter the task number to mark as completed: ")) - 1
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")

        def fliter_tasks(self):
            # Show only completed or incomplete tasks
            status = input("Show completed or incomplete tasks? (c/i): ").strip().lower()
            if status not in ["completed", "incomplete"]:
                print("Invalid choice.")
                return
            filtered = [task for task in self.tasks if task.completed == (status == "completed")]
            for task in filtered:
                print(task)

            
        # Main function provides a user interface loop
        def main():
            manager = TaskManager()
            while True:
                print("\nTo-Do Manager")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Edit Task")
                print("4. Delete Task")
                print("5. Mark Task as Completed")
                print("6. Filter Tasks")
                print("7. Save and Exit")
                choice = input("Choose an option: ").strip()
                
                if choice == '1':
                    manager.add_task()
                elif choice == '2':
                    manager.view_tasks()
                elif choice == '3':
                    manager.edit_task()
                elif choice == '4':
                    manager.delete_task()
                elif choice == '5':
                    manager.mark_task_completed()
                elif choice == '6':
                    manager.filter_tasks()
                elif choice == '7':
                    manager.save_tasks()
                    print("Tasks has been saved.")
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        # Entry point for the program
        if __name__ == "__main__":
            main()