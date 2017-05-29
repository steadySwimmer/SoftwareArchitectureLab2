from configuration.configParser import *
import Connection

import Book

if __name__ == '__main__':
	result_dict = config_parser_result()

	Connection.establish_connection(result_dict[save_type_key])
	print (Connection.conn)
	# book = Book(bookName='G', bookAuthor='K')