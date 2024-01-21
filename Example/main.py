# GitHubMain.py

import csv

def load_todos():
    """Load todos from the CSV file."""
    todos = []
    with open('savedata.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            todos.append(row)
    return todos

def save_todos(todos):
    """Save todos to the CSV file."""
    with open('savedata.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'task', 'status'])
        writer.writeheader()
        writer.writerows(todos)

def create_todo(todos, task, status):
    """Create a new todo with an auto-generated id."""
    if todos:
        id = max(todo['id'] for todo in todos) + 1
    else:
        id = 1
    todos.append({'id': id, 'task': task, 'status': status})

def read_todo(todos, id):
    """Read a todo by id."""
    for todo in todos:
        if todo['id'] == id:
            return todo
    return None

def update_todo(todos, id, task=None, status=None):
    """Update a todo by id."""
    for todo in todos:
        if todo['id'] == id:
            if task is not None:
                todo['task'] = task
            if status is not None:
                todo['status'] = status
            return True
    return False

def delete_todo(todos, id):
    """Delete a todo by id."""
    for todo in todos:
        if todo['id'] == id:
            todos.remove(todo)
            return True
    return False

def main():
    """Main function to handle user input."""
    todos = load_todos()
    while True:
        command = input('Enter command (create, read, update, delete, exit): ')
        if command == 'create':
            task = input('Enter task: ')
            status = input('Enter status: ')
            create_todo(todos, task, status)
        elif command == 'read':
            id = int(input('Enter id: '))
            todo = read_todo(todos, id)
            if todo is not None:
                print(todo)
            else:
                print('Todo not found.')
        elif command == 'update':
            id = int(input('Enter id: '))
            task = input('Enter task (leave blank to keep current task): ')
            status = input('Enter status (leave blank to keep current status): ')
            if update_todo(todos, id, task or None, status or None):
                print('Todo updated.')
            else:
                print('Todo not found.')
        elif command == 'delete':
            id = int(input('Enter id: '))
            if delete_todo(todos, id):
                print('Todo deleted.')
            else:
                print('Todo not found.')
        elif command == 'exit':
            break
        else:
            print('Invalid command.')
    save_todos(todos)

if __name__ == '__main__':
    main()