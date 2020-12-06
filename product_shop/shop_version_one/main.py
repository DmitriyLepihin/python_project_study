from product_shop.shop_version_one.utils import opening
from json import dump


def main():
    print('Hello, in our prooduct shop. We have:')
    my_shop = opening()
    for key in my_shop.keys():
        print(key, ':')
        for product, value in my_shop[key].items():
            if product == 'total':
                print('\t', f"{value} sum")
                continue
            print('\t'f"{product}\t{value.get('count')} kg \ton \t{value.get('price')} sum ")

    def communicate():
        product = input()
        product_fruit = ''
        fruit_kg = 0
        product_vegetables = ''
        vegetables_kg = 0
        if product == 'fruit':
            print('Ok, what fruit do you want: banana, apple, orange ?')
            product_name = input()
            product_fruit += product_name
            print('How many kg ?')
            weight = int(input())
            fruit_kg += weight
            print(f"Take your {product_fruit} exactly {fruit_kg} kg")
        if product == 'vegetables':
            print('Ok, what vegetable do you want: potato, tomato ?')
            weight = input()
            product_vegetables += weight
            print('How many kg ?')
            weight = int(input())
            vegetables_kg += weight
            print(f"Take your {product_vegetables} exactly {vegetables_kg} kg !")
        for key_shop, value_shop in my_shop.items():
            if key_shop == 'profit':
                continue
            if key_shop == product:
                for key_product, value_product in my_shop[product].items():
                    if key_product == product_fruit:
                        my_shop[product][product_fruit]['count'] = my_shop[product][product_fruit]['count'] - fruit_kg
                    if key_product == product_vegetables:
                        my_shop[product][product_vegetables]['count'] = my_shop[product][product_vegetables][
                                                                            'count'] - vegetables_kg
        with open('C:\\Users\\User\\PycharmProjects\\pythonProject8\\data_templates\\shop_json', 'w') as file:
            dump(my_shop, file, indent=3)

    return communicate()


main()
