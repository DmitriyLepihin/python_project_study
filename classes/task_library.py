from datetime import datetime, timedelta
import sqlite3 as sq


class Main:
    def __init__(self, administrator, reader, db, library):
        self.administrator = administrator
        self.reader = reader
        self.db = db
        self.library = library

    def start(self):
        self.administrator.communication_reader(self.reader, self.library, self.db)


class Library:
    def __init__(self):
        self.library_card = {}
        self.books = {}

    def add_info_library_card(self, book_id, id_reader=None, date=None, status=False):
        self.library_card[book_id].id_reader = id_reader
        self.library_card[book_id].info_return_date = date
        self.library_card[book_id].deleted_status = status

    def del_info_library_card(self, book_id):
        del self.library_card[book_id]

    def get_info_books(self, books):
        for book in books:
            self.books[book['book_id']] = Book(book['name'], book['author'], book['genre'])
            self.library_card[book['book_id']] = LibraryCard(book['name'], book['book_id'])


class LibraryCard:

    def __init__(self, name_book, book_id):
        self.name_book = name_book
        self.book_id = book_id
        self.id_reader = None
        self.deleted_status = True
        self.info_return_date = None

    def __repr__(self):
        return f"  {self.name_book} {self.book_id} {self.id_reader} {self.deleted_status} {self.info_return_date}"


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f" {self.name}: {self.author}, {self.genre} "


class Reader:
    def __init__(self):
        self.full_name = ''
        self.address = ''
        self.phone = ''
        self.user_id = None

    def add_user_id(self, db):
        db.insert_table_users(self.get_username, self.address, self.phone)
        for user_id in db.select_all_users():
            if user_id['full_name'] == self.get_username:
                self.user_id = user_id['user_id']

    def give_data_reader(self, db):
        self.full_name = db['full_name']
        self.address = db['address']
        self.phone = db['phone']
        self.user_id = db['user_id']

    @property
    def get_username(self):
        return f"{self.full_name}"

    def __repr__(self):
        return f"{self.get_username}"


