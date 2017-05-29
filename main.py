from configuration.configParser import *
from Connection import establish_connection

from Book import Book
if __name__ == '__main__':
	result_dict = config_parser_result()

	establish_connection(result_dict[save_type_key])

	book = Book(bookName='G', bookAuthor='K')