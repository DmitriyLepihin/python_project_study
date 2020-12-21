from datetime import datetime


class Shop:

    def __init__(self, accounts, customers, orders, purchase_amount=0):
        self.account = accounts
        self.customer = customers
        self.order = orders
        self.purchase_amount = purchase_amount

    def start(self):
        print('Hello, in our prooduct shop. We have:')
        self.account.write_account_info(f"{datetime.today().strftime('%A %x')} \
The following products have arrived in the store : \n", 'w')
        for key, value in self.account.load_product_range().items():
            print('\t'f"{key}\t{value.get('count')} kg. \ton \t{value.get('price')} byn - {value.get('type')} ")
            self.account.write_account_info('\t'f"{key}\t{value.get('count')} kg. \ton\
\t{value.get('price')} byn - {value.get('type')}\n", 'a')

    def product_check(self):
        if self.order.type_product in self.account.load_product_range():
            return self.order.type_product
        else:
            return False

    def calculation_purchase_amount(self):
        self.purchase_amount = self.account.load_product_range()[self.order.type_product]['price'] * self.order.count
        return self.purchase_amount

    def communication_with_customer(self):
        while True:
            if self.customer.wallet < self.account.min_price:
                print(f"You don't have enough money. In your wallet {self.customer.wallet} byn. Sorry. Try later...")
                break
            self.order.create_order()
            try:
                self.order.count = int(self.order.count)
            except ValueError:
                print(f"Re-enter the product of interest, ({self.order.count}) kilograms as a number!")
                continue
            self.product_check()
            if self.product_check():
                self.calculation_purchase_amount()
                if self.purchase_amount <= self.customer.wallet:
                    self.account.write_account_info(f"{self.order.type_product} sold for summ = \
{self.account.load_product_range()[self.order.type_product]['price'] * self.order.count}\
byn ({self.order.count} kg.)\n", 'a')
                    self.customer.credit(self.purchase_amount)
                    self.account.calculation_profit_day(self.purchase_amount)
                elif self.purchase_amount > self.customer.wallet > self.account.min_price:
                    print(f"You haven't got enough money for buying {self.order.type_product} - {self.order.count} \
kg.,\nyou have {self.customer.wallet} byn, you can buy no more than \
{self.customer.wallet // self.account.load_product_range()[self.order.type_product]['price']}\
 kg.{self.order.type_product} or choose other products!")
            else:
                print(f"Sorry {self.order.type_product} are out of stock!")
                break
        self.account.write_account_info(f"\tDaily revenue was: {self.account.profit_day} byn\n", 'a')


class Account:

    def __init__(self, file_name, min_price=0, profit_day=0):
        self.min_price = min_price
        self.file_name = file_name
        self.product = self.parse_product()
        self.profit_day = profit_day

    @staticmethod
    def load_product_range():
        return {
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

    def parse_product(self):
        product = list(self.load_product_range().values())
        self.min_price = product[0]['price']
        res = []
        for key, value in self.load_product_range().items():
            if value.get('price') < self.min_price:
                self.min_price = value.get('price')
            res.append(Product(key, value['type'], value['count']))
        return res

    def write_account_info(self, text, mode):
        with open(self.file_name, mode) as file:
            file.write(text)

    def calculation_profit_day(self, purchase):
        self.profit_day = self.profit_day + purchase
        return self.profit_day


class Customer:

    def __init__(self, money):
        self.wallet = money

    def credit(self, price):
        self.wallet -= price


class Product:

    def __init__(self, name, p_type, count):
        self.name = name
        self.p_type = p_type
        self.count = count

    def __repr__(self):
        return f"{self.name}: count {self.count}, type {self.p_type}"


class Order:
    order = str

    def __init__(self, type_product=str, count=int):
        self.type_product = type_product
        self.count = count

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
