from product_shop.shop_version_one.utils import loading_product_range
from random import randint
from datetime import datetime

my_shop = loading_product_range()


def main():
    product = list(my_shop.values())
    min_price = product[0]['price']
    print('Hello, in our prooduct shop. We have:')
    write_file(f"{datetime.today().strftime('%A %x')} The following products have arrived in the store : \n", 'w')
    for key, value in my_shop.items():
        if value.get('price') < min_price:
            min_price = value.get('price')
        print('\t'f"{key}\t{value.get('count')} kg. \ton \t{value.get('price')} byn - {value.get('type')} ")
        write_file('\t'f"{key}\t{value.get('count')} kg. \ton\
\t{value.get('price')} byn - {value.get('type')}\n", 'a')
    communicate(min_price)


def write_file(text, mode):
    with open('account', mode) as file:
        file.write(text)


def communicate(min_price):
    wallet = randint(5, 40)
    profit_day = 0
    while True:
        purchase_amount = 0
        if wallet < min_price:
            print(f"You don't have enough money. In your wallet {wallet} byn. Sorry. Try later...")
            break
        order = input().lower().split()
        type_product = order[0]
        count = order[1]
        try:
            count = int(count)
        except ValueError:
            print(f"Re-enter the product of interest, ({count}) kilograms as a number!")
            continue
        if type_product in my_shop:
            purchase_amount = my_shop[type_product]['price'] * count
            if purchase_amount <= wallet:
                write_file(f"{type_product} sold for summ = \
{my_shop[type_product]['price'] * int(count)} byn ({count} kg.)\n", 'a')
                wallet -= purchase_amount
                profit_day += purchase_amount
            elif purchase_amount > wallet > min_price:
                print(f"You haven't got enough money for buying {type_product} - {count} kg.,\n\
you have {wallet} byn, you can buy no more than {wallet // my_shop[type_product]['price']} kg. {type_product}\
 or choose other products!")
        else:
            print(f"Sorry {type_product} are out of stock!")
            break

    write_file(f"Daily revenue was: {profit_day} byn\n", 'a')


main()
