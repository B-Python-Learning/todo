# Developer Documentation

This Python script provides a simple command-line interface for managing a todo list. The todo list is stored in a CSV file named savedata.csv. Each todo item has an 'id', 'task', and 'status' field.

##  High-Level Design
The script is designed around a CRUD (Create, Read, Update, Delete) model for managing todo items. The main functions for these operations are create_todo, read_todo, update_todo, and delete_todo.

The script starts by loading the existing todos from the CSV file into memory. The user can then input commands to create, read, update, or delete todos. When the user is done, the script saves the todos back to the CSV file.

The 'id' field for new todos is auto-generated. It is one greater than the highest 'id' currently in the list.

## Functions
### load_todos
This function loads the todos from the CSV file into memory. It opens the CSV file for reading, creates a csv.DictReader object to read the file, and appends each row to the todos list. Each row is a dictionary where the keys are the column names and the values are the cell values. The 'id' field is converted from a string to an integer.

### save_todos
This function saves the todos from memory back to the CSV file. It opens the CSV file for writing, creates a csv.DictWriter object to write the file, and writes the todos list to the file. The fieldnames parameter specifies the order of the columns in the CSV file.

# Use Cases
This script can be used for any application that requires a simple, text-based interface for managing a todo list. The user can create new todos, read existing todos, update the task or status of a todo, or delete a todo. The todos are stored in a CSV file, so they persist between sessions.

The script can be run from the command line with the command python GitHubMain.py. The user will be prompted to enter a command. The valid commands are 'create', 'read', 'update', 'delete', and 'exit'. The 'create' command prompts the user to enter a task and status for the new todo. The 'read', 'update', and 'delete' commands prompt the user to enter the id of the todo. The 'exit' command saves the todos and exits the script.