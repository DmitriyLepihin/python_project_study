from datetime import datetime, timedelta
import sqlite3 as sq


class Main:
    def __init__(self, administrator, library, reader, db):
        self.administrator = administrator
        self.library = library
        self.reader = reader
        self.db = db

    def start_library(self):
        self.reader.add_user_id(self.db)
        self.administrator.communication_reader(self.reader, self.library, self.db)

    def start_return_book(self, book):
        self.administrator.return_book(book, self.reader, self.library, self.db)

    def start_prolong_book(self, book):
        self.administrator.prolong_book(book, self.reader, self.library, self.db)

    def start_info_missing_books(self):
        self.library.get_info_unavailable_books(self.db)


class Library:
    def __init__(self):
        self.library_card = {}
        self.books = {}

    def get_info_books(self, books):
        for book in books:
            self.books[book['name']] = Book(book['name'], book['author'], book['genre'])
            self.library_card[book['name']] = LibraryCard(book['name'], book['book_id'])

    def add_info_library_card(self, book, name_reader="", date=None, status=True):
        self.library_card[book].info_reader = name_reader
        self.library_card[book].info_return_date = date
        self.library_card[book].status = status

    def get_info_unavailable_books(self, db):
        for info in db.get_data_library_info_card():
            print(f" BOOK: '{info['name']}' took  {info['full_name']}, return_date: {info['return_date']}")


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"{self.name}: {self.author}, {self.genre} "


class LibraryCard:
    def __init__(self, info_book, book_id):
        self.info_reader = ""
        self.info_book = info_book
        self.book_id = book_id
        self.status = True
        self.info_return_date = None

    def __repr__(self):
        return f"{self.info_book}: {self.info_reader} {self.info_return_date} {self.book_id}"


class Administration:
    def __init__(self):
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

    def msg_unconfirmed_order(self, reader):
        print(f"{reader}, you have already taken {self.order_name_book} for reading. Try to place your order again!")

    def create_order_book(self):
        self.order_name_book = input().upper()

    def create_order_amount_of_days(self):
        self.order_amount_of_days = input()
        try:
            self.order_amount_of_days = int(self.order_amount_of_days)
        except ValueError:
            print(f"The number of days ({self.order_amount_of_days}) must be entered as a number. Please re-enter! ")
            self.create_order_amount_of_days()

    def book_availability_info(self, library, db):
        library.get_info_books(db.get_info_table_book())
        for key, value in library.books.items():
            print(f"\t{value.name}: author - {value.author}, genre - {value.genre}")

    def checking_the_availability_of_a_book(self, library):
        if self.order_name_book in library.books:
            return True
        else:
            return False

    def calculating_the_return_period_of_a_book(self):
        data_now = datetime.today()
        period = timedelta(self.order_amount_of_days)
        self.return_date = (data_now + period).date()

    def communication_reader(self, reader, library, db):
        self.msg_welcome_reader()
        self.book_availability_info(library, db)
        self.msg_what_available(reader.get_username)
        while True:
            self.create_order_book()
            if reader.card_reader.get(self.order_name_book):
                self.msg_unconfirmed_order(reader.get_username)
                continue
            if self.checking_the_availability_of_a_book(library):
                self.msg_number_of_days_of_order()
                self.create_order_amount_of_days()
                self.calculating_the_return_period_of_a_book()
                library.add_info_library_card(self.order_name_book, reader.get_username, self.return_date, False)
                reader.take_a_book(self.order_name_book, library.library_card[self.order_name_book])
                db.insert_table_info_lib_card(library.library_card[self.order_name_book].book_id, reader.user_id,
                                              self.return_date, False)
                db.update_column_book_is_missing(library.library_card[self.order_name_book].book_id)
                self.msg_data_return_book()
            elif db.check_return_date_missing_book(self.order_name_book) is not None:
                self.msg_the_book_has_already_taken(reader.get_username,
                                                    db.check_return_date_missing_book(self.order_name_book)
                                                    ['return_date'])
                break
            else:
                self.msg_no_book_in_library(reader.get_username)
                break

    def prolong_book(self, book, reader, library, db):
        book = book.upper()
        now = datetime.now().date()
        if now <= reader.card_reader[book].info_return_date:
            self.msg_how_many_days(reader.get_username)
            self.create_order_amount_of_days()
            self.return_date = self.return_date + timedelta(self.order_amount_of_days)
            reader.card_reader[book].info_return_date = self.return_date
            library.library_card[book].info_return_date = self.return_date
            db.update_table_info_library_card(self.return_date, library.library_card[book].book_id, reader.user_id)
            self.msg_data_return_book()
        else:
            overdue_days = (datetime.now()).date() - library.library_card[book].info_return_date
            self.msg_not_prolong_book(reader.get_username, overdue_days)
            self.return_book(book, reader, library, db)

    def return_book(self, book, reader, library, db):
        now = datetime.now().date()
        book = book.upper()
        if reader.card_reader.get(book) and library.library_card.get(book):
            if now <= reader.card_reader[book].info_return_date and now <= library.library_card[book].info_return_date:
                self.msg_offer_prolong_book(reader.get_username)
                renewal_request = input().upper()
                if renewal_request == 'YES':
                    self.prolong_book(book, reader, library, db)
                else:
                    library.add_info_library_card(book)
                    del reader.card_reader[book]
                    db.update_status_book(library.library_card[book].book_id, reader.user_id)
                    self.msg_gratitude_for_returning_book(reader.get_username)
            elif now > reader.card_reader[book].info_return_date and now > library.library_card[book].info_return_date:
                library.add_info_library_card(book)
                del reader.card_reader[book]
                db.update_status_book(library.library_card[book].book_id, reader.user_id)
                self.msg_the_late_delivery_of_the_book()
        else:
            self.msg_not_borrow_book(reader, book)


