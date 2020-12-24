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
                self.reader.add_book(self.administration.books[self.order.name_book], self.return_data)
                del self.administration.books[self.order.name_book]
                print(f"Ok, you will need to return the book {self.return_data}")
                self.administration.write_info_library(f"{self.reader.name} {self.reader.surname},\
 took the book - {self.order.name_book}. Return date - {self.return_data}\n", 'a')
            elif self.order.name_book in self.reader.library_card:
                print(
                    f"{self.reader.name} the book {self.order.name_book} is not in our library.\
 It must be passed before {self.reader.library_card[self.order.name_book]['date return']}.\
 Try to come to us after {self.reader.library_card[self.order.name_book]['date return']}! See you later ! ")
                break
            else:
                print(f"{self.reader.name}, the book {self.order.name_book} is not in our library.\
 Maybe she will appear next time. See you later!")
                break

    def prolong_book(self, reader, book):
        book = book.upper()
        if (datetime.now()).date() <= reader.library_card[book]['date return']:
            print(f"Dear {reader.name} {reader.surname}, indicate how many days you want to extend the book ! ")
            self.order.create_amount_of_days()
            self.return_data = self.return_data + timedelta(self.order.amount_of_days)
            self.reader.library_card[book]['date return'] = self.return_data
            print(f"Now you need to return the book no later {self.return_data}")
            self.administration.write_info_library(f"{self.reader.name} {self.reader.surname}, \
 prolong the book - {book} on {self.order.amount_of_days} days. Return date - {self.return_data}\n",
                                                   'a')
        else:
            print(f"{reader.name}, We will not renew the book for you, you are overdue by\
({(datetime.now()).date() - reader.library_card[book]['date return']})! You urgently need\
 to turn in your book to the library!")

    def return_book(self, reader, book):
        now = (datetime.now()).date()
        book = book.upper()
        for key, value in reader.library_card.items():
            if key == book and now <= value['date return']:
                print(f"{reader.name}, maybe you want to renew the book?")
                renewal_request = input().upper()
                if renewal_request == 'YES':
                    self.prolong_book(reader, book)
                else:
                    self.administration.books[key] = Book(key, value['author'], value['genre'])
                    self.administration.write_info_library(f"{reader.name} {reader.surname} returned the book\
 {book} date {now}", 'a')
                    del reader.library_card[book]
                    print(f"{reader.name} {reader.surname}, thank you for submitting the book on time.\
 Looking forward to seeing you next time!")
                    break
            elif key == book and now >= value['date return']:
                self.administration.books[key] = Book(key, value['author'], value['genre'])
                self.administration.write_info_library(f"{reader.name} {reader.surname} returned the book\
                 {book} date {now} (expired)", 'a')
                print(f"Today is {now}, which means that you are {now - value['date return']} days overdue.\
 Next time we won't give you a book for that long!")
                break


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

    def add_book(self, book, date):
        self.library_card[book.name] = {'author': book.author, 'genre': book.genre, 'date return': date}


class Order:

    def __init__(self):
        self.name_book = str
        self.amount_of_days = int

    def create_order_book(self):
        self.name_book = input().upper()

    def create_amount_of_days(self):
        self.amount_of_days = input()
        try:
            self.amount_of_days = int(self.amount_of_days)
        except ValueError:
            print(f"The number of days ({self.amount_of_days}) must be entered as a number. Please re-enter! ")
            self.create_amount_of_days()


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
library.return_book(reader, 'it')
