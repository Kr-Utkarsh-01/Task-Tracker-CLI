# Task-Tracker-CLI

**Task-Tracker-CLI** is a simple command-line tool written in Python that helps you manage your personal or work tasks efficiently. It uses a local JSON file for persistent task storage and supports operations such as adding, updating, deleting, and listing tasks directly from your terminal.

---

## Features

- Create new tasks with optional descriptions.  
- Update existing task details.  
- Delete individual tasks or clear all tasks at once.  
- Change task status between *To-do*, *In-progress*, and *Done*.  
- Filter and list tasks by their status.  
- Persistent local storage using `tasks.json`.

---

## Usage

Run the script using:
```
python taskAppScript.py <command> [arguments]
```

If no arguments are provided, a help menu with all available commands will be displayed.

---

## Commands

### Task Management

| Command | Usage | Description |
|----------|--------|-------------|
| `add` | `add <task> [description]` | Adds a new task with an optional description. |
| `update` | `update <id> <new_task>` | Updates the task text or name for a given task ID. |
| `delete` | `delete <id>` | Deletes a task using its ID. |
| `delete-all` | `delete-all` | Removes all existing tasks from storage. |

---

### Status Updates

| Command | Usage | Description |
|----------|--------|-------------|
| `mark-to-do` | `mark-to-do <id>` | Sets the task status to *To-do*. |
| `mark-in-progress` | `mark-in-progress <id>` | Sets the task status to *In-progress*. |
| `mark-done` | `mark-done <id>` | Sets the task status to *Done*. |

---

### Task Listing

| Command | Usage | Description |
|----------|--------|-------------|
| `list` | `list` | Displays all tasks. |
| `list todo` | `list todo` | Shows all tasks marked as *To-do*. |
| `list in-progress` | `list in-progress` | Shows all tasks marked as *In-progress*. |
| `list done` | `list done` | Shows all tasks marked as *Done*. |

---

### Help

| Command | Description |
|----------|-------------|
| `help` | Displays all available commands and their usage instructions. |

---

## Example Usage
```
python taskAppScript.py add "Write documentation" "Due Monday"
python taskAppScript.py list
python taskAppScript.py mark-in-progress 1
python taskAppScript.py update 1 "Write complete project documentation"
python taskAppScript.py mark-done 1
python taskAppScript.py delete 1
```

---

## Data Format

All tasks are stored in a local file named `tasks.json` with the following format:
```
{
"currIds": ["1", "2"],
"1": {
"task": "Write documentation",
"status": "Done",
"desc": "Due Monday",
"created": "2025-10-19 22:45:10",
"modified": "2025-10-20 00:12:03"
},
"2": {
"task": "Plan meeting agenda",
"status": "To-do",
"desc": "",
"created": "2025-10-20 00:15:37",
"modified": "2025-10-20 00:15:37"
}
}
```

---

## Notes

- Task IDs are automatically assigned sequentially.  
- Available task statuses: *To-do*, *In-progress*, and *Done*.  
- Always run the script from the directory containing `tasks.json` for proper functionality.
- project for https://roadmap.sh/projects/task-tracker