class Reader:

    def __init__(self, name, surname, address, phone):
        self.name = name
        self.surname = surname
        self.address = address
        self.phone = phone
        self.card_reader = {}
        self.user_id = None

    def add_user_id(self, db):
        if db.get_info_user_id(self.get_username) is None:
            db.insert_table_users(self.get_username, self.address, self.phone)
            for user_id in db.insert_table_users():
                if user_id['full_name'] == self.get_username:
                    self.user_id = user_id['user_id']
        else:
            self.user_id = db.get_info_user_id(self.get_username)['user_id']

    def take_a_book(self, book, library_card):
        self.card_reader[book] = library_card

    @property
    def get_username(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"{self.get_username}"


class DbSql:
    def __init__(self, name_db):
        self.name_db = name_db

    def insert_table_users(self, full_name, address, phone):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(f""" INSERT INTO users (full_name, address, phone)
                                VALUES ('{full_name}', '{address}', '{phone}') """)

    def select_users(self):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM users """)
            return cursor

    def insert_table_info_lib_card(self, book, date, reader, status):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(F""" INSERT INTO info_library_card VALUES('{book}','{date}', '{reader}', '{status}') """)

    def get_info_table_book(self):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM book WHERE book_is_missing LIKE 'False' """)
            return cursor

    def update_column_book_is_missing(self, book):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(f""" UPDATE book SET book_is_missing = 'True' WHERE book_id = '{book}' """)

    def get_info_user_id(self, reader):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(f""" SELECT user_id FROM users WHERE full_name = '{reader}' """)
            user_id = cursor.fetchone()
            return user_id

    def update_table_info_library_card(self, date, book, reader):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(f""" UPDATE info_library_card 
                                SET return_date = '{date}' WHERE book_id = '{book}' AND user_id = '{reader}' """)

    def get_data_library_info_card(self):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(""" SELECT name, users.full_name, info_library_card.return_date FROM book, users 
                               JOIN info_library_card ON info_library_card.book_id = book.book_id 
                               AND info_library_card.user_id = users.user_id 
                               AND info_library_card.is_deleted LIKE 'False' """)
            return cursor

    def update_status_book(self, book, reader):
        connect = None
        try:
            connect = sq.connect(self.name_db)
            cursor = connect.cursor()

            cursor.executescript(f""" BEGIN;
                                      UPDATE book SET book_is_missing = 'False' WHERE book_id = '{book}'; 
                                      UPDATE info_library_card SET is_deleted = 'True' 
                                      WHERE book_id = '{book}' AND user_id = '{reader}' 
                                    """)
            connect.commit()
        except sq.Error:
            if connect: connect.rollback()
            print('No database connection!')
        finally:
            if connect: connect.close()

    def check_return_date_missing_book(self, book):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(f""" SELECT return_date FROM info_library_card 
                                WHERE book_id = (SELECT book_id FROM book WHERE name LIKE '{book}' 
                                AND book_is_missing = 'True') 
                                AND is_deleted LIKE 'False' """)
            return_date = cursor.fetchone()
            return return_date


my_db = DbSql('library.db')
my_library = Library()
my_administration = Administration()
my_reader = Reader('Dmitriy', 'Lepihin', 'ul. Chkalova 24-2-59', '+375292900054')
start_library = Main(my_administration, my_library, my_reader, my_db)
start_library.start_library()
start_library.start_return_book('it')
