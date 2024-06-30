import json
import os

def read_file(file_path):
    """Reads data from a JSON file.

    Args:
        file_path (string): The path to the file to read.

    Returns:
        list: The data read from the file
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def write_to_file(file_path, data):
    """Writes data to a JSON file.

    Args:
        file_path (string): The path to the file to write.
        data (list):The data to write to the file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_to_file(file_path, new_data):
    """
     Appends new data to a JSON file.
    Args:
        file_path (string): The path to the file to append to.
        new_data (list): The new data to append to the file.
    """
    data = read_file(file_path)
    for record in data:
        if record['name'] == new_data['name']:
            print(f"Duplicate name found: {new_data['name']}. Record not added.")
            return
    data.append(new_data)
    write_to_file(file_path, data)
