import json

shop = {
    "banana": {
        "count": 10,
        "price": 4,
        "type": "fruit"
    },
    "apple": {
        "count": 5,
        "price": 6,
        "type": "fruit"
    },
    "orange": {
        "count": 13,
        "price": 4,
        "type": "fruit"
    },

    "potato": {
        "count": 47,
        "price": 1,
        "type": "vegetables"
    },
    "tomato": {
        "count": 50,
        "price": 4,
        "type": "vegetables"
    }
}
# перевел в json (стала str)
my_json = json.dumps(shop)
print(my_json)

# вернул в py (стал dict)
my_py = json.loads(my_json)
print(my_py)

# создал файл json
with open('first.json', 'w') as file:
    json.dump(my_py, file, indent=3)

# взял данные для чтения из json
with open('first.json', 'r') as file:
    my_dict_shop = json.load(file)

print(my_dict_shop)
