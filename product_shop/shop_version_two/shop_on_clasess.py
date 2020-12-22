from datetime import datetime
import json
from product_shop.shop_version_one.utils import PATH_FILE


class Shop:

    def __init__(self, accounts, customers, orders):
        self.account = accounts
        self.customer = customers
        self.order = orders
        self.purchase_amount = 0

    def welcome_customer(self):
        self.account.parse_product()
        print('Hello, in our prooduct shop. We have:')

    def start(self):
        self.welcome_customer()
        self.info_about_product_range()
        self.customer.balance()

    def info_about_product_range(self):
        self.account.write_account_info(f"{datetime.today().strftime('%A %x')} \
The following products have arrived in the store : \n", 'w')
        for key, value in self.account.products.items():
            print('\t'f"{key}\t{value.count} kg. \ton \t{value.price} byn - {value.p_type} ")
            self.account.write_account_info('\t'f"{key}\t{value.count} kg. \ton\
\t{value.price} byn - {value.p_type}\n", 'a')

    def checking_product_availability_in_the_store(self):
        if self.order.type_product in self.account.products:
            return self.order.type_product
        else:
            return False

    def making_purchase(self):
        self.account.write_account_info(f"{self.order.type_product} sold for summ = \
{self.account.products[self.order.type_product].price * self.order.count} byn ({self.order.count} kg.)\n", 'a')
        self.customer.buy(self.purchase_amount)
        self.account.calculation_profit_day(self.purchase_amount)

    def calculation_purchase_amount(self):
        self.purchase_amount = self.account.products[self.order.type_product].price * self.order.count
        return self.purchase_amount

    def msg_about_lack_of_money_in_the_wallet(self):
        print(f"You haven't got enough money for buying {self.order.type_product} - {self.order.count} \
kg.,\nyou have {self.customer.wallet} byn, you can buy no more than \
{self.customer.wallet // self.account.products[self.order.type_product].price}\
kg.{self.order.type_product} or choose other products!")

    def communication_with_customer(self):
        while True:
            if self.customer.wallet < self.account.min_price:
                print(f"You don't have enough money. Sorry. Try later...")
                break
            self.order.create_order()
            try:
                self.order.count = int(self.order.count)
            except ValueError:
                print(f"Re-enter the product of interest, ({self.order.count}) kilograms as a number!")
                continue
            if self.checking_product_availability_in_the_store():
                self.calculation_purchase_amount()
                if self.purchase_amount <= self.customer.wallet:
                    self.making_purchase()
                elif self.purchase_amount > self.customer.wallet > self.account.min_price:
                    self.msg_about_lack_of_money_in_the_wallet()
            else:
                print(f"Sorry {self.order.type_product} are out of stock!")
                break
        self.account.write_account_info(f"\tDaily revenue was: {self.account.profit_day} byn\n", 'a')


class Account:

    def __init__(self, file_name):
        self.min_price = 0
        self.file_name = file_name
        self.products = dict()
        self.profit_day = 0

    @staticmethod
    def load_product_range():
        with open(PATH_FILE, 'r') as file:
            return json.load(file)

    def parse_product(self):
        product = list(self.load_product_range().values())
        self.min_price = product[0]['price']
        for key, value in self.load_product_range().items():
            if value.get('price') < self.min_price:
                self.min_price = value.get('price')
            self.products[key] = Product(key, value['count'], value['price'], value['type'])

    def write_account_info(self, text, mode):
        with open(self.file_name, mode) as file:
            file.write(text)

    def calculation_profit_day(self, purchase):
        self.profit_day = self.profit_day + purchase
        return self.profit_day


class Customer:

    def __init__(self, money):
        self.wallet = money

    def buy(self, price):
        self.wallet -= price
        self.balance()

    def balance(self):
        print(f"You have {self.wallet} byn")


class Product:

    def __init__(self, name, count, price, p_type):
        self.name = name
        self.count = count
        self.price = price
        self.p_type = p_type

    def __repr__(self):
        return f"count: {self.count}, price: {self.price}, type: {self.p_type}"


class Order:
    order = str

    def __init__(self):
        self.type_product = str
        self.count = int

    def create_order(self):
        self.order = input().lower().split()
        self.type_product = self.order[0]
        self.count = self.order[1]
        return self.type_product, self.count


account = Account("account")
customer = Customer(10)
order = Order()
shop = Shop(account, customer, order)
shop.start()
shop.communication_with_customer()
