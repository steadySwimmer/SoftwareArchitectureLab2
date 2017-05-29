import sqlobject as sql
import Connection

class Book(sql.SQLObject):
    _connection = Connection.establish_connection('sqll')
    bookName = sql.StringCol(length=100, unique=True)
    bookAuthor = sql.StringCol(length=100)
    bookYear = sql.DateCol(default=None)
    bookRate = sql.SetCol(default=None)

Book.createTable(ifNotExists=True)