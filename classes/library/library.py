from classes.library import library_card, book


class Library:
    def __init__(self):
        self.library_card = {}
        self.books = {}

    def add_info_library_card(self, book_id, id_reader=None, date=None, taking_date=None, status=False):
        self.library_card[book_id].id_reader = id_reader
        self.library_card[book_id].info_return_date = date
        self.library_card[book_id].info_taking_date = taking_date
        self.library_card[book_id].deleted_status = status

    def get_info_books(self, db):
        self.books = {}
        self.library_card = {}
        for info_book in db.get_info_table_book():
            self.books[info_book['book_id']] = book.Book(info_book['name'], info_book['author'], info_book['genre'])
            self.library_card[info_book['book_id']] = library_card.LibraryCard(info_book['name'], info_book['book_id'])
