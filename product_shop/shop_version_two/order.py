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