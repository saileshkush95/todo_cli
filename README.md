# Todo Command Line Application

## Create a virtual environment (optional)

Python 3:
```
$ pip3 install virtualenv
$ virtualenv -p python3 venv
```

Activate the environment:

```
source venv/bin/activate
```

## Use cases

- Create a todo list
- Add, Edit and Delete todo items 
- Mark todo items as complete and incomplete
- Show all todo items in a todo list

## Commands

1. `todo add item_names`
2. `todo all`
3. `todo edit item_id new_item_name`
4. `todo remove item_id`
5. `todo complete item_id`
6. `todo incomplete item_id`
7. `help`
8. `quit`

## JSON Files

### todos.json

- stores a list of todo item
- each todo item is a dict having id, title, created_at, and completed field.
