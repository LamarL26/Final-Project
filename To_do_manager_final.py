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
    return self._dict_

    @staticmethod
    def from_dict(data):
        # Create a task object from a dictionary here
        return Task(**data)
    
