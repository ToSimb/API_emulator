import json

def open_json(name_str):
    try:
        file_name = f"files/{name_str}.json"
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.read()
        return json.loads(data)
    except FileNotFoundError:
        raise
