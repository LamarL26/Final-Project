# Test task manager

import pytest
from task_manager import Task, TaskManager
import os
import json

TEST_FILE = "test_tasks.json"

@pytest.fixture
def manager():
    mgr = TaskManager(filename=TEST_FILE)
    mgr.tasks = []  # Ensure clean slate
    return mgr

def test_create_task():
    task = Task("Test Title", "Test Desc", "2025-12-31", "high")
    assert task.title == "Test Title"
    assert task.description == "Test Desc"
    assert task.due_date == "2025-12-31"
    assert task.priority == "high"
    assert not task.completed

def test_mark_completed():
    task = Task("Test", "Desc", "2025-12-31", "low")
    task.mark_completed()
    assert task.completed

def test_edit_task():
    task = Task("Old Title", "Old Desc", "2025-01-01", "medium")
    task.edit(title="New Title", priority="high")
    assert task.title == "New Title"
    assert task.priority == "high"
    assert task.description == "Old Desc"

def test_to_dict_and_from_dict():
    task = Task("Dict Test", "Desc", "2025-01-01", "low", completed=True)
    task_dict = task.to_dict()
    new_task = Task.from_dict(task_dict)
    assert new_task.title == "Dict Test"
    assert new_task.completed

def test_save_and_load_tasks(manager):
    manager.tasks.append(Task("Save Test", "Desc", "2025-05-01", "medium"))
    manager.save_tasks()
    assert os.path.exists(TEST_FILE)

    loaded = TaskManager(filename=TEST_FILE)
    assert len(loaded.tasks) == 1
    assert loaded.tasks[0].title == "Save Test"

    os.remove(TEST_FILE)

def test_validate_date_true(manager):
    assert manager.validate_date("2025-12-31")

def test_validate_date_false(manager):
    assert not manager.validate_date("12/31/2025")
