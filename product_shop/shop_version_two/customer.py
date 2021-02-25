class Customer:

    def __init__(self, money):
        self.wallet = money

    def buy(self, price):
        self.wallet -= price
        self.balance()

    def balance(self):
        print(f"You have {self.wallet} byn")