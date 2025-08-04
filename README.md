# Task Tracker CLI

A command-line interface (CLI) application for managing tasks, built as part of the [Roadmap.sh Task Tracker Challenge](https://roadmap.sh/projects/task-tracker).

## 🚀 Features

- Add new tasks to your task list
- List all tasks or filter by status (to-do, in-progress, done)
- Update existing tasks
- Delete tasks
- Mark tasks as in-progress or done
- Persistent storage using JSON files

## 📁 Project Structure

```
task-tracker/
├── main.py                 # Main entry point and CLI argument parsing
├── tasks.json              # JSON file for persistent task storage
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── utils/                 # Utility modules
    ├── add_task.py        # Add new tasks functionality
    ├── list_tasks.py      # List and filter tasks functionality
    ├── update_task.py     # Update existing tasks functionality
    ├── delete_task.py     # Delete tasks functionality
    └── change_status.py   # Change task status functionality
```

### File Organization

- **`main.py`**: Contains the argument parser configuration and coordinates calls to utility functions
- **`utils/`**: Contains modular utility functions, each handling a specific task operation
- **`tasks.json`**: Stores all tasks in JSON format for persistence between sessions

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/jmlc643/task-tracker.git
cd task-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

The application uses command-line arguments to perform different operations:

### Add a new task
```bash
python main.py -add "Buy groceries"
```

### List tasks
```bash
# List all tasks
python main.py -list

# Filter by status
python main.py -list to-do
python main.py -list in-progress
python main.py -list done
```

### Update a task
```bash
python main.py -update 1 "Buy groceries and cook dinner"
```

### Delete a task
```bash
python main.py -delete 1
```

### Mark task as in-progress
```bash
python main.py -mark-in-progress 1
```

### Mark task as done
```bash
python main.py -mark-done 1
```

### Show version
```bash
python main.py -v
```

## 💾 JSON File Management

The application uses Python's native file system operations to interact with a JSON file (`tasks.json`) for data persistence.

### JSON File Creation and Management

1. **Automatic File Handling**: The application automatically handles the creation and management of the `tasks.json` file
2. **Empty File Handling**: If the JSON file is empty or doesn't exist, the application initializes it with an empty array `[]`
3. **Error Handling**: Robust error handling for file operations and JSON parsing
4. **Native File System**: Uses Python's built-in `open()` function and `json` module (part of the standard library)

### Task Structure

Each task is stored as a JSON object with the following structure:

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "to-do",
  "createdAt": "2025-01-01T10:00:00",
  "updatedAt": "2025-01-01T10:00:00"
}
```

### File Operations

- **Read**: Uses `json.load()` to parse the JSON file
- **Write**: Uses `json.dump()` to save tasks back to the file
- **Error Handling**: Catches `FileNotFoundError` and `json.JSONDecodeError` exceptions
- **Empty File**: Returns an empty list when the file is empty or corrupted

## 🎯 Challenge Requirements

This project fulfills the requirements of the [Roadmap.sh Task Tracker Challenge](https://roadmap.sh/projects/task-tracker):

- ✅ Add, Update, and Delete tasks
- ✅ Mark tasks as in progress or done
- ✅ List all tasks
- ✅ List tasks by status
- ✅ Store tasks in a JSON file
- ✅ Use native file system module for JSON interaction
- ✅ Handle edge cases (empty files, missing files)

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Dependencies**: argparse (built-in), json (built-in), os (built-in)
- **Storage**: JSON file with native file system operations
- **Architecture**: Modular design with separated utility functions

## 📝 License

This project is part of a coding challenge and is available for educational purposes.

## 🔗 Links

- [Original Challenge](https://roadmap.sh/projects/task-tracker)
- [Repository](https://github.com/jmlc643/task-tracker)
- [Roadmap.sh](https://roadmap.sh)