class Administration:
    def __init__(self):
        self.order_id_book = None
        self.order_amount_of_days = None
        self.return_date = ""
        self.date_now = datetime.now().date()

    def msg_greeting(self):
        print("Hello, are you registered? enter YES or NO!")

    def msg_enter_name(self):
        print("Enter your id or full name!")

    def msg_not_found(self):
        print("Your data was not found, please try again!")

    def msg_need_to_register(self):
        print("You need to register, it will take a few minutes!")

    def msg_enter_full_name(self):
        print("Enter your full name ...")

    def msg_enter_address(self):
        print("Enter your address ...")

    def msg_enter_phone(self):
        print("Enter your phone...")

    def msg_successfully_registered(self, full_name, user_id):
        print(f"{full_name} you have successfully registered, your ID - {user_id}")

    def msg_overdue_book(self, reader, book):
        print(f"""{reader}, you have the overdue book ({book}), to take new book you must return the overdue book!
Will you return the book?""")

    def msg_must_return_the_book(self, reader):
        print(f"{reader} if you want to take anew book, you must return overdue book!")

    def msg_accepted_the_book(self):
        print("This time we accepted the book. Be careful next time!")

    def msg_enter_book_id(self):
        print("Enter the id book you want to return...")

    def msg_successfully_return_book(self, reader):
        print(f"The return of the book was successful, thank you {reader}")

    def msg_about_wrong_book_id(self, book_id):
        print(f"You have entered the id of the book ({book_id}) incorrectly, be careful!")

    def msg_not_return_the_books(self, reader):
        print(f"{reader}, you do not return the following books")

    def msg_want_return_book(self):
        print("Do you want return book ?")

    def msg_want_prolong_book(self):
        print("Do you want prolong book ?")

    def msg_enter_book_id_prolong(self):
        print("Enter the id book you want to prolong...")

    def msg_how_many_days(self, reader):
        print(f"{reader}, how many days you want to prolong the book ?")

    def msg_prolong_successfully(self, reader, date):
        print(f"{reader}, the book has prolong successfully, the return date is: {date} ")

    def msg_to_take_the_book(self, reader):
        print(f"{reader} do you want to take the book in the library ?")

    def msg_available_books(self):
        print("There are following books in the library: ")

    def msg_id_book_oredering(self, reader):
        print(f"{reader}, please enter ID book for ordering...")

    def msg_number_of_days(self):
        print("Specify the number of days...")

    def msg_order_completed(self, reader, date):
        print(f"{reader}, the order completes, need to be returned: {date}")

    def msg_book_not_library(self, date):
        print(f"The book is not in the library, it will appear: {date}. See you later")

    def msg_not_book_id(self, book_id):
        print(f"You confused something, this id ({book_id}) was not found, please try to repeat the order")

    def msg_goodbye(self):
        print("Ok, see you next time !")

    def authentication_reader(self, reader, db):
        self.msg_greeting()
        answer_reader = input().upper()
        if answer_reader == 'YES':
            self.msg_enter_name()
            info_reader = input()
            if db.get_info_user(info_reader):
                reader_data = db.get_info_user(info_reader)
                reader.give_data_reader(reader_data)
            else:
                self.msg_not_found()
                self.registration(reader, db)
        else:
            self.registration(reader, db)

    def registration(self, reader, db):
        self.msg_need_to_register()
        self.msg_enter_full_name()
        full_name = input()
        reader.full_name = full_name
        self.msg_enter_address()
        address = input()
        reader.address = address
        self.msg_enter_phone()
        phone = input()
        reader.phone = phone
        reader.add_user_id(db)
        self.msg_successfully_registered(reader.full_name, reader.user_id)

    def check_overdue_books(self, reader, db, library):
        info_join_table = db.get_info_not_return_books(reader.user_id)
        if info_join_table:
            for info in info_join_table:
                library.library_card[info['book_id']] = LibraryCard(info['name'], info['book_id'])
                library.add_info_library_card(info['book_id'], info['user_id'], info['return_date'], info['is_deleted'])
                if self.date_now > datetime.strptime(library.library_card[info['book_id']].info_return_date,
                                                     '%Y-%m-%d').date():
                    self.msg_overdue_book(reader.get_username, library.library_card[info['book_id']].name_book)
                    answer = input().upper()
                    if answer == 'YES':
                        self.return_book(reader, db, library)
                    else:
                        self.msg_must_return_the_book(reader.get_username)
                        self.communication_reader(reader, library, db)
                else:
                    continue
        else:
            return False

    def return_book(self, reader, db, library):
        self.msg_enter_book_id()
        self.enter_id_book()
        if library.library_card.get(self.order_id_book):
            db.update_status_book(self.order_id_book, reader.user_id)
            library.del_info_library_card(self.order_id_book)
            self.msg_successfully_return_book(reader.get_username)
        else:
            self.msg_about_wrong_book_id(self.order_id_book)
            self.return_book(reader, db, library)

    def check_library_card(self, library, reader, db):
        while True:
            if library.library_card:
                self.msg_not_return_the_books(reader.get_username)
                for key, value in library.library_card.items():
                    if value.deleted_status == 'False':
                        print(f"ID: {key} book - {value.name_book} return date: {value.info_return_date}")
                self.msg_want_return_book()
                answer = input().upper()
                if answer == 'YES':
                    self.return_book(reader, db, library)
                elif answer != "YES":
                    self.msg_want_prolong_book()
                    answer_two = input().upper()
                    if answer_two == 'YES':
                        self.prolong_book(library, db, reader)
                    else:
                        break
            else:
                break

    def create_order_amount_of_days(self):
        self.order_amount_of_days = input()
        try:
            self.order_amount_of_days = int(self.order_amount_of_days)
        except ValueError:
            print(f"The number of days ({self.order_amount_of_days}) must be entered as a number. Please re-enter! ")
            self.create_order_amount_of_days()

    def prolong_book(self, library, db, reader):
        self.msg_enter_book_id_prolong()
        self.enter_id_book()
        if library.library_card.get(self.order_id_book):
            self.msg_how_many_days(reader.get_username)
            self.create_order_amount_of_days()
            self.return_date = datetime.strptime(library.library_card[self.order_id_book].info_return_date,
                                                 '%Y-%m-%d').date() + timedelta(self.order_amount_of_days)
            library.library_card[self.order_id_book].info_return_date = self.return_date
            self.msg_prolong_successfully(reader.get_username,
                                          library.library_card[self.order_id_book].info_return_date)
            db.update_table_info_library_card(self.return_date, self.order_id_book, reader.user_id)
        else:
            self.msg_about_wrong_book_id(self.order_id_book)
            self.prolong_book(library, db, reader)

    @staticmethod
    def book_availability_info(library, db):
        library.get_info_books(db.get_info_table_book())
        for key, value in library.books.items():
            print(f"\tBook ID {key}: {value.name}: author - {value.author}, genre - {value.genre}")

    def enter_id_book(self):
        self.order_id_book = input()
        try:
            self.order_id_book = int(self.order_id_book)
        except ValueError:
            print(f"Enter id ({self.order_id_book}) numbers. Please re-enter! ")
            self.enter_id_book()

    def checking_the_availability_of_a_book(self, library):
        if self.order_id_book in library.books and library.library_card[self.order_id_book].deleted_status:
            return True
        else:
            return False

    def calculating_the_return_period_of_a_book(self):
        data_now = datetime.today()
        period = timedelta(self.order_amount_of_days)
        self.return_date = (data_now + period).date()

    def offer_to_take_books(self, reader, library, db):
        self.msg_to_take_the_book(reader.get_username)
        answer = input().upper()
        if answer == 'YES':
            self.msg_available_books()
            self.book_availability_info(library, db)
            while True:
                self.msg_id_book_oredering(reader.get_username)
                self.enter_id_book()
                if self.checking_the_availability_of_a_book(library):
                    self.msg_number_of_days()
                    self.create_order_amount_of_days()
                    self.calculating_the_return_period_of_a_book()
                    db.insert_table_info_lib_card(self.order_id_book, reader.user_id, self.return_date, False)
                    db.update_column_book_is_missing(self.order_id_book)
                    library.add_info_library_card(self.order_id_book, reader.user_id, self.return_date)
                    self.msg_order_completed(reader.get_username, self.return_date)
                elif db.check_return_date_missing_book(self.order_id_book):
                    self.msg_book_not_library(db.check_return_date_missing_book(self.order_id_book)['return_date'])
                    self.offer_to_take_books(reader, library, db)
                else:
                    self.msg_not_book_id(self.order_id_book)
                    continue
        else:
            self.msg_goodbye()
            self.communication_reader(reader, library, db)

    def communication_reader(self, reader, library, db):
        self.authentication_reader(reader, db)
        self.check_overdue_books(reader, db, library)
        self.check_library_card(library, reader, db)
        self.offer_to_take_books(reader, library, db)


