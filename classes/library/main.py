from classes.library import library, administration, reader, dbsql


class Main:
    def __init__(self, administrator, reader, db, library):
        self.administrator = administrator
        self.reader = reader
        self.db = db
        self.library = library

    def start_library(self):
        self.administrator.communication_reader(self.reader, self.library, self.db)


admin = administration.Administration()
user = reader.Reader()
db = dbsql.DbSql('library.db')
biblio = library.Library()
start = Main(admin, user, db, biblio)
start.start_library()
