import json
from datetime import datetime
from random import randint


def get_data():
    """
    Get the deserialized data from the todo list json file
    """
    with open("todos.json", "r") as json_file:
        data = json.load(json_file)
    return data


def update_data(new_data):
    """
    Update the content of the todo list json file
    with the serialized version of 'new_data'
    """
    with open("todos.json", "w") as json_file:
        json.dump(new_data, json_file, sort_keys=True, indent=True)


def add_item(args):
    """
    Adds a todo item to the todo list
    """
    title = args[1]
    data = get_data()
    new_todo = {
        "id": randint(11111, 99999),
        "title": title,
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "completed": False,
    }
    data.append(new_todo)
    update_data(data)


def show_items(args):
    """
    Prints all the todo items
    """

    data = get_data()
    complete = 0
    if len(data) == 0:
        print("No todos in the list, why don't you add one?")
    else:
        for index, todo_item in enumerate(data):
            print(index + 1, todo_item["title"])
            if todo_item["completed"]:
                complete += 1
        print(f"{complete}/{len(data)} completed!")


def edit_item(args):
    """
    Edit title for  particular todo item
    """
    id = int(args[1])
    new_title = args[2]
    data = get_data()
    for d in data:
        if d.get("id", 0) == id:
            d["title"] = new_title
    update_data(data)


def remove_item(args):
    """
    Remove a todo item
    """
    id = int(args[1])
    data = [x for x in get_data() if not (id == x.get("id"))]
    update_data(data)


def complete_item(args):
    """
    Mark a todo item as completed
    """
    id = int(args[1])
    data = get_data()
    for d in data:
        if d.get("id", 0) == id:
            d["completed"] = True
    update_data(data)


def incomplete_item(args):
    """
    Mark a todo item as incomplete
    """
    id = int(args[1])
    data = get_data()
    for d in data:
        if d.get("id", 0) == id:
            d["completed"] = False
    update_data(data)