class DbSql:
    def __init__(self, name_db):
        self.name_db = name_db

    def insert_table_users(self, full_name, address, phone):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(f""" INSERT INTO users (full_name, address, phone)
                                VALUES ('{full_name}', '{address}', '{phone}') """)

    def get_info_user(self, info_user):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(f""" SELECT full_name, user_id, address, phone 
                                FROM users WHERE user_id = '{info_user}' """)
            info_reader = cursor.fetchone()
            if info_reader:
                return info_reader
            else:
                cursor.execute(f""" SELECT full_name, user_id, address, phone 
                                    FROM users WHERE full_name = '{info_user}' """)
                info_reader = cursor.fetchone()
                return info_reader

    def select_all_users(self):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM users """)
            return cursor

    def get_info_not_return_books(self, user_id):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(f""" 
                                SELECT name, book.book_id, users.user_id, info_library_card.is_deleted, return_date 
                                FROM book, users 
                                JOIN info_library_card ON info_library_card.book_id = book.book_id 
                                AND info_library_card.user_id = '{user_id}' 
                                AND info_library_card.is_deleted LIKE 'False'
                                                                                        """)
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

    def update_table_info_library_card(self, date, book, reader):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(f""" UPDATE info_library_card 
                                SET return_date = '{date}' WHERE book_id = '{book}' AND user_id = '{reader}' """)

    def get_info_table_book(self):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(""" SELECT * FROM book WHERE book_is_missing LIKE 'False' """)
            return cursor

    def insert_table_info_lib_card(self, book, date, reader, status):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(F""" INSERT INTO info_library_card VALUES('{book}','{date}', '{reader}', '{status}') """)

    def update_column_book_is_missing(self, book):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(f""" UPDATE book SET book_is_missing = 'True' WHERE book_id = '{book}' """)

    def check_return_date_missing_book(self, book):
        with sq.connect(self.name_db) as con:
            con.row_factory = sq.Row
            cursor = con.cursor()
            cursor.execute(f""" SELECT return_date FROM info_library_card 
                                WHERE book_id = (SELECT book_id FROM book WHERE book_id = '{book}' 
                                AND book_is_missing = 'True') 
                                AND is_deleted LIKE 'False' """)
            return_date = cursor.fetchone()
            return return_date


my_reader = Reader()
my_admin = Administration()
my_db = DbSql('library.db')
my_lib = Library()
start_library = Main(my_admin, my_reader, my_db, my_lib)
start_library.start()
