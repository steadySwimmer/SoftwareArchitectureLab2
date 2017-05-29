from View import View
from Model import Model
from random import *
'''Implemenation of Controller class'''

class Controller:
	''' The class is responsible for connection with 
	bussiness logic and it represantation.
	'''

	def __init__(self, main_model):
		""" Initialize Model class
        Args:
            main_model(Model): The model stores the data 
            of the app
        """
		self.model = main_model
		super().__init__()

	def start(self):
		'''Method implement the main menu logic.'''
		mode = 0
		View.main_menu()

		while mode != 9:
			try: 
				mode = int(input("Choose option: "))
			except ValueError:
				View.wrong_option()
				mode = 0

			if mode == 1:
				View.print_users(self.model.user_list)
				self.take_return_book_option()
				View.main_menu()
			elif mode == 2:
				self.create_user_manager()
				View.main_menu()
			elif mode == 3:
				View.detailed_print_users(self.model.user_list)
				View.main_menu()
			elif mode == 4:
				View.print_users(self.model.user_list)
				self.delete_user_manager()
				View.main_menu()
			elif mode == 5:
				View.print_books(self.model.book_list)
				self.set_book_rate_manager()
				View.main_menu()
			elif mode == 6:
				self.create_book_manager()
				View.main_menu()
			elif mode == 7:
				View.detailed_print_books(self.model.book_list)
				View.main_menu()
			elif mode == 8:
				View.print_books(self.model.book_list)
				self.remove_book_manager()
				View.main_menu()
			elif mode == 9:
				View.exit_message()
			elif mode not in range(1, 10):
				View.main_menu()

	def create_user_manager(self):
		'''Controller manager is responsible for create 
		user process.'''
		user_name = None
		user_age = 0
		try:
			user_name = str(input("Enter user name: "))
			user_age = int(input("Enter user age: "))
		except ValueError:
			View.wrong_input()
			return

		try:
			self.model.create_user(user_name, user_age)
		except Exception as e:
			print (e)
			return			

		View.success_user_create_message()
		return

	def take_return_book_option(self):
		'''Method let you to choose between take and return 
		book process '''
		user_number = 0
		try:
			user_number = int(input("Enter user number: "))
		except ValueError:
			View.wrong_input()
			return
		if (user_number not in range(1, len(self.model.user_list) + 1)):
			View.wrong_input()
			return

		View.take_return_book()
		option = 0
		try:
			option = int(input("Choose option: "))
		except ValueError:
			View.wrong_input()
			return

		if option == 1:
			self.take_book_manager(self.model.user_list[user_number - 1])
		elif option == 2:
			self.return_book_manager(self.model.user_list[user_number - 1])
		else:
			View.wrong_input()
			return

	def take_book_manager(self, chosen_user):
		''' Take book procces. Takes book from model
		book list and give to user.'''
		number = self.take_return_book_helper(self.model.book_list)
		try:
			chosen_book = self.model.book_list[number]
			self.model.take_book(chosen_user.user_name, chosen_book.book_name)
		except TypeError:
			View.wrong_input()

	def return_book_manager(self, chosen_user):
		'''Return book process. Returns book to library
		deletes if from user book list.'''
		number = self.take_return_book_helper(chosen_user.book_list)
		try:
			chosen_book = chosen_user.book_list[number]
			self.model.return_book(chosen_user.user_name, chosen_book.book_name)
		except TypeError:
			View.wrong_input()

	def take_return_book_helper(self, book_list):
		'''Helper methods for take and return manage.
		Made because of similiar organization.'''
		View.print_books(book_list)
		book_number = -1
		try:
			book_number = int(input("Enter book number: "))
		except ValueError:
			View.wrong_input()

		if (book_number not in range(1, len(book_list) + 1)):
			View.wrong_input()
			return
		return book_number - 1

	def delete_user_manager(self):
		''' Delete user from library and return all his book
		to libary.'''
		user_number = 0
		try:
			user_number = int(input("Enter user number: "))
		except ValueError:
			View.wrong_input()
			return
		if (user_number not in range(1, len(self.model.user_list) + 1)):
			View.wrong_input()
			return
		user = self.model.user_list[user_number - 1]
		self.model.remove_user(user.user_name)

	def set_book_rate_manager(self):
		''' Set book rate manager'''
		book_number = 0
		try:
			book_number = int(input("Enter book number: "))
		except ValueError:
			View.wrong_input()
			return

		if (book_number not in range(1, len(self.model.book_list) + 1)):
			View.wrong_input()
			return

		book_rate = 0.0
		try:
			book_rate = float(input("Set book rate: "))
		except ValueError:
			View.wrong_input()
			return

		book = self.model.book_list[book_number - 1]
		book.rate = book_rate
		print ("New book rate {} for Book {}".format(book.rate, book))

	def create_book_manager(self):
		'''Method is responsbile for creating a book'''
		book_name = ""
		book_year = 0
		book_author = ""

		try:
			book_name = str(input("Enter book name: "))
			book_author = str(input("Enter book author: "))
			book_year = int(input("Enter book year: "))
		except ValueError:
			View.wrong_input()
			return
		else:
			self.model.add_book(book_name, book_author, book_year)
			View.success_book_create_message()

	def remove_book_manager(self):
		'''Method is responsbile for removing a book.
		It removes book from library and from all owner's
		list of books.'''
		book_number = 0
		try:
			book_number = int(input("Enter book number: "))
		except ValueError:
			View.wrong_input()
			return

		if (book_number not in range(1, len(self.model.book_list) + 1)):
			View.wrong_input()
			return

		try:
			self.model.remove_book(self.model.book_list[book_number - 1].book_name)
		except Exception as e:
			print (e)


