class Product:

    def __init__(self, name, count, price, p_type):
        self.name = name
        self.count = count
        self.price = price
        self.p_type = p_type

    def __repr__(self):
        return f"count: {self.count}, price: {self.price}, type: {self.p_type}"