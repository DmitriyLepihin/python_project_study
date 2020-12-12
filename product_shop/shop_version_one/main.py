from product_shop.shop_version_one.utils import loading_product_range
from random import randint

my_shop = loading_product_range()


def main():
    print('Hello, in our prooduct shop. We have:')
    for key, value in my_shop.items():
        print('\t'f"{key}\t{value.get('count')} kg \ton \t{value.get('price')} byn - {value.get('type')} ")
    print('What would you like to buy?')


def write_file(value, text):
    with open('account', 'a') as file:
        file.write(text)


def communicate():
    wallet = randint(5, 40)
    profit_day = 0
    while wallet >= 0:
        purchase_amount = 0
        if wallet == 0:
            print(f"You have made all the money purchases. In your wallet {wallet} byn")
            break
        order = input().lower().split()
        if order[0] in my_shop:
            purchase_amount = my_shop[order[0]]['price'] * int(order[1])
            if purchase_amount <= wallet:
                write_file(order, f"{order[0]} sold for summ = \
{my_shop[order[0]]['price'] * int(order[1])} byn ({order[1]} kg)\n")
                wallet -= purchase_amount
                profit_day += purchase_amount
            else:
                print(f"You’ve already spent all your money. Our wallet has {wallet} byn")
        else:
            print(f"Sorry {' '.join(order)} are out of stock!")
            break
    write_file(profit_day, f"Daily revenue was: {profit_day} byn\n")


main()
communicate()
