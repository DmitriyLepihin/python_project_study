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
    def __init__(self, administrator, library, reader):
        self.administrator = administrator
        self.library = library
        self.reader = reader

    def start_library(self):
        self.administrator.communication_reader(self.reader, self.library)

    def start_return_book(self, book):
        self.administrator.return_book(book, self.reader, self.library)

    def start_prolong_book(self, book):
        self.administrator.prolong_book(book, self.reader, self.library)


class Library:
    def __init__(self):
        self.library_card = {}
        self.books = {}

    def get_info_books(self):
        for key, value in BOOKS.items():
            self.books[key] = Book(key, value['author'], value['genre'])
            self.library_card[key] = LibraryCard(key)

    def add_info_library_card(self, book, name_reader="", date=None, status=True):
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
        self.info_return_date = None

    def __repr__(self):
        return f"{self.info_book}: {self.info_reader} {self.info_return_date}"


class Administration:
    def __init__(self, file_name):
        self.file_name = file_name
        self.order_name_book = ""
        self.order_amount_of_days = None
        self.return_date = ""

    def msg_welcome_reader(self):
        print('Good day! Dear reader, in our library there are the following books:')

    def msg_what_available(self, reader):
        print(f"{reader}, what book do you want to borrow?")

    def msg_number_of_days_of_order(self):
        print('Thank you for your order. Indicate the number of days for which you want to take the book!')

    def msg_data_return_book(self):
        print(f"Ok, you will need to return the book {self.return_date}")

    def msg_no_book_in_library(self, reader):
        print(f"{reader} the book {self.order_name_book} is not in our library. Maybe she will appear next time.\
 See you later!")

    def msg_how_many_days(self, reader):
        print(f"{reader} how many days you want to extend the book?")

    def msg_offer_prolong_book(self, reader):
        print(f"{reader}, maybe you want to renew the book?")

    def msg_gratitude_for_returning_book(self, reader):
        print(f"{reader}, thank you for submitting the book on time. Looking forward to seeing you next time!")

    def msg_the_late_delivery_of_the_book(self):
        now = datetime.now().date()
        print(f"Today is {now}, You should have returned the book {self.return_date}. Next time we won't give you\
 a book for that long!")

    def msg_not_prolong_book(self, reader, date):
        print(f"{reader}, we transfer you to the book return department, bookkeeping is overdue by {date}")

    def msg_the_book_has_already_taken(self, reader, return_date):
        print(f"{reader}, Unfortunately the book {self.order_name_book} has already taken, it will be in our library\
 on {return_date}. See you later!")

    def msg_not_borrow_book(self, reader, book):
        print(f"{reader.get_username}, you did not borrow the book {book} from our library!")

    def create_order_book(self):
        self.order_name_book = input().upper()

    def create_order_amount_of_days(self):
        self.order_amount_of_days = input()
        try:
            self.order_amount_of_days = int(self.order_amount_of_days)
        except ValueError:
            print(f"The number of days ({self.order_amount_of_days}) must be entered as a number. Please re-enter! ")
            self.create_order_amount_of_days()

    def book_availability_info(self, library):
        library.get_info_books()
        self.write_info_library(f"{datetime.today().strftime('%A %x')} the library has the following books: \n", 'w')
        for key, value in library.books.items():
            print(f"\t{value.name}: author - {value.author}, genre - {value.genre}")
            self.write_info_library(f"\t{value.name}: author - {value.author}, genre - {value.genre}\n", 'a')

    def checking_the_availability_of_a_book(self, library):
        if self.order_name_book in library.books and library.library_card[self.order_name_book].status:
            return True
        else:
            return False

    def calculating_the_return_period_of_a_book(self):
        data_now = datetime.today()
        period = timedelta(self.order_amount_of_days)
        self.return_date = (data_now + period).date()

    def communication_reader(self, reader, library):
        self.msg_welcome_reader()
        self.book_availability_info(library)
        self.msg_what_available(reader.get_username)
        while True:
            self.create_order_book()
            if self.checking_the_availability_of_a_book(library):
                self.msg_number_of_days_of_order()
                self.create_order_amount_of_days()
                self.calculating_the_return_period_of_a_book()
                library.add_info_library_card(self.order_name_book, reader.get_username, self.return_date, False)
                reader.take_a_book(self.order_name_book, library.library_card[self.order_name_book])
                self.msg_data_return_book()
                self.write_info_library(f"{reader.get_username}, took the book - {self.order_name_book}. Return date -\
{self.return_date}\n", 'a')
            elif self.order_name_book in library.library_card and library.library_card[
                self.order_name_book].status == False:
                self.msg_the_book_has_already_taken(reader.get_username,
                                                    library.library_card[self.order_name_book].info_return_date)
                break
            else:
                self.msg_no_book_in_library(reader.get_username)
                break

    def write_info_library(self, text, mode):
        with open(self.file_name, mode) as file:
            file.write(text)

    def prolong_book(self, book, reader, library):
        book = book.upper()
        now = datetime.now().date()
        if now <= reader.card_reader[book].info_return_date:
            self.msg_how_many_days(reader.get_username)
            self.create_order_amount_of_days()
            self.return_date = self.return_date + timedelta(self.order_amount_of_days)
            reader.card_reader[book].info_return_date = self.return_date
            library.library_card[book].info_return_date = self.return_date
            self.msg_data_return_book()
            self.write_info_library(f"{reader.get_username}, prolong the book - {book} on {self.order_amount_of_days}\
 days. Return date - {self.return_date}\n", 'a')
        else:
            overdue_days = (datetime.now()).date() - library.library_card[book].info_return_date
            self.msg_not_prolong_book(reader.get_username, overdue_days)
            self.return_book(book, reader, library)

    def return_book(self, book, reader, library):
        now = datetime.now().date()
        book = book.upper()
        if reader.card_reader.get(book) and library.library_card.get(book):
            if now <= reader.card_reader[book].info_return_date and now <= library.library_card[book].info_return_date:
                self.msg_offer_prolong_book(reader.get_username)
                renewal_request = input().upper()
                if renewal_request == 'YES':
                    self.prolong_book(book, reader, library)
                else:
                    library.add_info_library_card(book)
                    self.write_info_library(f"{reader.get_username} returned the book {book} date {now}", 'a')
                    del reader.card_reader[book]
                    self.msg_gratitude_for_returning_book(reader.get_username)
            elif now > reader.card_reader[book].info_return_date and now > library.library_card[book].info_return_date:
                library.add_info_library_card(book)
                del reader.card_reader[book]
                self.write_info_library(f"{reader.get_username} ret. the book {book} date {now} (expired)", 'a')
                self.msg_the_late_delivery_of_the_book()
        else:
            self.msg_not_borrow_book(reader, book)


class Reader:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.card_reader = {}

    def take_a_book(self, book, library_card):
        self.card_reader[book] = library_card

    @property
    def get_username(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"{self.get_username}"


my_library = Library()
my_administration = Administration('books_report')
my_reader = Reader('Dmitriy', 'Lepihin')
start_library = Main(my_administration, my_library, my_reader)
start_library.start_library()
print(my_reader.card_reader)
print(my_library.library_card)
start_library.start_return_book('it')
