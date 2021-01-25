class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f" {self.name}: {self.author}, {self.genre} "
