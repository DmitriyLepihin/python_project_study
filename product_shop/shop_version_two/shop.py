from datetime import datetime
import json
from product_shop.shop_version_one.utils import PATH_FILE
from product_shop.shop_version_two.account import Account
from product_shop.shop_version_two.customer import Customer
from product_shop.shop_version_two.order import Order


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


account = Account("account")
customer = Customer(10)
order = Order()
shop = Shop(account, customer, order)
shop.start()
shop.communication_with_customer()
