from datetime import datetime, timedelta

BOOKS = {'THE LORD OF THE RINGS': {'author': 'John R. R. Tolkien', 'genre': 'fantasy'},
         'HARRY POTTER AND THE GOBLET OF FIRE': {'author': 'J.K. Rowling', 'genre': 'fantasy'},
         '1984': {'author': 'George Orwell', 'genre': 'dystopian novel'},
         'THE GODFATHER': {'author': 'Mario Puzo', 'genre': 'novel'},
         'DRACULA': {'author': 'Bram Stoker', 'genre': 'novel'},
         'IT': {'author': 'Stephen King', 'genre': 'novel-horrors'},
         'WAR AND PEACE': {'author': 'Lev Nikolaevich Tolstoy', 'genre': 'epic-novel'},
         'THE MASTER AND MARGARITA': {'author': 'Mikhail Bulgakov', 'genre': 'novel'},
         }


class Library:
    def __init__(self, administrations, readers, orders):
        self.administration = administrations
        self.reader = readers
        self.order = orders
        self.return_data = str

    def start_library(self):
        self.welcome_reader()
        self.book_availability_info()
        self.communication_reader()

    def welcome_reader(self):
        self.administration.parse_books()
        print('Good day! Dear reader, in our library there are the following books:')

    def book_availability_info(self):
        self.administration.write_info_library(f"{datetime.today().strftime('%A %x')} \
the library has the following books: \n", 'w')
        for key, value in self.administration.books.items():
            print(f"\t{value.name}: author - {value.author}, genre - {value.genre}")
            self.administration.write_info_library(f"\t{value.name}: author - {value.author}, genre - {value.genre}\n",
                                                   'a')

    def checking_the_availability_of_a_book(self):
        if self.order.name_book in self.administration.books:
            return self.order.name_book
        else:
            return False

    def calculating_the_return_period_of_a_book(self):
        data_now = datetime.today()
        period = timedelta(self.order.amount_of_days)
        self.return_data = (data_now + period).date()
        return self.return_data

    def communication_reader(self):
        print(f"{self.reader.name} {self.reader.surname} what book do you want to borrow?")
        while True:
            self.order.create_order_book()
            if self.checking_the_availability_of_a_book():
                print('Thank you for your order. Indicate the number of days for which you want to take the book!')
                self.order.create_amount_of_days()
                self.calculating_the_return_period_of_a_book()
                self.reader.add_book(self.administration.books[self.order.name_book])
                del self.administration.books[self.order.name_book]
                self.reader.add_return_date(self.return_data)
                print(f"Ok, you will need to return the book {self.return_data}")
                self.administration.write_info_library(f"{self.reader.name} {self.reader.surname}, \
 took the book - {self.order.name_book}. Return date - {self.return_data}\n", 'a')
                break
            else:
                print(f"{self.reader.name}, unfortunately there is no such book in our library, {self.order.name_book}\
 will arrive in exactly 2 weeks! Choose another book!")

    def prolong_book(self, reader):
        print(f"Good day {reader.name} {reader.surname}! You want to extend the return date. Enter the number of days!")
        self.order.create_amount_of_days()
        self.return_data = self.return_data + timedelta(self.order.amount_of_days)
        self.reader.add_return_date(self.return_data)
        print(f"Now you need to return the book no later {self.return_data}")
        self.administration.write_info_library(f"{self.reader.name} {self.reader.surname}, \
 prolong the book - {self.order.name_book} on {self.order.amount_of_days} days. Return date - {self.return_data}\n",
                                               'a')

    def return_book(self, reader):
        now = (datetime.now()).date()
        for key, value in reader.library_card.items():
            if key == 'book':
                self.administration.books[value.name] = Book(value.name, value.author, value.genre)
                self.administration.write_info_library(f"{reader.name} {reader.surname} returned the book\
 {value.name} date {now}", 'a')
            if key == 'date':
                if now <= value:
                    print(f"{reader.name} {reader.surname}, thank you for submitting the book on time.\
 Looking forward to seeing you next time!")
                else:
                    print(f"today is {now}, which means that you are {now - value} days overdue.\
 Next time we won't give you a book for that long!")
        reader.library_card.clear()


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"{self.name}: {self.author}, {self.genre} "


class Reader:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.library_card = {}

    def add_book(self, book):
        self.library_card['book'] = book

    def add_return_date(self, date):
        self.library_card['date'] = date


class Order:

    def __init__(self):
        self.name_book = str
        self.amount_of_days = int

    def create_order_book(self):
        self.name_book = input().upper()

    def create_amount_of_days(self):
        self.amount_of_days = int(input())


class Administration:
    def __init__(self, file_name):
        self.file_name = file_name
        self.books = dict()

    @staticmethod
    def load_books():
        return BOOKS

    def parse_books(self):
        for key, value in self.load_books().items():
            self.books[key] = Book(key, value['author'], value['genre'])

    def write_info_library(self, text, mode):
        with open(self.file_name, mode) as file:
            file.write(text)


administration = Administration('library')
reader = Reader('Dmitriy', 'Lepihin')
order = Order()
library = Library(administration, reader, order)
library.start_library()
print(reader.library_card)
library.prolong_book(reader)
print(reader.library_card)
print(administration.books)
library.return_book(reader)
print(administration.books)
print(reader.library_card)
