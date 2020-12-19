import json

PATH_FILE = 'C:\\Users\\User\\PycharmProjects\\pythonProject8\\data_templates\\new_structure_shop'


def loading_product_range():
    with open(PATH_FILE, 'r') as file:
        return json.load(file)
