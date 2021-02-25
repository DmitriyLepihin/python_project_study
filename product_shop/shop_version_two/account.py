import json

from product_shop.shop_version_one.utils import PATH_FILE
from product_shop.shop_version_two.product import Product


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