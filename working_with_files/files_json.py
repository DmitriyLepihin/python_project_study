import json

shop = {
    "fruit": {
        "banana": {
            "count": 10,
            "price": 150
        },
        "apple": {
            "count": 5,
            "price": 230
        },
        "orange": {
            "count": 13,
            "price": 137
        }
    },
    "vegetables": {
        "potato": {
            "count": 47,
            "price": 77
        },
        "tomato": {
            "count": 50,
            "price": 60
        }
    },
    "profit": {
        "total": 0
    }
}
# перевел в json (стала str)
my_json = json.dumps(shop)
print(my_json)

# вернул в py (стал dict)
my_py = json.loads(my_json)
print(my_py)

# создал файл json
with open('first_json', 'w') as file:
    json.dump(my_py, file, indent=3)

# взял данные для чтения из json
with open('first_json', 'r') as file:
    my_dict_shop = json.load(file)

print(my_dict_shop)