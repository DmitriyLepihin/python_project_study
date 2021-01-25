import sqlite3 as sq


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
            cursor.execute(f""" SELECT name, book.book_id, info_library_card.user_id, 
                                info_library_card.is_deleted, return_date, date_taking FROM book 
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

    def insert_table_info_lib_card(self, book, date, reader, status, date_taking):
        with sq.connect(self.name_db) as con:
            cursor = con.cursor()
            cursor.execute(F""" INSERT INTO info_library_card 
                                            VALUES('{book}','{date}', '{reader}', '{status}', '{date_taking}') """)

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
