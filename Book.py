import sqlobject
from Connection import conn

class Book(sqlobject.SQLObject):
    _connection = conn
    bookName = sqlobject.StringCol(length=100, unique=True)
    bookAuthor = sqlobject.StringCol(length=100)
    bookYear = sqlobject.DateCol(default=None)
    bookRate = sqlobject.SetCol(default=None)