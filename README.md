# Task Manager CLI v1.0.0

A simple, lightweight, in-memory command-line Task Manager built in Python. This project allows users to view, add, and remove tasks interactively through a clean terminal interface.

---

## 🚀 Features

* **View All Tasks:** Displays all current tasks with formatted details (ID, Name, Description, and Priority). Includes a clean fallback message (`"No task added."`) if the task list is empty.
* **Add Tasks:** Dynamically creates new tasks with auto-incremented IDs, custom names, descriptions, and priority levels (Low/Medium/High).
* **Remove Tasks:** Deletes specific tasks cleanly by entering their task ID (number).
* **Interactive Menu:** Continuous CLI loop with option handling and validation.

---

## 📁 Project Structure

```text
Task Manager/
│
├── main.py       # Core application logic, menu loop, and user input handling
└── database.py   # Data source containing the in-memory task list

```

---

## 🛠️ Code Architecture (`main.py`)

* **`good_looking(task)`**: Formats and prints individual task dictionaries cleanly.
* **`task_load(tasks)`**: Iterates through the task list and calls the display function.
* **`add_task()`**: Prompts the user for task metadata, automatically assigns a unique sequential ID, and appends the new task to `data.task_list`.
* **`remove_task()`**: Accepts an ID input, searches the database, and removes the matching task dictionary.
* **`show_menu()`**: Runs the main interactive loop for user navigation, including validation checks for empty states.

---

## ⚙️ Getting Started & Installation

1. Ensure you have **Python 3.x** installed on your machine.
2. Clone this repository or download the source files (`main.py` and `database.py`) into the same local directory.
3. Open your terminal or command prompt in that directory.

### Running the Application

Execute the main script using Python:

```bash
python main.py

```

---

## 📝 Usage Guide

When you launch the program, the following menu will appear:

```text
=== TASK MANAGER ===
1. View All Tasks
2. Add Task
3. Remove Task
4. Exit
Select an option (1-4): 

```

* **Option 1:** Prints all items currently stored in memory (or displays `No task added.` if the list is empty).
* **Option 2:** Prompts you to enter a task name, description, and priority.
* **Option 3:** Prompts you for a task ID number to safely delete that task.
* **Option 4:** Closes the application.

```
