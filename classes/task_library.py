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


class Main:
    def __init__(self, administrator):
        self.administrator = administrator

    def start_library(self):
        self.administrator.communication_reader()


class Library:
    def __init__(self):
        self.library_card = {}
        self.books = {}

    def get_info_books(self):
        for key, value in BOOKS.items():
            self.books[key] = Book(key, value['author'], value['genre'])
            self.library_card[key] = LibraryCard(key)

    def add_info_library_card(self, book, name_reader, date, status):
        self.library_card[book].info_reader = name_reader
        self.library_card[book].info_return_date = date
        self.library_card[book].status = status


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"{self.name}: {self.author}, {self.genre} "


class LibraryCard:
    def __init__(self, info_book):
        self.info_reader = ""
        self.info_book = info_book
        self.status = True
        self.info_return_date = 0

    def __repr__(self):
        return f"{self.info_book}: {self.info_reader} {self.info_return_date}"


class Administration:
    def __init__(self, file_name, reader, library):
        self.file_name = file_name
        self.reader = reader
        self.library = library
        self.order_name_book = ""
        self.order_amount_of_days = 0
        self.return_date = ""

    def create_order_book(self):
        self.order_name_book = input().upper()

    def create_order_amount_of_days(self):
        self.order_amount_of_days = input()
        try:
            self.order_amount_of_days = int(self.order_amount_of_days)
        except ValueError:
            print(f"The number of days ({self.order_amount_of_days}) must be entered as a number. Please re-enter! ")
            self.create_order_amount_of_days()

    @staticmethod
    def welcome_reader():
        print('Good day! Dear reader, in our library there are the following books:')

    def book_availability_info(self):
        self.library.get_info_books()
        self.write_info_library(f"{datetime.today().strftime('%A %x')} \
 the library has the following books: \n", 'w')
        for key, value in self.library.books.items():
            print(f"\t{value.name}: author - {value.author}, genre - {value.genre}")
            self.write_info_library(f"\t{value.name}: author - {value.author}, genre - {value.genre}\n",
                                    'a')

    def checking_the_availability_of_a_book(self):
        if self.order_name_book in self.library.books and self.library.library_card[self.order_name_book].status:
            return self.order_name_book
        else:
            return False

    def calculating_the_return_period_of_a_book(self):
        data_now = datetime.today()
        period = timedelta(self.order_amount_of_days)
        self.return_date = (data_now + period).date()

    def communication_reader(self):
        self.welcome_reader()
        self.book_availability_info()
        print(f"{self.reader.name} {self.reader.surname} what book do you want to borrow?")
        while True:
            self.create_order_book()
            if self.checking_the_availability_of_a_book():
                print('Thank you for your order. Indicate the number of days for which you want to take the book!')
                self.create_order_amount_of_days()
                self.calculating_the_return_period_of_a_book()
                self.reader.take_a_book(self.library.books[self.order_name_book], self.return_date)
                self.library.add_info_library_card(self.order_name_book, self.reader.surname, self.return_date, False)
                print(f"Ok, you will need to return the book {self.return_date}")
                self.write_info_library(f"{self.reader.name} {self.reader.surname}, took the book -\
{self.order_name_book}. Return date - {self.return_date}\n", 'a')
            elif self.order_name_book in self.library.library_card and self.library.library_card[
                self.order_name_book].status == False:
                print(f"{self.reader.name} the book {self.order_name_book} is not in our library. It must be passed\
 before {self.library.library_card[self.order_name_book].info_return_date}. Try to come to us after\
 {self.library.library_card[self.order_name_book].info_return_date}! See you later ! ")
                break
            else:
                print(f"{self.reader.name}, the book {self.order_name_book} is not in our library.\
 Maybe she will appear next time. See you later!")
                break

    def write_info_library(self, text, mode):
        with open(self.file_name, mode) as file:
            file.write(text)

    def prolong_book(self, book):
        book = book.upper()
        if (datetime.now()).date() <= self.reader.card_reader[book]['return date']:
            print(f"Dear {self.reader.name} {self.reader.surname}, indicate how many days you want to extend the book!")
            self.create_order_amount_of_days()
            self.return_date = self.return_date + timedelta(self.order_amount_of_days)
            self.reader.card_reader[book]['return date'] = self.return_date
            self.library.library_card[book].info_return_date = self.return_date
            print(f"Now you need to return the book no later {self.return_date}")
            self.write_info_library(f"{self.reader.name} {self.reader.surname}, \
 prolong the book - {book} on {self.order_amount_of_days} days. Return date - {self.return_date}\n",
                                    'a')
        else:
            print(f"{self.reader.name}, We will not renew the book for you, you are overdue by\
({(datetime.now()).date() - self.library.library_card[book].info_return_date})! You urgently need\
 to turn in your book to the library!")

    def return_book(self, book):
        now = (datetime.now()).date()
        book = book.upper()
        for name_book, info in self.library.library_card.items():
            if name_book == book and now <= info.info_return_date:
                print(f"{self.reader.name}, maybe you want to renew the book?")
                renewal_request = input().upper()
                if renewal_request == 'YES':
                    self.prolong_book(book)
                else:
                    self.library.add_info_library_card(book, '', 0, True)
                    self.write_info_library(f"{self.reader.name} {self.reader.surname} returned the book\
    {book} date {now}", 'a')
                    del self.reader.card_reader[book]
                    print(f"{self.reader.name} {self.reader.surname}, thank you for submitting the book on time.\
 Looking forward to seeing you next time!")
                    break
            elif name_book == book and now >= info.info_return_date:
                self.library.add_info_library_card(book, '', 0, True)
                del self.reader.card_reader[book]
                self.write_info_library(f"{self.reader.name} {self.reader.surname} returned the book\
 {book} date {now} (expired)", 'a')
                print(f"Today is {now}, which means that you are {now - info.info_return_date} days overdue.\
 Next time we won't give you a book for that long!")
                break


class Reader:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.card_reader = {}

    def take_a_book(self, book, date):
        self.card_reader[book.name] = {'author': book.author, 'return date': date}

    def __repr__(self):
        return f"{self.name} {self.surname}"


library = Library()
reader = Reader('Dmitriy', 'Lepihin')
administration = Administration('books_report', reader, library)
start_library = Main(administration)
start_library.start_library()
start_library.administrator.return_book("it")
