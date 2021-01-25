class Reader:
    def __init__(self):
        self.full_name = ""
        self.address = ""
        self.phone = ""
        self.user_id = None
        self.card_reader = {}

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

    def add_info_card(self, book_id, library_card):
        self.card_reader[book_id] = library_card

    def del_info_card_reader(self, book_id):
        del self.card_reader[book_id]

    @property
    def get_username(self):
        return f"{self.full_name}"

    def __repr__(self):
        return f"{self.get_username}"
