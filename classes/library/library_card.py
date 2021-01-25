class LibraryCard:

    def __init__(self, name_book, book_id):
        self.name_book = name_book
        self.book_id = book_id
        self.id_reader = None
        self.deleted_status = True
        self.info_return_date = None
        self.info_taking_date = None

    def __repr__(self):
        return f"  {self.name_book} {self.book_id} {self.id_reader} {self.deleted_status} {self.info_return_date}"
