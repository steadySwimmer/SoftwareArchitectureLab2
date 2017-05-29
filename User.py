import sqlobject
from Connection import *

class User(sqlobject.SQLObject):
	_connection = establish_connection()
	userName = sqlobject.StringCol(length=100, unique=False)
	age = sqlobject.IntCol(default=None)
	bookListId = sqlobject.MultipleJoin('Book', joinColumn='user_id')

	def __repr__(self):
        	return "name = '{0}', age = '{1}'".format(self.userName, self.age)

User.createTable(ifNotExists=True)