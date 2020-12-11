from product_shop.shop_version_one.utils import loading_product_range
from random import randint

my_shop = loading_product_range()
wallet = randint(5, 40)
profit_day = 0


def main():
    print('Hello, in our prooduct shop. We have:')
    for key, value in my_shop.items():
        print('\t'f"{key}\t{value.get('count')} kg \ton \t{value.get('price')} byn - {value.get('type')} ")
    print('What would you like to buy?')


def write_file(customer):
    with open('account', 'a') as file:
        file.write(f"{customer[0]} sold for summ = \
{my_shop[customer[0]]['price'] * int(customer[1])} byn ({customer[1]} kg)\n")


def communicate():
    purchase_amount = 0
    global wallet
    global profit_day
    while wallet >= 0:
        if wallet == 0:
            print(f"You have made all the money purchases. In your wallet {wallet}")
            break
        customer = input().lower().split()
        if customer[0] in my_shop:
            purchase_amount = my_shop[customer[0]]['price'] * int(customer[1])
        else:
            print(f"Sorry {' '.join(customer)} are out of stock!")
            break
        if purchase_amount > wallet:
            print(f"You’ve already spent all your money. Our wallet has {wallet} byn")
        else:
            write_file(customer)
            wallet -= my_shop[customer[0]]['price'] * int(customer[1])
            purchase_amount = 0
            profit_day += my_shop[customer[0]]['price'] * int(customer[1])
    with open('account', 'a') as file:
        file.write(f"Daily revenue was: {profit_day} byn\n")


main()
communicate()
