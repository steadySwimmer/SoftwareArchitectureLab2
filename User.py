import sqlobject
from Connection import conn 

class User(sqlobject.SQLObject):
	_connection = conn
    userName = sqlobject.StringCol(length=100, unique=False)
    age = sqlobject.IntCol(default=None)
    bookListId = sqlobject.IntCol(default=None)

#PhoneNumber.createTable(ifNotExists=True)