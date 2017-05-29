import sqlobject
import Connection

class User(sqlobject.SQLObject):
	_connection = Connection.conn
	userName = sqlobject.StringCol(length=100, unique=False)
	age = sqlobject.IntCol(default=None)
	bookListId = sqlobject.IntCol(default=None)

User.createTable(ifNotExists=True)