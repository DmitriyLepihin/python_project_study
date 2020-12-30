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
        self.info_return_date = None

    def __repr__(self):
        return f"{self.info_book}: {self.info_reader} {self.info_return_date}"


class Administration:
    def __init__(self, file_name):
        self.file_name = file_name
        self.order_name_book = ""
        self.order_amount_of_days = None
        self.return_date = ""

    @property
    def msg_welcome_reader(self):
        return f"Good day! Dear reader, in our library there are the following books:"

    @property
    def msg_what_borrow(self):
        return f"what book do you want to borrow?"

    @property
    def msg_number_of_days_of_order(self):
        return f"Thank you for your order. Indicate the number of days for which you want to take the book!"

    @property
    def msg_data_return_book(self):
        return f"Ok, you will need to return the book {self.return_date}"

    @property
    def msg_no_book_in_library(self):
        return f"the book {self.order_name_book} is not in our library. Maybe she will appear next time. See you later!"

    @property
    def msg_how_many_days(self):
        return f" how many days you want to extend the book?"

    @property
    def msg_offer_prolong_book(self):
        return f"maybe you want to renew the book?"

    @property
    def msg_gratitude_for_returning_book(self):
        return f"thank you for submitting the book on time. Looking forward to seeing you next time!"

    @property
    def msg_the_late_delivery_of_the_book(self):
        now = datetime.now().date()
        return f"Today is {now}, You should have returned the book {self.return_date}. Next time we won't give you\
 a book for that long!"

    @property
    def msg_not_prolong_book(self):
        return f"We transfer you to the book return department, bookkeeping is overdue by "

    @property
    def msg_the_book_has_already_taken(self):
        return f"Unfortunately the book {self.order_name_book} has already taken, it will be in our library on "

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
        print(self.msg_welcome_reader)
        self.book_availability_info(library)
        print(f"{reader.get_username}, {self.msg_what_borrow}")
        while True:
            self.create_order_book()
            if self.checking_the_availability_of_a_book(library):
                print(self.msg_number_of_days_of_order)
                self.create_order_amount_of_days()
                self.calculating_the_return_period_of_a_book()
                reader.take_a_book(library.books[self.order_name_book], self.return_date)
                library.add_info_library_card(self.order_name_book, reader.get_username, self.return_date, False)
                print(self.msg_data_return_book)
                self.write_info_library(f"{reader.get_username}, took the book - {self.order_name_book}. Return date -\
{self.return_date}\n", 'a')
            elif self.order_name_book in library.library_card and library.library_card[
                self.order_name_book].status == False:
                print(f"{reader.get_username} {self.msg_the_book_has_already_taken}\
{library.library_card[self.order_name_book].info_return_date}! See you later!")
                break
            else:
                print(f"{reader.get_username}, {self.msg_no_book_in_library}")
                break

    def write_info_library(self, text, mode):
        with open(self.file_name, mode) as file:
            file.write(text)

    def prolong_book(self, book, reader, library):
        book = book.upper()
        now = datetime.now().date()
        if now <= reader.card_reader[book]['return date']:
            print(f"{reader.get_username}, {self.msg_how_many_days}")
            self.create_order_amount_of_days()
            self.return_date = self.return_date + timedelta(self.order_amount_of_days)
            reader.card_reader[book]['return date'] = self.return_date
            library.library_card[book].info_return_date = self.return_date
            print(self.msg_data_return_book)
            self.write_info_library(f"{reader.get_username}, prolong the book - {book} on {self.order_amount_of_days}\
 days. Return date - {self.return_date}\n", 'a')
        else:
            print(f"{reader.get_username}, {self.msg_not_prolong_book},\
{(datetime.now()).date() - library.library_card[book].info_return_date}")
            self.return_book(book, reader, library)

    def return_book(self, book, reader, library):
        now = datetime.now().date()
        book = book.upper()
        try:
            reader.card_reader[book] and library.library_card[book]
        except KeyError:
            books_reader = (*reader.card_reader,)
            return print(f"You did not borrow the book {book} from our library! {reader.get_username} you\
 borrowed books from us: {books_reader}")
        if now <= reader.card_reader[book]['return date'] and now <= library.library_card[
            book].info_return_date:
            print(f"{reader.get_username}, {self.msg_offer_prolong_book}")
            renewal_request = input().upper()
            if renewal_request == 'YES':
                self.prolong_book(book, reader, library)
            else:
                library.add_info_library_card(book, '', None, True)
                self.write_info_library(f"{reader.get_username} returned the book {book} date {now}", 'a')
                del reader.card_reader[book]
                print(f"{reader.get_username}, {self.msg_gratitude_for_returning_book} ")
        elif now > reader.card_reader[book]['return date'] and now > library.library_card[
            book].info_return_date:
            library.add_info_library_card(book, '', None, True)
            del reader.card_reader[book]
            self.write_info_library(f"{reader.get_username} ret. the book {book} date {now} (expired)", 'a')
            print(self.msg_the_late_delivery_of_the_book)


class Reader:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.card_reader = {}

    def take_a_book(self, book, date):
        self.card_reader[book.name] = {'author': book.author, 'return date': date}

    @property
    def get_username(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"{self.name} {self.surname}"


my_library = Library()
my_administration = Administration('books_report')
my_reader = Reader('Dmitriy', 'Lepihin')
start_library = Main(my_administration, my_library, my_reader)
start_library.start_library()
start_library.start_return_book('it')
