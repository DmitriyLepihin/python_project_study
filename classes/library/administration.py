from datetime import datetime, timedelta
from classes.library import library_card


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

    def msg_overdue_book(self, reader, book, book_id):
        print(f"""{reader}, you have the overdue book ({book} - ID BOOK - {book_id}), 
to take new book you must return the overdue book! Will you return the book?""")

    def msg_must_return_the_book(self, reader):
        print(f"{reader} if you want to take anew book, you must return overdue book!")

    def msg_enter_book_id(self):
        print("Enter the id book you want to return...")

    def msg_successfully_return_book(self, reader):
        print(f"The return of the book was successful, thank you {reader}")

    def msg_about_wrong_book_id(self, book_id):
        print(f"You have entered the id of the book ({book_id}) incorrectly, be careful!")

    def msg_want_return_book_or_prolong(self):
        print("You have books you haven returned. Enter (1) if you want to prolong, enter (2) if you want to return!\
Enter (3) if continue! ")

    def msg_want_prolong_book(self):
        print("You have books you haven returned. Do you want to prolong ? ")

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
        print(f"The book is not in the library, it will appear: {date}.")

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
                library.library_card[info['book_id']] = library_card.LibraryCard(info['name'], info['book_id'])
                library.add_info_library_card(info['book_id'], info['user_id'], info['return_date'],
                                              info['date_taking'], info['is_deleted'])
                reader.add_info_card(info['book_id'], library.library_card[info['book_id']])
                if self.date_now > datetime.strptime(library.library_card[info['book_id']].info_return_date,
                                                     '%Y-%m-%d').date():
                    self.msg_overdue_book(reader.get_username, library.library_card[info['book_id']].name_book,
                                          info['book_id'])
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
        if library.library_card.get(self.order_id_book) and reader.card_reader.get(self.order_id_book):
            db.update_status_book(self.order_id_book, reader.user_id)
            library.library_card[self.order_id_book].deleted_status = True
            reader.del_info_card_reader(self.order_id_book)
            self.msg_successfully_return_book(reader.get_username)
        else:
            self.msg_about_wrong_book_id(self.order_id_book)
            self.return_book(reader, db, library)

    def check_card_reader(self, library, reader, db):
        while True:
            books_taken_earlier = 0
            books_taken_today = 0
            if reader.card_reader:
                for key, value in reader.card_reader.items():
                    if self.date_now != datetime.strptime(value.info_taking_date, '%Y-%m-%d').date():
                        books_taken_earlier += 1
                    else:
                        books_taken_today += 1
                if books_taken_earlier >= 1 and reader.card_reader:
                    for key, value in reader.card_reader.items():
                        print(f"ID: {key} book - {value.name_book} return date: {value.info_return_date}")
                    self.msg_want_return_book_or_prolong()
                    answer = input()
                    if answer == '1':
                        self.prolong_book(library, db, reader)
                    elif answer == '2':
                        self.return_book(reader, db, library)
                    else:
                        break
                elif books_taken_today >= 1 and reader.card_reader:
                    for key, value in reader.card_reader.items():
                        print(f"ID: {key} book - {value.name_book} return date: {value.info_return_date}")
                    self.msg_want_prolong_book()
                    answer = input().upper()
                    if answer == 'YES':
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
            reader.card_reader[self.order_id_book].info_return_date = self.return_date
            self.msg_prolong_successfully(reader.get_username,
                                          library.library_card[self.order_id_book].info_return_date)
            db.update_table_info_library_card(self.return_date, self.order_id_book, reader.user_id)
            reader.del_info_card_reader(self.order_id_book)
        else:
            self.msg_about_wrong_book_id(self.order_id_book)
            self.prolong_book(library, db, reader)

    @staticmethod
    def book_availability_info(library, db):
        library.get_info_books(db)
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

    def proposal_to_take_book(self, reader):
        print(f"{reader} do you want to take one more book ?")
        answer = input().upper()
        if answer == "YES":
            return True
        else:
            return False

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
                    db.insert_table_info_lib_card(self.order_id_book, reader.user_id, self.return_date, False,
                                                  self.date_now)
                    db.update_column_book_is_missing(self.order_id_book)
                    library.add_info_library_card(self.order_id_book, reader.user_id, self.return_date,
                                                  self.date_now)
                    self.msg_order_completed(reader.get_username, self.return_date)
                    if self.proposal_to_take_book(reader.get_username):
                        self.book_availability_info(library, db)
                        continue
                    else:
                        self.msg_goodbye()
                        reader.card_reader = {}
                        self.communication_reader(reader, library, db)
                elif db.check_return_date_missing_book(self.order_id_book):
                    self.msg_book_not_library(db.check_return_date_missing_book(self.order_id_book)['return_date'])
                    if self.proposal_to_take_book(reader.get_username):
                        self.book_availability_info(library, db)
                        continue
                    else:
                        self.msg_goodbye()
                        reader.card_reader = {}
                        self.communication_reader(reader, library, db)
                else:
                    self.msg_not_book_id(self.order_id_book)
                    continue
        else:
            self.msg_goodbye()
            reader.card_reader = {}
            self.communication_reader(reader, library, db)

    def communication_reader(self, reader, library, db):
        self.authentication_reader(reader, db)
        self.check_overdue_books(reader, db, library)
        self.check_card_reader(library, reader, db)
        self.offer_to_take_books(reader, library, db)
