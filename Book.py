from sqlobject import *
from Connection import *

class Book(SQLObject):
    _connection = establish_connection()
    bookName = StringCol(length=100, unique=True)
    bookAuthor = StringCol(length=100)
    bookYear = DateCol(default=None)
    bookRate = StringCol(default=None)

Book.createTable(ifNotExists=True)