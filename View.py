"""Implementation of View class."""


class View:
	"""The class is responsible for information output.
	Class consist of static methods, due to the absent
	of it initialization.
	"""

	@staticmethod
	def separator_line():
		print ("\n|-----------------------------------------------|\n")

	@staticmethod
	def main_menu():
		View.separator_line()
		print ("Enter a number to choose the option")
		print ("1. Choose user.")
		print ("2. Create user.")
		print ("3. List of user.")
		print ("4. Remove user.")
		print ("5. Choose book.")
		print ("6. Create book.") 
		print ("7. List of books.")
		print ("8. Remove book.")
		print ("9. Exit.")
		View.separator_line()

	@staticmethod
	def user_create():
		View.separator_line()
		print ("Enter the information about new user\n.")

	@staticmethod
	def book_create():
		View.separator_line()
		print ("Enter the information about new book\n.")

	@staticmethod
	def take_book():
		View.separator_line()
		print ("Take a book from the list. The library has only one copy of book.\n\
				So book can be taken only once or you should wait when someone will\n\
				return it.")

	@staticmethod
	def return_book():
		View.separator_line()
		print ("Choose a book from your list, which you wanna return.")

	@staticmethod
	def print_users(user_list):
		View.separator_line()
		for i in range(len(user_list)):
			user = user_list[i]
			print ("{}. {}".format(i + 1, user))
		View.separator_line()

	@staticmethod
	def detailed_print_users(user_list):
		View.separator_line()
		for i in range(len(user_list)):
			user = user_list[i]
			if user.book_list:
				print ("{}. {}\n{}".format(i + 1, user, user.book_list))
			else:
				print ("{}. {}".format(i + 1, user))

	@staticmethod
	def take_return_book():
		View.separator_line()
		print ("1. Take book.")
		print ("2. Return book.")

	@staticmethod
	def print_books(book_list):
		View.separator_line()
		for i in range(0, len(book_list)):
			book = book_list[i]
			print ("{}. {}".format(i + 1, book))
		View.separator_line()

	@staticmethod
	def detailed_print_books(book_list):
		View.separator_line()
		for i in range(len(book_list)):
			book = book_list[i]
			if (hasattr(book, "owner") and book.owner is not None):
				print ("{}. {}\nOwner: {}".format(i + 1, book, book.owner))
			else:
				print ("{}. {}".format(i + 1, book))

	@staticmethod
	def print_one_user(user):
		pass

	@staticmethod
	def print_one_book(book):
		pass

	@staticmethod
	def print_user_books(user):
		pass

	@staticmethod
	def success_user_create_message():
		print ("The user created successfully")

	@staticmethod
	def success_book_create_message():
		print ("The book creted successfully")

	@staticmethod
	def wrong_input():
		print ("The input is invalid")

	@staticmethod
	def wrong_option():
		print ("No current option.")

	@staticmethod
	def exit_message():
		print ("Bye, bye))")
