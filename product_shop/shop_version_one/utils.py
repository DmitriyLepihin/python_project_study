import json

PATH_FILE = 'C:\\Users\\User\\PycharmProjects\\pythonProject8\\data_templates\\shop_json'


def opening():
    with open(PATH_FILE, 'r') as file:
        return json.load(file)
