# Simple Python To-Do List App

This repository contains a beginner-friendly command-line to-do list app written in Python.

## Files in this project

### `todo_app.py`
This is the main application file. It contains:
- A menu-based interface you run in the terminal.
- Functions to **view**, **add**, **complete**, and **delete** tasks.
- File saving/loading so your tasks persist between runs.

### `tasks.json` (created automatically)
This file stores your tasks on disk in JSON format.
- It is created the first time you add a task.
- You do not need to create it manually.

## How to run it

1. Make sure Python 3 is installed:
   ```bash
   python3 --version
   ```

2. Run the app:
   ```bash
   python3 todo_app.py
   ```

3. Use the menu options:
   - `1` View tasks
   - `2` Add task
   - `3` Mark task complete
   - `4` Delete task
   - `5` Quit

## Example quick session

```text
To-Do List Menu
1) View tasks
2) Add task
3) Mark task complete
4) Delete task
5) Quit
Choose an option (1-5): 2
Enter task title: Buy milk
Task added.
```
