import sqlobject
from Connection import *

class User(sqlobject.SQLObject):
	_connection = establish_connection()
	userName = sqlobject.StringCol(length=100, unique=False)
	age = sqlobject.IntCol(default=None)
	bookListId = sqlobject.IntCol(default=None)

User.createTable(ifNotExists=True)