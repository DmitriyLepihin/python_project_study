from product_shop.shop_version_one.utils import loading_product_range
from random import randint
from datetime import datetime

my_shop = loading_product_range()


def main():
    print('Hello, in our prooduct shop. We have:')
    write_file(f"{datetime.today().strftime('%A %x')} The following products have arrived in the store : \n")
    for key, value in my_shop.items():
        print('\t'f"{key}\t{value.get('count')} kg \ton \t{value.get('price')} byn - {value.get('type')} ")
        write_file('\t'f"{key}\t{value.get('count')} kg \ton\
\t{value.get('price')} byn - {value.get('type')}\n")
    print('What would you like to buy?')
    communicate()


def write_file(text):
    with open('account', 'a') as file:
        file.write(text)


def communicate():
    wallet = randint(5, 40)
    profit_day = 0
    while True:
        purchase_amount = 0
        if wallet <= 0:
            print(f"You have made all the money purchases. In your wallet {wallet} byn")
            break
        order = input().lower().split()
        type_product = order[0]
        count = order[1]
        if type_product in my_shop:
            try:
                count = int(count)
            except ValueError:
                print("Please indicate the number of kilograms by the number!")
                count = int(input())
            purchase_amount = my_shop[type_product]['price'] * count
            if purchase_amount <= wallet:
                write_file(f"{type_product} sold for summ = \
{my_shop[type_product]['price'] * int(count)} byn ({count} kg)\n")
                wallet -= purchase_amount
                profit_day += purchase_amount
            else:
                print(f"You’ve already spent all your money. Our wallet has {wallet} byn")
        else:
            print(f"Sorry {' '.join(order)} are out of stock!")
            break
    write_file(f"Daily revenue was: {profit_day} byn\n")


main()
