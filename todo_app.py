"""A simple command-line to-do list application."""

from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks() -> list[dict[str, object]]:
    """Load tasks from disk, or return an empty list if none exist."""
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        return []
    return data


def save_tasks(tasks: list[dict[str, object]]) -> None:
    """Save tasks to disk."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def show_tasks(tasks: list[dict[str, object]]) -> None:
    """Print all tasks in a friendly numbered format."""
    if not tasks:
        print("\nNo tasks yet. Add one!\n")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")
    print()


def add_task(tasks: list[dict[str, object]]) -> None:
    """Ask for a new task title and add it to the list."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.\n")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.\n")


def complete_task(tasks: list[dict[str, object]]) -> None:
    """Mark a task as complete by number."""
    show_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter task number to mark complete: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.\n")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task marked complete.\n")


def delete_task(tasks: list[dict[str, object]]) -> None:
    """Delete a task by number."""
    show_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter task number to delete: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range.\n")
        return

    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted task: {removed['title']}\n")


def main() -> None:
    """Run the interactive menu loop."""
    tasks = load_tasks()

    while True:
        print("To-Do List Menu")
        print("1) View tasks")
        print("2) Add task")
        print("3) Mark task complete")
        print("4) Delete task")
        print("5) Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.\n")


if __name__ == "__main__":
    main()
