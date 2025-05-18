# test_task_manager.py
from task_manager import Task

def test_create_task():
    task = Task("Title", "Desc", "2025-12-31", "high")
    assert task.title == "Title"
    assert not task.completed

def test_mark_completed():
    task = Task("Title", "Desc", "2025-12-31", "high")
    task.mark_completed()
    assert task.completed
