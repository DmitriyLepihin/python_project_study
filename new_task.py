import json
shop = {
    "fruit": {
        "banana": {
            "count": 'Дмитрий',
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
new_shop = json.dumps(shop)
print(new_shop, type(new_shop))